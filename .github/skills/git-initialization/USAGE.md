# Git Initialization Usage Guide

## Standard Sequence
Check repository state:
```bash
git status
```

Initialize when needed:
```bash
git init -b main
```

Optional local config:
```bash
git config user.name "Your Name"
git config user.email "you@example.com"
```

Optional initial commit:
```bash
git add -A
git commit -m "Initial commit"
```

## Useful Checks
```bash
git config --list
git log --oneline -n 1
```
