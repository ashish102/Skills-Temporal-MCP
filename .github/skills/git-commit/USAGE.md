# Git Commit Usage Guide

## Standard Sequence
```bash
git status
```

If user specifies files:
```bash
git add <file1> <file2>
```

If user confirms all changes:
```bash
git add -A
```

Review staged content:
```bash
git diff --staged
```

Commit:
```bash
git commit -m "<meaningful message>"
```

Confirm:
```bash
git log --oneline -n 1
```

## Useful Variants
Unstage a file:
```bash
git restore --staged <file>
```

Amend last commit:
```bash
git commit --amend --no-edit
```
