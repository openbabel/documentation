.. _MDL_MOL_format:

MDL MOL format (mol, mdl, sdf, sd)
==================================

**Reads and writes V2000 and V3000 versions**




Read Options
~~~~~~~~~~~~ 

-s  *determine chirality from atom parity flags*

       The default setting is to ignore atom parity and
       work out the chirality based on the bond
       stereochemistry.
-T  *read title only*
-P  *read title and properties only*

       When filtering an sdf file on title or properties
       only, avoid lengthy chemical interpretation by
       using the ``T`` or ``P`` option together with the
       :ref:`copy format <Copy_raw_text>`.

Write Options
~~~~~~~~~~~~~ 

-3  *output V3000 not V2000 (used for >999 atoms/bonds)*
-m  *write no properties*
-w  *use wedge and hash bonds from input (2D only)*
-A  *output in Alias form, e.g. Ph, if present*


