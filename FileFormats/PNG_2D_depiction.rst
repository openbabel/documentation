.. _PNG_2D_depiction:

PNG 2D depiction (png)
======================

**Write a single molecule image file; 2D coordinates are added if not present.**

  obabel  mymol.smi  -O image.png
Chemical structure data can be embedded (in a tEXt chunk)
  obabel  mymol.mol  -O image.png -xO molfile
The parameter of the -xO option specifies the format ("file"can be added)
Molecules can be embedded in an existing PNG file:
  obabel  existing.png  mymol1.smi  mymol2.mol  -O augmented.png  -xO mol

Reading from a PNG file will extract any embedded chemical structure data:
  obabel  augmented.png  -O contents.sdf


Read Options
~~~~~~~~~~~~ 

-y <additional chunk ID>  *Look also in chunks with specified ID*


Write Options
~~~~~~~~~~~~~ 

-p <pixels>  *image size, default 300*
-O <format ID>  *Format of embedded text*
-y <additional chunk ID>  *Write to a chunk with specified ID*


