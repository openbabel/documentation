SVG depiction (svg)
===================

**Scalable Vector Graphics 2D rendering of molecular structure.**

 

 Single molecules are displayed at a fixed scale, as in normal diagrams, but multiple molecules are displayed in a table which expands to fill the containing element, such as a browser window.  

 Multiple molecules are displayed in a grid of dimensions specified by the -xr and -xc options (number of rows and columns respectively). When displayed in an appropriate program, e.g. Firefox, there is javascript support for zooming (with the mouse wheel) and panning (by dragging with the left mouse button).  

 If both -xr and -xc are specified, they define the maximum number of molecules that are displayed. If only one of them is displayed, then the other is calculated so that ALL the molecules are displayed. If neither are specified, all the molecules are output in an approximately square table.  

 By default, 2D atom coordinates are generated (using gen2D) unless they are already present. This can be slow with a large number of molecules. (3D coordinates are ignored.) Include --gen2D explicitly if you wish any existing 2D coordinates to be recalculated.  



Write Options
~~~~~~~~~~~~~

.. cmdoption:: u

  no element-specific atom coloring

.. note::

    Use this option to produce a black and white diagram

.. cmdoption:: b

  black background

.. note::

    The default is white. The atom colors work with both.

.. cmdoption:: C

  do not draw terminal carbon atoms explicitly

.. note::

    The default is to draw all hetero atoms and terminal C explicitly.

.. cmdoption:: a

  draw all carbon atoms

.. note::

    So propane would display as H3C-CH2-CH3

.. cmdoption:: d

  do not display molecule name

.. cmdoption:: e

  embed molecule as CML

.. note::

    OpenBabel can read the resulting svg file as a cml file.

.. cmdoption:: p#

  scale to bondlength in pixels(single mol only)

.. cmdoption:: c#

  number of columns in table

.. cmdoption:: r#

  number of rows in table

.. cmdoption:: N#

  max number objects to be output

.. cmdoption:: l

  draw grid lines

.. cmdoption:: i

  add index to each atom

.. note::

    These indices are those in sd or mol files and correspond to the
    order of atoms in a SMILES string.

.. cmdoption:: j

  do not embed javascript

.. note::

    Javascript is not usually embedded if there is one one molecule,
    but it is if the rows and columns have been specified as 1: -xr1 -xc1

.. cmdoption:: A

  display aliases, if present

.. note::

    This applies to structures which have an alternative, usually
    shorter, representation already present. This might have been input
    from an A or S superatom entry in an sd or mol file, or can be
    generated using the --genalias option. For example:
      echo "c1cc(C=O)ccc1C(=O)O" | babel -ismi out.svg --genalias -xA
    would add a aliases COOH and CHO to represent the carboxyl and
    aldehyde groups and would display them as such in the svg diagram.
    The aliases which are recognized are in data/superatom.txt, which
    can be edited.
Comments
~~~~~~~~

Additional option(not displayed in GUI)  x omit XML declaration     Useful if the output is to be embedded in another xml file.  If the input molecule(s) contain explicit hydrogen, you could consider improving the appearance of the diagram by adding an option -d to make it implicit. Hydrogen on hetero atoms and on explicitly drawn C is always shown. For example, if input.smi had 10 molecules:       babel input.smi out.svg -xbCe would produce a svg file with a black background, with no explict terminal carbon, and with an embedded cml representation of each molecule. The structures would be in two rows of four and one row of two. Not that it is possible to concatinate multiple single- letter options (with a single preceding -x). 

