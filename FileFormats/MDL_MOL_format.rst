.. _MDL_MOL_format:

MDL MOL format (mol, mdl, sdf, sd)
==================================

**Reads and writes V2000 and V3000 versions**


Open Babel supports an extension to the MOL file standard
that allows cis/trans and tetrahedral stereochemistry to be
stored in 0D MOL files. The tetrahedral stereochemistry is
stored as the atom parity, while the cis/trans stereochemistry
is stored using Up and Down bonds similar to how it is
represented in a SMILES string. Use the ``S`` option
when reading or writing if you want to avoid storing
or interpreting stereochemistry in 0D MOL files.



Read Options
~~~~~~~~~~~~ 

-s  *determine chirality from atom parity flags*

       The default setting for 2D and 3D is to ignore atom parity and
       work out the chirality based on the bond
       stereochemistry (2D) or coordinates (3D).
       For 0D the default is already to determine the chirality
       from the atom parity.
-S  *do not read stereochemistry from 0D MOL files*

       Open Babel supports reading and writing cis/trans
       and tetrahedral stereochemistry to 0D MOL files.
       This is an extension to the standard which you can
       turn off using this option.
-T  *read title only*
-P  *read title and properties only*

       When filtering an sdf file on title or properties
       only, avoid lengthy chemical interpretation by
       using the ``T`` or ``P`` option together with the
       :ref:`copy format <Copy_raw_text>`.

Write Options
~~~~~~~~~~~~~ 

-3  *output V3000 not V2000 (used for >999 atoms/bonds)*
-a  *write atomclass if available*
-m  *write no properties*
-w  *use wedge and hash bonds from input (2D only)*
-S  *do not store cis/trans stereochemistry in 0D MOL files*
-A  *output in Alias form, e.g. Ph, if present*
-H  *use HYD extension (always on if mol contains zero-order bonds)*


