Chemical Registration Systems
=============================

Chemical Registration is the "big brother" of cheminformatics.

A cheminformatics system is primarily devoted to recording chemical
structure. Chemical Registration systems are additionally concerned
with:


-  Structural novelty - ensure that each compound is only
   registered once
-  Structural normalization - ensure that structures with
   alternative representations (such as nitro groups, ferrocenes, and
   tautomers) are entered in a uniform way.
-  Structure drawing - ensure that compounds are drawn in a uniform
   fashion, so that they can be quickly recognized "by eye".
-  Maintaining relationships among related compounds. For example,
   all salt forms of a compound should be recognized as being related
   to one another, and compounds in different solvates are also
   related.
-  Registering mixtures, formulations and alternative structures.
-  Registering compounds the structure of which is unknown.
-  Roles, responsibilities, security, and company workflow.
-  Updates, amendments and corrections, and controlling propagation
   of changes (e.g. does changing a compound change a mixture
   containing that compound?)

The scope of Chemical Registration Systems is far beyond the goals
of this brief introduction to cheminformatics. However, to
illustrate just one of the points above, let's consider structural
novelty. In real life, chemical structure can be very ambiguous.
Imagine you have five bottles of a particular compound that has a
stereo center:


#. The contents of the first bottle were carefully analyzed, and
   found to be a single stereoisomer.
#. The contents of the second bottle were carefully analyzed and
   found to contain a racemic mixture of the stereoisomers.
#. The stereoisomers of the third bottle are unknown. It may be
   pure, or have one predominant form, or be a racemic mixture.
#. The fourth bottle was obtained by running part of the contents
   of bottle #2 through a chromatographic separation. It is
   isotopically pure, but you don't know which stereoisomer.
#. The fifth bottle is the other fraction from the same separation
   of #4. It is also isotopically pure, but you don't know which
   stereoisomer, *but you know it's the opposite of #4*.

Which of these five bottles contain the same compound, and which
are different? That is the essential task of a chemical registry
system, which would consider all five to be different. After all,
you probably have data about each bottle (that's why you have
them), and you must be able to record it and not confuse it with
the other bottles.

In this example above, consider what is known and not known:

======  ============================================================  =========
Bottle  Known                                                         Not Known
======  ============================================================  =========
1       Everything                                                    Nothing
2       Everything                                                    Nothing
3       Compound is known                                             Stereochemistry
4       Compound and purity known, stereochemistry is opposite of #5  Specific stereochemistry
5       Compound and purity known, stereochemistry is opposite of #4  Specific stereochemistry
======  ============================================================  =========

A cheminformatics system has no way to record the contents of the
five bottles; it is only concerned with structure. By contrast, a
chemical registration system can record both *what is known* as
well as *what is not known*. This is the critical difference
between the two.
