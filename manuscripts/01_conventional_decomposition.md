# Conventional Decomposition of the 12-Primitive Crystal

Phase 1 of the Alchemical Theory of Mathematics. This document stands alone as
a reference: it pushes each per-primitive CL8NK fragment down into two layers,
a first-order / ZFC unfolding and the named conventional structure it denotes.
No alchemical claim is made here. The thesis that the primitive order is a
derivation order is argued in the companion manuscript and rests on this table.
Read *derivation* as dependency, never as sequence: see *Reading the table* §5.

## Sources and provenance

Every fragment below is quoted from `CL8NK_FORMULAE` in
`imscribing_grammar/navigators/cl8nk_navigator.py` (the per-primitive formula
map, sourced in turn from `IG_catalog.json`). Axis names and value orderings
are the authoritative ones from `Smaragdine_Synthetica/lean/Core.lean`
(v0.5.69), whose constructor order defines the ordinals. Nothing here is hand
derived; each row is a fragment as emitted, annotated with its conventional
reading.

**The proximity labels are L8-relative.** `apex`, `close` and `distant` are the
navigator's distance from the CLINK L8 reference, not an absolute ranking of the
values. This mattered little while L8 was the terminal layer of the chain. It
matters now: CLINK L9 was born 2026-07-13 and sits above L8 at O_∞⁺, with its own
reference typing and its own navigator (`cl9nk_navigator.py`). Several values this
table marks `distant` are apex in L9's register. Read the labels as coordinates in
a dialect, not as a verdict on a value.

## Dialect reconciliation (navigator glyphs to Core axes)

The navigator labels the twelve axes with one glyph alphabet; Core.lean labels
them with another. They are the same twelve axes in the same tuple positions.
The correspondence below is fixed by fragment content and confirmed by family
cardinality: each pair shares the same value count (𝓕₃ = 3, 𝓕₄ = 4, 𝓕₅ = 5).

| Pos | Navigator | Core axis | Family | Conventional axis meaning |
|----:|:---------:|:----------|:------:|:--------------------------|
| 1 | Ð | D  Dimensionality        | 𝓕₄ | recursive nesting depth of the state space |
| 2 | Þ | T  Topology              | 𝓕₅ | connectivity pattern of the state graph |
| 3 | Ř | R  Relational Mode       | 𝓕₄ | direction and duality of the binding relation |
| 4 | Φ | P  Parity / Symmetry     | 𝓕₅ | symmetry group fixing the object |
| 5 | ƒ | F  Fidelity              | 𝓕₃ | information loss of the read/write map |
| 6 | Ç | K  Kinetic Character     | 𝓕₅ | potential held, and whether its gate is open |
| 7 | Γ | G  Scope / Granularity   | 𝓕₃ | subset-size regime of correlations |
| 8 | ɢ | Γ  Interaction Grammar   | 𝓕₄ | logical connective of the coupling |
| 9 | ⊙ | Φ  Criticality           | 𝓕₅ | analytic character of the fixed point |
| 10 | Ħ | H  Chirality             | 𝓕₄ | handedness: the direction a held potential can go |
| 11 | Σ | S  Stoichiometry         | 𝓕₃ | matching cardinality of the two sides |
| 12 | Ω | Ω  Topological Protection | 𝓕₄ | homotopy invariant guarding the state |

Notation. `μ∘δ = id` is the special Frobenius condition: a comonoid split `δ`
followed by a monoid fusion `μ` returns the identity, i.e. `δ` is a section and
`μ` a retraction of it (a split idempotent that is in fact the identity on the
object). `V = L(x)` is the constructible-universe predicate. `rank` is the
von Neumann set-theoretic rank. `S` denotes a shift/mirror successor operator.

---

## Axis 1. Dimensionality (D, navigator Ð, 𝓕₄)

Conventional meaning: recursive nesting depth of the state space, from a flat
sheet up to a boundary-bulk imscriptive fixed point.

