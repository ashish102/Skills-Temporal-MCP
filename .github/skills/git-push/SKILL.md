---
name: git-push
description: Use when users ask to push changes, publish commits, sync branch to remote, set upstream, or commit and push. Verifies commits to push, remote configuration, branch/upstream status, and performs safe push with clear handling for first push and rejected pushes.
---

# Git Push Instructions
When the user asks to push changes, follow these steps:
1. Check if there are local commits to push using `git status` or `git log origin/<branch>..HEAD`.
2. Verify the remote repository is configured using `git remote -v`.
3. If no remote exists, ask the user if they want to add one and guide them through it.
4. Check the current branch name using `git branch --show-current`.
5. Determine if this is the first push (no upstream branch) or a subsequent push.
6. For first push, use `git push -u origin <branch>` to set upstream tracking.
7. For subsequent pushes, use `git push` or `git push origin <branch>`.
8. Handle common scenarios:
   - Force push (only if user explicitly requests): `git push --force-with-lease`
   - Push tags: `git push --tags`
   - Push specific branch: `git push origin <branch>`
9. After pushing, confirm success and show the remote URL where changes were pushed.

Additional references:
- Overview: see OVERVIEW.md
- Usage details: see USAGE.md
- Examples: see EXAMPLES.md
