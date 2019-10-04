.. _Tinker_XYZ_format:

Tinker XYZ format (txyz)
========================

**The cartesian XYZ file format used by the molecular mechanics package TINKER.**

By default, the MM2 atom types are used for writing files but MM3 atom types
are provided as an option. Another option provides the ability to take the
atom type from the atom class (e.g. as used in SMILES, or set via the API).



Read Options
~~~~~~~~~~~~ 

-s  *Generate single bonds only*


Write Options
~~~~~~~~~~~~~ 

-m  *Write an input file for the CNDO/INDO program.*
-c  *Write atom types using custom atom classes, if available*
-3  *Write atom types for the MM3 forcefield.*


