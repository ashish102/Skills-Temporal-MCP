# Git Pull Request Usage Guide

## GitHub CLI (gh)

### Installation
```bash
# Windows (via winget)
winget install GitHub.cli

# macOS
brew install gh

# Linux (Debian/Ubuntu)
sudo apt install gh
```

### Authentication
```bash
gh auth login
```

### Basic Pull Request Creation

#### Create PR with Interactive Prompts
```bash
gh pr create
```

#### Create PR with Inline Options
```bash
gh pr create --title "Add new feature" --body "Description of changes"
```

#### Create PR Using Commit Message
```bash
gh pr create --fill
```

### Advanced PR Options

#### Set Target Branch
```bash
gh pr create --base main --head feature-branch
```

#### Add Reviewers
```bash
gh pr create --reviewer username1,username2
```

#### Add Assignees
```bash
gh pr create --assignee @me
```

#### Add Labels
```bash
gh pr create --label bug,urgent
```

#### Create Draft PR
```bash
gh pr create --draft
```

#### Link to Issue
```bash
gh pr create --body "Fixes #123"
```

### View and Manage PRs

#### List PRs
```bash
gh pr list
gh pr list --state open
gh pr list --author @me
```

#### View PR Details
```bash
gh pr view
gh pr view 123
gh pr view --web
```

#### Check PR Status
```bash
gh pr status
gh pr checks
```

## GitLab CLI (glab)

### Installation
```bash
# Windows (via scoop)
scoop install glab

# macOS
brew install glab

# Linux
sudo apt install glab
```

### Authentication
```bash
glab auth login
```

### Create Merge Request

#### Basic Creation
```bash
glab mr create
```

#### With Options
```bash
glab mr create --title "Add feature" --description "Details" --target-branch main
```

#### Fill from Commits
```bash
glab mr create --fill
```

#### Add Reviewers
```bash
glab mr create --reviewer username
```

#### Create Draft MR
```bash
glab mr create --draft
```

#### Add Labels
```bash
glab mr create --label "bug,critical"
```

### View Merge Requests

#### List MRs
```bash
glab mr list
glab mr view 42
```

## Without CLI Tools

### GitHub Web URL
```bash
# Get repository info
git remote -v

# Construct URL
https://github.com/OWNER/REPO/compare/main...BRANCH
```

### GitLab Web URL
```bash
https://gitlab.com/OWNER/REPO/-/merge_requests/new?merge_request[source_branch]=BRANCH
```

### Bitbucket Web URL
```bash
https://bitbucket.org/OWNER/REPO/pull-requests/new?source=BRANCH
```

## Best Practices

### PR Title
- Be descriptive and concise
- Use imperative mood: "Add feature" not "Added feature"
- Include ticket/issue number if applicable

### PR Description
Include:
- **What**: Summary of changes
- **Why**: Reason for changes
- **How**: Technical approach
- **Testing**: How to test the changes
- **Screenshots**: For UI changes
- **Related Issues**: Links to issues

### Example Template
```markdown
## What
Implements user authentication using JWT tokens.

## Why
Required for securing API endpoints and managing user sessions.

## How
- Added JWT middleware
- Created auth service
- Updated user model
- Added login/logout endpoints

## Testing
1. Run `npm test`
2. Test login at `/api/auth/login`
3. Verify protected routes require token

## Related
Closes #123
```

## Common Workflows

### Workflow 1: Feature Branch PR
```bash
# Create and switch to feature branch
git checkout -b feature-new-ui

# Make changes and commit
git add .
git commit -m "Implement new UI components"

# Push to remote
git push -u origin feature-new-ui

# Create PR
gh pr create --fill
```

### Workflow 2: Fix Bug with PR
```bash
# Create bugfix branch
git checkout -b fix-validation-bug

# Fix and commit
git commit -am "Fix email validation bug"

# Push
git push -u origin fix-validation-bug

# Create PR with label
gh pr create --fill --label bug
```

### Workflow 3: Draft PR for Early Feedback
```bash
# Create and push branch
git checkout -b experimental-feature
git push -u origin experimental-feature

# Create draft PR
gh pr create --draft --title "WIP: Experimental feature"
```
