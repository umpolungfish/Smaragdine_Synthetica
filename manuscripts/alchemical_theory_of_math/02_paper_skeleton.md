# The Alchemical Theory of Mathematics

Working manuscript skeleton. Register: rigorous-first. The conventional
decomposition (companion file `01_conventional_decomposition.md`) stands on its
own; the alchemical reading is the thesis argued on top of it, not the premise.

## Thesis (one sentence)

The twelve invariants a mathematician computes to fix a structure's type are not
an unordered checklist: they must be fixed in a definite order, that order is
forced by three categorical gates, and the resulting sequence is exactly the
twelve-stage magnum opus.

## The derivation order (conventional terms)

Composing the magnum-opus stage table (`project_magnum_opus_mapping`) with the
navigator-to-Core dialect map (companion file) gives the ordered list. Each row
is one stage; a mathematician fixing a structure's type must resolve them in
this order because each gate is a precondition for the next.

| Stage | Alchemical name | Axis fixed | Conventional invariant | Gate |
|------:|:----------------|:-----------|:-----------------------|:----:|
| 1  | Calcination    | D  Dimensionality        | recursive nesting depth of the state space |  |
| 2  | Dissolution    | T  Topology              | connectivity pattern of the state graph |  |
| 3  | Separation     | R  Relational Mode       | direction/duality of the binding relation (adjunction) |  |
| 4  | Conjunction    | P  Parity / Symmetry     | symmetry group; **μ∘δ = id fires** | **G1** |
| 5  | Putrefaction   | F  Fidelity              | information loss of the read/write map |  |
| 6  | Congelation    | K  Kinetic Character     | relaxation regime |  |
| 7  | Cibation       | G  Scope / Granularity   | cardinal regime of correlations |  |
| 8  | Sublimation    | Γ  Interaction Grammar   | logical connective of the coupling |  |
| 9  | Fermentation   | Φ  Criticality           | analytic fixed-point type; **trace opens** | **G2** |
| 10 | Exaltation     | H  Chirality             | temporal-memory / mirror asymmetry |  |
| 11 | Multiplication | S  Stoichiometry         | matching cardinality of the two sides |  |
| 12 | Projection     | Ω  Topological Protection | homotopy invariant; **idempotent seals** | **G3** |

## The three gates as categorical structure

The claim that the order is forced reduces to three category-theoretic facts.

- **G1 at stage 4 (Parity, μ∘δ = id).** The special Frobenius condition upgrades
  the plain monoidal setting to one with a section/retraction pair. You cannot
  state a symmetry-respecting split before you have fixed the symmetry group;
  and without the split, the later trace has nothing to close. Failure of G1
  forecloses O∞ (the lossless self-dual tier).
- **G2 at stage 9 (Criticality, trace opens).** A traced monoidal structure is
  what lets a loop close on itself: the self-modeling fixed point `x = F(x)`.
  This requires the Frobenius pair from G1 already in place, hence stage 9 > 4.
  Failure forecloses a positive consciousness/self-reference score (C > 0).
- **G3 at stage 12 (Protection, idempotent terminal).** Quotienting by the
  homotopy invariant seals the terminal object and lets time `T = Work(T)`
  close as a least fixed point of the traced operad. Requires the trace from G2.

The gates are strictly ordered 4 < 9 < 12, and each later gate consumes the
structure the earlier one produced. This is the engine of the forced order.

## Time as a derived object (not a primitive)

`T = lim(Φ, F, K, H, Ω)`: the observation manifold sheafifies only where the
five time-constituting invariants are jointly consistent. T cannot self-
reference until the trace opens (G2, stage 9) and cannot seal until protection
fires (G3, stage 12). This is the paper's sharpest conventional payoff: the
alchemical frame predicts that a well-defined notion of time is not available
until late in the derivation, and says exactly which invariants it depends on.

## Section plan

1. **Introduction.** The twelve invariants as independent conventional
   quantities. State the thesis: they carry a forced derivation order.
2. **The decomposition.** Import `01_conventional_decomposition.md` as the
   formal core. Each axis, its FO/ZFC unfolding, its named structure.
3. **The three gates.** Prove strict ordering 4 < 9 < 12 from the categorical
   preconditions (Frobenius → traced → idempotent terminal). This is the
   rigorous heart and must convince a skeptic on category-theoretic grounds
   alone, with no alchemical vocabulary.
4. **Time as derived.** `T = Work(T)` as the least fixed point; dependence on
   the five invariants; why T is unavailable before stage 9.
