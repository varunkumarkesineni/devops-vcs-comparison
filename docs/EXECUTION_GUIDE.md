# Execution Guide

Total time: about 3 to 4 hours. Take screenshots as listed in
`EVIDENCE_CHECKLIST.md` while you work.

## Step 0: Prerequisites
1. Install Git and Python 3.12. Check with `git --version` and `python --version`.
2. Create free accounts on **github.com**, **gitlab.com** and **bitbucket.org**.
   (Bitbucket needs an Atlassian account and a *workspace*.)
3. Configure Git once:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
4. Create an SSH key and add the public key on all three platforms
   (Settings > SSH keys):
   ```bash
   ssh-keygen -t ed25519 -C "you@example.com"
   cat ~/.ssh/id_ed25519.pub
   ```
   Test: `ssh -T git@github.com`, `ssh -T git@gitlab.com`, `ssh -T git@bitbucket.org`.

## Step 1: Prepare the local repository
```bash
cd devops-vcs-comparison
git init -b main
git add .
git commit -m "Initial commit: task manager sample project"
```

## Step 2: Create an empty repository on each platform
Create a **private or public** repository named `devops-vcs-comparison`
(do not add a README there, it must start empty).

| Platform | Where to click |
|----------|----------------|
| GitHub | `+` (top right) > New repository |
| GitLab | New project > Create blank project (untick "Initialize with a README") |
| Bitbucket | Create > Repository (choose Git) |

Note down how many clicks and fields each platform needed. This is part of the comparison.

## Step 3: Push the same code to all three
```bash
git remote add github    git@github.com:<user>/devops-vcs-comparison.git
git remote add gitlab    git@gitlab.com:<user>/devops-vcs-comparison.git
git remote add bitbucket git@bitbucket.org:<workspace>/devops-vcs-comparison.git

git push -u github main
git push -u gitlab main
git push -u bitbucket main
```
Pushing `main` also triggers the first CI run on each platform because the
three pipeline files are already in the repository.

## Step 4: Run the same activities on every platform
Repeat each activity on all three platforms and fill in the table in
`COMPARISON.md`.

### Activity A: Branching and pull / merge request
```bash
git checkout -b feature/delete-task
```
Add a `delete_task(tasks, task_id)` function to `taskmanager.py` and a test for it.
```bash
git add .
git commit -m "Add delete_task function with test"
git push -u github    feature/delete-task
git push -u gitlab    feature/delete-task
git push -u bitbucket feature/delete-task
```
On each site open a **Pull Request** (GitHub, Bitbucket) or **Merge Request**
(GitLab) from `feature/delete-task` into `main`. Watch the pipeline run on the request.

### Activity B: Code review
Ask a teammate to add the reviewer, leave an inline comment on one line, request
changes, then approve. Note how each platform shows comments, approvals and
merge options (merge commit, squash, fast-forward).

### Activity C: Issue tracking
Create 3 issues on each platform (one bug, one feature, one task) using the
provided templates. Add labels, an assignee and a milestone / due date where
available. Link an issue to the request by writing `Closes #1` in the description.

### Activity D: CI/CD pipeline
1. Open the pipeline page on each platform and take a screenshot of a **passed** run.
2. Make a deliberate failure: change one assertion in `test_taskmanager.py`,
   push on a new branch `test/break-build`, and capture the **failed** run.
3. Record: time to start, time to finish, how readable the logs are, how
   easy it was to re-run.

### Activity E: Access control and branch protection
- Add a teammate as collaborator / member with the *Developer* or *Write* role.
- Protect `main` so that direct pushes are blocked and one approval is required.
  (GitHub: Settings > Branches. GitLab: Settings > Repository > Protected branches
  and Settings > Merge requests. Bitbucket: Repository settings > Branch restrictions.)

### Activity F: Documentation, wiki and extras
Edit the wiki or README on each platform. Look for: wiki, project board
(Kanban), pages hosting, package / container registry, security scanning,
Jira or Slack integration. Mark each as available or not on the free plan.

### Activity G: Import, mirroring and webhooks (optional)
Mirror one repository into another platform, and add one webhook that posts to a
free test URL such as webhook.site.

## Step 5: Complete the comparison
1. Fill the observation tables in `docs/EVIDENCE_CHECKLIST.md`.
2. Give each platform a score from 1 to 5 in the scorecard of `docs/COMPARISON.md`
   based on **your own experience**.
3. Write the final conclusion in your own words.

## Step 6: Submit
1. Put all screenshots in a `screenshots/` folder.
2. Prepare the lab record / report: Aim, Tools, Procedure (Steps 1 to 4),
   Observations (comparison tables), Result and Conclusion.
3. Keep the three repository links ready for the viva.

## Common problems
| Problem | Fix |
|---------|-----|
| `Permission denied (publickey)` | Add the SSH public key to that platform, then run `ssh -T` again |
| Push rejected, remote has a README | Create the remote repo empty, or run `git pull <remote> main --allow-unrelated-histories` |
| Pipeline does not start on Bitbucket | Repository settings > Pipelines > enable Pipelines |
| GitLab pipeline blocked | New accounts may need identity verification before shared runners are used |
| Branch named `master` | Run `git branch -M main` |
