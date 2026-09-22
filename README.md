# Attention-Guided Credit Assignment in Planner–Executor LLMs

**Mingze Gao** · Nanjing University, School of Artificial Intelligence
With guidance from Junbo Li and Peihao Wang (UT Austin)

🔗 Project page: *(deploy the `index.html` + `style.css` in this repo, e.g. via GitHub Pages, and link it here)*
📄 Related work: [Attention Illuminates LLM Reasoning](https://arxiv.org/abs/2510.13554)

> Status: **Ongoing research project (2026)**. Results and analyses will be updated as the study develops.

---

## Overview

This repository hosts the project page for an ongoing study on how **attention patterns between a Planner agent and an Executor agent** can be used to understand — and eventually guide — credit assignment in multi-agent LLM reasoning systems.

**Research question:** Outcome-level rewards tell us whether a final answer was right or wrong, but not *which agent* or *which part of its trajectory* was responsible. We study whether internal attention between the Planner and Executor can reveal this hidden interaction structure and serve as a finer-grained signal for credit assignment.

### Why this project exists

An earlier attempt allocated outcome-level reward directly in proportion to Planner–Executor attention weights. This failed structurally: since attention weights are strictly positive, both agents always received reward of the *same sign* — even in cases like **Planner-wrong-but-Executor-right (FT)**, where the Planner's contribution was arguably negative despite a positive outcome. This motivated a step back to first characterize what attention actually looks like across correctness states, before trying to use it for credit assignment.

---

## What's in this page

The site walks through the project in order:

1. **Research Question** — motivation and the sign-mismatch problem that reframed the project.
2. **Attention Dynamics (§01)** — attention heatmaps and alignment/tracking-error metrics across four Planner×Executor correctness states (TT, TF, FT, FF), plus a Plan Attention Entropy analysis.
3. **Cross-Agent Token Influence (§02)** — a pipeline for scoring which Planner tokens the Executor actually depends on (Cross-Agent Token Influence, "CATI").
4. **Intervention Experiments (§03)** — masking high/low-CATI tokens on GSM8K (Qwen2.5-1.5B-Instruct) to test whether attention-identified tokens are functionally important, including a note that influence ≠ usefulness.
5. **RL Credit Assignment (§04)** — using the attention signal inside GRPO training, comparing agent-level reward splitting vs. token-level weighting against a vanilla GRPO baseline.
6. **The Planner–Executor Bottleneck (§05)** — no-plan / normal-plan / oracle-plan / random-plan ablations showing how much headroom exists in the interface itself.
7. **Planner Behavior Under RL (§06)** — how GRPO training changes Planner behavior (e.g. increased forbidden-calculation rate), suggesting outcome-only supervision can induce shortcut behaviors.
8. **Current Understanding & Ongoing Work** — a summary storyline and open directions.

## Key preliminary findings

- Attention alignment is **not equivalent to correctness** — an Executor can closely follow a Plan that is itself wrong.
- Mismatch conditions (TF/FT) show **more concentrated** (lower-entropy) attention than matched conditions, not more spread out.
- Masking high-CATI Planner tokens is far more disruptive to Executor accuracy than masking low-CATI or random tokens — evidence that cross-agent attention captures real token-level dependency.
- But dependency ≠ positive contribution: some high-CATI tokens are harmful, and some helpful tokens are low-CATI.
- Naive agent-level reward allocation from attention **underperforms** vanilla GRPO; token-level credit weighting on top of the vanilla reward gives a small preliminary improvement (+1.74 pts over baseline).
- Oracle-plan vs. random-plan ablations show large headroom in planning quality, and a noisy Planner can currently underperform having no plan at all.

*(All numbers above are preliminary, from a single setup — see the project page for exact figures, sample sizes, and caveats.)*

## Experimental setup (as referenced in the page)

- **Model:** Qwen2.5-1.5B-Instruct
- **Task:** GSM8K
- **Attention analysis:** middle layers 9–18, top 30% of heads by cumulative attention to the Plan span ("global heads"), 320 trajectories across the four correctness states

## Repository structure

```
.
├── index.html      # Project page markup
├── style.css       # Project page styling
└── images/         # Attention heatmaps, entropy plot, etc. (referenced by index.html)
```

> Note: this repository currently contains only the **project webpage**, not the experiment code. If/when the training and analysis code is released, it will be linked from here.

## Viewing the page locally

```bash
git clone https://github.com/Gao01183/Attention-credit.git
cd Attention-credit
# open index.html in a browser, or serve it locally:
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Ongoing work

- More robust cross-agent token importance estimation
- Separating attention-based dependency from contribution quality
- More principled credit assignment across Planner–Executor interactions
- Validation across models, seeds, and tasks

## Citation / acknowledgment

This project is inspired by [*Attention Illuminates LLM Reasoning*](https://arxiv.org/abs/2510.13554); the head-selection criterion and token-scoring procedure used here are designed for the cross-agent Planner–Executor setting and differ from that prior work's mechanisms.

## Contact

Mingze Gao — Nanjing University, School of Artificial Intelligence
GitHub: [Gao01183/Attention-credit](https://github.com/Gao01183/Attention-credit)

---
© 2026 Mingze Gao
