.. _fingerprints:

Molecular fingerprints and similarity searching
===============================================

Molecular fingerprints are a way of encoding the structure of a molecule. The most common type of fingerprint is a series of binary digits (bits) that represent the presence or absence of particular substructures in the molecule. Comparing fingerprints allows you to determine the similarity between two molecules, to find matches to a query substructure, etc.

Open Babel provides several fingerprints of different types: 

* :ref:`fingerprint_format_details`: the path-based fingerprint FP2; substructure based fingerprints FP3, FP4 and MACCS; user-defined substructures 
* :ref:`Multilevel_Neighborhoods_of_Atoms_(MNA)`: a circular fingerprint
* :ref:`MolPrint2D_format`: a circular fingerprint
* :ref:`spectrophores`: a fingerprint that encodes the 3D structure of a molecule

The next two sections describe the *Fingerprint format* and *Spectrophores* in depth. For the others, see the relevant sections listed above.

.. toctree::

   fingerprints.rst
   spectrophore.rst

