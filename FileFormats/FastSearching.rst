FastSearching (fs)
==================

**Uses molecular fingerprints in an index file.**

This format uses molecular fingerprints to prepare and search
an index of a multi-molecule datafile. It allows fast substructure
and structural similarity searching. The indexing is a slow process
(~30 minutes for a 250,000 molecule file). The subsequent seaching
is much faster, a few seconds, and so can be done interactively.

For more information on using the FastSearch index format, see
the user's tutorial.

Writing to the fs format makes an index (a very slow process)::

  babel datafile.xxx index.fs

Reading from the fs format does a fast search for:

- Identical molecule::

    babel index.fs -sSMILES outfile.yyy -ae  or
    babel datafile.xxx -ifs -sSMILES outfile.yyy -ae

- Substructure::

    babel index.fs -sSMILES outfile.yyy   or
    babel datafile.xxx -ifs -sSMILES outfile.yyy

- Molecular similarity based on Tanimoto coefficient::

    babel index.fs -sSMILES outfile.yyy -at0.7  (Tanimoto >0.7)
    babel index.fs -sSMILES outfile.yyy -at0.7,0.9  (Tanimoto >0.7 && Tanimoto < 0.9)
    babel index.fs -sSMILES outfile.yyy -at15   (best 15 molecules)

  The structure spec can be a molecule from a file: -Spatternfile.zzz

Note that the parameter of the -s option needs to be a valid SMILES
molecule when using fastsearch. You can use the more versatile SMARTS
in a normal substructure search.

Read Options
~~~~~~~~~~~~

.. cmdoption:: t#

  Do similarity search: #mols or # as min Tanimoto

.. cmdoption:: a

  Add Tanimoto coeff to title in similarity search

.. cmdoption:: l#

  Maximum number of candidates. Default<4000>

.. cmdoption:: e

  Exact match

.. cmdoption:: S"filename"

  Structure spec in a file:

.. cmdoption:: n

  No further SMARTS filtering after fingerprint phase

.. cmdoption:: h

  SMARTS uses explicit H in pattern file
Write Options
~~~~~~~~~~~~~

.. cmdoption:: f#

  Fingerprint type

.. cmdoption:: N#

  Fold fingerprint to # bits

.. cmdoption:: u

  Update an existing index
