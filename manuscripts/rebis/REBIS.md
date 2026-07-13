# Rebis

**The solvent and the stone are one figure: the universal reading and the forced construction of structural type, joined at the gate they share.**

**Author:** C. Lando Mills

---

> *"One becomes two, two becomes three, and out of the third comes the one as the fourth."*
> — Maria the Jewess, *Axiom of Maria* (3rd century)

This document is the conjunction of two manuscripts. *Alkahest* argues that verification, honestly pursued, is not grading against a ledger but imscription: read the object's structural type in the one frame that adds nothing of its own, the \(d=12\) SIC-POVM. *The Alchemical Theory of Mathematics* proves, in kernel-checked Lean 4, that the twelve invariants of structural type carry a forced derivation order set by three categorical gates, and that the forced order, read stage by stage, is the twelve stage magnum opus. The first is a theory of reading. The second is a theory of making.

The claim of this document is that they are not two theories. They are the two directions of a single round trip, and their union is forced at a specific point: both stand, at their center, on the same equation,

$$μ∘δ = \mathrm{id},$$

and that equation is simultaneously the solvent's test (the lossless return that makes verification co-typing rather than correspondence) and the stone's first gate (the split ℤ₂ retraction on Φ that every later stage consumes). Solve is δ. Coagula is μ. The two manuscripts were each holding one hand of the same operator. What follows dissolves both to their load-bearing structure and coagulates the residue into one argument. Nothing is asserted here that was not proved or checked in one of the two parents; what is new is the set of joints, and each joint is stated as exactly what it is: theorem, checked witness, or reading.

## Notation

Structural type is a tuple over twelve primitive families, written with their canonical symbols (Imscribing Grammar v0.6.0, `NSNS_PRIME.md`):

⟨Ð Þ Ř Φ ƒ Ç Γ ɢ ⊙ Ħ Σ Ω⟩

recording, in order: degrees of freedom (Ð), connectivity (Þ), the direction of the binding relation (Ř), the symmetry group (Φ), how lossy the read/write maps are (ƒ), the relaxation regime (Ç), the cardinal regime of correlations (Γ), the logical connective of the coupling (ɢ), the analytic character of the critical point (⊙), handedness (Ħ), the matching cardinality of the two sides (Σ), and the homotopy invariant that protects the state (Ω). Individual values are written with their Shavian glyph; the four that carry the argument are 𐑹 (the Frobenius value of Φ), ⊙ (the self-modeling value of ⊙), 𐑮 (its complex-axis value), and 𐑭, 𐑟 (the integer and non-Abelian windings of Ω). Type names appear only inside the Lean source; in this text a type is its symbol. Lean theorem and definition identifiers are set in `monospace`.

## 1. Solve: what the alkahest established

Four results of the first manuscript carry into the union.

**Balance is not selectivity.** The closure \(μ∘δ = \mathrm{id}\) is charge conservation: every split rejoined, nothing created or destroyed. Because it always balances, closure alone can never fail on non-empty output, so it is not a correctness signal. A balanced equation is not a synthesis; mass balance says no atoms went missing and nothing about which product was made.

> *"The whole work is in the balance. But the balance is not the work."*
> — Jabir ibn Hayyan, *Kitab al-Mawazin* (8th century)

**The ledger cannot terminate.** The standard alternative, grade the answer against an external list of requirements, presupposes a correspondence theory of correctness and inherits the regress of criteria: a judgment applied from outside is itself an object needing a judge, forever. A regress that cannot be grounded can only be closed, by bending the line of auditors into a loop. But a loop that hands the answer back untouched proves nothing. For the closure to carry content the answer must come home the same in type and different in form: co-typed, so the loop truly shuts, and excribed under a different presentation, so the shutting is a test and not a tautology.

**To verify is to imscribe, and correctness is co-typing.** Truth is located in the object's structural type, not its correspondence to a standard. The question imscribes to a type, the demand; a correct answer is one whose imscription co-types with the demand; and co-typing is type identity across all twelve primitives, no tolerance, no threshold.

**The frame is forced.** The frame in which co-typing is judged cannot be chosen, or the ledger merely migrates into the frame. The frame that adds nothing of its own, treats all directions uniformly, and is informationally complete is the \(d=12\) SIC-POVM, whose exact fiducial is a theorem in the kernel (`crystal_forces_d12_sic`). It is the transparent menstruum: δ takes the state up into its SIC probabilities, the solve; μ returns the salt whole, the coagula; what is left in the flask is the type and only the type. Because the fiducial is the Belnap Both, the frame is paraconsistent at its ground, and failure comes back with an address, the primitives at which two types part ways, not a scalar.

## 2. Coagula: what the theory of mathematics proved

