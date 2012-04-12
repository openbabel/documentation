.. _The_LAMMPS_data_format:

The LAMMPS data format (lmpdat)
===============================
.. note:: This is a write-only format.

Write Options
~~~~~~~~~~~~~ 

-q <water-model>  *Set atomic charges for water:*

      SPC (default), SPCE
-d <length>  *Set the lenght of the boundary box*

    around the molecule.
    The default is to make a cube around the molecule
    adding 50% to the most positive and negative
    cartesian coordinate.
