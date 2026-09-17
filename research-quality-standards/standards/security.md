# Security and Secret-Handling Standards

Version: 0.1.0
Last updated: 2026-09-17

Use for tasks involving credentials, configuration, APIs, deployment, data access, external services, or sensitive data.

## Required practices

- Never write real secrets, private keys, credentials, or tokens to repository files, logs, reports, examples, or reviewer packets.
- Treat `.env`, `secrets.*`, credential files, private keys, and deployment credentials as read-only unless explicitly authorized.
- Use placeholders and environment variables; prefer secret scanning and `.env.example` files.
- Do not send confidential, restricted, or human-subjects data to external services without explicit authorization and policy support.
- State the domain, purpose, and necessity before network access involving protected material.

Use `BLOCKER` for exposed credentials, unauthorized external disclosure, or unsafe auth/permission changes. Stop rather than redacting after disclosure.
