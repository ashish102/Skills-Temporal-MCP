# Git Pull Request Skill Overview

## Purpose
Create a pull request or merge request from the current branch.

## Flow Summary
1. Confirm current branch is not target branch.
2. Ensure commits are pushed.
3. Detect hosting platform from remote URL.
4. Use platform CLI when available.
5. Otherwise provide web URL and required fields.
6. Return created PR URL.

## Guardrails
- Do not create PR from `main`/`master` to itself.
- Collect missing metadata (title/body/base/reviewers) before creation.

## Prerequisites
- Branch is pushed and user has repo access.
