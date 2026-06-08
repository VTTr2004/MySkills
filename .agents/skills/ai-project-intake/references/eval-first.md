# Eval First For AI

Define evaluation before implementation.

Minimum fields:
- Input
- Expected behavior
- Required evidence or source behavior
- Failure mode to watch
- Pass/fail notes

Useful metrics:
- Correctness
- Relevance
- Faithfulness to provided context
- Tool-use correctness
- Latency
- Cost
- Human rating

For RAG:
- Check whether retrieved context contains the answer.
- Check whether final answer cites or uses the context correctly.
- Penalize overconfident answers outside available evidence.
