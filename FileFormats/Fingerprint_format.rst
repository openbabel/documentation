.. _Fingerprint_format:

Fingerprint format (fpt)
========================

**Generate or display molecular fingerprints.**

This format constructs and displays fingerprints and (for multiple input objects)
the Tanimoto coefficient and whether a superstructure of the first object.

A list of available fingerprint types can be obtained by::

  babel -L fingerprints

The current default type FP2 is is of the Daylight type, indexing a molecule
based on the occurrence of linear fragment up to 7 atoms in length. To use a
fingerprint type other than the default, use the -xf option, for example::

  babel infile.xxx -ofpt -xfFP3

For a single molecule the fingerprint is output in hexadecimal form
(intended mainly for debugging).

With multiple molecules the hexadecimal form is output only if the -xh
option is specified. But in addition the Tanimoto coefficient between the
first molecule and each of the subsequent ones is displayed. If the first
molecule is a substructure of the target molecule a note saying this is
also displayed.

The Tanimoto coefficient is defined as::

 Number of bits set in (patternFP & targetFP) / Number of bits in (patternFP | targetFP)

where the boolean operations between the fingerprints are bitwise.

The Tanimoto coefficient has no absolute meaning and depends on the design of the fingerprint.

In Fingerprint FP4 each bit corresponds to a particular chemical feature,
which are specified as SMARTS patterns in SMARTS_InteLigand.txt. Use the -xs
option to output a tab separated list of the features in a molecule. For
instance a well-known molecule gives::

 Primary_carbon: Carboxylic_acid: Carboxylic_ester: Carboxylic_acid_derivative:
 Vinylogous_carbonyl_or_carboxyl_derivative: Vinylogous_ester: Aromatic:
 Conjugated_double_bond: C_ONS_bond: 1,3-Tautomerizable: Rotatable_bond: CH-acidic:



.. note:: This is a write-only format.

Write Options
~~~~~~~~~~~~~ 

-f <id>  *fingerprint type*
-N <num>  *fold to specified number of bits, 32, 64, 128, etc.*
-h  *hex output when multiple molecules*
-o  *hex output only*
-s  *describe each set bit*
-u  *describe each unset bit*
