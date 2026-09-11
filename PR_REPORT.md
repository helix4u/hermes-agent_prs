# Hermes Agent - New Pull Requests Report

This report contains all newly opened PRs.

## Important Findings

- **[feat(voice): GPT-Live voice chat mode — full-duplex voice frontend delegating to Hermes (Desktop)](https://github.com/NousResearch/hermes-agent/pull/108137)** (by teknium1)
  - *Preview:* **Selecting `voice.voice_chat_mode: gpt-live` in the Desktop app turns the voice button into a full-duplex GPT-Live conversation whose every real request is answered by Hermes — with whatever model an...
- **[Desktop: Bot Mode no longer spawns or dials a backend per profile on launch and every roster tick (#102978, #99336, #102913)](https://github.com/NousResearch/hermes-agent/pull/108134)** (by teknium1)
  - *Preview:* Opening Bot Mode on a desktop with dozens of registered profiles no longer queues one pooled backend spawn per profile at launch: roster avatar sync (`profiles.get_asset` / `set_asset`) now asks the a...
- **[feat(desktop): edit Kanban priority in task drawer](https://github.com/NousResearch/hermes-agent/pull/108131)** (by awilhite)
  - *Preview:* ## What does this PR do?  Makes an existing Kanban task's priority editable directly in the native desktop task drawer. The control uses the drawer's existing task PATCH path, so reprioritizing a card...
- **[state.db FTS damage no longer kills turns; doctor/repair/recover handle real incident shapes (#97794, #88587, #100227, #103840, #106667, #102240, #98050, #103647, #96591, #105887; salvage #97843 #88604 #56824 #91413 #102808 #103657 #106890 #103321)](https://github.com/NousResearch/hermes-agent/pull/108130)** (by teknium1)
  - *Preview:* A damaged FTS5 index no longer kills turns or gets mislabelled as whole-file corruption, and the recovery lane (`hermes doctor`, `sessions repair`, `sessions recover`, `optimize-storage`) now handles ...
- **[feat: emit narrow runtime request success evidence](https://github.com/NousResearch/hermes-agent/pull/108129)** (by Poxel2)
  - *Preview:* Adds an opt-in, success-only hook carrying an opaque credential-pool entry ID, timestamp, request ID, provider and model.  Includes isolated full-turn integration coverage using a synthetic Credential...
- **[feat(telegram): optionally hide unauthenticated model providers](https://github.com/NousResearch/hermes-agent/pull/108128)** (by KoNit-K)
  - *Preview:* ## What does this PR do?  Adds an opt-in Telegram model-picker setting, telegram.show_all_providers: false, that hides provider rows without explicit authentication or configuration. The filter runs a...
- **[fix(desktop): sidebar no longer trapped by titlebar tabs on macOS (#107196 #107774 #107927 #106009 #107351, salvage #107209 #107223 #107456)](https://github.com/NousResearch/hermes-agent/pull/108125)** (by teknium1)
  - *Preview:* The macOS Desktop sidebar can no longer be trapped by the titlebar tabs: `SESSIONS` is fully readable, the zone chevron and ⌘B / the sidebar toggle round-trip, and gear / layout / HUD keep taking clic...
- **[feat(compression): make Codex auxiliary no-progress timeout configurable per task](https://github.com/NousResearch/hermes-agent/pull/108119)** (by chelsealong)
  - *Preview:* ## What does this PR do?  Adds a task-scoped `auxiliary.<task>.no_progress_timeout` config option (documented for `auxiliary.compression`) so operators can widen the Codex/Responses auxiliary stream's...
- **[Desktop: profile switches no longer spawn a duplicate primary or strand pool wakes, and a slot-cap timeout is actionable (#105082, #103230; salvage #102892 #103295 #105264)](https://github.com/NousResearch/hermes-agent/pull/108118)** (by teknium1)
  - *Preview:* Switching profiles in Desktop no longer spawns a duplicate primary backend that eats a pool slot forever, a replacement wake no longer times out racing an evicted child for its slot, and a real slot-c...
- **[feat(model): add per-model fast-mode overrides](https://github.com/NousResearch/hermes-agent/pull/108116)** (by KoNit-K)
  - *Preview:* ## What does this PR do?  Adds persistent per-model fast/priority-mode preferences through `agent.service_tier_overrides`, using the same tolerant model-key matching as `agent.reasoning_overrides`.  T...
- **[Desktop: clicking a pooled remote profile no longer storms reconnects while the VPS backend cold-starts (#107997, salvage #108009 #97914)](https://github.com/NousResearch/hermes-agent/pull/108112)** (by teknium1)
  - *Preview:* Clicking a pooled remote (SSH/VPS) profile no longer fails its dispatch probe against a backend that is merely cold-starting, so the probe→retire→reconnect→cold-start storm that pinned single-vCPU VPS...
- **[fix(gateway): Windows stop skips the drain wait when the event loop is provably wedged (#106359)](https://github.com/NousResearch/hermes-agent/pull/108110)** (by lEWFkRAD)
  - *Preview:* ## What does this PR do?  `hermes gateway stop` on Windows always paid the full planned-stop drain window (~30 s) before the bounded hard kill — even when the gateway's asyncio event loop is provably ...
- **[Desktop: hovering the Bots roster no longer spawns a backend per row (#103631, salvage #103634)](https://github.com/NousResearch/hermes-agent/pull/108107)** (by teknium1)
  - *Preview:* Hovering across the Bots roster no longer spawns a profile backend per row: every plugin-SDK warm now goes through the same guarded prewarm resolver as the built-in profile rail, so a pointer sweep ca...

## Other PRs

- [fix(desktop): recover trapped sidebars and keep titlebar controls clickable](https://github.com/NousResearch/hermes-agent/pull/108148)
- [fix(classifier): classify kimi reasoning_details invalid type as thinking_signature](https://github.com/NousResearch/hermes-agent/pull/108146)
- [fix(plugins): bound background discovery handoff](https://github.com/NousResearch/hermes-agent/pull/108144)
- [fix(tui): freeze event replay payloads within byte budget](https://github.com/NousResearch/hermes-agent/pull/108143)
- [Connectors reach installs with a saved toolset list (connections toolset auto-enable)](https://github.com/NousResearch/hermes-agent/pull/108142)
- [fix(desktop): accept named primary descriptor without profile](https://github.com/NousResearch/hermes-agent/pull/108140)
- [fix(compression): keep pre-compression messages visible after rotation](https://github.com/NousResearch/hermes-agent/pull/108138)
- [fix(gateway): surface Windows session id in `gateway status`, warn on Session 0](https://github.com/NousResearch/hermes-agent/pull/108133)
- [Price vendor-prefixed model ids on generic OpenAI-compatible routes](https://github.com/NousResearch/hermes-agent/pull/108124)
- [fix(agent): recover xAI OAuth stale-token 403s instead of aborting the turn](https://github.com/NousResearch/hermes-agent/pull/108123)
- [fix(desktop): keep collapsed pane chrome recoverable](https://github.com/NousResearch/hermes-agent/pull/108120)
- [fix(desktop): route the theme search copy through i18n](https://github.com/NousResearch/hermes-agent/pull/108117)
- [fix(desktop/radio): preserve stream on external pause for Fluid Voice resume](https://github.com/NousResearch/hermes-agent/pull/108115)
- [fix(desktop): skip non-primary local bot relay route](https://github.com/NousResearch/hermes-agent/pull/108111)
- [fix(mcp): stop removed servers from surviving in live gateways](https://github.com/NousResearch/hermes-agent/pull/108103)
- [fix(mcp): retire removed servers before reconnect](https://github.com/NousResearch/hermes-agent/pull/108099)
- [fix(desktop): yield the titlebar band only to mounted chrome](https://github.com/NousResearch/hermes-agent/pull/108098)