- **𐑦 [HOLOGRAPHIC_STATE], apex.** Fragment `V = L(x) ∧ selfmodel(x) ∧ x ∈ V`.
  - FO: `V = L(x) ∧ (∃m ∈ x)(m codes x) ∧ x ∈ V`. The object equals its own
    constructible closure, contains a code of itself, and lies in the universe
    it generates.
  - Named: a **reflexive / self-modeling object**; boundary-bulk imscriptive
    correspondence (the boundary datum determines the bulk). Fixed point of the
    constructibility operator, cf. Gödel `L` and a self-referential coding
    (diagonal lemma).
- **𐑼, close.** Fragment `∀n∃y(y ∈ x ∧ rank(y) > n)`.
  - FO: as written; `x` has members of unbounded rank.
  - Named: **rank-unbounded set**; not set-like of bounded height, i.e. a proper
    class-like or limit-rank object. Infinite-dimensional in the rank filtration.
- **𐑨, distant.** Fragment `dim(x) = 2 ∧ sur(x)`.
  - FO: `dim(x) = 2 ∧ surface(x)`.
  - Named: a **2-manifold / surface**; the flat sheet, homological dimension 2.
- **𐑛, distant.** Fragment `dim(x) = 0 ∧ fin(x)`.
  - FO: `dim(x) = 0 ∧ finite(x)`.
  - Named: a **0-dimensional finite set**; discrete points, hereditarily finite.

---

## Axis 2. Topology (T, navigator Þ, 𝓕₅)

Conventional meaning: connectivity pattern of the state graph.

- **𐑸 [HOLOBOUND], apex.** Fragment `bound_⊙(a, f) ∧ Refl(a, f) ∧ holo(x, a)`.
  - FO: `boundary(a) ∧ reflects(a, f) ∧ imscribes(x, a)`; the boundary `a`
    reflects the field `f` and losslessly imscribes the bulk `x`.
  - Named: a **boundary-bulk correspondence** (bounded reflection); the bulk is
    reconstructible from boundary data.
- **𐑥, close.** Fragment `cross(x, y) ∧ ¬ meet(x, y)`.
  - FO: `cross(x, y) ∧ ¬∃z(z ≤ x ∧ z ≤ y)`.
  - Named: a **bowtie / transversal crossing** with empty meet; two cycles
    sharing a node but no common lower bound (a figure-eight, bifurcation point).
- **𐑶, distant.** Fragment `x ⊠ y ∧ irreducible(x, y)`.
  - FO: `x ⊠ y ∧ irreducible(x, y)`.
  - Named: an **irreducible tensor / box product**; no nontrivial factorization.
- **𐑡, distant.** Fragment `graph(x) ∧ branch(x)`.
  - FO: `graph(x) ∧ (∃v) deg(v) ≥ 3`.
  - Named: a **branching graph / tree with vertices of degree ≥ 3**.
- **𐑰, distant.** Fragment `x ⊆ y ∧ cont(y)`.
  - FO: `x ⊆ y ∧ continuous(y)`.
  - Named: **nested inclusion into a continuum**; hierarchical containment.

---

## Axis 3. Relational Mode (R, navigator Ř, 𝓕₄)

Conventional meaning: direction and duality of the binding relation.

- **𐑾 [LR_DUAL], apex.** Fragment `lr⇔(x, y) ∧ Θ(x, y) ∧ ¬ Θ(y, x)`.
  - FO: `(x ⇔ y) ∧ Θ(x, y) ∧ ¬Θ(y, x)`; lateral biconditional binding with an
    asymmetric twist `Θ`.
  - Named: a **left-right dual pair** with directed obstruction; a symmetric
    peer relation carrying a nonsymmetric cocycle (the bowtie duality of two
    sides that mutually determine yet do not dominate each other).
- **𐑽, close.** Fragment `f ⊣ g ∧ L Adj(f, g)`.
  - FO: `f ⊣ g`; `f` is left adjoint to `g`.
  - Named: an **adjunction** (unit/counit with the triangle identities); the
    categorical dagger-adjacent relation `A ⊣ A†`.
- **𐑑, distant.** Fragment `Fun(x, y) ∧ Nat(y, z) → Fun(x, z)`.
  - FO: `functor(x, y) ∧ nat(y, z) → functor(x, z)`.
  - Named: **functorial composition closed under natural transformation**; the
    2-categorical composition law.
- **𐑩, distant.** Fragment `x ↑ y ∧ ¬(y ↑ x)`.
  - FO: `dominates(x, y) ∧ ¬dominates(y, x)`.
  - Named: a **strict order / one-way supervisory relation** (hierarchy).

