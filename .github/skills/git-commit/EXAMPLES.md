# Git Commit Examples

## Example 1: Basic Commit All Changes
**User Request**: "Commit all my changes"

**Steps**:
1. Check status
2. Show what will be committed
3. Stage all changes
4. Create commit

**Commands**:
```bash
git status
git add .
git status
git commit -m "Add new features and bug fixes"
```

---

## Example 2: Commit Specific Files
**User Request**: "Commit only the README and config files"

**Steps**:
1. Check status
2. Stage specific files
3. Verify what's staged
4. Create commit

**Commands**:
```bash
git status
git add README.md config.json
git status
git commit -m "Update README and configuration"
```

---

## Example 3: Commit with Detailed Message
**User Request**: "Commit the authentication changes with a detailed message"

**Steps**:
1. Stage relevant files
2. Create commit with multi-line message

**Commands**:
```bash
git add src/auth/
git commit -m "Implement JWT-based authentication

- Add JWT token generation and validation
- Implement refresh token mechanism
- Add middleware for protected routes
- Update user model with token fields

Refs: #123"
```

---

## Example 4: Review Before Committing
**User Request**: "Let me review the changes before committing"

**Steps**:
1. Show status
2. Show diff of changes
3. Stage changes
4. Show staged diff
5. Commit after approval

**Commands**:
```bash
git status
git diff
git add .
git diff --staged
git commit -m "Implement feature X"
```

---

## Example 5: Amend Last Commit
**User Request**: "I forgot to add a file to my last commit"

**Steps**:
1. Stage the forgotten file
2. Amend the previous commit
3. Verify the change

**Commands**:
```bash
git add forgotten_file.py
git commit --amend --no-edit
git show
```

---

## Example 6: Partial Commit with Interactive Staging
**User Request**: "I want to commit only some changes from this file"

**Steps**:
1. Use interactive staging
2. Select which hunks to stage
3. Commit staged changes

**Commands**:
```bash
git add -p myfile.py
# Select 'y' for changes to include, 'n' for changes to skip
git commit -m "Partially update myfile.py"
```

---

## Example 7: Commit After Checking Modified Files
**User Request**: "Commit my work on the data processing module"

**Steps**:
1. Check what's modified
2. Stage module files
3. Review changes
4. Commit with descriptive message

**Commands**:
```bash
git status
git add src/data_processing/
git diff --staged --stat
git commit -m "Refactor data processing module

- Improve error handling
- Add input validation
- Optimize performance for large datasets"
```
