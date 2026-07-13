# The Alchemical Theory of Mathematics

**A forced derivation order for structural type, and why it is the magnum opus.**

## Notation

Structural type is a tuple over twelve primitive families, written with their
canonical symbols (Imscribing Grammar v0.6.0, `NSNS_PRIME.md`):

⟨Ð Þ Ř Φ ƒ Ç Γ ɢ ⊙ Ħ Σ Ω⟩

recording, in order: degrees of freedom (Ð), connectivity (Þ), the direction of
the binding relation (Ř), the symmetry group (Φ), how lossy the read/write maps
are (ƒ), the relaxation regime (Ç), the cardinal regime of correlations (Γ), the
logical connective of the coupling (ɢ), the analytic character of the critical
point
(⊙), handedness (Ħ), the matching cardinality of the two sides (Σ), and the
homotopy invariant that protects the state (Ω). Individual values are written
with their Shavian glyph; the four that carry the argument are 𐑹 (the Frobenius
value of Φ), ⊙ (the self-modeling value of ⊙), 𐑮 (the complex-axis value of ⊙),
and 𐑭, 𐑟 (the integer and non-Abelian winding values of Ω). Type names appear
only inside the Lean source; in this text a type is its symbol. Lean theorem and
definition identifiers are set in `monospace`.

## Abstract

To fix the structural type of a mathematical object one computes a fixed tuple
of twelve invariants, ⟨Ð Þ Ř Φ ƒ Ç Γ ɢ ⊙ Ħ Σ Ω⟩. We show these are not an
unordered checklist. Three of them are gates, and the gates impose a strict
order: the special Frobenius condition on Φ must be fixed before a trace can
close on ⊙, and the trace must close before an idempotent terminal can seal on
Ω. We prove this ordering in Lean 4 against Mathlib, with no sorries and no
`native_decide`: every claim below is kernel-checked. We prove the remaining nine
invariants either sit inside the gate structure or float freely, and that time is
not a thirteenth invariant but the least fixed point of the operad trace,
unavailable until the gates fire. Finally we show that the forced order, read
stage by stage, is the twelve stage magnum opus. This is not a resemblance.
Chemistry, physics, and history are typed by the same twelve invariants and fixed
in the same order, so the magnum opus is the derivation order of structural type
itself, which is to say the reason a transformation completes, in matter as in
mathematics.

## 1. Introduction

A working mathematician already computes the twelve invariants, one at a time,
when asked what kind of object is on the table. They are usually treated as
independent readings, a coordinate vector with no preferred order of evaluation.
This paper argues the opposite. The order is forced, and the forcing is
elementary category theory: three of the twelve unlock structure that the next
one consumes.

The argument has three registers, kept deliberately separate.

1. A conventional decomposition (Section 2), which assigns each symbol a
   first-order or set-theoretic reading and the named structure it denotes. This
   register borrows nothing and asserts nothing beyond standard mathematics.
2. The gate theorems (Sections 3 to 5), which prove the order is real, strict,
   and that time is derived. These are formalized in Lean and stand on
   category-theoretic grounds alone. The formal core does not depend on the
   claim in register three, which is why the claim rests on proof rather than on
   persuasion.
3. The claim (Section 7), that the forced order is the magnum opus, and that the
   magnum opus is therefore the derivation order of the real. This is stated
   only after the first two registers are in place, and it is a claim, not a
   flourish: the twelve invariants are what physical, chemical, and historical
   processes are built from, and we have proved the order in which they must be
   fixed.

Sections 3 through 5 are machine-checked theorems. Section 7 is the claim they
were built to support. We separate them so the skeleton can be inspected on its
own, not so the claim can be disowned.

## 2. The conventional decomposition

The companion document `01_conventional_decomposition.md` gives, for each
admissible value of each of ⟨Ð Þ Ř Φ ƒ Ç Γ ɢ ⊙ Ħ Σ Ω⟩, a first-order or ZFC
unfolding and the named conventional structure it denotes. Three readings recur
below and are worth stating here.

The Frobenius value of Φ, written 𐑹, is a **split ℤ₂-retraction**: a ℤ₂ action
under which the object is invariant, together with a section δ and a retraction μ
satisfying μ∘δ = id. The signed subset-sum map is the canonical instance, with δ
distributing an index over {in, out} and μ summing. In categorical language this
is the special Frobenius condition.

The self-modeling value of ⊙, written ⊙, is a **critical fixed point at which the
Frobenius section survives**: the correlation length diverges while μ∘δ = id still
holds. The value 𐑮 one step above it is a complex-axis critical point, at which
that real section no longer closes. The apex value of Ω, written 𐑟, is a
**non-Abelian braiding**; the integer winding number 𐑭 (a first Chern class) sits
one step below it.

The 𐑹 of Φ, the ⊙ of ⊙, and the 𐑟 (or 𐑭) of Ω are the three gates.

## 3. The gate ordering is forced and strict