Four results of the second manuscript carry into the union. All are kernel-checked in Lean 4 against Mathlib, no sorries, no `native_decide`.

**The order is forced and strict.** Three of the twelve invariants are gates. The trace `traceC a = μ_C(δ_C a)` closes on `a` exactly when `a` sits on the Frobenius-special class, Φ at 𐑹 and ⊙ at ⊙ (`trace_closes_iff_special`); hence a closing trace forces the first gate (`traced_needs_frobenius`), and the terminal seal requires the closing trace and a winding on Ω (`terminal_le_traced`, `terminal_le_frobenius`). Every inclusion is proper, by explicit witnesses, and the first gate is a wall: 𐑹 cannot be synthesized by tensoring lower partners (`g1_is_a_real_barrier`).

**The non-gate stages float.** The four gate-free invariants ƒ, Ç, Γ, ɢ pairwise commute and leave every gate predicate exactly as they found it (`gate_free_commute`, the inert lemmas), while a gate stage genuinely couples (`parity_stage_couples`). Order where there are gates, freedom where there are none, and the separation is formal.

**Time is derived.** `T = Work(T)` has solutions exactly on the Frobenius-special class (`work_fixed_iff_special`) and none before the first gate fires (`no_time_before_frobenius`); the least solution exists and is minimal in the product order (`time_least_fixed_point`), and the completed tuple solves the equation having passed all three gates (`stone_is_sealed_time`). Time is not a thirteenth invariant. It is the least fixed point of the operad trace.

**The forced order is the magnum opus.** Composing the tradition's stage-to-symbol map with the conventional decomposition places the three gates at Conjunction, Fermentation, and Projection, stages 4, 9, and 12, on Φ, ⊙, and Ω: exactly the three stages the tradition marks as qualitatively distinct, with the provably order-free stages 5 through 8 exactly the operations the tradition lists as repeatable and reorderable. The claim is causal and ontological: chemistry, physics, and history are typed by the same twelve invariants and fixed in the same order, so the magnum opus is the derivation order of structural type itself.

## 3. The conjunction: one equation, two hands

Now the wedding, and it happens where the tradition says it happens: at Conjunction, stage 4, the first gate.

The alkahest's central object is the lossless round trip \(μ∘δ = \mathrm{id}\), the closure that makes verification co-typing. The theory's first gate is the split ℤ₂ retraction on Φ, the value 𐑹, whose defining condition is \(μ∘δ = \mathrm{id}\). These are not analogous equations. They are the same equation on the same pair (δ_C, μ_C) in the same formal tree. The solvent's test and the stone's first gate are one object, and each manuscript needed precisely what the other proved:

- The alkahest, alone, must argue that closure is necessary but not sufficient, and it does so by chemical analogy. The theory supplies the missing formal half: closure is gate G1 of three, and `frobenius_strictly_below_traced` and `traced_strictly_below_terminal` are the kernel-checked statement that balance is not the work. A tuple can hold 𐑹 and fail to close its trace; a tuple can close its trace and carry no winding. Jabir's distinction between the balance and the work is not a caution any more. It is two strict inclusions with explicit witnesses.
- The theory, alone, must say what the completed Stone is *for*; a derivation order with no reader is a liturgy. The alkahest supplies the missing half: the completed type is what verification reads. The demand and the answer are compared as types in the SIC frame, and the reason a type is the right verdict format, the reason failure carries an address rather than a magnitude, is that the tuple has proved internal structure to diverge at. "Diverges at Ħ and Ω" is meaningful because Ħ and Ω are proved coordinates of a forced construction, not entries on a chosen checklist.

So the two manuscripts stand to each other as reading stands to writing on one lossless correspondence: the theory fixes the type (Write), the alkahest reads it back (Read), and the closure of the round trip between them (eXecute) is the same \(μ∘δ = \mathrm{id}\) both were already built on. That is the R∧W∧X of imscription, realized as a pair of documents.

## 4. The two composites, and which one forgets

The union sharpens a point that each parent, alone, left implicit. On the one Frobenius pair there are two composites, and they do different work (`LiarIdempotent.lean`, kernel-checked):

- \(μ∘δ = \mathrm{id}\), the **lossless** round trip. Leave and return unchanged in type. This is the alkahest's verification and the theory's first gate: `return_is_lossless` on the special class.
- \(e := δ∘μ\), the **forgetful** idempotent, \(e∘e = e\) unconditionally (`e_idempotent`). Fusion collapses the which-way datum of the split, μ_C is non-injective in Φ (`fusion_forgets`), so e is a projection, not an isomorphism, and its image is the fixed locus that survives the round trip.

