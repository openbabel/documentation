.. _SMILES_format_using_Smiley_parser:

SMILES format using Smiley parser (smy)
=======================================
The Smiley parser presents an alternative to the standard SMILES parser
(:ref:`SMILES_format`). It was written to be strictly compatible with the
OpenSMILES standard (http://opensmiles.org). In comparison, the standard
parser is more forgiving to erroneous input, and also supports some extensions
such as for radicals.

In addition, the Smiley parser returns detailed error messages when problems
arise parsing or validating the SMILES, whereas the standard parser seldom
describes the specific problem. For a detailed description of the OpenSMILES
semantics, the specification should be consulted. In addition to syntactical
and grammatical correctness, the Smiley parser also verifies some basic
semantics.

Here are some examples of the errors reported::

   SyntaxError: Bracket atom expression contains invalid trailing characters.
   F.FB(F)F.[NH2+251][C@@H](CP(c1ccccc1)c1ccccc1)C(C)(C)C 31586112
                  ^^
   SyntaxError: Unmatched branch opening.
   CC(CC
     ^^^
   SyntaxError: Unmatched branch closing.
   CC)CC
   ^^^
   SemanticsError: Unmatched ring bond.
   C1CCC
   ^
   SemanticsError: Conflicing ring bonds.
   C-1CCCCC=1

Hydrogen with Hydrogen Count
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hydrogen atoms can not have a hydrogen count. Hydrogen bound to a hydrogen
atom should be specified by two bracket atom expressions.

Eamples::

  [HH]        invalid
  [HH1]       invalid (same as [HH]
  [HH3]       invalid
  [HH0]       valid (same as [H])
  [H][H]      valid

Unmatched Ring Bond
~~~~~~~~~~~~~~~~~~~
Report unmatched ring bonds.

Example::

  C1CCC

Conflicting Ring Bonds
~~~~~~~~~~~~~~~~~~~~~~
When the bond type for ring bonds are explicitly specified at both ends,
these should be the same.

Example::

  C-1CCCCCC=1

Invalid Ring Bonds
~~~~~~~~~~~~~~~~~~
There are two types of invalid ring bonds. The first is when two atoms both
have the same two ring bonds. This would mean adding a parallel edge in the
graph which is not allowed. The second type is similar but results in a
self-loop by having a ring bond number twice.

Eamples::

  C12CCCC12      parallel bond
  C11            self-loop bond

Invalid Chiral Valence
~~~~~~~~~~~~~~~~~~~~~~
When an atom is specified as being chiral, it should have the correct
number of neighboring atoms (possibly including an implicit H inside the
bracket.

The valid valences are::

  Tetrahedral (TH)          : 4
  Allene (AL)               : 4 (*)
  Square Planar (SP)        : 4
  Trigonal Bypiramidal (TB) : 5
  Octahedral(OH)            : 6

  (*) The chiral atom has only 2 bonds but the neighbor's neighbors are
      counted: NC(Br)=[C@AL1]=C(F)I

Invalid Chiral Hydrogen Count
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Chiral atoms can only have one hydrogen in their bracket since multiple
hydrogens would make them not chiral.

Example::

  C[C@H2]F



.. note:: This is a read-only format.

