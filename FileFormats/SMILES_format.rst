.. _SMILES_format:

SMILES format (smi, smiles)
===========================

**A linear text format which can describe the connectivity and chirality of a molecule**

Open Babel implements the `OpenSMILES specification <http://opensmiles.org>`_.

It also implements an extension to this specification for radicals.

Note that the ``l <atomno>`` option, used to specify a "last" atom, is
intended for the generation of SMILES strings to which additional atoms
will be concatenated. If the atom specified has an explicit H within a bracket
(e.g. ``[nH]`` or ``[C@@H]``) the output will have the H removed along with any
associated stereo symbols.

.. seealso::

  The :ref:`Canonical_SMILES_format` produces a canonical representation
  of the molecule in SMILES format. This is the same as the ``c`` option
  below but may be more convenient to use.



Write Options
~~~~~~~~~~~~~ 

-a  *Output atomclass like [C:2], if available*
-c  *Output in canonical form*
-h  *Output explicit hydrogens as such*
-i  *Do not include isotopic or chiral markings*
-n  *No molecule name*
-r  *Radicals lower case eg ethyl is Cc*
-t  *Molecule name only*
-x  *append X/Y coordinates in canonical-SMILES order*
-C  *'anti-canonical' random order (mostly for testing)*
-f <atomno>  *Specify the first atom*

     This atom will be used to begin the SMILES string.
-l <atomno>  *Specify the last atom*

     The output will be rearranged so that any additional
     SMILES added to the end will be attached to this atom.

