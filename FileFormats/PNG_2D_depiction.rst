.. _PNG_2D_depiction:

PNG 2D depiction (png)
======================

**2D depiction of a single molecule, or add/extract a chemical structure from a .png file**


The PNG format has several uses. The most common is to generate a
:file:`.png` file for a single structure (which may contain several
disconnected components). 2D coordinates are generated if not present::

  obabel mymol.smi -O image.png

Chemical structure data can be embedded in the :file:`.png` file
(in a ``tEXt`` chunk)::

  obabel mymol.mol -O image.png -xO molfile

The parameter of the ``-xO`` option specifies the format ("file"can be added).
Note that if you intend to embed a 2D or 3D format, you may have to call
``--gen2d`` or ``--gen3d`` to generate the required coordinates if they are
not present in the input.

Molecules can also be embedded in an existing PNG file::

  obabel existing.png mymol1.smi mymol2.mol -O augmented.png -xO mol

Reading from a PNG file will extract any embedded chemical structure data::

  obabel augmented.png -O contents.sdf



Read Options
~~~~~~~~~~~~ 

-y <additional chunk ID>  *Look also in chunks with specified ID*


Write Options
~~~~~~~~~~~~~ 

-p <pixels>  *image size, default 300*
-O <format ID>  *Format of embedded text*

      For example, ``molfile`` or ``smi``.
-y <additional chunk ID>  *Write to a chunk with specified ID*


