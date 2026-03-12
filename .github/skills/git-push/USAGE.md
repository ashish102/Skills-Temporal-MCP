# Git Push Usage Guide

## Standard Sequence
Check branch and commits:
```bash
git branch --show-current
git status
git log --oneline -n 5
```

Check remote:
```bash
git remote -v
```

First push for branch:
```bash
git push -u origin <branch>
```

Subsequent pushes:
```bash
git push
```

## Useful Variants
Push specific branch:
```bash
git push origin <branch>
```

Force push when explicitly requested:
```bash
git push --force-with-lease origin <branch>
```

Add remote when missing:
```bash
git remote add origin <remote-url>
```
