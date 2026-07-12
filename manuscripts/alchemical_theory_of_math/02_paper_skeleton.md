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

## Fresh formalization: DONE and building (2026-07-12)

`Imscribing/GateOrdering.lean` (in `p4rakernel/p4ramill/`, mirrored to
`Smaragdine_Synthetica/lean/`). Builds green against Mathlib v4.28.0, zero
sorries, and no `native_decide`: every proof is kernel-checked. The four operad
layers are a linearly ordered `inductive Layer` (plain < frobenius < traced <
terminal). The trace `traceC` is built on the existing `μ_C/δ_C` polarization
Frobenius pair. Theorems now available to cite in Section 3:

- `trace_closes_iff_special` : the traced layer is EXACTLY the special class
  `pol = or' ∧ crit = monad`. This is the hinge; it uses
  `mu_delta_C_id_on_special`.
- `traced_needs_frobenius` : `traceCloses a → a.pol = or'`. Stage 4 < 9 as a
  theorem (you cannot close a loop you never split).
- `terminal_le_traced`, `terminal_le_frobenius` : G3 presupposes G2 presupposes
  G1 (the precedence chain).
- `frobenius_strictly_below_traced`, `traced_strictly_below_terminal` : every
  inclusion is PROPER, each witnessed by an explicit tuple (`w_frob`,
  `w_traced`) inhabiting one layer but not the next. The tower does not collapse.
- `g1_is_a_real_barrier` : re-exports `frobenius_not_synthesizable` — `or'` is
  not reachable by tensoring lower parities, so stage 4 is a genuine gate.
- `gate_order` : `4 < 9 ∧ 9 < 12` (the stage arithmetic).
- `gate_ordering_theorem` : the headline conjunction bundling all of the above,
  plus `w_stone` inhabiting the terminal layer.

Resolution of earlier mismatch #2 (Protection irrelevant to O_inf): handled by
defining `unlockTerminal` to require BOTH a protective winding (Ω ∈ {ah, zoo})
AND the O_inf tier on top of a closing trace, rather than reading G3 off the
bare tier function. G3 acts on the traced operad, exactly as the category theory
says; the tier function's silence on Ω-within-O_inf is sidestepped, not relied
on. If the paper later wants Ω to refine O_inf in `Core.lean` itself, that is a
separate, additive change.

## Stages 5-8 are order-free: PROVED (2026-07-12)

Settled in `GateOrdering.lean` §8. The four gate-free stages are single-axis
projections toward the Stone on axes no unlock predicate reads (F, K, G, Γ).
Two theorems make "order-free" precise and separate them from the gates:

- `gate_free_commute` : the four projections pairwise commute (all six orders
  agree). Updates on disjoint axes.
- `stageFid_inert_traced`, `stageKin_inert_traced`, `stageGran_inert_traced`,
  `stageGram_inert_traced` (+ `gate_free_inert_frobenius`) : each gate-free
  stage is INERT on the gates. It neither opens nor closes a gate, so it can be
  interleaved anywhere in the sequence.
- `parity_stage_couples` : the CONTRAST. A gate stage (parity, G1) is not inert
  — setting the parity axis can flip `unlockTraced` from false to true
  (witness `{w_stone with pol := nun}`). That coupling is precisely why the
  gates are ordered while 5-8 float.
- `gate_free_order_freedom` : bundles commutation, inertness, and the coupling
  contrast.

So the theory's cleanest form holds: 5-8 commute and float; 4, 9, 12 are forced.

## Remaining open questions

- Which conventional theorem best witnesses G2 (trace opens)? Candidate:
  existence of a trace on a compact-closed category (Joyal-Street-Verity). This
  is a naming/citation task for Section 3 prose, not a proof obligation.
- Should Ω refine O_inf inside `Core.lean` (sealed/unsealed), making the tier
  function itself carry G3? Currently G3 lives in `unlockTerminal`. Additive,
  optional; only needed if the paper wants the tier classifier to be complete.
