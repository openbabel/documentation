Depiction
=========

As the old Chinese proverb has it, molecular depiction is worth a thousand words. This chapter covers everything relevant to using Open Babel to generate or read/write a depiction.

When we talk about a depiction in cheminformatics, there are really two different concepts covered by this term:

1. Graphical display of a molecule's structure as a 2D image (such as the PNG and SVG formats). Here is an example:

.. image:: ../_static/acidchloride.png

2. Storage of the 2D coordinates (and associated stereo symbols) associated with Concept 1 (using formats such as Mol and Mol2). Here is the connection table from the corresponding Mol file for the above depiction::
   
    3  2  0  0  0  0  0  0  0  0999 V2000
      0.8660   -0.5000    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0
      1.7321   -0.0000    0.0000 O   0  0  0  0  0  0  0  0  0  0  0  0
      0.0000    0.0000    0.0000 Cl  0  0  0  0  0  0  0  0  0  0  0  0
    1  2  2  0  0  0  0
    1  3  1  0  0  0  0

.. note::

        The focus in this chapter is on 2D depiction and not 3D. It is of course possible to store 3D coordinates in many of the file formats supported by Open Babel, but the only support for depiction is the Povray format, used to create ray-traced ball-and-stick diagrams of molecules. 
        Other Open Source chemistry projects such as Avogadro, PyMOL and Jmol cover this area very well.

Create a depiction
------------------

More here.
