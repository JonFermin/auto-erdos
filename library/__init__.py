"""auto-erdos constructions library — read-only baselines for agents.

Import from ``library.sidon`` or ``library.capset`` directly. Each
construction is literature-grade (Singer, Erdős–Turán, product-lift) and
is part of the fixed environment alongside ``prepare.py`` — agents may
call these but must not modify them.

Typical usage in ``strategy.py``::

    from library import sidon, capset
    s = sidon.singer_for_n(spec["N"])           # start from Singer LB
    # ... try to extend s with greedy/SA/swap-moves ...

    cap = capset.recursive_product(spec["n"])    # 4^(n/2) * 2^(n%2) cap
    # ... try to augment cap ...

The keep rule still requires score > running_best, so returning a library
set verbatim discards (it equals the literature baseline by construction).
"""
from library import capset, sidon  # noqa: F401  (re-export)