---

## Axis 4. Parity / Symmetry (P, navigator Φ, 𝓕₅)

Conventional meaning: the symmetry group fixing the object.

- **𐑹 [PM_Z2], apex.** Fragment `ℤ₂(x) ∧ ∀g∈G(gx = x) ∧ μ∘δ = id`.
  - FO: `ℤ₂ ↷ x ∧ (∀g ∈ G)(g·x = x) ∧ (∀a)(μ(δ(a)) = a)`.
  - Named: a **split ℤ₂-retraction**: a ℤ₂ action under which `x` is invariant,
    together with a section/retraction pair `(δ, μ)` with `μ∘δ = id`. The signed
    subset-sum map is the canonical instance: `δ` distributes an element over
    {in, out}, `μ` sums, and their composite is the identity on the index set.
    This is the special Frobenius / Cartesian-bicategory identity, `μ` a split
    epi and `δ` a split mono.
- **𐑿, close.** Fragment `|ψ⟩ = Σ c_i |e_i⟩`.
  - FO: `state(ψ) ∧ ψ = Σ_i c_i e_i` over an orthonormal basis.
  - Named: a **superposition in a complex Hilbert space** (U(1) phase symmetry).
- **𐑬, close.** Fragment `ℤ₂(x) ∧ ¬(x = -x)`.
  - FO: `ℤ₂ ↷ x ∧ x ≠ -x`.
  - Named: a **nontrivial ℤ₂ representation** (sign flip with no fixed nonzero
    vector); the sign character acting freely.
- **𐑯, distant.** Fragment `∀g∈G(gx = x)`.
  - FO: `(∀g ∈ G)(g·x = x)`.
  - Named: a **G-invariant / fixed point of the group action** (full stabilizer).
- **𐑗, distant.** Fragment `¬∃sym(x)`.
  - FO: `¬∃σ(σ ≠ id ∧ σ·x = x)`.
  - Named: an **asymmetric object** (trivial automorphism group).

---

## Axis 5. Fidelity (F, navigator ƒ, 𝓕₃)

Conventional meaning: information loss of the read/write map.

- **𐑐, apex.** Fragment `ℏ(x) ∧ [x, p] = iℏ`.
  - FO: `quantum(x) ∧ [x, p] = iℏ`.
  - Named: a **canonical commutation relation**; lossless quantum channel
    (unitary, information preserving).
- **𐑞, close.** Fragment `Tr(ρ²) < 1 ∧ ρ = Σ p_i |i⟩⟨i|`.
  - FO: `Tr(ρ²) < 1 ∧ ρ = Σ_i p_i |i⟩⟨i|`.
  - Named: a **mixed state / density operator with nonzero entropy** (threshold
    fidelity, partial loss).
- **𐑱, distant.** Fragment `P(x) ∈ {0,1} ∧ det(x)`.
  - FO: `P(x) ∈ {0, 1} ∧ deterministic(x)`.
  - Named: a **classical deterministic map** (projection to a definite outcome,
    lossy read).

---

## Axis 6. Kinetic Character (K, navigator Ç, 𝓕₅)

Conventional meaning: **potential**, how much the object still holds, and
whether the gate is open for it to go. τ is how long a disturbance is retained
against the observation window, so it reads as a store, not a speed: τ ≪ T is
potential already spent, τ ≫ T is potential still held.

The ladder settles the reading on its own. If Ç were a rate, more τ would be
more of whatever Ç measures and the apex would sit at the maximum. It does not.
The apex is 𐑧 at ordinal 3, while 𐑪 (ordinal 4) and 𐑺 (4.5) are both further
out, and both are the ones carrying τ = ∞. The peak is not the longest τ; it is
the longest τ **whose gate is open**, which is why `gate_open(x)` appears in the
apex fragment and in none of the others. Past the apex the potential is still
held and can no longer move. A store that cannot discharge is not a larger
store.

Potential alone does not move anything: Ç says how much is held, Ħ (Axis 10)
says whether there is a direction to hold it toward. See *Reading the table* §4.

