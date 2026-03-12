---
name: git-pr
description: Use when users ask to create a pull request, open a PR, submit changes for review, or push and create PR. Verifies branch/remote readiness, gathers PR metadata, uses platform-specific CLI when available, and returns the resulting PR URL.
---

# Git Pull Request Instructions
When the user asks to create a pull request, follow these steps:
1. Verify the current branch is not the target branch (e.g., not on main/master).
2. Ensure all commits are pushed to the remote repository.
3. Determine the platform (GitHub, GitLab, Bitbucket) from the remote URL.
4. For GitHub:
   - Use GitHub CLI (`gh pr create`) if available
   - Or provide the web URL to create PR manually
5. For GitLab:
   - Use GitLab CLI (`glab mr create`) if available
   - Or provide the web URL
6. Gather PR details:
   - Title (use latest commit message as default)
   - Description/body
   - Target branch (usually main/master)
   - Reviewers (if specified)
   - Labels (if specified)
7. Create the PR and provide the URL to view it.
8. If CLI tools are not available, provide web URLs and instructions.

Additional references:
- Overview: see OVERVIEW.md  
- Usage details: see USAGE.md
- Examples: see EXAMPLES.md
