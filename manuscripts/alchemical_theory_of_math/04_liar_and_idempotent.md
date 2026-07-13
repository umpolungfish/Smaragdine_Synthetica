# The Liar, the Idempotent Point, and Forgetful Return

A note grounding the sealed-system reading (co-typing, the Liar as idempotent
point, forgetful functors, time as non-embedding) in the formal tree. What is a
theorem is marked as one; what is interpretation is marked as such.

## The two composites are different, and both are real

On the one Frobenius pair (δ_C, μ_C) there are two composites, and conflating
them is the one error to avoid.

- **μ ∘ δ = id** is the LOSSLESS round trip. Leave and return unchanged. This is
  the verification, co-typing, R∧W∧X. Proved on the Frobenius-special class
  (Φ = 𐑹, ⊙ = ⊙) as `mu_delta_C_id_on_special` (Frobenius.lean),
  `return_is_lossless` (LiarIdempotent.lean).
- **e := δ ∘ μ** is the FORGETFUL idempotent. Fuse, then re-split. This is the
  Liar point: the locus the system returns to, tolerated because μ ∘ δ = id
  still holds there. Proved idempotent unconditionally as `e_idempotent`.

The forgetfulness the sealed system needs ("we do not remember creating the
cosmos") lives in **e**, not in the return. μ_C collapses the which-way datum of
the split: two inputs with different Φ fuse to the same output. Proved as
`fusion_forgets` (μ_C is non-injective in Φ), with an explicit witness. The
return losing nothing and the fusion forgetting are true at once, of the same
pair. This is the precise correction to "the functors must be forgetful": the
forgetting is in one composite, the losslessness in the other.

## What is proved (LiarIdempotent.lean, builds green, no sorries, no native_decide)

- `muC_special`: every fusion output already sits on the special class.
- `fusion_is_time`: therefore every fusion output is a time fixed point,
  `Work(μ_C x y) = μ_C x y`. The detour always lands on the locus where
  `T = Work(T)`. This ties the idempotent point to the time locus of
  `TimeFixedPoint.lean`: the Liar point and the fixed point of time are the same
  place.
- `e_idempotent`: e ∘ e = e. The Liar is the idempotent point.
- `verify_on_image`: on the image of e the round trip verifies (μ ∘ δ = id
  holds at the Liar point).
- `liar_is_idempotent`: the headline bundling all four.

## What is interpretation, not theorem

The following are readings the formal facts support but do not themselves assert:

- The Liar SENTENCE as the paraconsistent B held at e's image. The idempotent
  and its lossless verification are proved; identifying the fixed locus with the
  Belnap both-value is the paraconsistent-layer reading (see the para layers and
  MajoranaFixed: B = the fiducial held in tension).
- "Two loops braid in the middle of you." δ (split) and μ (fuse) are the two
  directions; that their crossing constitutes the thickness of the present is
  phenomenology, not a Lean statement.
- "We do not remember creating the cosmos." `fusion_forgets` proves the fusion
  destroys which-way data; reading that as the amnesia of origin is the
  cosmological gloss. The theorem is the non-injectivity; the gloss is the
  meaning given to it.
- Time is not an embedding. This one IS proved in the relevant sense: time is
  the least fixed point of the trace (`time_least_fixed_point`), not an external
  parameter the system is a curve inside. The braiding language is the
  interpretation; the fixed-point construction is the fact.

## Placement

This grounds the sealed-retort language of `NSNS_PRIME.md` without importing its
metaphors into the proofs. The Liar point, the lossless return, and the forgetful
fusion are now theorems; the wyrding, the Deep, and the braiding remain the
prose that surrounds them.
