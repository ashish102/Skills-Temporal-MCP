# Git Initialization Usage Guide

## Basic Usage

### Check for Existing Repository
```bash
git status
# or
test -d .git && echo "Git repo exists" || echo "No Git repo"
```

### Initialize New Repository
```bash
git init
```

### Initialize with Initial Branch Name
```bash
git init -b main
# or
git init --initial-branch=main
```

## Configuration Setup

### Set User Information
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Set Global Configuration
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Verify Configuration
```bash
git config --list
```

## Initial Commit Creation

### Stage All Files
```bash
git add .
```

### Create Initial Commit
```bash
git commit -m "Initial commit"
```

## Common Workflows

### Full Initialization Flow
1. Check for existing repository
2. Initialize if needed
3. Set up configuration (if not globally configured)
4. Create .gitignore file (optional)
5. Stage initial files
6. Create initial commit

### Reinitialize Repository
```bash
# This is safe - doesn't destroy existing history
git init
```

## Error Handling
- **Already initialized**: Inform user, no action needed
- **No write permissions**: Check directory permissions
- **Git not installed**: Verify Git installation
