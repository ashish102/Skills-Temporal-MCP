# Git Pull Request Examples

## Example 1: Basic GitHub PR with CLI
**User Request**: "Create a pull request for my feature"

**Steps**:
1. Verify branch is pushed
2. Create PR using commit message

**Commands**:
```bash
git status
git push
gh pr create --fill
```

**Output**:
```
Creating pull request for feature-awesome-thing into main in owner/repo

https://github.com/owner/repo/pull/42
```

---

## Example 2: PR with Custom Title and Description
**User Request**: "Create a PR titled 'Add user dashboard' with details"

**Steps**:
1. Check current branch
2. Create PR with specified details

**Commands**:
```bash
git branch --show-current
gh pr create \
  --title "Add user dashboard" \
  --body "Implements a new dashboard for users with analytics and settings"
```

---

## Example 3: PR with Reviewers and Labels
**User Request**: "Create a PR and request review from john and jane, mark it as a feature"

**Steps**:
1. Push branch if needed
2. Create PR with reviewers and labels

**Commands**:
```bash
git push
gh pr create \
  --fill \
  --reviewer john,jane \
  --label feature,needs-review
```

---

## Example 4: Draft PR for Work in Progress
**User Request**: "Create a draft PR so the team can see my progress"

**Steps**:
1. Ensure latest code is pushed
2. Create draft PR

**Commands**:
```bash
git push
gh pr create \
  --draft \
  --title "WIP: Refactor authentication module" \
  --body "Early work on refactoring. Not ready for review yet."
```

---

## Example 5: PR Linked to Issue
**User Request**: "Create a PR that closes issue #87"

**Steps**:
1. Include issue reference in PR description
2. Create PR

**Commands**:
```bash
gh pr create \
  --title "Fix login timeout bug" \
  --body "Resolves the login timeout issue.

Fixes #87"
```

---

## Example 6: GitLab Merge Request
**User Request**: "Create a merge request on GitLab"

**Steps**:
1. Verify GitLab remote
2. Create MR using glab CLI

**Commands**:
```bash
git remote -v
git push
glab mr create --fill
```

---

## Example 7: PR Without CLI Tool
**User Request**: "Create a PR but I don't have gh installed"

**Steps**:
1. Get repository URL
2. Construct and provide web URL
3. Guide user to web interface

**Commands**:
```bash
git remote -v
git branch --show-current
```

**Response**:
```
Please open this URL in your browser to create the pull request:
https://github.com/owner/repo/compare/main...feature-branch

Fill in:
- Title: [Your PR title]
- Description: [Details about changes]
- Reviewers: [Select team members]
```

---

## Example 8: PR to Different Base Branch
**User Request**: "Create a PR to merge my feature into the develop branch"

**Steps**:
1. Specify base and head branches
2. Create PR

**Commands**:
```bash
gh pr create \
  --base develop \
  --head feature-new-api \
  --title "Add new API endpoints" \
  --body "New endpoints for user management"
```

---

## Example 9: Check PR Status
**User Request**: "Check the status of my pull requests"

**Steps**:
1. List your open PRs
2. Check specific PR details

**Commands**:
```bash
gh pr list --author @me
gh pr status
gh pr checks
```

**Output**:
```
Current branch
  #42  Add user dashboard [feature-dashboard]
   - Checks passing - 3/3 ✓
   - Review required

Other branches
  #38  Fix bug in parser [bugfix-parser]  
   - Approved
   - Ready to merge
```

---

## Example 10: Interactive PR Creation
**User Request**: "Help me create a PR with all the details"

**Steps**:
1. Run interactive creation
2. Follow prompts

**Commands**:
```bash
gh pr create
```

**Interactive Prompts**:
```
? Where should we push the 'feature-branch' branch?  owner/repo

? Title Add awesome feature
? Body [(e) to launch vim, enter to skip] Implements the awesome feature
  - New component
  - Updated tests
  - Added documentation

? What's next? Submit
```

---

## Example 11: Create PR from Forked Repository
**User Request**: "Create a PR from my fork to the upstream repository"

**Steps**:
1. Ensure upstream is configured
2. Push to fork
3. Create PR to upstream

**Commands**:
```bash
git remote -v
git push origin feature-contribution
gh pr create \
  --repo upstream-owner/repo \
  --head your-username:feature-contribution \
  --title "Add new feature" \
  --body "Contributing a new feature to the project"
```

---

## Example 12: Full Workflow Example
**User Request**: "Walk me through creating a complete PR from scratch"

**Steps**:
1. Create feature branch
2. Make changes
3. Commit changes
4. Push to remote  
5. Create PR with all details
6. View PR in browser

**Commands**:
```bash
# Create feature branch
git checkout -b feature-user-profile
  
# Make changes to files
# ... edit files ...

# Stage and commit
git add .
git commit -m "Add user profile page

- Create profile component
- Add profile API endpoint  
- Update routing
- Add tests"

# Push to remote
git push -u origin feature-user-profile

# Create PR
gh pr create \
  --title "Add user profile page" \
  --body "Implements user profile functionality

## Changes
- New profile component with bio and avatar
- REST API endpoint for profile data
- Client-side routing updates
- Unit and integration tests

## Testing
1. Run \`npm test\`
2. Visit \`/profile/:userId\`
3. Verify profile displays correctly

## Screenshots
[Attach screenshots]

Closes #45" \
  --reviewer alice,bob \
  --label feature,frontend \
  --assignee @me

# Open PR in browser
gh pr view --web
```
