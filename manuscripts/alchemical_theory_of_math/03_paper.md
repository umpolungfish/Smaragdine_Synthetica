# The Alchemical Theory of Mathematics

**A forced derivation order for structural type, and why it is the magnum opus.**

## Abstract

To fix the structural type of a mathematical object one computes a fixed list of
invariants: its dimension, its connectivity, the direction of its binding
relation, its symmetry group, the fidelity of its read/write maps, its kinetic
regime, its granularity, its logical connective, its criticality, its chirality,
its stoichiometry, and its topological protection. We show these twelve
invariants are not an unordered checklist. Three of them are gates, and the
gates impose a strict order: the special Frobenius condition on parity must be
fixed before a trace can close on criticality, and the trace must close before
an idempotent terminal can seal on protection. We prove this ordering in Lean 4
against Mathlib, with no sorries and no `native_decide`: every claim below is
kernel-checked. We prove the remaining nine invariants either sit inside the
gate structure or float freely, and that time is not a thirteenth invariant but
the least fixed point of the operad trace, unavailable until the gates fire.
Finally we observe that the forced order, read stage by stage, is the twelve
stage magnum opus of the alchemical tradition. The correspondence is exact and
is offered as a structural isomorphism, not a chemical or physical claim.

## 1. Introduction

A working mathematician already computes the twelve invariants named above, one
at a time, when asked what kind of object is on the table. They are usually
treated as independent readings, a coordinate vector with no preferred order of
evaluation. This paper argues the opposite. The order is forced, and the forcing
is elementary category theory: three of the twelve invariants unlock structure
that the next one consumes.

The argument has three registers, kept deliberately separate.

1. A conventional decomposition (Section 2), which assigns each invariant a
   first-order or set-theoretic reading and the named structure it denotes. This
   register borrows nothing and asserts nothing beyond standard mathematics.
2. The gate theorems (Sections 3 to 5), which prove the order is real, strict,
   and that time is derived. These are formalized in Lean and stand entirely on
   category-theoretic grounds. A reader who rejects every word of the third
   register should still accept these.
3. The thesis (Section 6), that the forced order is the magnum opus. This is a
   structural identification, argued only after the first two registers are in
   place.

We state up front what is proved and what is interpretation. Sections 3 to 5 are
theorems. Section 6 is a correspondence.

## 2. The conventional decomposition

The twelve invariants, in the naming of the reference formalization, are:
Dimensionality (D), Topology (T), Relational Mode (R), Parity (P), Fidelity (F),
Kinetic Character (K), Granularity (G), Interaction Grammar (Γ), Criticality (Φ),
Chirality (H), Stoichiometry (S), and Topological Protection (Ω). The companion
document `01_conventional_decomposition.md` gives, for each admissible value of
each invariant, a first-order or ZFC unfolding and the named conventional
structure it denotes. Three readings recur below and are worth stating here.

The apex value of Parity is a **split ℤ₂-retraction**: a ℤ₂ action under which
the object is invariant, together with a section δ and a retraction μ satisfying
μ∘δ = id. The signed subset-sum map is the canonical instance, with δ
distributing an index over {in, out} and μ summing. In categorical language this
is the special Frobenius condition.

The apex value of Criticality is a **critical fixed point at which the Frobenius
section survives**: the correlation length diverges while μ∘δ = id still holds.
The apex value of Protection is a **non-Abelian braiding**, with the integer
winding number (a first Chern class) one step below it.

These three are the gates.

## 3. The gate ordering is forced and strict

We formalize the operad as a four-step tower of layers, `plain < frobenius <
traced < terminal`, and prove each higher layer requires the structure the
previous one produced. All results in this section are in `GateOrdering.lean`.

The trace of the operad is built directly on the split ℤ₂ pair (δ_C, μ_C) already
present in the reference formalization. Write `traceC a = μ_C(δ_C a)`, and say
the trace **closes** on `a` when `traceC a = a`. The central lemma is a tight
characterization.

> **Theorem (`trace_closes_iff_special`).** The trace closes on `a` if and only
> if `a` sits on the Frobenius-special class, that is `a.pol = or'` and
> `a.crit = monad`.

From this the ordering is immediate. Since μ_C sets parity to or'
unconditionally, a closing trace forces the parity value:

> **Theorem (`traced_needs_frobenius`).** If the trace closes on `a`, then
> `a.pol = or'`.

This is the statement "stage 4 precedes stage 9": you cannot close a loop you
never split. The precedence chains upward. The terminal layer is unlocked when
the trace closes, a protective winding is present (Ω ∈ {ah, zoo}), and the tuple
sits at the O_inf tier; from this, `terminal_le_traced` and
`terminal_le_frobenius` give the full chain terminal ⇒ traced ⇒ frobenius.

