.. _Crystallographic_Information_File:

Crystallographic Information File (cif)
=======================================

**The CIF file format is the standard interchange format for small-molecule crystal structures**


Fractional coordinates are converted to cartesian ones using the following convention:

- The x axis is parallel to a
- The y axis is in the (a,b) plane
- The z axis is along c*

Ref: Int. Tables for Crystallography (2006), vol. B, sec 3.3.1.1.1
  (the matrix used is the 2nd form listed)



Read Options
~~~~~~~~~~~~ 

-v  *Verbose CIF conversion*
-s  *Output single bonds only*
-b  *Disable bonding entirely*
-B  *Use bonds listed in CIF file from _geom_bond_etc records (overrides option b)*


