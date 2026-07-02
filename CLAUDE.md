# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **Claude Code personal configuration monorepo** — not a traditional software project. It stores custom slash commands, agent definitions, reusable skills, prompts, and utility scripts. The repo lives at `D:\claudegithub` with a secondary working directory at `C:\Users\c_w_l` for user-level Claude config (~/.claude/rules/, ~/.claude/agents/, ~/.claude/settings.json).

### Directory Map

| Directory | Purpose |
|-----------|---------|
| `.claude/` | Project-level Claude Code config: `settings.json`, `settings.local.json`, and `commands/` (custom slash commands) |
| `01-slash-commands/` | Source originals for custom slash commands; copied into `.claude/commands/` when activated |
| `agenthub/` | Shared agent/skill/prompt registry for team use via VS Code "Agent Resources" extension |
| `agenthub/.agents/` | Agent definitions (`*.agent.md`) |
| `agenthub/.skills/` | Reusable skills (subdirectories containing `SKILL.md`) |
| `agenthub/.prompts/` | Reusable prompt templates (`*.prompt.md`) |
| `claude-Re/` | Separate git repo for Claude Code experiments (referenced, not a submodule) |
| `test/` | Python utility scripts (DeepSeek API wrappers for summarization and translation) |

### Custom Slash Commands

- **`/optimize`** — Analyzes codebase for performance, readability, and maintainability improvements. Source at `01-slash-commands/optimize.md`, installed at `.claude/commands/optimize.md`.

### Settings

- `.claude/settings.json` — Project-level: allows reads under `C:\Users\c_w_l` and adds it as an additional working directory.
- `.claude/settings.local.json` — Local overrides: allows `WebFetch` (github.com), `WebSearch`, `git *` commands, and the copy command that installs the optimize slash command.
- User-level config at `~/.claude/settings.json` controls permissions, hooks, and model preferences globally.

### Python Scripts (`test/`)

- `summarizer.py` — Summarizes Chinese text to one sentence via DeepSeek API.
- `translate.py` — CLI translation tool (Chinese ↔ English) via DeepSeek API. Supports `-i`/`-o` for file I/O and `--to` for target language.

**Required env var:** `DEEPSEEK_API_KEY` must be set in `.env` or environment. Scripts use `openai` package pointed at `https://api.deepseek.com`.

```bash
# Run the translator
python test/translate.py "你好世界" --to 英文
python test/translate.py -i input.txt -o output.txt --to 中文
```

---

## Behavioral Guidelines

Guidelines to reduce common LLM coding mistakes. **Tradeoff:** bias toward caution over speed. For trivial tasks, use judgment.

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
