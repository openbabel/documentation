.. _VASP_format:

VASP format (CONTCAR, POSCAR)
=============================

**Reads in data from POSCAR and CONTCAR to obtain information from VASP calculations.**


Due to limitations in Open Babel's file handling, reading in VASP files can
be a bit tricky; the client that is using Open Babel must use
OBConversion::ReadFile() to begin the conversion. This change is usually
trivial. Also, the complete path to the CONTCAR file must be provided,
otherwise the other files needed will not be found.


.. note:: This is a read-only format.

