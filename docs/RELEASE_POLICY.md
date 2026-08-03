# Release and ownership policy

## Canonical publication path

The public `main` branch is the canonical source installed by:

```bash
npx skills add preferences-ai/preferences-validate
```

A GitHub Release is not required for the Skills CLI to install the skill. Publishing a change therefore means merging the reviewed change into `main`. Release tags are still useful for immutable snapshots and must be owner-controlled.

The repository is intentionally configured with declarative files, but GitHub branch and tag rules are repository settings and cannot be enforced by committed files alone. Complete the following setup in `preferences-ai/preferences-validate` before announcing the repository publicly.

## Required GitHub settings

The owner/admin team is [`@preferences-ai/skill-collaborators`](https://github.com/orgs/preferences-ai/teams/skill-collaborators), configured in [`.github/CODEOWNERS`](../.github/CODEOWNERS). The team must retain access to this repository.

### Protect `main`

Create an active branch ruleset or branch protection rule targeting `main` with:

- Require a pull request before merging.
- Require at least one approving review.
- Require review from Code Owners.
- Dismiss stale approvals when new commits are pushed.
- Require the `validate` status check.
- Block force pushes and branch deletion.
- Do not permit ordinary collaborators to bypass the rule.

Keep the Preferences AI owner/admin team as the only administrative bypass group when an emergency bypass is necessary. The normal publication path remains an owner-reviewed pull request merged into `main`.

### Protect release tags

Create an active tag ruleset targeting `v*` (or the exact release-tag pattern the team adopts) with:

- Restrict tag creation to the Preferences AI owner/admin team.
- Restrict tag updates and deletion to the same team.
- Do not grant bypass access to contributors, fork authors, or GitHub Actions.

If GitHub Releases are used, create each release from an owner-controlled tag that points at the reviewed `main` commit. Do not allow a release page to create an unrestricted tag.

### Limit repository and Actions permissions

- Give repository write/admin access only to the Preferences AI owner/admin team.
- Keep the default workflow token permission at read-only.
- Do not add secrets to the validation workflow.
- Require maintainer approval for workflows from outside contributors if additional workflows are added later.
- Review every workflow change as an ownership-sensitive change; the workflow and CODEOWNERS files are assigned to the owner team.

## Verification checklist

Before the first public announcement:

- [ ] Confirm `@preferences-ai/skill-collaborators` retains access to the repository.
- [ ] Copy the production `SKILL.md` and reference files into `skills/preferences-validate/`.
- [ ] Remove `skills/preferences-validate/.gitkeep`.
- [ ] Confirm `python3 scripts/validate_skill.py` passes.
- [ ] Confirm `npx skills add preferences-ai/preferences-validate` discovers the skill.
- [ ] From a non-owner account, verify a direct `main` update is rejected.
- [ ] From a non-owner account, verify creating, moving, or deleting a `v*` tag is rejected.
- [ ] Verify an external contributor can open a pull request but cannot merge it without the required owner review.
- [ ] Verify a release created from an owner-controlled tag points to the intended `main` commit.