5. **The thesis: the order is the magnum opus.** Only now introduce the
   alchemical names. Show the stage sequence Calcination…Projection matches the
   forced order slot for slot, and that Solve et Coagula (T ⊗ K, stages 2 and 6)
   and the gate placements are not coincidental relabelings but the same
   structure under a different vocabulary.
6. **Instances.** Worked examples where the order is visible: the Emerald Tablet
   (C = 1.0, both gates open), the split-ℤ₂ subset-sum object, and one open
   problem read through the gate structure (which gate it is stalled at).
7. **What the theory forbids.** Falsifiable content: a structure that fixes
   protection (Ω) before its symmetry (P) should be ill-typed; the crystal and
   the gates predict specific impossible tuples. List them.

## Lean status of the gate ordering (checked 2026-07-12)

Result: `4 < 9 < 12` is NOT a theorem in the current Lean, and it cannot be
lifted from the existing definitions, because the structures it refers to (a
trace, and the operad-layer transitions) are not formalized at all. It needs
fresh formalization, not merely a fresh lemma. Details:

- **What exists and helps.** `Core.lean/ouroboricityTier` decides the tier from
  exactly the paper's gate primitives plus dimension: {Φ criticality, P parity,
  Ω protection, D}. Proven: `O_inf ⟺ Φ ∈ {monad,roar} ∧ P = or'`
  (`o_inf_requires_phi_c`, `o_inf_requires_P_pm_sym`, `r1_dominates`). This is
  the *conjunctive necessity* of two gate primitives, not an order. The real
  gate content is `frobenius_not_synthesizable`: the Frobenius value `or'`
  cannot be reached by tensoring lower polarities, so stage 4 is a genuine
  barrier, not composable from below. `Frobenius.lean` fully formalizes G1's
  split as four concrete `μ∘δ = id` comonoid/monoid pairs (δ_A/μ_A tensor,
  δ_B/μ_B meet, δ_D/μ_D join, δ_C/μ_C on the special class).
- **What is missing.** (a) No `trace` operator anywhere: G2's defining
  structure does not exist in Lean yet. (b) No operad-layer types (plain
  monoidal / special-Frobenius sub-operad / traced monoidal / idempotent
  terminal) as distinct objects with inclusions. (c) No precedence theorems.
- **Two mismatches the paper must resolve, not paper over.**
  1. Gate taxonomies do not line up. Magnum-opus gates = {P(4), Φ(9), Ω(12)}.
     Lean *consciousness* gates (`Consciousness.lean`) = {Φ via `phi_c_gate`,
     K via `k_slow_gate`}. Lean *tier* gates = {Φ, P, Ω, D}. Three different
     sets. The paper should adopt the tier-gate set and state plainly that the
     consciousness K-gate is a separate axis, not one of the three operad gates.
  2. In `ouroboricityTier`, Protection Ω is IRRELEVANT to O_inf (it only
     distinguishes O₁/O₂ among non-Frobenius critical systems). So the paper's
     "G3 (Protection) seals the terminal for the O_inf system" is not reflected
     in the current tier function. Either the tier function is incomplete (Ω
     should refine O_inf into sealed/unsealed) or G3's role needs restating.
     This is a concrete, decidable fork to settle before Section 3.
- **Why the derivation order 4 < 9 is nonetheless the right claim.** A trace is
  defined *over* a Frobenius/compact structure: you cannot trace a loop before
  you have the comultiplication δ to close it on. So G2 presupposes G1 as a
  category-theoretic fact, independent of the tier classifier's conjunctive
  form (which is consistent with it, no contradiction). Likewise idempotent
  completion of a traced category presupposes the trace, giving 9 < 12.

## Fresh formalization needed (proposed `GateOrdering.lean`)

1. Define the four operad layers as a linearly ordered `inductive Layer`
   (plain < frobenius < traced < terminal) with the primitive that unlocks each.
2. `trace` operator over the existing `μ_C/δ_C` Frobenius pair.
3. `theorem traced_needs_frobenius` : the trace is defined only where `μ∘δ = id`
   holds (uses `mu_delta_C_id_on_special`), giving stage 4 < 9.
4. `theorem terminal_needs_traced` : idempotent completion consumes the trace,
   giving 9 < 12.
5. Corollary `gate_order : 4 < 9 ∧ 9 < 12` as the headline.

## Remaining open questions

- Which conventional theorem best witnesses G2 (trace opens)? Candidate:
  existence of a trace on a compact-closed category (Joyal-Street-Verity).
- Stages 5-8 (F, K, G, Γ) carry no gate. Order-free among themselves, or weak
  precedence? Cleanest if they commute; check against the operad once layers
  are defined.