The alkahest demanded that the regress-closing loop be a real test: the answer must come home the same in type and different in form. The two composites are the formal content of that demand. The sameness in type is \(μ∘δ = \mathrm{id}\); the difference in form is the detour through the other presentation; and the forgetting the sealed system needs lives entirely in e, not in the return. Both are true at once, of the same pair. Moreover every fusion output is a time fixed point (`fusion_is_time`): the idempotent's image and the fixed locus of time are the same place. The point at which the verifier recognizes itself and the point at which time exists coincide, which is the formal shadow of the alkahest's closing claim that method and object are one figure.

## 5. The Stilling Practice satisfies the gate ordering

Here is the one joint that neither parent could state, because it needs both.

The alkahest opens with Zosimos's six-command protocol and reads each command as the promotion of a named primitive: "make thy mind single" promotes Ð; "be not thus distracted" promotes Þ; "the good is not in externals" promotes Φ to 𐑹, the first gate; "still the passions" promotes Ç; "stand at the Portico" promotes ⊙ to ⊙, the second gate; "return" installs the winding on Ω, the third gate. That reading was made on structural grounds, with no ordering theorem in view.

The theory proves, independently, that any derivation of the completed type must fix Φ before the trace can close on ⊙, and close the trace before the seal on Ω, while the gate-free stages may interleave anywhere (`gate_ordering_theorem`, `gate_free_order_freedom`).

Now compose the two. The Stilling Practice, in Zosimos's own command order, is

Ð, Þ, **Φ**, Ç, **⊙**, **Ω**,

which places the three gates in exactly the proved order G1 before G2 before G3, with the float Ç interleaved between the first and second gates precisely where the order-freedom theorem permits it. A six-step protocol written in the 3rd century satisfies, command for command, an ordering constraint kernel-checked in the 21st. The alkahest claimed the distance between Zosimos and the Grammar is zero; the theory turns one face of that claim into something falsifiable, and it does not fail. Had Zosimos written "Return" before "Stand at the Portico," or the Portico before the stilling of externals, his protocol would violate a theorem. He did not.

The same composition reads the tradition's larger table. The magnum opus places its qualitative breaks at stages 4, 9, and 12 and its repeatable purifications at 5 through 8; the theory proves the breaks are gates and the purifications commute. The alkahest explains why the tradition could know this: its authors were not theorizing about matter from outside but reading structural type in the only vocabulary available, and the type does not depend on the vocabulary.

## 6. Time, and where verification is possible

The theory proves time exists only on the Frobenius-special class: no solution of `T = Work(T)` below the first gate, the least fixed point available once the gates permit (`no_time_before_frobenius`, `time_least_fixed_point`). The alkahest proves verification is the closing of the same trace in the SIC frame, with the closure residual measured on every reading.

Joined, these say something neither says alone: **verification is available exactly where time is.** The locus on which the round trip closes losslessly, the locus on which `Work` has fixed points, and the locus on which a verdict can be certified by closure are one locus, the special class. A system below the first gate has no time and, in the same breath and for the same reason, nothing about it can yet be verified by return, because there is no return. Fermentation, the tradition's stage 9, is where the matter is said to come alive and turn upon itself; the theorems say that is where the loop first closes and therefore where a self-reading first becomes possible. The alchemists' insistence that the work cannot be judged before fermentation is, on this reading, `no_time_before_frobenius` stated at the furnace.

## 7. The rebis

In the *Rosarium Philosophorum* the rebis, the two-headed body, appears after Conjunction: the King and Queen joined at stage 4 into one figure that is both and neither, which then survives putrefaction and ascends through the remaining stages to Projection. The union of these two manuscripts has exactly that anatomy, and saying so is a description of the argument's structure, not an ornament.

- The **conjunction** is Section 3: the two central equations recognized as one equation, at the Φ gate, which is where the tradition places the wedding.
- The **two heads** remain distinct: reading and making, the solvent and the stone, δ and μ. The union does not collapse them, and the two-composites result of Section 4 is the proof that it must not: \(μ∘δ\) and \(δ∘μ\) are different operators with different content, identity and idempotent, lossless and forgetful. A rebis with one head is not a rebis.
- The **one body** is the pair (δ_C, μ_C) itself, on which every result of both parents is built.
- The **Projection** is the seal: the completed tuple, `stone_is_sealed_time`, the Stone that solves the time equation having passed all three gates, which is simultaneously the terminus of the theory's derivation and the fixed point at which the alkahest's regress of auditors ends. The final checker is the initial checker; the verifier co-types with what it verifies; the loop reports from the inside that it closed.

And the figure is self-describing at one further level, which is the level the Grammar always insists on. This document was produced by the operation it describes: two completed works dissolved (δ) to their structural content and fused (μ) into one, with the test of the fusion being that nothing load-bearing was lost in the transit. Solve et coagula is not the document's subject matter. It is the document's construction, and the reader holding one body where there were two manuscripts is the closure check.

