Babel - Convert, Filter and Manipulate Chemical Data
====================================================

Synopsis
--------

``<b>babel</b> [<b>-H</b> <i>help-options</i>]``

``<b>babel</b> [<i>OPTIONS</i>] [<b>-i</b> <i>input-type</i>] <i>infile</i> [<b>-o</b> <i>output-type</i>] <i>outfile</i>``

Description
-----------

Babel is a cross-platform program designed to interconvert between
many file formats used in molecular modeling and computational
chemistry and related areas.

Open Babel is also a complete programmers toolkit for developing
chemistry software. For more information, se the Open Babel web
pages <**`http://openbabel.org/ <http://openbabel.org/>`_**>.

Options
-------

If only input and ouput files are given, Open Babel will guess the
file type from the
`filename extension </wiki/List_of_extensions>`_.

**-a** *options* 
    Format-specific input options. See **-H** *format-ID* for options
    allowed by a particular format
**--addtotitle** 
    Append text after the current molecule title
**--addformula** 
    Append the molecular formula after the current molecule title
**--append** *property list* 
    Append properties values to the current molecule title. For more
    information, see `append </wiki/--append>`_.
**-b** 
    Convert dative bonds (e.g., ``[N+]([O-])=O`` to ``N(=O)=O``
**-c** 
    Center atomic coordinates at (0,0,0)
**-C** 
    Combine molecules in first file with others having the same name
**-d** 
    Delete Hydrogens
**-e** 
    Continue to convert molecules after errors
**---errorlevel** *2* 
    Filter the level of errors and warnings displayed:
    
    -  1 = critical errors only
    -  2 = include warnings too (**default**)
    -  3 = include informational messages too
    -  4 = include "audit log" messages of changes to data
    -  5 = include debugging messages too


**-f** *#* 
    For multiple entry input, start import with molecule # as the first
    entry
**-F** 
    Output the available fingerprint types
**--filter** *criteria* 
    Filter based on molecular properties. See
    `filter </wiki/--filter_option>`_ for examples and a list of
    criteria.
**-h** 
    Add hydrogens
**-H** 
    Output usage information
**-H** *format-ID* 
    Output formatting information and options for
    `format </wiki/Category:Formats>`_ specified
**-Hall** 
    Output formatting information and options for all
    `formats </wiki/Category:Formats>`_
**-i<format-ID>** 
    Specifies input format, see below for the available
    `formats </wiki/Category:Formats>`_
**-j** **--join** 
    Join all input molecules into a single output molecule entry
**-k** 
    Translate computational chemistry modeling keywords (e.g.,
    `GAMESS </w/index.php?title=GAMESS&action=edit&redlink=1>`_ and
    `Gaussian </w/index.php?title=Gaussian&action=edit&redlink=1>`_)
**-m** 
    Produce multiple output files, to allow:
    
    -  Splitting one input file - put each molecule into consecutively
       numbered output files
    -  Batch conversion - convert each of multiple input files into a
       specified output format


**-l** *#* 
    For multiple entry input, stop import with molecule # as the last
    entry
**-o** *format-ID* 
    Specifies output format, see below for the available
    `formats </wiki/Category:Formats>`_
**-p** *pH* 
    Add Hydrogens appropriate for pH (use transforms in phmodel.txt)
**--property** 
    Add or replace a property (e.g., in an
    `MDL SD </w/index.php?title=MDL_SD&action=edit&redlink=1>`_ file)
**-s** *`SMARTS </wiki/SMARTS>`_* 
    Convert only molecules matching the `SMARTS </wiki/SMARTS>`_
    pattern specified
**--separate** 
    Separate disconnected fragments into individual molecular records
**-t** 
    All input files describe a single molecule
**--title** *title* 
    Add or replace molecular title
**-x** *options* 
    Format-specific output options. See **-H** *format-ID* for options
    allowed by a particular format
**-v** *`SMARTS </wiki/SMARTS>`_* 
    Convert only molecules **NOT** matching `SMARTS </wiki/SMARTS>`_
    pattern specified
**-V** 
    Output version number and exit
**-z** 
    Compress the output with gzip

File Formats
------------

For information on the file formats supported by Open Babel, please see :ref:`file formats`.

Format Options
--------------

Individual file formats may have additional formatting options.

Input format options are preceded by ‘a’, e.g. -as

Output format options are preceded by ‘x’, e.g. -xn

For further specific information and options, use -H<format-type>
e.g., -Hcml

Examples
--------

Standard conversion:

::

    babel -ixyz ethanol.xyz -opdb ethanol.pdb

Conversion from a SMI file in STDIN to a Mol2 file written to
STDOUT:

::

    babel -ismi -omol2

Split a multi-molecule file into new1.smi, new2.smi, etc.:

::

    babel infile.mol new.smi -m
