# Git Collaboration & Troubleshooting Guide

This document outlines the standard workflow for repository management, team collaboration, and resolving common Git errors.

---

## 🛠 1. Repository Initialization
*For creators setting up a new project.*

* [cite_start]**Create README**: Create a basic documentation file: `echo "# test22" >> README.md` [cite: 2]
* [cite_start]**Initialize Git**: Start a new Git repository: `git init` [cite: 3]
* [cite_start]**Stage & Commit**: Add the README and create the first save point: `git add README.md` && `git commit -m "first commit"` [cite: 4, 5]
* [cite_start]**Set Branch**: Ensure the default branch is named 'main': `git branch -M main` [cite: 6]
* [cite_start]**Connect to Remote**: Link your local folder to GitHub: `git remote add origin https://github.com/` [cite: 7]
* [cite_start]**Initial Push**: Upload your code: `git push -u origin main` [cite: 8]

---

## 🤝 2. Team Collaboration Workflow
*Steps for contributors joining an existing project.*

### Step 1: Access & Setup
* [cite_start]**Grant Access**: The repository creator must add team members as contributors in the repository settings[cite: 9].
* [cite_start]**Clone the Repo**: Once added, download the project: `git clone <repo-url>`[cite: 10, 11].

### Step 2: Feature Branching
* [cite_start]**Create Branch**: Create a personal branch to work safely: `git branch Arsalan`[cite: 12, 13].
* [cite_start]**Switch Branch**: Move into your new branch: `git checkout Arsalan`[cite: 14].
* [cite_start]**Save Changes**: Stage your files and commit them: `git add the_file.py` && `git commit -m "Arsalan's modules"`[cite: 15, 16].
* [cite_start]**Push Branch**: Upload your branch to GitHub: `git push -u origin Arsalan`[cite: 17].

---

## 🔄 3. Merging Changes to Main
[cite_start]*How to combine your work with the main project branch.* [cite: 18, 19]

1.  [cite_start]**Switch to Main**: `git checkout main` [cite: 20]
2.  [cite_start]**Pull Latest**: Get recent updates from others: `git pull origin main` [cite: 21]
3.  [cite_start]**Merge**: Combine your feature branch: `git merge Arsalan` [cite: 22]
4.  [cite_start]**Final Push**: Update the main branch on GitHub: `git push origin main` [cite: 23]

---

## 🔴 4. Common Errors & Resolutions

| Error Type | Description | Fix / Command |
| :--- | :--- | :--- |
| **Merge Conflict** | [cite_start]Same lines modified in two branches[cite: 25, 26]. | [cite_start]Edit markers (`<<<<<<<`, `=======`), then `git add` and `git commit` [cite: 30-40]. |
| **Non-fast-forward** | [cite_start]Remote `main` has updates you don't have[cite: 41, 42]. | [cite_start]`git pull origin main --rebase` followed by `git push`[cite: 46, 47]. |
| **Uncommitted Changes** | [cite_start]Local work prevents branch switching [cite: 48-52]. | `git add . [cite_start]&& git commit` OR use `git stash`[cite: 54, 55]. |
| **Unrelated Histories** | [cite_start]Merging two different repositories[cite: 56, 57]. | [cite_start]`git merge <branch> --allow-unrelated-histories`[cite: 60]. |
| **Merge Aborted** | [cite_start]Conflict prevents merge from starting[cite: 61, 63]. | [cite_start]`git merge --abort` and clean your directory [cite: 65-67]. |
| **Permission Denied** | [cite_start]Error 403: No write access [cite: 68-71]. | [cite_start]Verify collaborator status or check login credentials[cite: 73, 75]. |
| **Deleted Branch** | [cite_start]Trying to merge a branch deleted on GitHub [cite: 76-78]. | [cite_start]Merge locally or re-push the branch using `git push`[cite: 80, 81]. |
| **Detached HEAD** | [cite_start]You are on a commit, not a branch [cite: 82-84]. | [cite_start]Switch back to a branch: `git switch main`[cite: 85, 86]. |

---

## ✅ Pro Tips
* [cite_start]**Commit Often**: Always commit or stash your work before switching branches[cite: 87, 88].
* [cite_start]**Stay Updated**: Always pull the latest changes before you start merging[cite: 89].
* [cite_start]**Clean History**: If merging is too messy, try `git rebase` for a linear history[cite: 90].