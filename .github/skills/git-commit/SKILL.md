---
name: git-commit
description: Use when users ask to commit changes, save work, create a commit, stage files and commit, or commit and push. Ensures safe staging scope selection (all vs specific files), staged diff review, meaningful commit messages, and commit confirmation with hash.
---

# Git Commit Instructions
When the user asks to commit changes, follow these steps:
1. Check the current status of the repository using `git status` to see what files have changed.
2. If specific files are mentioned, stage only those files using `git add <files>`.
3. If no specific files are mentioned, ask the user if they want to stage all changes or specific files.
4. Before committing, show the user what will be committed using `git status` or `git diff --staged`.
5. Create a commit with a meaningful message. If the user provides a message, use it; otherwise, help craft one based on the changes.
6. After committing, confirm the commit was successful and show the commit hash.
7. Optionally show commit details using `git log` or `git show`.

Additional references:
- Overview: see OVERVIEW.md
- Usage details: see USAGE.md
- Examples: see EXAMPLES.md

