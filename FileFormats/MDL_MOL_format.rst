.. _MDL_MOL_format:

MDL MOL format (mol, mdl, sdf, sd)
==================================

**Reads and writes V2000 and V3000 versions**

Read Options
~~~~~~~~~~~~ 

-s  *determine chirality from atom parity flags*

       This is valid only for 0D information. Atom
       parity is always ignored on reading for MOL files
       containing 2D or 3D information.
-T  *read title only*
-P  *read title and properties only*

       When filtering an sdf file on title or properties
       only, avoid lengthy chemical interpretation by
       using the T or P option together with copy format.

Write Options
~~~~~~~~~~~~~ 

-3  *output V3000 not V2000 (used for >999 atoms/bonds)*
-m  *write no properties*
-w  *recalculate wedge and hash bonds(2D structures only)*
-A  *output in Alias form, e.g. Ph, if present*


