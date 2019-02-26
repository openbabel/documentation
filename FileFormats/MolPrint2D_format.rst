.. _MolPrint2D_format:

MolPrint2D format (mpd)
=======================

**An implementation of the circular fingerprint MolPrint2D**

MolPrint2D is an atom-environment fingerprint developed by Bender et al [bmg2004]_
which has been used in QSAR studies and for measuring molecular similarity.

The format of the output is as follows::

   [Molec_name]\t[atomtype];[layer]-[frequency]-[neighbour_type];

Example for the SMILES string ``CC(=O)Cl``::

   acid chloride   1;1-1-2;2-1-9;2-1-15;   2;1-1-1;1-1-9;1-1-15;
                   9;1-1-2;2-1-1;2-1-15;   15;1-1-2;2-1-1;2-1-9;

.. [bmg2004] Andreas Bender, Hamse Y. Mussa, and Robert C. Glen. **Molecular
             Similarity Searching Using Atom Environments, Information-Based
             Feature Selection, and a Naive Bayesian Classifier.**
             *J. Chem. Inf. Comput. Sci.* **2004**, *44*, 170-178.
             [`Link <https://doi.org/10.1021/ci034207y>`_]



.. note:: This is a write-only format.

Write Options
~~~~~~~~~~~~~ 

-n  *prefix molecule names with name of file*
-c  *use XML style separators instead*
-i  *use IDX atom types of babel internal*


