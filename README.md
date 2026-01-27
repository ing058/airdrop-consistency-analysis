# Airdrop Consistency Analysis

This project investigates whether activity consistency, measured by active days,
plays a critical role in obtaining privileged access (e.g. Full Access roles),
even when users exhibit sufficient behavioral diversity.

Building on a previous behavioral analysis, this study focuses on users
who met diversity requirements but failed to obtain access, examining
whether insufficient activity duration explains these exceptions.

## Research Question

Among users with sufficient behavioral diversity,
does activity duration (active_days) differentiate
those who obtain Full Access from those who do not?

## Data & Method

This analysis reuses the simulated dataset from the previous project,
focusing on users with behavioral_diversity ≥ 2.

Users are segmented into:
- Full Access users
- Non-Full Access users

The distribution of active days is compared between the two groups.

## Key Findings

- Users with sufficient behavioral diversity but shorter activity duration
  were significantly less likely to obtain Full Access.
- Activity consistency appears to function as a gating factor,
  complementing behavioral diversity rather than replacing it.

## Interpretation

These results suggest that while diverse participation is necessary,
it is not sufficient on its own.
Sustained engagement over time may serve as a stronger signal of user commitment
in early-stage crypto ecosystems.
