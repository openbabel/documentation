VASP format (CONTCAR, POSCAR)
=============================

**Reads in data from POTCAR and CONTCAR to obtain information from VASP calculations.**

Due to limitations in OB's file handling, reading in VASP files can be a bit tricky:
	The client that is using OpenBabel must use OBConversion::ReadFile() to begin the conversion.
	This change is usually trivial, ask the package mantainer to look into it. Also, the complete
	path to the CONTCAR file must be provided, otherwise the other files need won't be found.


