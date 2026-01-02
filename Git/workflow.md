# Daily Git Workflow Guide

## Getting Started Each Day

### 1. Pull Latest Changes

Before you start working, update your local branch with the latest changes from the remote repository.

```bash
$ git pull origin main
```

This fetches and merges changes from the remote branch into your current branch.

---

## Making Changes

### 2. Create or Switch to a Branch

Create a new branch for your feature or fix. Branch names should be descriptive.

```bash
$ git checkout -b feature/your-feature-name
```

Or switch to an existing branch:

```bash
$ git checkout branch-name
```

### 3. Make Your Modifications

Edit the files you need to change using your editor.

### 4. Check Your Changes

View what files have been modified:

```bash
$ git status
```

View the specific changes made to files:

```bash
$ git diff
```

---

## Saving Your Work

### 5. Stage Your Changes

Add files to the staging area before committing. You can stage specific files:

```bash
$ git add path/to/file.js
```

Or stage all changes:

```bash
$ git add .
```

### 6. Commit Your Changes

Create a meaningful commit message describing what you changed. Use present tense and be concise.

```bash
$ git commit -m "Add user authentication feature"
```

For more detailed commit messages:

```bash
$ git commit
```

This opens an editor where you can write a detailed message.

### 7. Push Your Changes

Upload your commits to the remote repository:

```bash
$ git push origin feature/your-feature-name
```

---

## Creating and Merging Pull Requests

### 8. Create a Pull Request

After pushing your branch, go to GitHub and create a pull request (PR):

1. Navigate to your repository on GitHub
2. Click the "Pull requests" tab
3. Click "New pull request"
4. Select your branch as the "compare" branch and `main` as the "base" branch
5. Add a clear title and description of your changes
6. Click "Create pull request"

### 9. Request Review

- Assign reviewers to your PR
- Address any feedback or comments
- Make additional commits to the same branch if changes are requested
- These new commits automatically appear in the PR

### 10. Merge the Pull Request

Once approved:

1. Click "Merge pull request" on GitHub
2. Choose a merge strategy (typically "Create a merge commit")
3. Click "Confirm merge"
4. Delete the branch after merging (optional but recommended)

---

## Working with Branches

### List Branches

View all local branches:

```bash
$ git branch
```

View all branches (local and remote):

```bash
$ git branch -a
```

### Delete a Branch

After merging, delete the local branch:

```bash
$ git branch -d feature/your-feature-name
```

Force delete (if not fully merged):

```bash
$ git branch -D feature/your-feature-name
```

### Rename a Branch

```bash
$ git branch -m old-branch-name new-branch-name
```

---

## Handling Merge Conflicts

### Understanding Conflicts

Merge conflicts occur when two branches modify the same lines in a file. Git cannot automatically decide which changes to keep.

### 11. Identify Conflicts

After pulling or attempting to merge, Git will mark conflicted files:

```bash
$ git status
```

### 12. Resolve Conflicts

Open the conflicted files in your editor. You'll see markers like:

```
<<<<<<< HEAD
Your changes here
=======
Their changes here
>>>>>>> branch-name
```

**Decide what to keep:**

- Keep your changes only (remove the markers and their changes)
- Keep their changes only (remove the markers and your changes)
- Keep both (remove the markers and merge the logic)

### 13. Complete the Merge

After resolving conflicts:

```bash
$ git add .
$ git commit -m "Resolve merge conflict"
$ git push origin your-branch-name
```

---

## Daily Workflow Summary

1. **Pull** latest changes: `git pull origin main`
2. **Create/Switch** to a branch: `git checkout -b feature/name`
3. **Modify** files in your editor
4. **Check** status: `git status` and `git diff`
5. **Stage** changes: `git add .`
6. **Commit** changes: `git commit -m "message"`
7. **Push** to remote: `git push origin branch-name`
8. **Create** a pull request on GitHub
9. **Resolve** any conflicts if needed
10. **Merge** the PR after approval
11. **Delete** the branch when complete

---

## Useful Commands Reference

| Command                   | Purpose                                           |
| ------------------------- | ------------------------------------------------- |
| `git status`              | Show current branch and modified files            |
| `git log`                 | View commit history                               |
| `git log --oneline`       | View compact commit history                       |
| `git diff`                | Show changes not yet staged                       |
| `git diff --staged`       | Show staged changes                               |
| `git stash`               | Temporarily save uncommitted changes              |
| `git stash pop`           | Restore stashed changes                           |
| `git reset HEAD file.js`  | Unstage a file                                    |
| `git checkout -- file.js` | Discard changes to a file                         |
| `git rebase main`         | Update your branch with main without merge commit |
