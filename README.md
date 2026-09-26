# ⚽ Football Tactical Strategy Analyser

A system that takes information about two football teams and produces a **coordinated, explainable tactical plan** — starting as a rule-based reasoning engine and evolving toward a live, natural-language-driven tactical assistant.

> **Core principle:** the reasoning engine is always the tactical brain. Data inputs get richer over time (structured → live → natural language), but the decision-making logic stays deterministic, traceable, and explainable at every stage.

---

## Pipeline (target end-state)

```
Observe → Understand → Diagnose → Reason → Plan → Explain → Adapt
```

| Stage | What it does |
|---|---|
| Observe | Take in information about both teams (structured, live, or natural language) |
| Understand | Parse it into a consistent tactical data model |
| Diagnose | Identify tactical problems and their root causes |
| Reason | Match our strengths against their weaknesses, considering formation relationships |
| Plan | Generate a coordinated tactical response (defensive, attacking, transition, player instructions, shape) |
| Explain | State *why* each adjustment is recommended |
| Adapt | Update the plan as the match situation changes (later versions) |

---

## Roadmap

### 🟢 V1 — Structured Tactical Engine *(current focus)*
**Goal:** Build the core tactical brain.

**Inputs (structured data, no live match data yet):**
- **Our team:** formation, tactical strengths, tactical weaknesses, players (position, strengths, weaknesses)
- **Opponent:** formation, tactical strengths, tactical weaknesses, 1–2 key threats, players (position, strengths, weaknesses)

**Engine steps:**
1. Identify the tactical problem
2. Determine why it's happening
3. Identify our vulnerability
4. Identify exploitable opponent weaknesses
5. Match our strengths against their weaknesses
6. Consider formation relationships
7. Generate a coordinated tactical response

**Output:** a tactical plan covering Defensive / Attacking / Transition / Player instructions / Formation-shape adjustments, each with a stated reason.

`V1 = structured data → rule-based tactical reasoning → tactical plan`

---

### 🟡 V2 — Deeper Tactical Analysis
**Goal:** Make the reasoning more sophisticated.

- More player relationships and formation interactions
- More tactical patterns and response patterns
- Handling of multiple simultaneous threats
- More detailed tactical consequences
- A method for prioritizing which tactical problems matter most

`V2 = deeper understanding of tactical relationships`

---

### 🟠 V3 — Match State
**Goal:** Make the analyser context-aware.

Introduces: match minute, score, possession, recent events, substitutions, changing tactical situations.

The same tactical problem can produce different recommendations depending on context — e.g. a problem at 10' while winning is treated differently than the same problem at 85' while losing.

`V3 = tactical analysis + match context`

---

### 🔴 V4 — Live Tactical Planner
**Goal:** Move from analysing a snapshot to continuously analysing the match.

```
Live match data
   ↓
Understand current situation
   ↓
Detect tactical problem/opportunity
   ↓
Determine cause
   ↓
Generate tactical adjustments
   ↓
Explain reasoning
   ↓
Update when the match changes
```

`V4 = live match → continuously updated tactical plan`

---

### 🟣 V5 — NLP / LLM Layer
**Goal:** Let a human describe what they see in natural language.

> *"Their left winger keeps getting behind our right back, and their left back is pushing really high."*

```
Human observation
   ↓
LLM/NLP
   ↓
Structured tactical data
   ↓
Tactical reasoning engine
   ↓
Tactical plan
   ↓
Explanation
```

**Key architectural rule:** the LLM only interprets natural language into structured data — it never makes the tactical decision itself. The reasoning engine (built in V1–V4) remains the sole source of tactical judgment.

`V5 = natural-language input + tactical reasoning`

---

## Version Summary

| Version | Main Capability |
|---|---|
| V1 | Structured tactical engine |
| V2 | Deeper tactical relationships |
| V3 | Match-state awareness |
| V4 | Live tactical planning |
| V5 | NLP/LLM interface |

---

## Status

- [ ] V1 — Structured Tactical Engine (in progress)
- [ ] V2 — Deeper Tactical Analysis
- [ ] V3 — Match State
- [ ] V4 — Live Tactical Planner
- [ ] V5 — NLP/LLM Layer

## Design Notes

- **Formations** are modeled as structured shapes (defensive line, midfield line(s), attacking line, width, and position adjacency) so the engine can reason about formation-vs-formation relationships, not just isolated player matchups.
- **Tactical rules** are encoded as explicit condition → cause → response mappings, so every recommendation traces back to a specific, statable reason.
- **Explainability is a hard requirement**, not an afterthought — every version of the engine must be able to justify its recommendations, since this is what separates a genuine tactical tool from an LLM improvising commentary.