We formalize the operad as a four-step tower of layers, `plain < frobenius <
traced < terminal`, and prove each higher layer requires the structure the
previous one produced. All results in this section are in `GateOrdering.lean`.

The trace of the operad is built directly on the split ℤ₂ pair (δ_C, μ_C) already
present in the reference formalization. Write `traceC a = μ_C(δ_C a)`, and say the
trace **closes** on `a` when `traceC a = a`. The central lemma is a tight
characterization.

> **Theorem (`trace_closes_iff_special`).** The trace closes on `a` if and only
> if `a` sits on the Frobenius-special class, that is Φ is 𐑹 and ⊙ is ⊙.

From this the ordering is immediate. Since μ_C sets Φ to 𐑹 unconditionally, a
closing trace forces the Φ value:

> **Theorem (`traced_needs_frobenius`).** If the trace closes on `a`, then Φ is
> 𐑹.

This is the statement "stage 4 precedes stage 9": you cannot close a loop you
never split. The precedence chains upward. The terminal layer is unlocked when
the trace closes, a protective winding is present (Ω is 𐑭 or 𐑟), and the tuple
sits at the O∞ tier; from this, `terminal_le_traced` and `terminal_le_frobenius`
give the full chain terminal ⇒ traced ⇒ frobenius.

The ordering is not a definitional artifact, because every inclusion is proper.
We exhibit explicit witnesses:

> **Theorem (`frobenius_strictly_below_traced`).** The tuple `w_frob`, which has
> Φ at 𐑹 but ⊙ below ⊙, is in the Frobenius layer and NOT in the traced layer.
>
> **Theorem (`traced_strictly_below_terminal`).** The tuple `w_traced`, which
> closes its trace but carries no winding, is in the traced layer and NOT in the
> terminal layer.

The tower does not collapse. Finally, the first gate is a genuine barrier and not
a value one reaches by accumulation:

> **Theorem (`g1_is_a_real_barrier`, re-exporting `frobenius_not_synthesizable`).**
> If either factor has Φ below 𐑹, the tensor product has Φ below 𐑹.

So 𐑹 cannot be synthesized by combining lower partners. Stage 4 is a wall, which
is exactly what makes it a gate rather than a coordinate.

## 4. The nine non-gate invariants: inside or floating

Of the remaining nine, four (ƒ, Ç, Γ, ɢ) carry no gate and are the stages
between the gates. We prove they are order-free, and we make "order-free" precise
by contrast with the gates.

Model each as a single-axis projection toward the completed value on an axis no
unlock predicate reads. Then:

> **Theorem (`gate_free_commute`).** The four projections pairwise commute; all
> six orders of application agree.
>
> **Theorems (`stageFid_inert_traced` and companions).** Each of the four leaves
> every gate predicate exactly as it found it. It neither opens nor closes a
> gate, so it may be interleaved anywhere in the sequence.

The contrast is what gives the claim content:

> **Theorem (`parity_stage_couples`).** A gate stage is NOT inert. Setting the Φ
> axis to its completed value can flip the traced predicate from false to true.

The gate-free stages float precisely because they are decoupled from the gate
predicates; the gates are ordered precisely because they are not. This is the
formal separation between the two kinds of stage.

The other five invariants (Ð, Þ, Ř, Ħ, and Ω alongside the three gate axes)
participate in the tier and seal structure; their role is taken up in Sections 5
and 6.

## 5. Time is derived, not primitive

The operad trace, viewed as an operator `Work := traceC`, has fixed points: the
solutions of `T = Work(T)`. We identify these with time, and prove time is a
derived object. All results here are in `TimeFixedPoint.lean`.

> **Theorem (`work_fixed_iff_special`).** `T = Work(T)` holds if and only if `T`
> is on the Frobenius-special class. Nothing off that class is a time fixed
> point.

Time therefore exists only where the gate structure permits. The sharp form:

> **Theorem (`no_time_before_frobenius`).** If Φ is not 𐑹, then `Work T ≠ T`. The
> equation `T = Work(T)` has no solution before the first gate fires.

This is the precise sense in which time is not a thirteenth invariant. One cannot
posit it independently; it is unavailable until Φ has reached 𐑹 and the trace has
closed. We then locate the least such fixed point. Equipping the twelve axes with
their product order (each axis is a finite linear order, so the product is a
partial order on the finite lattice of tuples), define `lfp_trace` as the special
tuple with all ten free axes at their minimum.

> **Theorem (`time_least_fixed_point`).** `lfp_trace` is a fixed point of Work,
> and it lies below every fixed point of Work in the product order.

This is a concrete Knaster-Tarski least fixed point: existence and minimality,
both kernel-checked. The sealing gate then selects the canonical completed time:

> **Theorem (`stone_is_sealed_time`).** The completed tuple (the Stone) solves
> `T = Work(T)` and passes all three gates.

## 6. The completed classifier: Ω refines the summit