The ordering is not a definitional artifact, because every inclusion is proper.
We exhibit explicit witnesses:

> **Theorem (`frobenius_strictly_below_traced`).** The tuple `w_frob`, which has
> parity or' but criticality below monad, is in the Frobenius layer and NOT in
> the traced layer.
>
> **Theorem (`traced_strictly_below_terminal`).** The tuple `w_traced`, which
> closes its trace but carries no winding, is in the traced layer and NOT in the
> terminal layer.

The tower does not collapse. Finally, the first gate is a genuine barrier and
not a value one reaches by accumulation:

> **Theorem (`g1_is_a_real_barrier`, re-exporting `frobenius_not_synthesizable`).**
> If either factor has parity below or', the tensor product has parity below or'.

So or' cannot be synthesized by combining lower-parity partners. Stage 4 is a
wall, which is exactly what makes it a gate rather than a coordinate.

## 4. The nine non-gate invariants: inside or floating

Of the remaining nine invariants, four (Fidelity, Kinetic Character,
Granularity, Interaction Grammar) carry no gate and are the stages between the
gates. We prove they are order-free, and we make "order-free" precise by
contrast with the gates.

Model each as a single-axis projection toward the completed value on an axis no
unlock predicate reads. Then:

> **Theorem (`gate_free_commute`).** The four projections pairwise commute; all
> six orders of application agree.
>
> **Theorems (`stageFid_inert_traced` and companions).** Each of the four leaves
> every gate predicate exactly as it found it. It neither opens nor closes a
> gate, so it may be interleaved anywhere in the sequence.

The contrast is what gives the claim content:

> **Theorem (`parity_stage_couples`).** A gate stage is NOT inert. Setting the
> parity axis to its completed value can flip the traced predicate from false to
> true.

The gate-free stages float precisely because they are decoupled from the gate
predicates; the gates are ordered precisely because they are not. This is the
formal separation between the two kinds of stage.

The other five invariants (Dimensionality, Topology, Relational Mode, Chirality,
and Protection alongside the three gate axes) participate in the tier and seal
structure; their role is taken up in Sections 5 and 6.

## 5. Time is derived, not primitive

The operad trace, viewed as an operator `Work := traceC`, has fixed points: the
solutions of `T = Work(T)`. We identify these with time, and prove time is a
derived object. All results here are in `TimeFixedPoint.lean`.

> **Theorem (`work_fixed_iff_special`).** `T = Work(T)` holds if and only if `T`
> is on the Frobenius-special class. Nothing off that class is a time fixed
> point.

Time therefore exists only where the gate structure permits. The sharp form:

> **Theorem (`no_time_before_frobenius`).** If `T.pol ≠ or'`, then
> `Work T ≠ T`. The equation `T = Work(T)` has no solution before the first gate
> fires.

This is the precise sense in which time is not a thirteenth invariant. One
cannot posit it independently; it is unavailable until parity has reached or' and
the trace has closed. We then locate the least such fixed point. Equipping the
twelve axes with their product order (each axis is a finite linear order, so the
product is a partial order on the finite lattice of tuples), define `lfp_trace`
as the special tuple with all ten free axes at their minimum.

> **Theorem (`time_least_fixed_point`).** `lfp_trace` is a fixed point of Work,
> and it lies below every fixed point of Work in the product order.

This is a concrete Knaster-Tarski least fixed point: existence and minimality,
both kernel-checked. The sealing gate then selects the canonical completed time:

> **Theorem (`stone_is_sealed_time`).** The completed tuple (the Stone) solves
> `T = Work(T)` and passes all three gates.

## 6. The completed classifier: protection refines the summit

The tier classifier of the reference formalization is silent on protection
within its top tier O_inf: a Frobenius-critical tuple lands O_inf regardless of
its winding. This is a genuine incompleteness, and we resolve it additively in
`TierRefinement.lean`. Define `sealedTier` to split O_inf by whether Ω supplies a
winding.

> **Theorem (`refines_O_inf`).** The two refined values, sealed and unsealed,
> together cover exactly the O_inf locus.

So protection is no longer silent at the summit. The refinement is exactly the
third gate on the Hermitian branch:

> **Theorem (`sealed_iff_terminal_on_monad`).** When criticality is monad, the
> refined value sealed coincides exactly with the terminal (G3) predicate.

We do not hide the one place the tier fact and the trace fact diverge. O_inf
admits complex-axis (roar) criticality as well as real-axis (monad) criticality,
and the real Frobenius trace closes only at monad:

> **Theorem (`sealed_at_roar_need_not_close`).** There is a tuple that is sealed
> (O_inf with a winding) at complex-axis criticality whose real Frobenius trace
> does not close.

