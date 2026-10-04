# Semantic Throttle

## Policy aperture

Rate limits count calls. Agents evade them with paraphrases.

Semantic Throttle freezes a plain-language operating policy, an authorized agent, named action categories, per-category quotas, and an epoch duration. Each proposed action passes through a validator-classified aperture before deterministic quota logic decides whether it may consume capacity.

```text
new intent + remaining category capacity -> APPROVED
semantic replay                         -> DENIED_DUPLICATE
new intent + exhausted category         -> DENIED_QUOTA
expired epoch                           -> permissionless reset
```

## What consensus owns

Validators agree on the exact category, a bounded canonical intent, and the complete indexes of semantically equivalent prior actions. Every stored field that can influence the verdict is independently checked. The contract, not the model, applies quotas and verdicts.

## Epoch discipline

Only the frozen agent may request an action. Anyone may advance an expired epoch, preventing an absent owner from trapping future capacity. The owner may close the throttle, but cannot rewrite its policy, categories, or limits.

## Inspection

```bash
genvm-lint contracts/contract.py
python -m pytest -q
```

This repository contains an Intelligent Contract only. It has no frontend and moves no funds.
