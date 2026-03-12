# Git Initialization Skill Overview

## Purpose
Initialize Git safely, or confirm that a repository already exists.

## Flow Summary
1. Check whether `.git` already exists.
2. If initialized, report state and ask before reinitializing.
3. If not initialized, run `git init`.
4. Optionally set `user.name` and `user.email`.
5. Optionally create an initial commit.

## Guardrails
- Do not assume reinitialization intent.
- Keep branch naming explicit when needed (`main`).

## Prerequisites
- Git is installed.
- User has write access to the workspace.