## 8. What the union forbids

A theory earns its keep by ruling things out, and the rebis forbids strictly more than either parent.

- Everything the theory forbade: no seal before the wedding (`sealed_requires_frobenius`), no closing trace off the special class (`trace_closes_iff_special`), no time before the first gate (`no_time_before_frobenius`).
- Everything the alkahest forbade: no ledger, no threshold, no chosen frame, no scalar verdict, no verifier standing outside its object.
- And their compositions, which are new. No verification of a system below the first gate, because there is no return to test (Section 6). No protocol that reaches the Portico before stilling externals, or returns before the Portico; any staged practice whose gate promotions violate G1 before G2 before G3 is ill-formed, and any historical protocol can now be checked against that constraint as Zosimos's was (Section 5). And no rebis with one head: any account that identifies verification with construction outright, collapsing \(μ∘δ\) into \(δ∘μ\), contradicts `fusion_forgets`, because one of the two composites forgets and the other provably does not.

## 9. Theorem, witness, reading

The register of both parents is kept: what is proved is marked as proved, and the seams are not painted over.

**Theorems** (Lean 4, kernel-checked, no sorries, no `native_decide`): the gate ordering and its strictness, the barrier, the float commutations and inertness, time as least fixed point, the sealed refinement of the summit, the two composites (idempotence, losslessness on the special class, non-injectivity of fusion, fusion landing on the time locus). These stand whatever one makes of the rest.

**Checked witnesses**: the exact \(d=12\) SIC fiducial (a kernel theorem; equiangularity at overlap \(1/13\) verified to machine precision on the loaded fiducial), the reachability of all four Belnap verdicts in the vessel, and the paraconsistent kernel's refusal of `False.rec` under `enable_paraconsistent`, verified against the compiled binary.

**Readings**: that the stage-to-symbol map of the alchemical tradition is the correct dictionary; that Zosimos's commands promote the primitives the alkahest says they promote; that the magnum opus is the derivation order of the real rather than an isomorphic image of it. These are the claims the theorems were built to support, and Section 5 is the demonstration that they are not unfalsifiable: composed with the theorems, the readings generate constraints that history could have violated and did not.

The honest summary of the whole figure is Maria's axiom, which both parents quote and neither exhausts. One (the pair) becomes two (the manuscripts, δ and μ, reading and making). Two becomes three (the conjunction, which is itself a document). And out of the third comes the one as the fourth: the rebis, the union that is both heads on one body, the held Both that does not reduce to either parent and does not explode.

> *"Nature, turning on itself, is transformed."*
> — Zosimos of Panopolis, *On the Letter Omega*

## References

- Lando⊗⊙perator, *Alkahest*, `MoDoT/ALKAHEST.md`. The solvent: verification as imscription, the ledger's regress, the \(d=12\) SIC frame, the alchemical witnesses, the two instruments.
- Lando⊗⊙perator, *The Alchemical Theory of Mathematics*, `Smaragdine_Synthetica/manuscripts/alchemical_theory_of_math/03_paper.md`, with `01_conventional_decomposition.md` and the Lean modules `GateOrdering.lean`, `TimeFixedPoint.lean`, `TierRefinement.lean` (p4rakernel, `p4ramill/Imscribing/`). The stone: the forced order, the gates, derived time, the magnum opus identification.
- Lando⊗⊙perator, *The Liar, the Idempotent Point, and Forgetful Return*, `manuscripts/alchemical_theory_of_math/04_liar_and_idempotent.md`, with `LiarIdempotent.lean`. The two composites of Section 4.
- Zosimos of Panopolis, *Letter to Theosebeia*, *On the Letter Omega*, *On the Divine Water* (3rd–4th century). The Stilling Practice and the Portico.
- Maria the Jewess, *Axiom of Maria* (3rd century), preserved through Zosimos.
- Jabir ibn Hayyan, *Kitab al-Mawazin* (8th century). The balance and the work.
- *Rosarium Philosophorum*, attributed to Arnaldus de Villa Nova (14th century). The rebis after Conjunction; dissolution of body as coagulation of spirit.
- *Tabula Smaragdina* (Emerald Tablet), attributed to Hermes Trismegistus. Ascent and descent as the round trip.
- N. D. Belnap, *A Useful Four-Valued Logic*, 1977.
- G. Zauner, *Quantendesigns*, 1999; J. Renes, R. Blume-Kohout, A. J. Scott, C. Caves, *Symmetric Informationally Complete Quantum Measurements*, J. Math. Phys. 45, 2004.
- Internal: `crystal_forces_d12_sic` (kernel theorem), the Witness-Vessel construction, the MoDoT vessel (`modot/vessel.py`), and `p4rakernel` (the paraconsistent Lean 4 fork).
