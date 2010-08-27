.. _InChI_format:

InChI format (inchi)
====================

**IUPAC/NIST molecular identifier**




Read Options
~~~~~~~~~~~~ 

-X <Option string>  *List of InChI options*
-n  *molecule name follows InChI on same line*
-a  *add InChI string to molecule name*


Write Options
~~~~~~~~~~~~~ 


    Standard InChI is written unless certain InChI options are used

-K  *output InChIKey only*
-t  *add molecule name after InChI*
-w  *ignore less important warnings*

    These are:
    'Omitted undefined stereo'
    'Charges were rearranged'
    'Proton(s) added/removed'
    'Metal was disconnected'
-a  *output auxilliary information*
-l  *display InChI log*

    **Uniqueness options** (see also ``--unique`` and ``--sort`` which are more versatile)
-u  *output only unique molecules*
-U  *output only unique molecules and sort them*
-e  *compare first molecule to others*

    This can also be done with :ref:`InChICompare format <Compare_molecules_using_InChI>`::

      babel first.smi second.mol third.cml -ok

-T <param>  *truncate InChI according to various parameters*

    See below for possible truncation parameters.
    These can be combined, e.g. ``/nochg/noiso``
-X <Option string>  *Additional InChI options*

    See InChI documentation.
    These options should be space delimited in a single quoted string.

    - Structure perception (compatible with stdInChI): ``NEWPSOFF``, ``DoNotAddH``, ``SNon``
    - Stereo interpretation (produces non-standard InChI): ``SRel``, ``SRac``,
      ``SUCF``, ``ChiralFlagON``, ``ChiralFlagOFF``
    - InChI creation options (produces non-standard InChI): ``SUU``, ``SLUUD``,
      ``FixedH``, ``RecMet``, ``KET``, ``15T``

    The following options are for convenience, e.g. ``-xF``
    but produce non-standard InChI.
-F  *include fixed hydrogen layer*
-M  *include bonds to metal*


Comments
~~~~~~~~
Truncation parameters used with ``-xT``:

/formula   formula only
/connect   formula and connectivity only
/nostereo  ignore E/Z and sp3 stereochemistry
/sp3       ignore sp3 stereochemistry
/noEZ      ignore E/Z steroeochemistry
/nochg     ignore charge and protonation
/noiso     ignore isotopes

