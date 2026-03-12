```skill
---
name: git-initialization
description: Use this skill to initialize a new Git repository or check if one already exists.
---

# Git Initialization Instructions
When the user asks to initialize a Git repository, follow these steps:
1. Check if a Git repository already exists in the current directory using `git status` or by checking for a `.git` folder.
2. If a repository exists, inform the user and ask if they want to reinitialize.
3. If no repository exists, run `git init` to initialize a new repository.
4. Optionally set up initial configuration (user.name, user.email) if provided by the user.
5. Optionally create an initial commit if requested.

Additional references:
- Overview: see OVERVIEW.md
- Usage details: see USAGE.md
- Examples: see EXAMPLES.md

```
