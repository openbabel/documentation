Molecular Mechanics and Force Fields
=======================

Used by a number of features, such as 3D coordinate generation,
conformer searching, etc., Open Babel provides support for a variety
of all-atom molecular mechanics force fields. The key idea is to use
classical mechanics to rapidly simulate molecular systems.

Each force field method is parameterized for a set of possible
molecules (e.g., proteins, organic molecules, etc.), building in
assumptions about how various aspects of the molecules contribute to
the overall potential energy.

The total potential energy of the system is usually given as a sum of
multiple components, including some or all of (but not limited to):
  * Bond stretching
  * Angle bending
  * Dihedral torsions
  * Out-of-plane bending
  * Van der Waals repulsion
  * Atomic partial charges (electrostatic)

Open Babel supports several force field methods. In general, we
recommend use of either the :ref:`Generalized_Amber_Force_Field` or
:ref:`MMFF94_Force_Field` for organic molecules, and the
:ref:`Universal_Force_Field` for other types of molecules.


.. toctree::

   gaff.rst
   ghemical.rst
   mmff94.rst
   uff.rst
