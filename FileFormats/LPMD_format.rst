.. _LPMD_format:

LPMD format (lpmd)
==================

**Read and write LPMD's atomic configuration file**




Read Options
~~~~~~~~~~~~ 

-s  *Output single bonds only*
-b  *Disable bonding entirely*


Write Options
~~~~~~~~~~~~~ 


   f# Indicate the level of the ouput file 0 (default), 1 or 2.
   m# Indicate the mode if ``-xl 1`` is used
        0 (default) is for accelerations and 1 for forces.
   c <vectorcells> Set the cell vectors if not present
        Example: ``-xc 10.0,0,0,0.0,10.0,0.0,0.0,0.0,20.0``
   e Add the charge to the output file

