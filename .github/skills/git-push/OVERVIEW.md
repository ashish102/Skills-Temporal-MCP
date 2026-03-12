# Git Push Skill Overview

## Purpose
This skill handles pushing local Git commits to remote repositories. It ensures safe and proper synchronization of local work with remote repositories on platforms like GitHub, GitLab, or Bitbucket.

## Key Features
- **Remote Verification**: Check that remote repositories are properly configured
- **Branch Tracking**: Set up upstream branch tracking for new branches
- **Safety Checks**: Verify what will be pushed before executing
- **Force Push Protection**: Use `--force-with-lease` instead of `--force` for safety
- **Tag Management**: Support for pushing tags along with commits
- **Error Handling**: Handle authentication, conflicts, and network issues

## When to Use
- Sharing local commits with team members
- Backing up work to a remote repository  
- Deploying code to production or staging environments
- Synchronizing changes across multiple machines
- Publishing open source contributions

## Safety Considerations
- Always review what's being pushed before executing
- Avoid force pushing to shared branches (main/master)
- Use `--force-with-lease` instead of `--force` when necessary
- Ensure you have proper authentication credentials
- Be cautious with sensitive data (passwords, API keys)

## Prerequisites
- Git repository must have commits to push
- Remote repository must be configured
- User must have push access to the remote repository
- Network connectivity to the remote server
- Proper authentication (SSH keys or HTTPS credentials)