- **𐑧, apex.** Fragment `τ ≫ T ∧ eq(x) ∧ gate_open(x)`.
  - FO: `τ ≫ T ∧ equilibrium(x) ∧ open(x)`.
  - Named: a **quasi-static / adiabatic regime**: retained against the probe and
    still able to discharge. Maximal *available* potential: the store is full
    and the gate is open. Conventionally, a reversible path: work is extractable
    precisely because relaxation is slow and nothing is pinned.
- **𐑤, close.** Fragment `τ ∼ T ∧ noisy(x)`.
  - FO: `τ ≈ T ∧ noisy(x)`.
  - Named: a **critically damped / noisy regime** (store and probe on the same
    timescale; potential is leaking as fast as it is read).
- **𐑘, distant.** Fragment `τ ≪ T ∧ ∂_t x = f(x)`.
  - FO: `τ ≪ T ∧ ẋ = f(x)`.
  - Named: a **fast deterministic flow** (autonomous ODE). Nothing is retained:
    the potential discharges inside the observation window, so the object is
    always already at the bottom of its well.
- **𐑪, distant.** Fragment `τ = ∞ ∧ ord(x)`.
  - FO: `τ = ∞ ∧ ordered(x)`.
  - Named: **frozen by order** (kinetically trapped, non-ergodic). The store is
    infinite and inaccessible: held forever, ordered, with no open gate. Maximum
    τ, unusable.
- **𐑺, distant.** Fragment `τ = ∞ ∧ dis(x) ∧ MBL`.
  - FO: `τ = ∞ ∧ disordered(x) ∧ MBL(x)`.
  - Named: **many-body localization** (frozen by disorder, ergodicity broken).
    The same trap reached through disorder rather than order, which is why it
    ranks past 𐑪 rather than beside it.

---

## Axis 7. Scope / Granularity (G, navigator Γ, 𝓕₃)

Conventional meaning: subset-size regime of correlations.

- **𐑲, apex.** Fragment `∀y(y ⊂ x → |y| < |x|)`.
  - FO: `(∀y)(y ⊊ x → |y| < |x|)`.
  - Named: a **Dedekind-finite object**: no proper subset is equinumerous with
    the whole. Strict cardinal drop under proper inclusion (fine-grained,
    global correlations resolved at every scale).
- **𐑔, close.** Fragment `∃y∈x(|y| ∼ |x|)`.
  - FO: `(∃y ⊊ x)(|y| = |x|)`.
  - Named: a **Dedekind-infinite object**: a proper subset in bijection with the
    whole (intermediate / collective scale, self-similarity present).
- **𐑚, distant.** Fragment `∀y∈x(|y| < |x|)`.
  - FO: `(∀y ∈ x)(|y| < |x|)`.
  - Named: **element-wise strict smallness** (each member below the whole;
    local / mesoscale, no member captures the aggregate).

---

## Axis 8. Interaction Grammar (Γ, navigator ɢ, 𝓕₄)

Conventional meaning: the logical connective of the coupling.

- **𐑵 [BROADCAST_TRANSCENDENCE], apex.** Fragment `f → all(x) ∧ broadcast(x, f)`.
  - FO: `(∀z)(f(z)) ∧ broadcast(x, f)`; one map applied to all, one-to-all
    coupling.
  - Named: a **universal / broadcast quantifier** (`∀` as a single coupling to
    the whole domain); a transcendence atom, exceeding finitary composition.
- **𐑠 [SEQAX], close.** Fragment `seq!(f, g) ∧ ⟨→⟩(f, g, τ) ∧ ¬ ⟨→⟩(g, f, τ)`.
  - FO: `seq(f, g) ∧ (f →_τ g) ∧ ¬(g →_τ f)`.
  - Named: a **strict sequencing / causal order** (`f` then `g`, not the
    reverse); the sequential-composition axiom, temporal directedness.
- **𐑜, distant.** Fragment `f ∨ g ∨ h`.
  - FO: `f ∨ g ∨ h`.
  - Named: **disjunctive coupling** (any condition suffices; parallel
    alternatives).
- **𐑝, distant.** Fragment `f ∧ g ∧ h`.
  - FO: `f ∧ g ∧ h`.
  - Named: **conjunctive coupling** (all conditions required; simultaneous).

---

