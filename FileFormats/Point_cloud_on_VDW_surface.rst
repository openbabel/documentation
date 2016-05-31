.. _Point_cloud_on_VDW_surface:

Point cloud on VDW surface (pointcloud)
=======================================

**Generates a point cloud on the VDW surface around the molecule**


The surface location is calculated by adding the probe atom radius
(if specified) to the Van der Waal radius of the particular atom multipled
by the specified multiple (1.0 if unspecified).Output is a list of {x,y,z} tuples in Angstrom. Alternatively, if the ``x``
option is specified, the :ref:`XYZ_cartesian_coordinates_format` is used
instead.



.. note:: This is a write-only format.

Write Options
~~~~~~~~~~~~~ 

-r <radii>  *create a surface for each VDS radius (default 1.0)*

        A comma-separated list of VDW radius multiples
-d <densities>  *for each surface, specify the point density (default 1.0 Angstrom^2)*

        A comma-separated list of densities
-p <radius>  *radius of the probe atom in Angstrom (default 0.0)*
-x  *output in xyz format*


