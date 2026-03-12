# Git Pull Request Usage Guide

## Standard Sequence
Verify branch and push state:
```bash
git branch --show-current
git status
git remote -v
```

Create GitHub PR with defaults:
```bash
gh pr create --fill
```

Create GitHub PR with explicit metadata:
```bash
gh pr create --base main --title "<title>" --body "<description>"
```

Create GitLab MR:
```bash
glab mr create --fill
```

## Web Fallback
If CLI is unavailable, provide platform URL to open PR/MR from current branch.

GitHub pattern:
```text
https://github.com/OWNER/REPO/compare/main...BRANCH
```
