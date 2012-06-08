.. _The_LAMMPS_data_format:

The LAMMPS data format (lmpdat)
===============================
LAMMPS is a classical molecular dynamics code, and an acronym for
Large-scale Atomic/Molecular Massively Parallel Simulator.



.. note:: This is a write-only format.

Write Options
~~~~~~~~~~~~~ 

-q <water-model>  *Set atomic charges for water.*

    There are two options: SPC (default) or SPCE
-d <length>  *Set the length of the boundary box around the molecule.*

    The default is to make a cube around the molecule
    adding 50% to the most positive and negative
    cartesian coordinate.
