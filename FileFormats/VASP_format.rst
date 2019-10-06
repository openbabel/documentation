.. _VASP_format:

VASP format (CONTCAR, POSCAR, VASP)
===================================

**Reads in data from POSCAR and CONTCAR to obtain information from VASP calculations.**


Due to limitations in Open Babel's file handling, reading in VASP
files can be a bit tricky; the client that is using Open Babel must
use OBConversion::ReadFile() to begin the conversion. This change is
usually trivial. Also, the complete path to the CONTCAR/POSCAR file
must be provided, otherwise the other files needed will not be
found.

Both VASP 4.x and 5.x POSCAR formats are supported.

By default, atoms are written out in the order they are present in the input
molecule. To sort by atomic number specify ``-xw``. To specify the sort
order, use the ``-xz`` option.



Read Options
~~~~~~~~~~~~ 

-s  *Output single bonds only*
-b  *Disable bonding entirely*


Write Options
~~~~~~~~~~~~~ 

-w  *Sort atoms by atomic number*
-z <list of atoms>  *Specify the order to write out atoms*

       'atom1 atom2 ...': atom1 first, atom2 second, etc. The remaining
       atoms are written in the default order or (if ``-xw`` is specified)
       in order of atomic number.
-4  *Write a POSCAR using the VASP 4.x specification.*

    The default is to use the VASP 5.x specification.