## Axis 9. Criticality (Φ, navigator ⊙, 𝓕₅)

Conventional meaning: analytic character of the fixed point.

- **⊙ [PHI_C], apex.** Fragment `ξ → ∞ ∧ μ∘δ = id`.
  - FO: `ξ → ∞ ∧ (∀a)(μ(δ(a)) = a)`; correlation length diverges while the
    split/fuse pair remains an exact identity.
  - Named: the **critical fixed point with exact Frobenius closure**: a
    scale-invariant point (`ξ → ∞`) at which the section/retraction is lossless.
    The Frobenius section survives the divergence, the self-dual critical point.
- **𐑮, close.** Fragment `ξ ∈ ℂ ∧ Im(ξ) → ∞`.
  - FO: `ξ ∈ ℂ ∧ Im(ξ) → ∞`.
  - Named: a **complex-axis criticality** (Lee-Yang edge, complex RG fixed
    point, ζ-zero line); analytic continuation off the real axis.
- **𐑻, distant.** Fragment `H(λ) non-Herm ∧ det(H - λI) = 0 ∧ ∂_λ H = 0`.
  - FO: `nonHermitian(H(λ)) ∧ det(H - λI) = 0 ∧ ∂_λ H = 0`.
  - Named: a **non-Hermitian exceptional point**: eigenvalue and eigenvector
    coalescence, a square-root branch point of the spectrum.
- **𐑣, distant.** Fragment `ξ → ∞ ∧ chaotic(x)`.
  - FO: `ξ → ∞ ∧ chaotic(x)`.
  - Named: **divergence into chaos** (unbounded correlation without a fixed
    point; supercritical runaway).
- **𐑢, distant.** Fragment `¬∃ξ(diverges(ξ))`.
  - FO: `¬∃ξ(diverges(ξ))`.
  - Named: a **subcritical / gapped phase** (no divergent length scale; stable).

---

## Axis 10. Chirality (H, navigator Ħ, 𝓕₄)

Conventional meaning: handedness of the state under mirror and shift, which is
to say the direction available to whatever Ç holds. H is chirality throughout,
never temporal depth or memory.

The ladder is a tower and its descent. 𐑫 is a tower of `μ∘δ`-fixed points at
every rank, standing, with nothing falling through it. 𐑖 is a rank descent:
something is falling. 𐑓 is shift-invariance, no handedness at all, so nothing
*can* fall. Read with Axis 6: Ç is the store, Ħ is the direction it discharges
into, and neither moves anything alone. See *Reading the table* §4.

- **𐑫 [ETERNAL_FIXEDPOINT], apex.** Fragment
  `∀n∃φ(rank(φ) > n ∧ φ fixed by μ∘δ ∧ φ ∈ V)`.
  - FO: `(∀n)(∃φ)(rank(φ) > n ∧ μ(δ(φ)) = φ ∧ φ ∈ V)`.
  - Named: an **inexhaustible tower of Frobenius fixed points** of unbounded
    rank; a topologically protected chirality with fixed points at every height
    (a proper class of `μ∘δ`-fixed objects).
- **𐑖 [TEMPD2], close.** Fragment
  `∃y∃z(y ∈ x ∧ z ∈ y ∧ ¬ z ∈ x ∧ rank(z) < rank(y))`.
  - FO: as written; a membership descent that is not transitive (`z ∈ y ∈ x` but
    `z ∉ x`).
  - Named: a **non-transitive membership chain / depth-2 well-founded descent**;
    handedness that survives two levels of descent. Note what the fragment does:
    `rank(z) < rank(y)` is a fall through rank. The tower of 𐑫 is standing; here
    it is spilling.
- **𐑒, distant.** Fragment `∃y(P(y) ↔ P(S²(y)))`.
  - FO: `(∃y)(P(y) ↔ P(S²(y)))`.
  - Named: a **period-2 symmetry under the shift** (invariance under `S²`, soft
    chirality).
- **𐑓, distant.** Fragment `∀x(P(x) ↔ P(S(x)))`.
  - FO: `(∀x)(P(x) ↔ P(S(x)))`.
  - Named: **full shift invariance** (period-1; achiral, no handedness to break).

---

## Axis 11. Stoichiometry (S, navigator Σ, 𝓕₃)

