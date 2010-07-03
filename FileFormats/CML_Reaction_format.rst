CML Reaction format (cmlr)
==========================

**A minimal implementation of the CML Reaction format**

This implementation uses libxml2.


Write Options
~~~~~~~~~~~~~

.. cmdoption:: 1

  output CML1 (rather than CML2)

.. cmdoption:: a

  output array format for atoms and bonds

.. cmdoption:: l

  molecules NOT in MoleculeList

.. cmdoption:: h

  use hydrogenCount for all hydrogens

.. cmdoption:: x

  omit XML declaration

.. cmdoption:: r

  omit rate constant data

.. cmdoption:: N<prefix>

  add namespace prefix to elements

.. cmdoption:: M

  add obr prefix on non-CMLReact elements

.. cmdoption:: p

  add properties to molecules
Comments
~~~~~~~~
The implementation of this format which reads and writes to and from
OBReaction objects is fairly minimal at present. (Currently the only
other reaction format in OpenBabel is RXN.) During reading, only the
elements <reaction>, <reactant>, <product> and <molecule>  are acted
upon (the last through CML). The molecules can be collected together
in a list at the start of the file and referenced in the reactant and
product via e.g. <molecule ref="mol1">.

On writing, the list format can be specified with the -xl option. The
list containers are <moleculeList> and <reactionList> and the overall
wrapper is <mechanism>. These are non-standard CMLReact element names
and would have to be changed (in the code) to <list>,<list> and <cml>
if this was unacceptable.