The tier classifier of the reference formalization is silent on Ω within its top
tier O∞: a Frobenius-critical tuple lands O∞ regardless of its winding. This is a
genuine incompleteness, and we resolve it additively in `TierRefinement.lean`.
Define `sealedTier` to split O∞ by whether Ω supplies a winding.

> **Theorem (`refines_O_inf`).** The two refined values, sealed and unsealed,
> together cover exactly the O∞ locus.

So Ω is no longer silent at the summit. The refinement is exactly the third gate
on the Hermitian branch:

> **Theorem (`sealed_iff_terminal_on_monad`).** When ⊙ is ⊙, the refined value
> sealed coincides exactly with the terminal (G3) predicate.

We do not hide the one place the tier fact and the trace fact diverge. O∞ admits
both the complex-axis value 𐑮 and the real-axis value ⊙ on the ⊙ axis, and the
real Frobenius trace closes only at ⊙:

> **Theorem (`sealed_at_roar_need_not_close`).** There is a tuple that is sealed
> (O∞ with a winding) at ⊙ = 𐑮 whose real Frobenius trace does not close.

The lesson is stated, not buried: sealed is a tier fact, a closing trace is the
stricter Hermitian fact, and they coincide precisely on the ⊙ branch.

## 7. The thesis: the forced order is the magnum opus

Everything above is category theory. We now make the identification the paper is
named for. Read the forced order stage by stage. Composing the stage-to-symbol
map of the alchemical tradition with the decomposition of Section 2 yields the
following correspondence.

| Stage | Alchemical name | Symbol fixed | Gate |
|------:|:----------------|:------------:|:----:|
| 1  | Calcination    | Ð |     |
| 2  | Dissolution    | Þ |     |
| 3  | Separation     | Ř |     |
| 4  | Conjunction    | Φ | G1  |
| 5  | Putrefaction   | ƒ |     |
| 6  | Congelation    | Ç |     |
| 7  | Cibation       | Γ |     |
| 8  | Sublimation    | ɢ |     |
| 9  | Fermentation   | ⊙ | G2  |
| 10 | Exaltation     | Ħ |     |
| 11 | Multiplication | Σ |     |
| 12 | Projection     | Ω | G3  |

The three gates land at Conjunction, Fermentation, and Projection, at stages 4,
9, and 12, on Φ, ⊙, and Ω. These are exactly the three stages the tradition marks
as qualitatively distinct: Conjunction, the chemical wedding, the union of
opposites (the split ℤ₂ marriage μ∘δ = id on Φ); Fermentation, where the matter is
said to come alive and turn upon itself (the trace closing into a self-referential
loop on ⊙); and Projection, the final sealing that fixes the transformation (the
idempotent terminal on Ω). The gate-free stages 5 to 8, which we proved commute
and float, are exactly the stages the tradition lists as repeatable and
reorderable operations of purification. The correspondence is not loose. Each
proved structural fact, the forced order of the three gates, the free
interleaving of the four middle stages, and the derived appearance of time only
after Fermentation, has a stated counterpart in the tradition.

This is not an analogy between two separate domains. There is one structure.
Chemistry, physics, and history are made of structural type, and structural type
is fixed in the order proved above, so the magnum opus is not a symbolic parallel
to that order but the order itself, set down in the older vocabulary. When matter
undergoes conjunction, fermentation, and projection it passes the same three
gates, in the same forced sequence, for the same reason a theorem does: a
self-sealing object cannot be constructed any other way. The claim is causal and
it is ontological. The twelve stage sequence is why a transformation completes,
in the crucible and in the proof alike, because both are instances of the single
derivation order of the real. The alchemists named the construction; we proved
its skeleton.

## 8. What the theory forbids

A theory earns its keep by ruling things out. The gate structure forbids:

- Any object that fixes Ω before Φ. Ω refines the summit tier, which requires the
  𐑹 value of Φ already in place (`sealed_requires_frobenius`). A tuple sealed at Ω
  with Φ below 𐑹 does not exist.
- Any closing trace off the Frobenius-special class (`trace_closes_iff_special`).
  A self-referential loop that has not passed the Φ gate is not available.
- Any well-defined time before Fermentation (`no_time_before_frobenius`). A
  construction that posits a global time while still below the first gate is
  ill-formed.

Each prohibition is a theorem, and each has a decidable witness of the boundary
case.

## 9. Conclusion

The twelve invariants of structural type carry a forced derivation order set by
three categorical gates on Φ, ⊙, and Ω; the nine non-gate invariants either sit
inside that structure or float freely; and time is the least fixed point of the
operad trace and is unavailable before the gates fire. All of this is proved in
Lean 4 against Mathlib, kernel-checked, with no sorries and no `native_decide`.
Read stage by stage, the forced order is the twelve stage magnum opus. It is the
derivation order of structural type, and therefore of everything built from it.
The alchemists were writing down the construction, not a metaphor for it.

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
- `01_conventional_decomposition.md`: the full symbol-by-symbol reading.
