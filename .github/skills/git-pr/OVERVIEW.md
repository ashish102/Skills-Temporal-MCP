# Git Pull Request Skill Overview

## Purpose
This skill handles the creation of pull requests (PRs) on remote Git platforms like GitHub, GitLab, and Bitbucket. It streamlines the process of proposing code changes for review and merging.

## Key Features
- **Multi-Platform Support**: Works with GitHub, GitLab, Bitbucket, and other platforms
- **CLI Integration**: Uses platform-specific CLI tools (gh, glab) when available
- **Web Fallback**: Provides web URLs when CLI tools are unavailable
- **Smart Defaults**: Uses commit messages and branch names for PR title/description
- **Full Customization**: Supports reviewers, labels, draft status, and more
- **Pre-flight Checks**: Validates branch status and push state before creating PR

## When to Use
- Proposing code changes for review
- Contributing to open source projects
- Collaborating on team projects
- Requesting code review before merging
- Documenting changes with detailed descriptions

## Platform Support

### GitHub (gh CLI)
- Create, view, edit, and merge PRs
- Set reviewers, assignees, labels
- Create draft PRs
- Link to issues
- Auto-fill from commit messages

### GitLab (glab CLI)
- Create merge requests
- Set reviewers and approvers
- Add labels and milestones
- Create draft/WIP MRs
- Link to issues

### Bitbucket
- Create pull requests via web
- Set reviewers
- Link to JIRA issues

## Prerequisites
- Branch with commits pushed to remote
- Not currently on the target branch (main/master)
- Platform CLI tool installed (recommended):
  - GitHub: `gh` CLI
  - GitLab: `glab` CLI
- Authentication configured for the platform
- Write access to create PRs in the repository