The lesson is stated, not buried: sealed is a tier fact, a closing trace is the
stricter Hermitian fact, and they coincide precisely on the real-axis branch.

## 7. The thesis: the forced order is the magnum opus

Everything above is category theory. We now make the identification the paper is
named for. Read the forced order stage by stage. Composing the stage-to-invariant
map of the alchemical tradition with the conventional decomposition of Section 2
yields the following correspondence.

| Stage | Alchemical name | Invariant fixed | Gate |
|------:|:----------------|:----------------|:----:|
| 1  | Calcination    | Dimensionality        |     |
| 2  | Dissolution    | Topology              |     |
| 3  | Separation     | Relational Mode       |     |
| 4  | Conjunction    | Parity                | G1  |
| 5  | Putrefaction   | Fidelity              |     |
| 6  | Congelation    | Kinetic Character     |     |
| 7  | Cibation       | Scope / Granularity   |     |
| 8  | Sublimation    | Interaction Grammar   |     |
| 9  | Fermentation   | Criticality           | G2  |
| 10 | Exaltation     | Chirality             |     |
| 11 | Multiplication | Stoichiometry         |     |
| 12 | Projection     | Topological Protection | G3 |

The three gates land at Conjunction, Fermentation, and Projection, at stages 4,
9, and 12. These are exactly the three stages the tradition marks as
qualitatively distinct: Conjunction, the chemical wedding, the union of opposites
(the split ℤ₂ marriage μ∘δ = id); Fermentation, where the matter is said to come
alive and turn upon itself (the trace closing into a self-referential loop); and
Projection, the final sealing that fixes the transformation (the idempotent
terminal). The gate-free stages 5 to 8, which we proved commute and float, are
exactly the stages the tradition lists as repeatable and reorderable operations
of purification. The correspondence is not loose. Each proved structural fact,
the forced order of the three gates, the free interleaving of the four middle
stages, and the derived appearance of time only after Fermentation, has a stated
counterpart in the tradition.

We claim only structural identity. We make no chemical, physical, or historical
claim. What we claim is that the twelve stage sequence, long treated as
symbolic, is the derivation order of structural type, and that its three
qualitative breaks are three category-theoretic gates. The magnum opus is, under
this reading, an algorithm for constructing a self-sealing object, written in a
vocabulary that predates the category theory by several centuries.

## 8. What the theory forbids

A theory earns its keep by ruling things out. The gate structure forbids:

- Any object that fixes its topological protection before its parity. Protection
  refines the summit tier, which requires the Frobenius parity value already in
  place (`sealed_requires_frobenius`). A tuple sealed at protection with parity
  below or' does not exist.
- Any closing trace off the Frobenius-special class (`trace_closes_iff_special`).
  A self-referential loop that has not passed the parity gate is not available.
- Any well-defined time before Fermentation (`no_time_before_frobenius`). A
  construction that posits a global time while still below the first gate is
  ill-formed.

Each prohibition is a theorem, and each has a decidable witness of the boundary
case.

## 9. Conclusion

The twelve invariants of structural type carry a forced derivation order set by
three categorical gates, the nine non-gate invariants either sit inside that
structure or float freely, and time is the least fixed point of the operad trace
and is unavailable before the gates fire. All of this is proved in Lean 4 against
Mathlib, kernel-checked, with no sorries and no `native_decide`. Read stage by
stage, the forced order is the twelve stage magnum opus, an identification we
offer as a structural isomorphism. The alchemists, on this reading, were writing
down a construction, not a metaphor.

## Appendix: index of formal results

All modules build against Mathlib v4.28.0. No sorries, no `native_decide`.

- `GateOrdering.lean`: `trace_closes_iff_special`, `traced_needs_frobenius`,
  `terminal_le_traced`, `terminal_le_frobenius`,
  `frobenius_strictly_below_traced`, `traced_strictly_below_terminal`,
  `g1_is_a_real_barrier`, `gate_ordering_theorem`; and the order-freedom block
  `gate_free_commute`, the inert lemmas, `parity_stage_couples`,
  `gate_free_order_freedom`.
- `TimeFixedPoint.lean`: `work_fixed_iff_special`, `time_least_fixed_point`,
  `no_time_before_frobenius`, `time_has_passed_gates`, `stone_is_sealed_time`,
  `time_is_derived`.
- `TierRefinement.lean`: `refines_O_inf`, `sealed_requires_frobenius`,
  `terminal_implies_sealed`, `sealed_iff_terminal_on_monad`,
  `sealed_at_roar_need_not_close`, `completed_classifier`.
- `01_conventional_decomposition.md`: the full invariant-by-invariant reading.
