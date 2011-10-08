.. _InChIKey:

InChIKey (inchikey)
===================

**A hashed representation of the InChI.**


The InChIKey is a fixed-length (27-character) condensed digital
representation of an InChI, developed to make it easy to perform
web searches for chemical structures.

An InChIKey consists of 14 characters (derived from the connectivity
layer in the InChI), a hyphen, 9 characters (derived from the
remaining layers), a character indicating the InChI version, a hyphen
and a final checksum character. Contrast the InChI and InChIKey of the
molecule represented by the SMILES string `CC(=O)Cl`::

  obabel -:CC(=O)Cl -oinchi
  InChI=1S/C2H3ClO/c1-2(3)4/h1H3

  obabel -:CC(=O)Cl -oinchikey
  WETWJCDKMRHUPV-UHFFFAOYSA-N

This is the same as using ``-oinchi -xK`` and can take the same options
as the InChI format (see :ref:`InChI_format`)::

  obabel -:CC(=O)Cl -oinchi -xK
  WETWJCDKMRHUPV-UHFFFAOYSA-N

Note that while a molecule with a particular InChI will always give the
same InChIKey, the reverse is not true; there may exist more than one
molecule which have different InChIs but yield the same InChIKey.


.. note:: This is a write-only format.

