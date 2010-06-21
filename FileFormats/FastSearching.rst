FastSearching (fs)
==================

FastSearching Uses molecular fingerprints in an index file. Writing to the fs format makes an index (a very slow process)   babel datafile.xxx index.fs Reading from the fs format does a fast search for:   Identical molecule     babel index.fs -sSMILES outfile.yyy -ae  or     babel datafile.xxx -ifs -sSMILES outfile.yyy -ae   Substructure     babel index.fs -sSMILES outfile.yyy   or     babel datafile.xxx -ifs -sSMILES outfile.yyy   Molecular similarity based on Tanimoto coefficient     babel index.fs -sSMILES outfile.yyy -t0.7  (Tanimoto >0.7)     babel index.fs -sSMILES outfile.yyy -t15   (best 15 molecules)   The structure spec can be a molecule from a file: -Spatternfile.zzz  Note that the parameter of the -s option needs to be a valid SMILES molecule when using fastsearch. You can use the more versatile SMARTS in a normal substructure search. 

Write Options
~~~~~~~~~~~~~
**f#**
    Fingerprint type
**N#**
    Fold fingerprint to # bits
**u**
    Update an existing index
