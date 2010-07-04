.. _InChI_format:

InChI format (inchi)
====================

**IUPAC/NIST molecular identifier**

Experimental InChI read support was added in version 2.1,
although this does not always support stereochemistry.



Read Options
~~~~~~~~~~~~ 

-X <Option string>  *List of InChI options*
-n  *molecule name follows InChI on same line*
-a  *add InChI string to molecule name*


Write Options
~~~~~~~~~~~~~ 

-X <Option string>  *List of additional InChI options*
-t  *add molecule name*
-a  *output auxilliary information*
-K  *output InChIKey*
-w  *don't warn on undef stereo or charge rearrangement*
-l  *display InChI log*
-u  *output only unique molecules*
-U  *output only unique molecules and sort them*
-e  *compare first molecule to others*
-T <param>  *truncate InChI, /nostereo etc.*


Comments
~~~~~~~~
Currently the output is standard InChI only. InChI options may be
reintroduced later.

The InChI options should be space delimited in a single quoted string.
See InChI documentation for possible options.

Truncation parameters used with -xT:

/formula   formula only
/connect   formula and connectivity only
/nostereo  ignore E/Z and sp3 stereochemistry
/sp3       ignore sp3 stereochemistry
/noEZ      ignore E/Z steroeochemistry
/nochg     ignore charge and protonation
/noiso     ignore isotopes

