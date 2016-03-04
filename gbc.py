"""Combinatorial generation module.

This module provides a generator function L() that generates all
combinatorial objects of a binary $n$-tuple in Gray binary code order.
"""
__author__  = 'Jason Mader'
__credits__ = 'Don Knuth'

__all__ = ['L']

# Algorithm 7.2.1.1L from The Art of Computer Programming, Volume 4
#
# L ``visits all binary $n$-tuples $(a_{n-1},\ldots,a_0)$ in the order
# of the Gray binary code.'' [Knuth]
#
def L(s1, s0):
    """Loopless Gray binary generation

    Two arguments that must be equal length sequences determine what
    this generator will yield for 1 and 0 at each element $a_j$."""

    # A temporary variable is used to cache the pattern for each
    # visit. It is set after complementing $a_j$.
    pattern = list(s0)

    n = len(s1)

    # L1. [Initialize.]
    a = ([0] * n)
    f = [i for i in range(0, n+1)]

    while True:
        # L2. [Visit.]
        yield pattern

        # L3. [Choose j.]
        j = f[0]
        f[0] = 0

        if j == n: return  # Terminate

        f[j] = f[j+1]
        f[j+1] = j+1

        # L4. [Complement the coordinate j.]
        a[j] = 1 - a[j]

        if a[j]: pattern[j] = s1[j]  # Updating by conditional is faster
        else: pattern[j] = s0[j]     # than using s[ a[j] ][j].
