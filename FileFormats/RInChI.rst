.. _RInChI:

RInChI (rinchi)
===============

**The Reaction InChI**

The Reaction InChI (or RInChI) is intended to be a unique
string that describes a reaction. This may be useful for
indexing and searching reaction databases. As with the InChI
it is recommended that you always keep the original reaction
information and use the RInChI in addition.

The RInChI format is a hierarchical, layered description of a
reaction with different levels based on the Standard InChI
representation of each structural component participating in
the reaction.



.. note:: This is a write-only format.

Write Options
~~~~~~~~~~~~~ 

-e  *Treat this reaction as an equilibrium reaction*

    Layer 5 of the generated RInChI will have /d=

