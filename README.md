# Comparing GitHub, GitLab and Bitbucket Using a Sample Project

**Subject:** DevOps (Lab Project)

## Aim
To compare the features of GitHub, GitLab and Bitbucket by hosting and managing
the **same sample project** on each platform and performing the same set of
DevOps activities on all three.

## What is inside

| Path | Purpose |
|------|---------|
| `sample-app/` | Small Python task manager with unit tests (the project we host) |
| `.github/` | GitHub Actions workflow, issue template, pull request template |
| `.gitlab-ci.yml`, `.gitlab/` | GitLab CI/CD pipeline, issue and merge request templates |
| `bitbucket-pipelines.yml` | Bitbucket Pipelines configuration |
| `docs/EXECUTION_GUIDE.md` | Step-by-step instructions to run the experiment |
| `docs/COMPARISON.md` | Feature comparison, terminology map, scorecard, conclusion |
| `docs/EVIDENCE_CHECKLIST.md` | Screenshots and observations to collect for the report |

## Quick start
```bash
cd sample-app
python -m unittest -v        # run the tests locally
python taskmanager.py add "Finish DevOps lab"
python taskmanager.py list
```

Then follow `docs/EXECUTION_GUIDE.md` to push the project to the three platforms.

## Tools used
Git, Python 3.12, GitHub Actions, GitLab CI/CD, Bitbucket Pipelines.
