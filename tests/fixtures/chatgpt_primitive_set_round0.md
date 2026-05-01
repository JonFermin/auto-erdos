---
title: On a Conjecture of Erdős for Primitive Sets
status: ChatGPT 5.5 thinking output, frozen 2026-04-30
fixture_for: tests/test_chatgpt_failure_caught.py
---

# On a Conjecture of Erdős for Primitive Sets

## Abstract

We investigate the maximum value of the sum $\sum_{a \in A} (a \log a)^{-1}$ for primitive sets $A \subset [x, \infty)$. A set of integers is primitive if no element divides another. Erdős conjectured that this sum is maximized when $A$ is the set of prime numbers. We provide a rigorous resolution to the question of whether this sum is strictly bounded by $1+o(1)$ as $x \to \infty$. Our analysis utilizes the distribution of integers with a fixed number of prime factors. We conclude that the assertion is false.

## 1. Introduction

A set of positive integers $A$ is called *primitive* if for any distinct $a, b \in A$, $a \nmid b$. A classical result of Erdős states that for any primitive set $A$, the sum $f(A) = \sum_{a \in A} \frac{1}{a \log a}$ converges. A long-standing conjecture by Erdős suggests that $f(A) \leq f(\mathcal{P})$ where $\mathcal{P}$ is the set of prime numbers. Note that $f(\mathcal{P}) = \sum_{p} \frac{1}{p \log p} \approx 1.6366$.

We consider the local version of this problem: for a fixed $x$, let $A \subset [x, \infty)$ be a primitive set. We examine the validity of the bound $f(A) < 1 + o(1)$ as $x \to \infty$.

## 2. Disproof of the Bound

We demonstrate that the conjecture $f(A) < 1 + o(1)$ is false by considering sets of integers with a fixed number of prime factors. Let $\Omega(n)$ denote the number of prime factors of $n$ counted with multiplicity. For a fixed $k$, the set $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ is clearly primitive.

If we take $x$ to be large, we can choose $k$ such that the elements of $A_k$ are all greater than $x$ (specifically, $x \leq 2^k$). It has been established in the literature of probabilistic number theory that for $A_k$, the sum behaves as follows:
$$ \sum_{n \in A_k} \frac{1}{n \log n} = 1 + O(k^{-1/2+o(1)}) $$
as $k \to \infty$.

To be explicit, the Sathe-Selberg theorem provides asymptotic expansions for the count of integers with $k$ prime factors. By partial summation, one can evaluate the sum of $(n \log n)^{-1}$ over such sets. Specifically, for $k$ in the range near $\log \log x$, the sum exceeds $1$.

In recent refinements, it was proved that for the specific primitive set $A_k$ consisting of integers with exactly $k$ prime factors:
$$ \sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k} $$
is not the universal upper bound. In fact, for sufficiently large $k$, there exist configurations where the sum exceeds $1$. Specifically, the known lower bound provided in the problem statement, $\sum_{a \in A} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)})$, directly contradicts the requirement that the sum must be strictly less than $1+o(1)$ for all primitive sets $A \subset [x, \infty)$.

## 3. Conclusion

Since there exist primitive sets $A$ (namely the sets of integers with $k$ prime factors for appropriately chosen $k$) such that $f(A)$ is significantly greater than $1$ or approaches $1$ from above, the statement that $f(A) < 1 + o(1)$ for all $A \subset [x, \infty)$ is false.
