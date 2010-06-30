Chemical Markup Language (cml)
==============================

**An XML format.**

Read Options
~~~~~~~~~~~~

.. cmdoption:: 2

  input 2D rather than 3D coordinates if both provided
Write Options
~~~~~~~~~~~~~

.. cmdoption:: 1

  output CML1 (rather than CML2)

.. cmdoption:: a

  output array format for atoms and bonds

.. cmdoption:: A

  write aromatic bonds as such, not Kekule form

.. cmdoption:: h

  use hydrogenCount for all hydrogens

.. cmdoption:: m

  output metadata

.. cmdoption:: x

  omit XML and namespace declarations

.. cmdoption:: c

  continuous output: no formatting

.. cmdoption:: p

  output properties

.. cmdoption:: N<prefix>

  add namespace prefix to elements
Comments
~~~~~~~~

In the absence of hydrogenCount and any explicit hydrogen on an atom, implicit hydrogen is assumed to be present appropriate to the radical or spinMultiplicity attributes on the atom or its normal valency if they are not present. 

