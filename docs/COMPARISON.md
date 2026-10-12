# Feature Comparison: GitHub vs GitLab vs Bitbucket

> Free-plan limits and pricing change often. Check each platform's pricing page
> before writing the final report.

## 1. Overview

| Point | GitHub | GitLab | Bitbucket |
|-------|--------|--------|-----------|
| Owner | Microsoft | GitLab Inc. | Atlassian |
| Launched | 2008 | 2011 | 2008 |
| Main idea | Social coding and open source community | One complete DevOps platform in a single application | Git hosting tightly linked with Jira and Trello |
| Version control | Git | Git | Git (Mercurial support removed in 2020) |
| Self-hosting | GitHub Enterprise Server (paid) | GitLab Community Edition (free) and Enterprise | Bitbucket Data Center (paid) |

## 2. Feature comparison

| Feature | GitHub | GitLab | Bitbucket |
|---------|--------|--------|-----------|
| Code review | Pull Requests | Merge Requests | Pull Requests |
| CI/CD | GitHub Actions (`.github/workflows/*.yml`) | Built-in GitLab CI/CD (`.gitlab-ci.yml`) | Bitbucket Pipelines (`bitbucket-pipelines.yml`) |
| Reusable pipeline parts | Marketplace actions | Includes, templates, CI/CD catalog | Pipes |
| Issue tracking | Issues, Projects boards | Issues, boards, epics, milestones | Basic issues, best through Jira |
| Wiki | Yes | Yes | Yes |
| Container / package registry | GitHub Packages | Built-in registry | Limited (use external registry) |
| Security scanning | Dependabot, code scanning, secret scanning | SAST, secret detection and more built in (more in paid tiers) | Basic, via pipes or Jira ecosystem |
| Static website hosting | GitHub Pages | GitLab Pages | Not offered for general sites |
| Cloud dev environment | Codespaces | Web IDE / Workspaces | Web editor |
| AI assistant | GitHub Copilot | GitLab Duo | Atlassian Rovo |
| Third-party integrations | Largest marketplace | Good, many built in | Excellent with Atlassian tools |
| Community size | Largest | Medium | Smaller |
| Best fit | Open source, student portfolios | Teams wanting everything in one tool | Teams already using Jira |

## 3. Same idea, different names

| Concept | GitHub | GitLab | Bitbucket |
|---------|--------|--------|-----------|
| Merge proposal | Pull Request | Merge Request | Pull Request |
| Pipeline file | `.github/workflows/*.yml` | `.gitlab-ci.yml` | `bitbucket-pipelines.yml` |
| Build machine | Runner | Runner | Runner |
| Grouping of repos | Organization | Group | Workspace |
| Code owners file | `CODEOWNERS` | `CODEOWNERS` | Default reviewers setting |
| Secret storage | Secrets and variables | CI/CD variables | Repository variables |

## 4. Free plan snapshot (verify before submitting)

| Item | GitHub Free | GitLab Free | Bitbucket Free |
|------|-------------|-------------|----------------|
| Private repositories | Unlimited | Unlimited | Unlimited |
| Users | Unlimited collaborators on repos | 5 users per top-level group on SaaS | Up to 5 users |
| CI/CD minutes | About 2,000 per month | About 400 compute minutes per month | About 50 build minutes per month |

## 5. Your scorecard (fill from your own experience)
Score 1 (poor) to 5 (excellent).

| Criteria | GitHub | GitLab | Bitbucket |
|----------|:------:|:------:|:---------:|
| Ease of creating and pushing a repository | | | |
| Pull / merge request experience | | | |
| CI/CD setup and log readability | | | |
| Issue tracking and project boards | | | |
| Built-in security and extras | | | |
| Integrations | | | |
| Documentation and learning resources | | | |
| **Total** | | | |

## 6. Conclusion (draft, edit with your results)
All three platforms host Git repositories and support pull or merge requests,
branch protection and automated pipelines, so the basic workflow is the same.
The difference is in the ecosystem:

- **GitHub** is the easiest to start with and has the biggest community and
  marketplace. It is the best choice for open source projects and student portfolios.
- **GitLab** gives the most features in one place (repository, CI/CD, registry,
  security, boards). It suits teams that want a complete DevOps lifecycle in one tool.
- **Bitbucket** is a strong choice when a team already works in Jira and Trello,
  because commits, branches and builds link directly to Jira issues.

No platform is best for every case. The right choice depends on team size,
budget, existing tools and whether self-hosting is needed.
