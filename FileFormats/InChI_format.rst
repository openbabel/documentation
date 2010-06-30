InChI format (inchi)
====================

**IUPAC/NIST molecular identifier**

Read Options
~~~~~~~~~~~~

.. cmdoption:: X <Option string>

  List of InChI options

.. cmdoption:: n

  molecule name follows InChI on same line

.. cmdoption:: a

  add InChI string to molecule name
Write Options
~~~~~~~~~~~~~

.. cmdoption:: X <Option string>

  List of additional InChI options

.. cmdoption:: t

  add molecule name

.. cmdoption:: a

  output auxilliary information

.. cmdoption:: K

  output InChIKey

.. cmdoption:: w

  don't warn on undef stereo or charge rearrangement

.. cmdoption:: l

  display InChI log

.. cmdoption:: u

  output only unique molecules

.. cmdoption:: U

  output only unique molecules and sort them

.. cmdoption:: e

  compare first molecule to others

.. cmdoption:: T <param>

  truncate InChI, /nostereo etc.
Comments
~~~~~~~~

Currently the output is standard InChI only.InChI options may be reintroduced later. The InChI options should be space delimited in a single quoted string.  See InChI documentation for possible options.   Truncation parameters used with -xT /formula  formula only /connect  formula and connectivity only /nostereo ignore E/Z and sp3 stereochemistry /sp3      ignore sp3 stereochemistry /noEZ     ignore E/Z steroeochemistry /nochg    ignore charge and protonation /noiso    ignore isotopes 

