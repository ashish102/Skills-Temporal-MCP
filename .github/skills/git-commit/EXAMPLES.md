# Git Commit Examples

## Example 1: Commit Specific Files
User request: "Commit only README and config changes"

```bash
git status
git add README.md config.json
git diff --staged
git commit -m "Update README and config"
git log --oneline -n 1
```

## Example 2: Commit All Changes (Explicit)
User request: "Commit all changes"

```bash
git status
git add -A
git diff --staged
git commit -m "Refactor data processing"
git log --oneline -n 1
```

## Example 3: Amend Last Commit
User request: "Add one missed file to previous commit"

```bash
git add missed_file.py
git commit --amend --no-edit
git show --stat --oneline -n 1
```
