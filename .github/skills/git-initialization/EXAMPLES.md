# Git Initialization Examples

## Example 1: Basic Initialization
**User Request**: "Initialize a git repository"

**Steps**:
1. Check if `.git` exists
2. Run `git init`
3. Confirm initialization

**Commands**:
```bash
git status 2>&1 | grep -q "not a git repository"
git init
```

**Output**:
```
Initialized empty Git repository in /path/to/project/.git/
```

---

## Example 2: Initialize with Configuration
**User Request**: "Initialize git and set my name as John Doe"

**Steps**:
1. Check for existing repository
2. Initialize repository
3. Set user configuration
4. Verify configuration

**Commands**:
```bash
git init
git config user.name "John Doe"
git config user.email "john.doe@example.com"
git config --list | grep user
```

---

## Example 3: Initialize with Initial Commit
**User Request**: "Initialize git and create an initial commit"

**Steps**:
1. Initialize repository
2. Stage all files
3. Create initial commit
4. Show commit log

**Commands**:
```bash
git init -b main
git add .
git commit -m "Initial commit"
git log --oneline
```

---

## Example 4: Checking Existing Repository
**User Request**: "Is this a git repository?"

**Steps**:
1. Check git status
2. Report findings

**Commands**:
```bash
git status
```

**Possible Outputs**:
- If repository exists: Shows branch and status information
- If no repository: "fatal: not a git repository (or any of the parent directories): .git"

---

## Example 5: Full Setup Flow
**User Request**: "Set up git for this project with my credentials"

**Steps**:
1. Initialize repository with main branch
2. Set user configuration
3. Create .gitignore
4. Stage and commit initial files

**Commands**:
```bash
git init -b main
git config user.name "Jane Smith"
git config user.email "jane@example.com"
echo "node_modules/\n.env\n.DS_Store" > .gitignore
git add .
git commit -m "Initial commit with project setup"
```
