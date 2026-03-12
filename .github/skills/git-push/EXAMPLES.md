# Git Push Examples

## Example 1: Basic Push to Existing Remote
**User Request**: "Push my changes"

**Steps**:
1. Check status and what will be pushed
2. Verify remote configuration
3. Push to remote

**Commands**:
```bash
git status
git log origin/main..HEAD --oneline
git remote -v
git push
```

---

## Example 2: First Push of New Branch
**User Request**: "Push my new feature branch"

**Steps**:
1. Check current branch
2. See commits to be pushed
3. Push and set upstream tracking

**Commands**:
```bash
git branch --show-current
git log --oneline -5
git push -u origin feature-authentication
```

**Output**:
```
Branch 'feature-authentication' set up to track remote branch 'feature-authentication' from 'origin'.
```

---

## Example 3: Push to New Remote Repository
**User Request**: "Push to a new GitHub repository"

**Steps**:
1. Add remote
2. Verify remote was added
3. Push with upstream tracking

**Commands**:
```bash
git remote add origin https://github.com/username/my-project.git
git remote -v
git push -u origin main
```

---

## Example 4: Push with Tags
**User Request**: "Push my commits and the version tags"

**Steps**:
1. Show existing tags
2. Push commits and tags

**Commands**:
```bash
git tag
git push --follow-tags
# or push all tags explicitly
git push && git push --tags
```

---

## Example 5: Force Push After Rebase
**User Request**: "I rebased my branch and need to force push"

**Steps**:
1. Check commit history
2. Use safe force push
3. Verify push success

**Commands**:
```bash
git log origin/feature-branch..HEAD --oneline
git push --force-with-lease origin feature-branch
git log origin/feature-branch..HEAD
```

**Note**: Only force push on branches you own, never on shared branches!

---

## Example 6: Push Rejected - Remote Has New Changes
**User Request**: "My push was rejected"

**Steps**:
1. Check status
2. Pull remote changes
3. Resolve conflicts if any
4. Push again

**Commands**:
```bash
git status
git pull origin main
# If conflicts occur, resolve them
# git add <resolved-files>
# git commit
git push origin main
```

---

## Example 7: Push Specific Branch to Remote
**User Request**: "Push only my bugfix branch"

**Steps**:
1. Verify branch exists and has commits
2. Push specific branch

**Commands**:
```bash
git branch -vv
git log origin/bugfix-123..bugfix-123 --oneline
git push origin bugfix-123
```

---

## Example 8: Push All Branches
**User Request**: "Push all my branches to backup"

**Steps**:
1. Check all local branches
2. Push all branches

**Commands**:
```bash
git branch -a
git push --all origin
```

---

## Example 9: Delete Remote Branch
**User Request**: "Delete the old feature branch from remote"

**Steps**:
1. Verify branch exists on remote
2. Delete remote branch
3. Confirm deletion

**Commands**:
```bash
git branch -r | grep feature-old
git push origin --delete feature-old
git branch -r | grep feature-old
```

---

## Example 10: Setup and Push to Multiple Remotes
**User Request**: "Push to both GitHub and GitLab"

**Steps**:
1. Add both remotes
2. Verify remotes
3. Push to each

**Commands**:
```bash
git remote add github git@github.com:username/repo.git
git remote add gitlab git@gitlab.com:username/repo.git
git remote -v
git push github main
git push gitlab main
```
