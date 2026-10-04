# Session handoff (session s_1004-080734-fd2b)

**Stop reason**: logical milestone — one exploit keep (R110) closing both
queued steps of Q0930-083610-2 (capacity lemma + numeric squeeze test).

**Consecutive exploit sessions on current program**: 1
(R110 claimed Q0930-083610-2 and did exploit-shaped work on the spectral
program. The NEXT session may exploit once more; at 2 the session after
that MUST claim a kind: explore qid or open with ideation.)

**What happened (R110, keep_progress)**:

- New lemma `c16_capacity_girth9` (proved, 4 CHECKs, worst 17 s):
  (K1/K2) every composite type has girth gamma(T) in {5,6,7} and
  N_T(G) <= kappa(T) c_gamma(T)(G) for ANY cubic host (embedding
  exploration: dihedral anchor 2*gamma, then cubic-degree factors;
  kappa in [10,1280]; 124 host-type validation pairs, 0 violations).
  (K3) composite mass <= K5 c5 + K6 c6 + K7 c7,
  (K5,K6,K7) = (367360, 104448, 53760) — pure spectral functional via
  the moment dictionary.
  (K4) THE GIRTH-9 C16 THEOREM (unconditional): every connected cubic
  graph with girth >= 9 and n <= 130 contains a 16-cycle. Sharp window
  at this precision (S5 bound flips sign at n=132). With F3
  (Markström n<=29): any cubic Erdős–Gyárfás counterexample on
  n <= 130 has girth in {3,5,6,7}.
- **Squeeze verdict** (executed BEFORE infeasibility effort, per the
  qid's own protocol): NEGATIVE for girth-5 — capacity cap overshoots
  actual mass 83.9x on the n=30 carrier (3520256 vs 41952); even
  K5*1 = 367360 dwarfs the S5 requirement (~5.4e4). The squeeze
  closes exactly the girth->=9 stratum; (K4) is its honest extent.

**qid state**: Q0930-083610-2 RELEASED with continuation: (1)
host-aware capacity (per-Z dart-budget accounting — a C5 has only 5
off-cycle darts; could cut K5 by orders of magnitude), (2) k=32
moment stacking (needs a k=32 support census — offline-sized), (3)
n=28 girth-5 C8-free SAT population floor (still queued).
Q0930-083610-3 (rigidity SAT: MK/Pappus/Desargues, offline-grade) and
Q81/Q85 unchanged.

**GRADING NOTE (confirmed again this session)**: the falsify critic
needs ~511 s on opus (prompt 739 KB) — ABOVE the hard 240 s cap. The
documented fix protocol works: render prompts via
proof_prepare._render_critic_prompt, call
library._critic_subprocess.call_critics_parallel(items,
timeout_s=1200) to warm the shared cache, then run proof_prepare
(cache-hits all 7). Do this BEFORE the first verifier run of every
session; total prewarm ~9 min.

**Files modified this session**:
- proof_strategy.md (Section 147)
- proof_lemmas/lemma_c16_capacity_girth9__1004-080734-fd2b.md (new,
  status proved)
- records/proof_erdos_gyarfas_f52f8b7c3333_6040fdf.json (R110)
- proof_open_questions.jsonl, proof_journal.jsonl, ledger

**Suggested next moves**:
1. (exploit OK, one more) Host-aware capacity: formalize the per-Z
   dart-budget — for a fixed 5-cycle Z in a cubic girth->=5 C8-free
   host, every composite copy through Z consumes Z's 5 off-cycle
   darts; joint accounting across the 31 gamma=5 types should
   replace K5 = 367360 by something near the per-dart walk mass.
2. Rigidity SAT offline-grade (MK first, symmetry-broken or
   binary-adder encoding) — unchanged from s_1003's handoff.
3. If exploring: mu<=4 multigraph-skeleton rigidity sweep (8^9
   patterns, numpy-chunked, one round) to hunt a smaller rigid core.
