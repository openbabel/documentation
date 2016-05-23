.. _Fastsearch_format:

Fastsearch format (fs)
======================

**Fingerprint-aided substructure and similarity searching**


Writing to the fs format makes an index of a multi-molecule datafile::

      obabel dataset.sdf -ofs

This prepares an index :file:`dataset.fs` with default parameters, and is slow
(~30 minutes for a 250,000 molecule file).

However, when reading from the fs format searches are much faster, a few seconds,
and so can be done interactively.

The search target is the parameter of the ``-s`` option and can be
slightly extended SMILES (with ``[#n]`` atoms and ``~`` bonds) or
the name of a file containing a molecule.

Several types of searches are possible:

- Identical molecule::

      obabel index.fs -O outfile.yyy -s SMILES exact

- Substructure::

      obabel index.fs -O outfile.yyy  -s SMILES   or
      obabel index.fs -O outfile.yyy  -s filename.xxx

  where ``xxx`` is a format id known to OpenBabel, e.g. sdf
- Molecular similarity based on Tanimoto coefficient::

      obabel index.fs -O outfile.yyy -at15  -sSMILES  # best 15 molecules
      obabel index.fs -O outfile.yyy -at0.7 -sSMILES  # Tanimoto >0.7
      obabel index.fs -O outfile.yyy -at0.7,0.9 -sSMILES
      #     Tanimoto >0.7 && Tanimoto < 0.9

The datafile plus the ``-ifs`` option can be used instead of the index file.

NOTE that the datafile MUST NOT be larger than 4GB. (A 32 pointer is used.)

Dative bonds like -[N+][O-](=O) are indexed as -N(=O)(=O), and when searching
the target molecule should be in the second form.

.. seealso::

    :ref:`fingerprints`



Read Options
~~~~~~~~~~~~ 

-t <num>  *Do similarity search:<num>mols or <num> as min Tanimoto*
-a  *Add Tanimoto coeff to title in similarity search*
-l <num>  *Maximum number of candidates. Default<4000>*
-e  *Exact match*

     Alternative to using exact in ``-s`` parameter, see above
-n  *No further SMARTS filtering after fingerprint phase*


Write Options
~~~~~~~~~~~~~ 

-f <num>  *Fingerprint type*

     If not specified, the default fingerprint (currently FP2) is used
-N <num>  *Fold fingerprint to <num> bits*
-u  *Update an existing index*


