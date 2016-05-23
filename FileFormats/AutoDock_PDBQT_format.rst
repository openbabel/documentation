.. _AutoDock_PDBQT_format:

AutoDock PDBQT format (pdbqt)
=============================

**Reads and writes AutoDock PDBQT (Protein Data Bank, Partial Charge (Q), & Atom Type (T)) format**

Note that the torsion tree is by default. Use the ``r`` write option
to prevent this.



Read Options
~~~~~~~~~~~~ 

-b  *Disable automatic bonding*
-d  *Input file is in dlg (AutoDock docking log) format*


Write Options
~~~~~~~~~~~~~ 

-b  *Enable automatic bonding*
-r  *Output as a rigid molecule (i.e. no branches or torsion tree)*
-c  *Combine separate molecular pieces of input into a single rigid molecule (requires "r" option or will have no effect)*
-s  *Output as a flexible residue*
-p  *Preserve atom indices from input file (default is to renumber atoms sequentially)*
-h  *Preserve hydrogens*
-n  *Preserve atom names*


