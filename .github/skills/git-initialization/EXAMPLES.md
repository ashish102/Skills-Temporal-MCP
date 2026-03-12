# Git Initialization Examples

## Example 1: Initialize Repository
User request: "Initialize git here"

```bash
git status
git init -b main
git status
```

## Example 2: Initialize with Local Identity
User request: "Initialize git and set my identity"

```bash
git init -b main
git config user.name "Jane Smith"
git config user.email "jane@example.com"
git config --list
```

## Example 3: Initialize and Create First Commit
User request: "Initialize and make initial commit"

```bash
git init -b main
git add -A
git commit -m "Initial commit"
git log --oneline -n 1
```
