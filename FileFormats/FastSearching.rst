FastSearching (fs)
==================

**Uses molecular fingerprints in an index file.**

Writing to the fs format makes an index (a very slow process)   babel datafile.xxx index.fs Reading from the fs format does a fast search for:   Identical molecule     babel index.fs -sSMILES outfile.yyy -ae  or     babel datafile.xxx -ifs -sSMILES outfile.yyy -ae   Substructure     babel index.fs -sSMILES outfile.yyy   or     babel datafile.xxx -ifs -sSMILES outfile.yyy   Molecular similarity based on Tanimoto coefficient     babel index.fs -sSMILES outfile.yyy -at0.7  (Tanimoto >0.7)     babel index.fs -sSMILES outfile.yyy -at0.7,0.9  (Tanimoto >0.7 && Tanimoto < 0.9)     babel index.fs -sSMILES outfile.yyy -at15   (best 15 molecules)   The structure spec can be a molecule from a file: -Spatternfile.zzz  

 Note that the parameter of the -s option needs to be a valid SMILES molecule when using fastsearch. You can use the more versatile SMARTS in a normal substructure search.  



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
