# Contributing

Thanks for helping improve `preferences-validate`.

## Before opening a pull request

1. Fork the repository and create a focused branch.
2. Keep skill instructions and references under `skills/preferences-validate/`.
3. Run the validator:

   ```bash
   python3 scripts/validate_skill.py
   ```

4. Check that examples do not contain real API keys, tokens, wallet credentials, personal data, or production user data.
5. Explain the user-facing or maintenance benefit of the change in the pull request.

## Pull requests

- Pull requests must target `main`.
- Keep unrelated refactors out of a skill-content change.
- Update references when changing an instruction that depends on them.
- Do not modify `.github/CODEOWNERS`, workflows, or release-policy files without calling out the security impact.
- Maintainer approval is required before changes can enter `main`.

The repository may reject a pull request when the skill is missing, its frontmatter is invalid, a local reference is broken, or the skill exceeds the documented size limit. The validator permits the initial scaffold placeholder; once the production skill is copied in, the full checks apply.
