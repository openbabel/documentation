.. _Canonical_SMILES_format:

Canonical SMILES format (can)
=============================

**A canonical form of the SMILES linear text format**

The SMILES format is a linear text format which can describe the
connectivity and chirality of a molecule. Canonical SMILES gives a single
'canonical' form for any particular molecule.

.. seealso::

  The "regular" :ref:`SMILES_format` gives faster
  output, since no canonical numbering is performed.



Write Options
~~~~~~~~~~~~~ 

-a  *Output atomclass like [C:2], if available*
-h  *Output explicit hydrogens as such*
-i  *Do not include isotopic or chiral markings*
-n  *No molecule name*
-r  *Radicals lower case eg ethyl is Cc*
-t  *Molecule name only*
-F <atom numbers>  *Generate Canonical SMILES for a fragment*

     The atom numbers should be specified like "1 2 4 7".
-f <atomno>  *Specify the first atom*

     This atom will be used to begin the SMILES string.
-l <atomno>  *Specify the last atom*

     The output will be rearranged so that any additional
     SMILES added to the end will be attached to this atom.
     See the :ref:`SMILES_format` for more information.