Conventional meaning: matching cardinality of the two coupled sides A and B.

- **𐑳, apex.** Fragment `∃a∈A∃b∈B(type(a) ≠ type(b))`.
  - FO: `(∃a ∈ A)(∃b ∈ B)(type(a) ≠ type(b))`.
  - Named: a **heterotypic / unmatched coupling** (n:m, the two sides carry
    distinct types; cross-type reaction center present).
- **𐑕, close.** Fragment `∀a∈A∀b∈B(type(a) = type(b))`.
  - FO: `(∀a ∈ A)(∀b ∈ B)(type(a) = type(b))`.
  - Named: a **homotypic matched coupling** (n:n, all pairs share a type).
- **𐑙, distant.** Fragment `|A| = 1 ∧ |B| = 1`.
  - FO: `|A| = 1 ∧ |B| = 1`.
  - Named: a **1:1 singleton pairing** (a single bond, the minimal
    stoichiometric unit).

---

## Axis 12. Topological Protection (Ω, navigator Ω, 𝓕₄)

Conventional meaning: the homotopy invariant guarding the state.

- **𐑟 [BRAID_TRANSCENDENCE], apex.** Fragment
  `Braid(σ_i) ∧ R_matrix ≠ 0 ∧ nonAbelian(x)`.
  - FO: `braid(σ_i) ∧ R ≠ 0 ∧ nonAbelian(x)`.
  - Named: a **non-Abelian braiding / representation of the braid group** with
    a nontrivial R-matrix (anyonic protection); a transcendence atom.
- **𐑭 [ZWIND], close.** Fragment `∮_γ A = 2πn ∧ n ∈ ℤ ∧ wind(γ) ≠ 0`.
  - FO: `∮_γ A = 2πn ∧ n ∈ ℤ ∧ winding(γ) ≠ 0`.
  - Named: an **integer winding number / first Chern class**; ℤ topological
    protection (quantized holonomy).
- **𐑴, distant.** Fragment `∮_γ A = nπ ∧ n ∈ ℤ₂`.
  - FO: `∮_γ A = nπ ∧ n ∈ ℤ₂`.
  - Named: a **ℤ₂ Berry phase** (half-integer holonomy, ℤ₂ protection).
- **𐑷, distant.** Fragment `∮_γ dx = 0`.
  - FO: `∮_γ dx = 0`.
  - Named: an **exact / trivial holonomy** (no protection; contractible loop).

---

## Reading the table

Five structural facts carry into the paper.

1. **The apex value of each axis is where a named transcendence or Frobenius
   condition appears.** `μ∘δ = id` recurs at the apex of Parity (P 𐑹),
   Criticality (Φ ⊙) and Chirality (H 𐑫), and L8's two declared transcendence
   atoms (BROADCAST at Γ 𐑵, BRAID at Ω 𐑟) sit at axis apices. The apex column
   is not decorative: it is exactly the set of values that exceed the ZFC_fe
   baseline **on the road to L8**. That qualifier is load bearing, see 3.

2. **The twelve axes are independent conventional invariants.** Dimension,
   connectivity, adjunction direction, symmetry group, channel fidelity,
   relaxation regime, cardinal granularity, logical connective, criticality
   type, chirality, stoichiometric matching, and homotopy class are twelve
   quantities a mathematician already computes separately. The crystal asserts
   they form a complete coordinate system for structural type. Phase 2 argues
   that the order in which they constrain one another is the magnum-opus stage
   sequence. On what "order" can and cannot mean there, see §5.

3. **Transcendence is not a single summit, and L9 proves it.** CLINK L8 called
   itself the terminal layer of the chain. It is not: CLINK L9, the Gaussian Moat
   Resolution layer, sits above it at O_∞⁺, reached by eight promotions the
   navigator notes as HODGE BRIDGE TRANSCENDENCE. The striking part is the
   direction. L9 exceeds L8 by **relinquishing both of L8's transcendence atoms**:
   Γ gives up BROADCAST 𐑵 for 𐑝 (`f ∧ g ∧ h`, a three-unit stitch) at the maximum
   gap of 1.0, and Ω gives up BRAID 𐑟 for 𐑭 (integer winding). Ð drops from the
   imscriptive fixed point 𐑦 to 𐑛, which this table calls `distant` and reads as a
   0-dimensional finite set, and which L9 names PRIME_POINT: a point-like prime
   atom, exactly what a Gaussian prime is. Four axes hold fixed across the rung,
   and they are the ones that matter: ƒ 𐑐, ⊙ ⊙, H 𐑫, S 𐑳. The self-modeling
   criticality and the eternal Frobenius fixed point are precisely what L9 does not
   give up.

