.. _PNG2_format:

PNG2 format (png2)
==================

**2D depiction of a single molecule as a .png file**


The PNG2 format is used 'behind the scenes' by the PNG format
if generating image files, but the best way to use it is
actually through the PNG format. While it possible to generate
a :file:`.png` file directly using the PNG2 format as follows...::

  obabel -:"CC(=O)Cl" -opng2 -O mymol.png

...it is much better to generate it using the PNG format
as this allows you to embed a chemical structure in the
:file:`.png` file header which you can later extract::

  $ obabel -:"CC(=O)Cl" -O mymol.png -xO smi
  $ obabel mymol.png -osmi
  CC(=O)Cl

The PNG2 format uses the Cairo library to generate the
:file:`.png` files.
If Cairo was not found when Open Babel was compiled, then
this format will be unavailable. However, it will still be possible
to use the PNG format to read :file:`.png` files if they contain
embedded information.



.. note:: This is a write-only format.

Write Options
~~~~~~~~~~~~~ 

-p <pixels>  *image size, default 300*
