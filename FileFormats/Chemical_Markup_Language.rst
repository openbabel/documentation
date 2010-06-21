Chemical Markup Language (cml)
==============================

Chemical Markup Language XML format. This implementation uses libxml2.

Write Options
~~~~~~~~~~~~~
**1**
    output CML1 (rather than CML2)
**a**
    output array format for atoms and bonds
**A**
    write aromatic bonds as such, not Kekule form
**h**
    use hydrogenCount for all hydrogens
**m**
    output metadata
**x**
    omit XML and namespace declarations
**c**
    continuous output: no formatting
**p**
    output properties
**N<prefix>**
    add namespace prefix to elements
**Input**
    options, e.g. -a2
**2**
    input 2D rather than 3D coordinates if both provided
