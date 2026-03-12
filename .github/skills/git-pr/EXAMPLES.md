# Git Pull Request Examples

## Example 1: Create GitHub PR
User request: "Create a PR for this branch"

```bash
git branch --show-current
git push
gh pr create --fill
```

## Example 2: Create PR with Explicit Base
User request: "Create PR to develop branch"

```bash
gh pr create --base develop --title "Add API endpoint" --body "Implements endpoint and tests"
```

## Example 3: No CLI Available
User request: "Create PR but gh is not installed"

```bash
git remote -v
git branch --show-current
```

Provide URL pattern:
```text
https://github.com/OWNER/REPO/compare/main...BRANCH
```
