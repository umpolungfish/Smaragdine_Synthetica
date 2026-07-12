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

## Open questions to resolve before drafting prose

- Precise statement and proof obligation for "each gate consumes the prior
  structure." Is stage 4 < 9 provable from the operad definitions in
  `Smaragdine_Synthetica/lean`, or does it need a fresh lemma?
- Which conventional theorem best witnesses G2 (trace opens)? Candidate: the
  existence of a trace on a compact-closed category (Joyal-Street-Verity).
- The stages 5-8 (F, K, G, Γ) carry no gate. Are they order-free among
  themselves, or is there a weaker precedence? The theory is cleanest if they
  commute; check against the operad.
