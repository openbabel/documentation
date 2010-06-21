CML Reaction format (cmlr)
==========================

CML Reaction format Minimal implementation This implementation uses libxml2.

Write Options
~~~~~~~~~~~~~
**1**
    output CML V1.0 or
**2**
    output CML V2.0 (default)
**a**
    output array format for atoms and bonds
**l**
    molecules NOT in MoleculeList
**h**
    use hydrogenCount for all hydrogens
**x**
    omit XML declaration
**r**
    omit rate constant data
**N<prefix>**
    add namespace prefix to elements
**M**
    add obr prefix on non-CMLReact elements
**p**
    add properties to molecules
