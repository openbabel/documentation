.. _Extended_XYZ_cartesian_coordinates_format:

Extended XYZ cartesian coordinates format (exyz)
================================================

**A generic coordinate format**

The "EXYZ" chemical file format is an extended version of the standard "XYZ" chemical file format
with additional keywords and informations about the unit cell and virtual atoms
* Line one of the file contains the number of atoms in the file.
* Line two of the file contains a title, comment, filename and/or the following keywords:
 %PBC or %VIRTUAL

Any remaining lines are parsed for atom information until a blank line. Lines start with the element
symbol, followed by X, Y, and Z coordinates in angstroms separated by whitespace and - if %VIRTUAL is specified - the
optional word VIRTUAL to mark virtual atoms
 the second block contains - if %PBC is specified - the 3 vectors for the unit cell in angstrom and the offset
Example::

4
%PBC
   C        0.00000        1.40272        0.00000
   H        0.00000        2.49029        0.00000
   C       -1.21479        0.70136        0.00000
   H       -2.15666        1.24515        0.00000

Vector1    2.445200    0.000000    0.000000
Vector2    0.000000    1.000000    0.000000
Vector3    0.000000    0.000000    1.000000
Offset     0.000000    0.000000    0.000000
On **output**, the first line written is the number of atoms in the molecule
(warning - the number of digits is limited to three for some programs,
e.g. Maestro). Line two is the title of the molecule or the filename if
no title is defined. Remaining lines define the atoms in the file. The
first column is the atomic symbol (right-aligned on the third character),
followed by the XYZ coordinates in "15.5" format separated by an addition whitespace, in angstroms. This means
that all coordinates are printed with five decimal places.

The next block starts with a blank line to separate the coordinates from the unit cell vectors
followed by the vectors of the unit cell marked with the keywords Vector1/2/3
the vectors themselves are written in the same format like the atom coordinates
the last line contains the keyword Offset and the offset of the unit cell.
The unit is always angstrom
Example::

4
%PBC Extended xyz-file written by ORCA-AICCM
C     0.600475   -0.323347    0.000000
H    -0.600476    0.323347    0.000000
C     0.600441   -1.434346    0.000000
H    -0.600441    1.434347    0.000000

Vector1    2.445200    0.000000    0.000000
Vector2    0.000000    1.000000    0.000000
Vector3    0.000000    0.000000    1.000000
Offset     0.000000    0.000000    0.000000


Read Options
~~~~~~~~~~~~ 

-s  *Output single bonds only*
-b  *Disable bonding entirely*


