# Git Push Examples

## Example 1: Push Current Branch
User request: "Push my commits"

```bash
git branch --show-current
git remote -v
git push
```

## Example 2: First Push for New Branch
User request: "Push my new branch"

```bash
git branch --show-current
git push -u origin feature-branch
```

## Example 3: Remote Missing
User request: "Push to this repository URL"

```bash
git remote -v
git remote add origin https://github.com/username/repo.git
git push -u origin main
```
