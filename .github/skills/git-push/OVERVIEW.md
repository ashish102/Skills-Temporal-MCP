# Git Push Skill Overview

## Purpose
Push local commits safely to a configured remote.

## Flow Summary
1. Confirm there are commits to push.
2. Verify remote configuration.
3. Check current branch and upstream.
4. Use first-push or regular push command as appropriate.
5. Confirm push result and remote destination.

## Guardrails
- If no remote exists, ask before adding one.
- Only force push when user explicitly asks.
- Prefer `--force-with-lease` over `--force`.

## Prerequisites
- Repository has local commits.
- Remote is reachable and user has permission.
