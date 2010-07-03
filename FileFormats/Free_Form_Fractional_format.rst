Free Form Fractional format (fract)
===================================

**General purpose crystallographic format**

The "free-form" fractional format attempts to allow for input from a
range of fractional / crystallography file formats. As such, it has only
a few restrictions on input:

- Line one of the file contains a title or comment.
- Line two of the file contains the unit cell parameters separated by
  whitespace and/or commas (i.e. "a b c alpha beta gamma").
- Any remaining lines are parsed for atom information. Lines start with
  the element symbol, followed by fractional X, Y, and Z coordinates
  (in angstroms) separated by whitespace.

Any numeric input (i.e., unit cell parameters, XYZ coordinates) can include
designations of errors, although this is currently ignored. For example::

  C 1.00067(3) 2.75(2) 3.0678(12)

will be parsed as::

  C 1.00067 2.75 3.0678

When used as an **output** format, The first line written is the title of the
molecule or the filename if no title is defined. If a molecule has a defined
unit cell, then the second line will be formatted as::

  a b c alpha beta gamma

where a, b, c are the unit cell vector lengths, and alpha, beta, and gamma are
the angles between them. These numbers are formatted as "10.5", which means that
5 decimal places will be output for all numbers. In the case where no unit cell
is defined for the molecule, the vector lengths will be defined as 1.0, and the
angles to 90.0 degrees.

Remaining lines define the atoms in the file. The first column is the atomic
symbol, followed by the XYZ coordinates in 10.5 format (in angstroms).

Here is an example file::

 ZnO test file
 3.14 3.24 5.18 90.0 90.0 120.0
 O 0.66667  0.33333  0.3750
 O 0.33333  0.66667  0.8750
 Zn 0.66667  0.33333  0.0000
 Zn 0.33333  0.66667  0.5000



Read Options
~~~~~~~~~~~~

.. cmdoption:: s

  Output single bonds only

.. cmdoption:: b

  Disable bonding entirely
