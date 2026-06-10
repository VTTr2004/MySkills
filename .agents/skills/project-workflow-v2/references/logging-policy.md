# Logging Policy

## Workflow Log

Use short, auditable entries:

- timestamp
- phase
- task id
- agent or subagent
- purpose
- input summary
- output summary
- files changed
- commands run
- test/eval result
- supervisor decision

## Runtime Log

For AI/tool apps, record:

- request id
- user input summary
- selected route
- retrieved source ids when using RAG
- tools used
- model name when relevant
- latency
- sanitized error
- eval notes when available

## Do Not Log

- hidden prompts
- internal reasoning
- secrets
- private credentials
- raw sensitive user data
- full debug traces in user-facing UI

## User-Facing Status

Show only useful product state:

- processing status
- result
- sources or evidence when relevant
- warnings or limitations
- clear error messages

