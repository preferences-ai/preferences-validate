# preferences-validate

`preferences-validate` is an open-source Agent Skill from Preferences AI that acts as a validation layer before build and launch. It helps agents compare product, pricing, messaging, and UX concepts with an AI Digital Population, then deepen the research with surveys, simulations, analytics, and optional live deployment.

The skill uses the public Preferences AI Dashboard API with a Team API key and PAI Credits. It is distributed as a portable `SKILL.md` package and can be used with Claude Code, Codex, Cursor, Grok Build, Hermes Agent, and other agents that support the Agent Skills format.

## What this skill does

Use `preferences-validate` when you need evidence for a product decision:

| Need | Validation path |
| --- | --- |
| Compare 2–6 concepts, headlines, messages, or mockups | Freemium or paid quick concept test, or a full scenario |
| Get deeper preference or product-market-fit evidence | Build a survey, run an AI Digital Population simulation, and interpret the findings |
| Collect answers from real people | Deploy a survey, collect responses, and run analytics |
| Investigate a completed simulation | Run a follow-up simulation |
| Avoid duplicate work or unnecessary spend | List existing scenarios, surveys, and simulations before creating new work |

The recommended progression is to start with a low-cost scenario test and escalate to survey → simulation → insights only when a directional concept comparison is not enough.

## Prerequisites and safety

1. Create a Preferences AI Team and Team API key in [API Management](https://dashboard.preferencesai.io).
2. Export the key as `PREFERENCES_AI_API_KEY`.
3. Ensure `curl` is available.
4. Before any paid operation, call `GET /balance`, confirm the available PAI Credits, and ask for confirmation before spending on the user's behalf.

The default API base is `https://dashboard.preferencesai.io/api/v1`; set `PAI_API_BASE` to target another environment. Authentication uses `X-API-Key: $PREFERENCES_AI_API_KEY`, and the team is inferred from the key—never send `team_id` in request bodies.

The skill's current catalog includes free quick concept tests when trials remain, paid quick concept tests at `0.99` PAI, full scenarios at `1.99` PAI, survey simulations at `2.49` or `3.99` PAI, and follow-up simulations at `1.99` PAI. Always check the live balance and catalog response rather than assuming a balance or price.

## Install

The recommended installer is the open-source [`skills`](https://github.com/vercel-labs/skills) CLI. It downloads the complete repository, including the reference files under [`skills/preferences-validate/`](skills/preferences-validate/).

### Install for the current project

The project-scoped installation is shared with the project team:

```bash
npx skills add preferences-ai/preferences-validate
```

The CLI uses symlinks by default and places a canonical copy under `.agents/skills/`. Use `--copy` when symlinks are not available.

### Install globally

Global installation makes the skill available across projects for your user account:

```bash
npx skills add preferences-ai/preferences-validate \
  --global
```

### Install for multiple agents

Install the same skill for every supported agent detected by the CLI:

```bash
npx skills add preferences-ai/preferences-validate \
  --agent '*'
```

For scripts and CI, add `--yes` to skip confirmation prompts. Review any skill before use because skills provide instructions that an agent may follow with the permissions available in that agent.

## Install by agent harness or coding agent

The skill content is the same across frameworks. Only the target integration directory changes.

| Agent Harness / Coding Agent | Project installation | Project skill directory |
| --- | --- | --- |
| Claude Code | `npx skills add preferences-ai/preferences-validate --agent claude-code` | `.claude/skills/` |
| Codex | `npx skills add preferences-ai/preferences-validate --agent codex` | `.agents/skills/` |
| Cursor | `npx skills add preferences-ai/preferences-validate --agent cursor` | `.agents/skills/` |
| Grok Build | `npx skills add preferences-ai/preferences-validate --agent grok` | `.grok/skills/` |
| Hermes Agent | `npx skills add preferences-ai/preferences-validate --agent hermes-agent` | `.hermes/skills/` |
| OpenClaw | `npx skills add preferences-ai/preferences-validate --agent openclaw` | `skills/` |

For Grok Build or Hermes Agent, the repository can also be copied manually into the project or global skill directory shown above. Keep the complete `preferences-validate` folder, not only `SKILL.md`, because the workflow references the supporting API guides. Using the full repository with the Skills CLI is the recommended way to preserve those references.

After installation, start a new agent session if the framework does not reload skills dynamically. The skill is invoked according to each agent's normal skill behavior, typically by asking for a Preferences AI concept test or using the `preferences-validate` skill name.

## Repository layout

```text
skills/preferences-validate/
├── SKILL.md
├── references/
│   ├── setup-auth.md
│   ├── combinations.md
│   ├── scenarios.md
│   ├── surveys.md
│   ├── simulations.md
│   └── ...
└── eval/
    └── eval_queries.json
```

Read [`SKILL.md`](skills/preferences-validate/SKILL.md) for the complete workflow. The reference guides cover authentication and scopes, pricing, API keys, scenarios, surveys, simulations, recipes, errors, and presenting findings.

## Security

- Never commit or paste API keys, wallet credentials, tokens, or user data.
- Keep `PREFERENCES_AI_API_KEY` in an environment variable or secret store.
- Grant API keys only the scopes required for the workflow.
- Never send `team_id`; the Team API key determines tenancy.
- Check balances before billable work and confirm paid spend when acting for a user.

See [`SECURITY.md`](SECURITY.md) for repository vulnerability reporting.

## Contributing and releases

Changes are submitted through pull requests. The `main` branch is protected, and changes to the skill and repository controls require review from the Preferences AI owner team. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

`main` is the canonical source used by the Skills CLI. Owner-only branch and release-tag controls are documented in [`docs/RELEASE_POLICY.md`](docs/RELEASE_POLICY.md).

## License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE).
