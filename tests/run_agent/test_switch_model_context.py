"""Tests that switch_model preserves config_context_length."""

from unittest.mock import MagicMock, patch

from run_agent import AIAgent
from agent.context_compressor import ContextCompressor


def _make_agent_with_compressor(config_context_length=None) -> AIAgent:
    """Build a minimal AIAgent with a context_compressor, skipping __init__."""
    agent = AIAgent.__new__(AIAgent)

    # Primary model settings
    agent.model = "primary-model"
    agent.provider = "openrouter"
    agent.base_url = "https://openrouter.ai/api/v1"
    agent.api_key = "sk-primary"
    agent.api_mode = "chat_completions"
    agent.client = MagicMock()
    agent.quiet_mode = True

    # Store config_context_length for later use in switch_model
    agent._config_context_length = config_context_length
    agent._default_model = "primary-model"
    agent._default_provider = "openrouter"
    agent._default_base_url = "https://openrouter.ai/api/v1"
    agent._custom_provider_context_lengths = {}

    # Context compressor with primary model values
    compressor = ContextCompressor(
        model="primary-model",
        threshold_percent=0.50,
        base_url="https://openrouter.ai/api/v1",
        api_key="sk-primary",
        provider="openrouter",
        quiet_mode=True,
        config_context_length=config_context_length,
    )
    agent.context_compressor = compressor

    # For switch_model
    agent._primary_runtime = {}

    return agent


@patch("agent.model_metadata.get_model_context_length", return_value=131_072)
def test_switch_model_clears_default_context_override_for_different_model(mock_ctx_len):
    """Top-level model.context_length should not bleed onto other models."""
    agent = _make_agent_with_compressor(config_context_length=32_768)

    assert agent.context_compressor.model == "primary-model"
    assert agent.context_compressor.context_length == 32_768  # From config override

    # Switch model
    agent.switch_model("new-model", "openrouter", api_key="sk-new", base_url="https://openrouter.ai/api/v1")

    # Verify get_model_context_length was called without the default-model override
    mock_ctx_len.assert_called_once()
    call_kwargs = mock_ctx_len.call_args.kwargs
    assert call_kwargs.get("config_context_length") is None

    # Verify compressor was updated
    assert agent.context_compressor.model == "new-model"


def test_switch_model_without_config_context_length():
    """When switching models without config override, config_context_length should be None."""
    agent = _make_agent_with_compressor(config_context_length=None)

    with patch("agent.model_metadata.get_model_context_length", return_value=128_000) as mock_ctx_len:
        # Switch model
        agent.switch_model("new-model", "openrouter", api_key="sk-new", base_url="https://openrouter.ai/api/v1")

        # Verify get_model_context_length was called with None
        mock_ctx_len.assert_called_once()
        call_kwargs = mock_ctx_len.call_args.kwargs
        assert call_kwargs.get("config_context_length") is None


def test_resolve_config_context_length_matches_default_runtime():
    agent = _make_agent_with_compressor(config_context_length=32_768)

    resolved = agent._resolve_config_context_length_for_model(
        "primary-model",
        base_url="https://openrouter.ai/api/v1",
        provider="openrouter",
    )

    assert resolved == 32_768


def test_resolve_config_context_length_prefers_custom_provider_entry():
    agent = _make_agent_with_compressor(config_context_length=None)
    agent._custom_provider_context_lengths = {
        ("http://custom-endpoint.test/v1", "glm-5"): 200_000,
    }

    resolved = agent._resolve_config_context_length_for_model(
        "glm-5",
        base_url="http://custom-endpoint.test/v1",
        provider="custom",
    )

    assert resolved == 200_000
