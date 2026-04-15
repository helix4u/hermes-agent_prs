from unittest.mock import patch

from hermes_cli.model_switch import switch_model


_MOCK_VALIDATION = {
    "accepted": True,
    "persist": True,
    "recognized": True,
    "message": None,
}


def test_same_provider_copilot_switch_recomputes_api_mode():
    with patch("hermes_cli.model_switch.resolve_alias", return_value=None), \
         patch("hermes_cli.model_switch.list_provider_models", return_value=[]), \
         patch(
             "hermes_cli.runtime_provider.resolve_runtime_provider",
             return_value={
                 "api_key": "gh-token",
                 "base_url": "https://api.githubcopilot.com",
                 "api_mode": "codex_responses",
             },
         ), \
         patch("hermes_cli.models.validate_requested_model", return_value=_MOCK_VALIDATION), \
         patch("hermes_cli.model_switch.get_model_info", return_value=None), \
         patch("hermes_cli.model_switch.get_model_capabilities", return_value=None), \
         patch("hermes_cli.models.detect_provider_for_model", return_value=None):
        result = switch_model(
            raw_input="claude-opus-4.6",
            current_provider="copilot",
            current_model="gpt-5.4",
        )

    assert result.success, f"switch_model failed: {result.error_message}"
    assert result.new_model == "claude-opus-4.6"
    assert result.target_provider == "copilot"
    assert result.api_mode == "chat_completions"


def test_explicit_copilot_switch_uses_selected_model_api_mode():
    with patch("hermes_cli.model_switch.resolve_alias", return_value=None), \
         patch("hermes_cli.model_switch.list_provider_models", return_value=[]), \
         patch(
             "hermes_cli.runtime_provider.resolve_runtime_provider",
             return_value={
                 "api_key": "gh-token",
                 "base_url": "https://api.githubcopilot.com",
                 "api_mode": "codex_responses",
             },
         ), \
         patch("hermes_cli.models.validate_requested_model", return_value=_MOCK_VALIDATION), \
         patch("hermes_cli.model_switch.get_model_info", return_value=None), \
         patch("hermes_cli.model_switch.get_model_capabilities", return_value=None), \
         patch("hermes_cli.models.detect_provider_for_model", return_value=None):
        result = switch_model(
            raw_input="claude-opus-4.6",
            current_provider="openrouter",
            current_model="anthropic/claude-sonnet-4.6",
            explicit_provider="copilot",
        )

    assert result.success, f"switch_model failed: {result.error_message}"
    assert result.new_model == "claude-opus-4.6"
    assert result.target_provider == "github-copilot"
    assert result.api_mode == "chat_completions"
