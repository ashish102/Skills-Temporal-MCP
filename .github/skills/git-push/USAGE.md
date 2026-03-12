# Git Push Usage Guide

## Basic Usage

### Check What Will Be Pushed
```bash
# Check if there are commits to push
git status

# See commits not yet pushed
git log origin/main..HEAD

# See commits with details
git log origin/main..HEAD --oneline
```

### View Remote Configuration
```bash
# List all remotes
git remote -v

# Show remote details
git remote show origin
```

## Pushing Changes

### Basic Push
```bash
# Push current branch (if upstream is set)
git push

# Push specific branch
git push origin main
```

### First Push (Set Upstream)
```bash
# Push and set upstream tracking
git push -u origin main
# or
git push --set-upstream origin feature-branch
```

### Push to Different Remote
```bash
git push upstream main
git push backup --all
```

### Push All Branches
```bash
git push --all origin
```

### Push Tags
```bash
# Push specific tag
git push origin v1.0.0

# Push all tags
git push --tags

# Push commits and tags together
git push --follow-tags
```

## Advanced Push Operations

### Force Push (Use with Caution!)
```bash
# Safer force push - fails if someone else pushed
git push --force-with-lease origin main

# Dangerous force push - overwrites remote (avoid!)
git push --force origin main
```

### Delete Remote Branch
```bash
git push origin --delete feature-branch
# or
git push origin :feature-branch
```

### Push with Specific Refspec
```bash
# Push local branch to different remote branch name
git push origin local-branch:remote-branch
```

## Setting Up Remotes

### Add Remote
```bash
git remote add origin https://github.com/username/repo.git
# or with SSH
git remote add origin git@github.com:username/repo.git
```

### Change Remote URL
```bash
git remote set-url origin https://github.com/username/new-repo.git
```

### Remove Remote
```bash
git remote remove origin
```

## Troubleshooting

### Push Rejected (Remote Has Changes)
```bash
# Pull and merge first
git pull origin main
# or rebase
git pull --rebase origin main
# Then push
git push origin main
```

### Authentication Issues
```bash
# For HTTPS, check credentials
git config credential.helper

# For SSH, verify key
ssh -T git@github.com
```

### Large File Issues
```bash
# Check file sizes
git ls-files -z | xargs -0 du -h | sort -h

# Consider using Git LFS
git lfs install
git lfs track "*.psd"
```

## Best Practices

1. **Always pull before pushing** to avoid conflicts
2. **Review commits** before pushing with `git log`
3. **Use meaningful branch names** for feature branches
4. **Don't force push** to shared branches (main/master)
5. **Push regularly** to back up work and enable collaboration
6. **Use SSH keys** for better security than HTTPS passwords
7. **Check push status** with `git status` after pushing
