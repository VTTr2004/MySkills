# VinUni AI Project Workflow Diagram

Open this file in Visual Studio Code and use **Markdown: Open Preview**.
VS Code can render Mermaid diagrams in Markdown preview. If your VS Code does not render it, install the extension **Markdown Preview Mermaid Support**.

## Main Workflow

```mermaid
flowchart TD
    A[Start new AI project] --> B[Read skill pack]
    B --> C[Run intake questions]
    C --> D{Answer clear and level-fit?}
    D -- No --> E[Explain risk or ambiguity]
    E --> F[Offer options and recommend default]
    F --> C
    D -- Yes --> G[Recommend project level]
    G --> H[Ask for extra notes]
    H --> I[Write intake summary]
    I --> J{User confirms summary?}
    J -- No --> C
    J -- Yes --> K[Draft project artifacts]
    K --> L[Project brief]
    K --> M[Architecture]
    K --> N[Evaluation plan]
    K --> O[Implementation plan]
    L --> P[Ask user to approve plan]
    M --> P
    N --> P
    O --> P
    P --> Q{Plan approved?}
    Q -- No --> K
    Q -- Yes --> R[Scaffold by selected level]
    R --> S[Implement AI core first]
    S --> T[Add thin API or UI wrapper if needed]
    T --> U[Run evaluation cases]
    U --> V[Update README, worklog, decision log]
    V --> W[Handoff usable project]
```

## Level Selection

```mermaid
flowchart TD
    A[Project context] --> B{Goal type}
    B -- Quick idea test, 1-3 hours --> L0[Level 0: Spike]
    B -- Daily course demo --> L1[Level 1: Course Demo]
    B -- Reusable or extendable prototype --> L2[Level 2: Structured Agent]
    B -- Final presentation or grading demo --> L3[Level 3: Demo Day]
    B -- Real product intent --> L4[Level 4: Product Ready]

    L0 --> S0[One script or minimal app]
    L1 --> S1[Agent, basic logs, README, eval 5 cases]
    L2 --> S2[Clean agent structure, docs, tests, eval 10-20 cases]
    L3 --> S3[Backend/frontend split, Docker, CI/CD, deploy evidence]
    L4 --> S4[Auth, database, observability, security, production checklist]
```

## Artifact Flow

```mermaid
flowchart LR
    A[Intake answers] --> B[INTAKE_SUMMARY.md]
    B --> C[PROJECT_BRIEF.md]
    B --> D[ARCHITECTURE.md]
    B --> E[EVALUATION_PLAN.md]
    B --> F[IMPLEMENTATION_PLAN.md]
    C --> G[Scaffold]
    D --> G
    E --> H[Evaluation cases]
    F --> G
    G --> I[AI core]
    I --> J[API or UI wrapper]
    J --> H
    H --> K[WORKLOG.md]
    H --> L[DECISION_LOG.md]
```