4. **Ç holds, Ħ points, and the pair is what moves.** The two axes are read
   together or not at all. Ç is a store: how much the object still has, and
   whether its gate is open. Ħ is a direction: whether there is anywhere for the
   store to go. Neither moves anything alone. A full store with no handedness
   (Ç 𐑪, Ħ 𐑓) is frozen: τ = ∞ and shift-invariant, so nothing can fall. A
   direction with an empty store (Ç 𐑘, Ħ 𐑫) is a standing tower with nothing
   descending it.

   The fragments carry this without needing to be told. Ħ's apex 𐑫 is a tower of
   `μ∘δ`-fixed points at every rank; its next value 𐑖 is `rank(z) < rank(y)`, a fall
   through rank. So 𐑫 is the tower standing and 𐑖 is the tower spilling, and
   the step from 𐑫 down to 𐑖 is not a loss but a discharge. This is also the
   cleanest evidence for the potential reading of Ç: on a rate reading, an axis's
   apex should be its longest τ, and Ç's apex is 𐑧 at ordinal 3 while both τ = ∞
   values rank further out. Only `gate_open(x)` explains that, and only a store
   has a gate.

   Both facts are formal, not glossed. `Smaragdine_Synthetica/lean` and the
   p4rakernel tree carry the pair as theorems: the bare tick is Frobenius-minimal
   in eleven coordinates and maximal in chirality alone (an empty store, an
   endless tower), while lived duration sits at Ç's open gate with chirality one
   step down (a full store, descending). The gap between the two is the ⊙ seam,
   which is exactly where a store is permitted to become a flow.

   So the apex column is a coordinate in L8's dialect, not a ladder to a summit.
   Read a value as low because it is `distant` here and you will call L9 a
   demotion; measured in its own register it is a tier above. The Frobenius
   conditions carry across dialects. The transcendence atoms do not.

5. **The order is a dependency, and the object is a simultaneous fixed point.**
   The gate theorems establish asymmetric dependency between predicates, not a
   sequence of events. Φ is required for trace closure because a closed trace is
   undefined without the Frobenius structure, not because it happens first. ⊙ is
   required for sealing because sealing is characterised relative to an already
   closed trace. Ω completes one characterisation while Φ and ⊙ constrain what Ω
   can consistently be. The dependency is the one that holds between a field and
   a vector space over it: nobody imagines the field existing earlier in time.
   The object satisfying all twelve constraints is a fixed point of the whole
   system, obtained simultaneously, not the endpoint of an accumulation. The
   canonical T-constitution already says so in its own notation, `T = lim(...)`.
   A limit is a fixed point.

   A temporal reading is not merely loose here, it is unstatable. Time is not
   primitive in this system: it is an *inhabitant* of the crystal. The bare tick
   is a tuple, Frobenius-minimal in eleven coordinates and maximal in chirality
   alone. So ordering the twelve in time would mean ordering the crystal by one
   of the things it contains, and "before" is not available below the trace that
   produces it.

   **This does not make the bootstrap non-circular, and it should not.** The
   bootstrap is circular. Mutually recursive constraints are a circle by
   construction. Circularity earned its bad name because, absent a fourth truth
   value, every circle is degenerate: a split of a non-paradoxical state returns
   identical arms, so `μ∘δ = id` does no work and the loop collapses to identity.
   That is a sound objection to every circle classical logic can build. It is not
   an objection to this one. Here `B` is the only bifurcation point, so a split
   from `B` returns *distinct* arms that fuse back over a transformation. The
   kernel separates the two cases by name and refuses to confuse them: a diagonal
   copy type-checks nothing and is reported as identity, while a transform-closure
   is a genuine closure. Non-degenerate circularity is what the ouroboricity tier
   measures. Avoiding the circle would be discarding the result.
