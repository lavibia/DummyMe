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

### Understanding Branches

A branch is an independent line of development. The main branch (typically `main` or `master`) is your production-ready code. Feature branches are temporary branches where you develop new features or fixes.

### Branching Strategy

Follow a consistent naming convention:

- `feature/feature-name` - New features
- `bugfix/bug-name` - Bug fixes
- `hotfix/issue-name` - Urgent production fixes
- `refactor/description` - Code refactoring

### Create a New Branch

Create a branch from the current branch (usually `main`):

```bash
$ git checkout -b feature/your-feature-name
```

Or create a branch and track a remote branch:

```bash
$ git checkout -b feature/your-feature-name origin/feature/your-feature-name
```

### List Branches

View all local branches:

```bash
$ git branch
```

View all branches (local and remote):

```bash
$ git branch -a
```

View branches with last commit info:

```bash
$ git branch -v
```

### Switch Between Branches

Switch to an existing branch:

```bash
$ git checkout branch-name
```

Or use the newer syntax:

```bash
$ git switch branch-name
```

### Delete a Branch

Delete a local branch (only if fully merged):

```bash
$ git branch -d feature/your-feature-name
```

Force delete (if not fully merged):

```bash
$ git branch -D feature/your-feature-name
```

Delete a remote branch:

```bash
$ git push origin --delete feature/your-feature-name
```

### Rename a Branch

Rename the current branch:

```bash
$ git branch -m new-branch-name
```

Rename a different branch:

```bash
$ git branch -m old-branch-name new-branch-name
```

### Update Your Branch with Latest Changes

Keep your branch up-to-date with the main branch using rebase (keeps history clean):

```bash
$ git rebase origin/main
```

Or using merge (creates a merge commit):

```bash
$ git merge origin/main
```

**Rebase vs Merge:**

- **Rebase**: Replays your commits on top of the latest main branch. Creates a clean, linear history. Use for local branches.
- **Merge**: Creates a merge commit combining both branches. Preserves complete history. Use when merging to main.

---

## Git Merge Strategies

Merging combines changes from one branch into another. There are several merge strategies to understand:

### 1. Merge Commit (Three-Way Merge)

Creates a merge commit that ties together the histories of both branches. Use this when merging feature branches to main.

```bash
$ git merge feature/your-feature-name
```

This creates a commit like: "Merge branch 'feature/your-feature-name' into main"

**Best for:** Integrating feature branches to main; preserves complete history

### 2. Fast-Forward Merge

When your branch has no diverging commits from main, Git simply moves the main pointer forward. No merge commit is created.

```bash
$ git merge feature/your-feature-name
```

**Best for:** Keeping history clean when working on isolated features

To force a merge commit even if fast-forward is possible:

```bash
$ git merge --no-ff feature/your-feature-name
```

### 3. Squash Merge

Combines all commits from the feature branch into a single commit on main. Useful for keeping main branch clean.

```bash
$ git merge --squash feature/your-feature-name
```

After squashing, you still need to commit:

```bash
$ git commit -m "Add new feature"
```

**Best for:** Keeping main branch history concise; useful for PR workflows

### 4. Rebase and Merge

Replays feature branch commits on top of main, then fast-forwards. Creates clean, linear history without merge commits.

```bash
$ git rebase main
$ git checkout main
$ git merge feature/your-feature-name
```

Or combined with one command (available in some Git versions):

```bash
$ git merge --rebase feature/your-feature-name
```

**Best for:** Maintaining linear history; preferred by many teams for feature branches

### Merge from Command Line

To merge a branch into your current branch:

```bash
$ git merge source-branch-name
```

### Abort a Merge

If you start a merge and want to cancel:

```bash
$ git merge --abort
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
| `git merge branch-name`   | Merge a branch into current branch                |
| `git merge --squash`      | Squash all commits before merging                 |
| `git merge --no-ff`       | Force merge commit even if fast-forward possible  |
| `git merge --abort`       | Cancel an in-progress merge                       |
