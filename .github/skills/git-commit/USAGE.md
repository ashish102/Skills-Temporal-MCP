# Git Commit Usage Guide

## Basic Usage

### Check Repository Status
```bash
git status
```

### View Changes
```bash
# View unstaged changes
git diff

# View staged changes
git diff --staged
# or
git diff --cached
```

## Staging Files

### Stage All Changes
```bash
git add .
# or
git add -A
```

### Stage Specific Files
```bash
git add file1.txt file2.py
```

### Stage by Pattern
```bash
git add *.py
git add src/
```

### Interactive Staging
```bash
git add -p
# This allows you to stage changes in chunks
```

### Unstage Files
```bash
git reset HEAD <file>
# or in newer Git versions
git restore --staged <file>
```

## Creating Commits

### Basic Commit
```bash
git commit -m "Commit message"
```

### Multi-line Commit Message
```bash
git commit -m "Short summary

Detailed description of changes
- Point 1
- Point 2"
```

### Commit with Editor
```bash
git commit
# Opens default editor for message
```

### Stage and Commit in One Step
```bash
# Only for tracked files
git commit -am "Commit message"
```

### Amend Last Commit
```bash
# Change commit message
git commit --amend -m "New message"

# Add more changes to last commit
git add forgotten_file.txt
git commit --amend --no-edit
```

## Viewing Commits

### Show Recent Commits
```bash
git log
git log --oneline
git log -n 5  # Last 5 commits
```

### Show Commit Details
```bash
git show
git show <commit-hash>
```

### Show Commit Stats
```bash
git log --stat
```

## Commit Message Best Practices

### Format
```
Short summary (50 chars or less)

More detailed explanation (wrap at 72 chars)
- What was changed
- Why it was changed
- Any breaking changes or important notes

Refs: #issue-number (if applicable)
```

### Good Examples
- "Add user authentication feature"
- "Fix null pointer exception in data parser"
- "Update dependencies to latest versions"
- "Refactor database connection logic"

### Avoid
- "Fixed stuff"
- "WIP"
- "asdf"
- "Updated files"
