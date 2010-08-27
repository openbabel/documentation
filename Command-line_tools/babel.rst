babel and obabel - Convert, Filter and Manipulate Chemical Data
===============================================================

:command:`babel` and :command:`obabel` are cross-platform programs designed to interconvert between many file formats used in molecular modeling and computational chemistry and related areas. They can also be used for filtering molecules and for simple manipulation of chemical data.

Synopsis
--------

.. hlist::

   * ``babel [-H <help-options>]``
   * ``obabel [-H <help-options>]`` 
   * ``babel  [-i <input-ID>] infile [-o <output-ID>] [outfile] [OPTIONS]``
   * ``obabel [-i <input-ID>] infile [-o <output-ID>] [-O outfile] [OPTIONS]``

:command:`obabel` is recommended over :command:`babel` (see :ref:`babel vs obabel`).

.. _babel options:

Options
-------

.. rubric:: Information and help

*  ``babel  [-H <help-options>]``
*  ``obabel [-H <help-options>]``

-H 
    Output usage information
-H <format-ID> 
    Output formatting information and options for
    the format specified
-Hall 
    Output formatting information and options for all
    formats
-L  
    List plugin types (formats, descriptors, ops, etc.)
-L <plugin type>
    List plugins of this type
-L <plugin-ID>
    Details of a plugin of any type
-V 
    Output version number

.. rubric:: Conversion options

* ``babel  [-i <input-ID>] infile [-o <output-ID>] [outfile] [OPTIONS]``
* ``obabel [-i <input-ID>] infile [-o <output-ID>] [-O outfile] [OPTIONS]`` 

.. note::

  If only input and output files are given, Open Babel will guess the file type from the filename extension. For information on the file formats supported by Open Babel, please see :ref:`file formats`.

-a <options>
    Format-specific input options. See ``-H <format-ID>`` for options
    allowed by a particular format
--add <list>
    Add properties (for SDF, CML, etc.) from descriptors in list
--addindex
    Append output index to title
--addtotitle <text>
    Append the text after the each molecule title
--append <list> 
    Append properties or descriptor values appropriate for a molecule to its title. For more
    information, see :ref:`append option`.
-b 
    Convert dative bonds (e.g. ``[N+]([O-])=O`` to ``N(=O)=O``)
-c 
    Center atomic coordinates at (0,0,0)
-C 
    Combine molecules in first file with others having the same name
-d 
    Delete hydrogens (make all hydrogen implicit)
--delete <list> 
    Delete properties in list
-e 
    Continue to convert molecules after errors
--errorlevel <N>
    Filter the level of errors and warnings displayed:
    
    -  1 = critical errors only
    -  2 = include warnings too (**default**)
    -  3 = include informational messages too
    -  4 = include "audit log" messages of changes to data
    -  5 = include debugging messages too

-f <#> 
    For multiple entry input, start import with molecule # as the first
    entry
--filter <criteria> 
    Filter based on molecular properties. See
    :ref:`filter options` for examples and a list of
    criteria.
--gen2d 
    Generate 2D coordinates
--gen3d 
    Generate 3D coordinates
-h 
    Add hydrogens (make all hydrogen explicit)
-i <format-ID> 
    Specifies input format. See :ref:`file formats`.
-j, --join 
    Join all input molecules into a single output molecule entry
-k 
    Translate computational chemistry modeling keywords (e.g.,
    `GAMESS </w/index.php?title=GAMESS&action=edit&redlink=1>`_ and
    `Gaussian </w/index.php?title=Gaussian&action=edit&redlink=1>`_)
-m 
    Produce multiple output files, to allow:    

    -  Splitting one input file - put each molecule into consecutively
       numbered output files
    -  Batch conversion - convert each of multiple input files into a
       specified output format
-l <#> 
    For multiple entry input, stop import with molecule # as the last
    entry
-o <format-ID> 
    Specifies output format. See :ref:`file formats`.
-p <pH> 
    Add hydrogens appropriate for pH (use transforms in phmodel.txt)
--property <name  value>
    Add or replace a property (for example, in an SD file, :ref:`MDL_MOL_format`)
-r 
    Remove all but the largest contiguous fragment (strip salts)
--readconformers
    Combine adjacent conformers in multi-molecule input into a single molecule
-s <SMARTS> 
    Convert only molecules matching the SMARTS pattern specified
-s <filename.xxx>
    Convert only molecules with the molecule in the file as a substructure
--separate 
    Separate disconnected fragments into individual molecular records
--sort
    Output molecules ordered by the value of a descriptor. See :ref:`sorting option`.
--title <title> 
    Add or replace molecular title
--unique, --unique <param>
    Do not convert duplicate molecules. See :ref:`removing duplicates`.
--writeconformers 
    Output multiple conformers as separate molecules
-x <options> 
    Format-specific output options. See ``-H <format-ID>`` for options
    allowed by a particular format
-v <SMARTS>
    Convert only molecules **NOT** matching the SMARTS pattern specified
-z 
    Compress the output with gzip (not on Windows)


Examples
--------

The examples below assume the files are in the current directory. Otherwise you may need to include the full path to the files e.g. :file:`/Users/username/Desktop/mymols.sdf` and you may need to put quotes around the filenames (especially in Windows when they can contain spaces).

Standard conversion::

    babel ethanol.xyz ethanol.pdb

Conversion if the files do not have an extension that describes their format::
  
    babel -ixyz ethanol.aa -opdb ethanol.bb

Molecules from multiple input files (which can have different formats) are normally combined in the output file:: 

    babel ethanol.xyz acetal.sdf benzene.cml allmols.smi

Conversion from a SMI file in STDIN to a Mol2 file written to STDOUT::

    babel -ismi -omol2

Split a multi-molecule file into new1.smi, new2.smi, etc.::

    babel infile.mol new.smi -m

In Windows this can also be written::

    babel infile.mol new*.smi

Multiple input files can be converted in batch format too. To convert all files ending in .xyz (\*.xyz) to PDB files, you can type::

    babel *.xyz -opdb -m

Open Babel will not generate coordinates unless asked, so while a conversion from SMILES to SDF will generate a valid SDF file, the resulting file will not contain coordinates. To generate coordinates, use either the ``--gen3d`` or  the ``--gen2d`` option::

     babel infile.smi out.sdf --gen3d

If you want to remove all hydrogens, i.e. make them all implicit, when doing the conversion the command would be::

     babel mymols.sdf -osmi outputfile.smi -d

If you want to add hydrogens, i.e. make thenm all explicit, when doing the conversion the command would be::

     babel  mymols.sdf outputfile.smi  -h

If you want to add hydrogens appropriate for pH7.4 when doing the conversion the command would be::

     babel  mymols.sdf outputfile.smi' -p

The protonation is done an atom-by-atom basis so molecules with multiple ionizable centers will have all centers ionized.

Of course you don't actually need to change the file type to modify the hydrogens. If you want to add all hydrogens the command would be::

     babel  mymols.sdf mymols_H.sdf -h

Some functional groups e.g. nitro or sulphone can be represented either as ``[N+]([O-])=O`` or ``N(=O)=O``. To convert all to the dative bond form::

     babel  mymols.sdf outputfile.smi  -b

If you only want to convert a subset of molecules you can define them using -f and -l, so to convert molecules 2-4 of the file mymols.sdf type::

     babel  mymols.sdf -f 2 -l 4 -osdf  outputfile.sdf 

Alternatively you can select a subset matching a SMARTS pattern, so to select all molecules containing bromobenzene use::

     babel   mymols.sdf   selected.sdf  -s "c1ccccc1Br"

You can select a subset that do not match a SMARTS pattern, so to select all molecules not containing bromobenzene use::

     babel   mymols.sdf   selected.sdf    -v "c1ccccc1Br"

You can of course combine options, so to join molecules and add hydrogens type::

     babel   mymols.sdf  myjoined.sdf -h   -j

Files compressed with gzip are read transparently, whether or not they have a .gz suffix::

     babel  compressed.sdf.gz  expanded.smi

On platforms other than Windows, the output file can be compressed with gzip, but note if you don't specify the ".gz" suffix it will not be added automatically, which could cause problems when you try to open the file::

     babel   mymols.sdf  outputfile.sdf.gz   -z

.. _babel vs obabel:

Differences between babel and obabel
------------------------------------

Essentially :command:`obabel` is a modern version of :command:`babel` with additional capabilities and a more standard interface. Over time, :command:`obabel` will replace :command:`babel` and so we recommend that you start using :command:`obabel` now. 

Specifically, the differences are as follows:

* :command:`obabel` requires that the output file be specified with a ``-O`` option. This is closer to the normal Unix convention for commandline programs, and prevents users accidentally overwriting the input file.

* :command:`obabel` is more flexible when the user needs to specify parameter values on options. For instance,  the ``--unique`` option can be used with or without a parameter (specifying the criteria used).  With :command:`babel`, this only works when the option is the last on the line; with :command:`obabel`, no such restriction applies. Because of the original design of :command:`babel`, it is not possible to add this capability in a backwards-compatible way.

* :command:`obabel` has a shortcut for entering SMILES strings. Preceed the SMILES by -: and use in place of an input file. For example::

     obabel -:O=C(O)c1ccccc1OC(=O)C -ocan

More than one can be used, and a molecule title can be included if enclosed in quotes::

     obabel "-:O=C(O)c1ccccc1OC(=O)C aspirin" "-:Oc1ccccc1C(=O)O salicylic acid" -ofpt
 
* :command:`obabel` cannot use concatenated single-character options. 

.. tip::

    To adapt a command line for :command:`babel` into one for :command:`obabel` you can usually simply put ``-O`` in front of the output filename.

Format Options
--------------

Individual file formats may have additional formatting options. These are listed in the documentation for the individual formats (see :ref:`file formats`) or can be shown using the ``-H <format-Id>`` option, e.g. ``-H cml``.

To use these additional options, input format options are preceded by ``-a``, e.g. ``-as``. Output format options, which are much more common, are preceded by ``-x``, e.g. ``-xn``. So to read the 2D coordinates rather than a from a molecule in a CML file and display it on a blackground::

      babel mymol.cml out.svg -a2 -xb

.. _append option:

Append property values to the title
-----------------------------------

The command line option ``--append`` adds extra information to the title of the molecule.

The information can be calculated from the structure of the molecule or can originate from a property attached to the molecule, usually from an sdf or cml input file. It is used as follows::

 babel infile.sdf -osmi --append "MW CAT_NO"

``MW`` is the ID of a descriptor which calculates the molecular weight of the molecule, and ``CAT_NO`` is a property of the molecule from the sdf input file. The values of these are added to the title of the molecule. For input files with many molecules these additions are specific to each molecule. (The option ``--addtotitle`` adds the same text to every title.)

The append option only takes one parameter, which means that all of the descriptor IDs or property names must be enclosed together in a single set of quotes.

If the name of the property in the sdf file (internally the Attribute in OBPairData) contains spaces, these spaces should be replaced by underscore characters, '_'. So the example above would also work for a property named ``CAT NO``.

By default, the extra items are added to the title separated by spaces. But if the first character in the parameter is a whitespace or punctuation character other than '_', it is used as the separator instead. In the GUI, because tab is used to move between controls, if a tab character was required it would have to be pasted in. 

.. _filter options:

Filtering molecules from a multimolecule file
---------------------------------------------

Five of the options above can be used to filter molecules:

* ``-s`` - convert molecules that match a SMARTS string
* ``-v`` - convert molecules that don't match a SMARTS string
* ``-f`` and ``-l`` - convert molecules in a certain range
* ``--filter`` - convert molecules that meet specified chemical (and other) criteria

This section focuses on the ``--filter`` option, which is very versatile and can select a subset of molecules based either on properties imported with the molecule (as from a SDF file) or from calculations made by Open Babel on the molecule.

The aim has been to make the option flexible and intuitive to use; don't be put off by the long description.

You use it like this::

  babel filterset.sdf -osmi --filter "MW<130 ROTATABLE_BOND > 2"

It takes one parameter which probably needs to be enclosed in double quotes to avoid confusing the shell or operating system. (You don't need the quotes with the Windows GUI.) It contains one or more conditional tests. By default, these have all to be true for the molecule to be converted. As well as this implicit AND behaviour, you can write a full Boolean expression, see below. As you can see, there can be spaces or not in sensible places and the conditional tests could be separated by a comma or semicolon.

You can filter on two types of property:

* An SDF property, as the identifier ROTATABLE_BOND could be. There is no need for it to be previously known to OpenBabel.
* An ID of an OBDescriptor object. This is a plug-in class so that new objects can easily be added. MW is the ID of a descriptor which calculates molecular weight. You can see a list of available descriptors by::

    babel -L descriptors

  or from a menu item in the GUI.

.. sidebar:: Faster filtering

  Open Babel provides a number of utility file formats (see :ref:`file formats`). Of these, using the *copy format* as the output format is particularly useful when filtering (see :ref:`Copy_raw_text`). This copies the content of the molecular file directly from input to output. If you are not converting the molecules between different formats, this procedure is much faster and avoids any possibility of information loss.

  In addition, if you are converting SDF files and are filtering based on the title, you should consider using ``-aT`` (see :ref:`MDL_MOL_format`). Rather than perceiving the chemistry of the entire molecule, this option will only read in the title.

The descriptor names are case-insensitive. With the property names currently, you need to get the case right. Both types of identifier can contain letters, numbers and underscores, '_'. Properties can contain spaces, but then when writing the name in the filter parameter, you need to replace them with underscores. So in the example above, the test would also be suitable for a property 'ROTATABLE BOND'.

OpenBabel uses a SDF-like property (which is held internally in the class OBPairData) in preference to a descriptor if one exists in the molecule. So with the example file, which can be found here::

  babel filterset.sdf -osmi --filter "logP>5"

converts only a molecule with a property logP=10.900, since the others do not have this property and logP, being also a descriptor, is calculated and is always much less than 5.

If a property does not have a conditional test, then it returns true only if it exists. So::

  babel filterset.sdf -osmi --filter "ROTATABLE_BOND MW<130"

converts only those molecules with a ROTATABLE_BOND property and a molecular weight less than 130. If you wanted to also include all the molecules without ROTATABLE_BOND defined, use::

  babel filterset.sdf -osmi --filter "!ROTATABLE_BOND || (ROTATABLE_BOND & MW<130)"

The ! means negate. AND can be & or &&, OR can be | or ||. The brackets are not strictly necessary here because & has precendent over | in the normal way. If the result of a test doesn't matter, it is parsed but not evaluated. In the example, the expression in the brackets is not evaluated for molecules without a ROTATABLE_BOND property. This doesn't matter here, but if evaluation of a descriptor involved a lot of computation, it would pay to include it late in the boolean expression so that there is a chance it is skipped for some molecules.

Descriptors must have a conditional test and it is an error if they don't. The default test, as used by MW or logP, is a numerical one, but the parsing of the text, and what the test does is defined in each descriptor's code (a virtual function in the OBDescriptor class). Three examples of this are described in the following sections.

String descriptors
~~~~~~~~~~~~~~~~~~

::

  babel filterset.sdf -osmi --filter "title='Ethanol'"

The descriptor, title, when followed by a string, here enclosed by single quotes, does a case-sensitive string comparison. ('ethanol' wouldn't match anything in the example file.) The comparison does not have to be just equality::

  babel filterset.sdf -osmi --filter "title>='D'"

converts molecules with titles Dimethyl Ether and Ethanol in the example file.

It is not always necessary to use the single quotes when the meaning is unambiguous: the two examples above work without them. But a numerical, rather than a string, comparison is made if both operands can be converted to numbers. This can be useful::

  babel filterset.sdf -osmi --filter "title<129"

will convert the molecules with titles 56 123 and 126, which is probably what you wanted.

::

  babel filterset.sdf -osmi --filter "title<'129'"

converts only 123 and 126 because a string comparison is being made.

String comparisons can use * as a wildcard. It can only be used as the first or last character of the string. So ``--filter "title='*ol'`` will match molecules with titles 'methanol', 'ethanol' etc. and ``--filter "title='eth*'`` will match 'ethanol', 'ethyl acetate', 'ethical solution' etc.

SMARTS descriptor
~~~~~~~~~~~~~~~~~

This descriptor will do a SMARTS test (substructure and more) on the molecules. The smarts ID can be abreviated to s and the = is optional. More than one SMARTS test can be done::

  babel filterset.sdf -osmi --filter "s='CN' s!='[N+]'"

This provides a more flexible alternative to the existing ``-s`` and ``-v`` options, since the descriptor versions can be combined with other tests.

InChI descriptor
~~~~~~~~~~~~~~~~

::

  babel filterset.sdf -osmi --filter "inchi='InChI=1/C2H6O/c1-2-3/h3H,2H2,1H3'"

will convert only ethanol. It uses the default parameters for InChI comparison, so there may be some messages from the InChI code. There is quite a lot of flexibility on how the InChI is presented (you can miss out the non-essential bits)::

  babel filterset.sdf -osmi --filter "inchi='1/C2H6O/c1-2-3/h3H,2H2,1H3'"
  babel filterset.sdf -osmi --filter "inchi='C2H6O/c1-2-3/h3H,2H2,1H3'"
  babel filterset.sdf -osmi --filter "inchi=C2H6O/c1-2-3/h3H,2H2,1H3"
  babel filterset.sdf -osmi --filter "InChI=1/C2H6O/c1-2-3/h3H,2H2,1H3"

all have the same effect.

The comparison of the InChI string is done only as far as the parameter's length. This means that we can take advantage of InChI's layered structure::

  babel filterset.sdf -osmi --filter "inchi=C2H6O"

will convert both Ethanol and Dimethyl Ether. 

Substructure and similarity searching
-------------------------------------

For information on using :command:`babel` for substructure searching and similarity searching, see :ref:`fingerprints`.

.. _sorting option: 

Sorting molecules
-----------------

The ``--sort`` option is used to output molecules ordered by the value of a descriptor::

 babel  infile.xxx  outfile.xxx  --sort desc

If the descriptor desc provides a numerical value, the molecule with the smallest value is output first. For descriptors which provide a string output the order is alphabetical, but for the inchi descriptor a more chemically informed order is used (e.g. "CH4" is before than "C2H6", "CH4" is less than "ClH" hydrogen chloride).

The order can be reversed by preceding the descriptor name with ``~``, e.g.::

 babel  infile.xxx  outfile.yyy  --sort ~logP

As a shortcut, the value of the descriptor can be appended to the molecule name by adding a ``+`` to the descriptor, e.g.::

 babel  aromatics.smi  -osmi  --sort ~MW+
  c1ccccc1C=C	styrene 104.149
  c1ccccc1C	toluene 92.1384
  c1ccccc1	benzene 78.1118

.. _removing duplicates:

Remove duplicate molecules
---------------------------

The ``--unique`` option is used to remove, i.e. not output, any chemically identical molecules during conversion::

 babel  infile.xxx  outfile.yyy  --unique [param]

The optional parameter param defines what is regarded as "chemically identical". It can be the name of any descriptor, although not many are likely to be useful. If param is omitted, the InChI descriptor is used. Other useful descriptors are 'cansmi' and 'cansmiNS' (canonical SMILES, with and without stereochemical information),'title' and truncated InChI, see below.

Note that if you want to use ``--unique`` without a parameter with :command:`babel`, it needs to be last on the line. With the alternative commandline interface, :command:`obabel`, it can be anywhere after the output file.

A message is output for each duplicate found::

      Removed methyl benzene - a duplicate of toluene (#1)

Clearly, this is more useful if each molecule has a title. The (#1) is the number of duplicates found so far.

If you wanted to identify duplicates but not output the unique molecules, you could use nulformat::

 babel  infile.xxx  -onul  --unique    

Truncated InChI
~~~~~~~~~~~~~~~

It is possible to relax the criterion by which molecules are regarded as "chemically identical" by using a truncated InChI specification as param. This takes advantage of the layered structure of InChI. So to remove duplicates, treating stereoisomers as the same molecule::

 babel  infile.xxx  outfile.yyy  --unique /nostereo

Truncated InChI specifications start with '/' and are case-sensitive. param can be a concatenation of these e.g. /nochg/noiso ::

 /formula   formula only
 /connect   formula and connectivity only
 /nostereo  ignore E/Z and sp3 stereochemistry
 /nosp3     ignore sp3 stereochemistry
 /noEZ      ignore E/Z stereoochemistry
 /nochg     ignore charge and protonation
 /noiso     ignore isotopes

Multiple files
~~~~~~~~~~~~~~

The input molecules do not have to be in a single file. So to collect all the unique molecules from a set of mol files::

 babel  *.mol  uniquemols.sdf  --unique

If you want the unique molecules to remain in individual files::

 babel  *.mol  U.mol  -m  --unique

On the GUI use the form::

 babel  *.mol  U*.mol  --unique

Either form is acceptable on the Windows command line.

The unique molecules will be in files with the original name prefixed by 'U'. Duplicate molecules will be in similar files but with zero length, which you will have to delete yourself.

Aliases for chemical groups
---------------------------------

There is a limited amount of support for representing common chemical groups by an alias, e.g. benzoic acid as ``Ph-COOH``, with two alias groups. Internally in Open Babel, the molecule usually has a 'real' structure with the alias names present as only an alternative representation. For MDL mol and sd files alias names can be read from or written to an 'A' line. The more modern RGroup representations are not yet recognized. Reading is transparent; the alias group is expanded and the 'real' atoms given reasonable coordinates if the the molecule is 2D or 3D. Writing in alias form, rather than the 'real' structure, requires the use the ``-xA`` option.  SVGFormat will also display any aliases present in a molecule if the ``-xA`` option is set.

The alias names that are recognized are in the file :file:`superatoms.txt` which can be edited.

Normal molecules can have certain common groups given alternative alias representation using the ``--genalias`` option. The groups that are recognized and converted are a subset of those that are read. Displaying or writing them still requires the ``-xA`` option. For example, if :file:`aspirin.smi` contained ``O=C(O)c1ccccc1OC(=O)C``, it could be displayed with the  aliases ``COOH`` and ``OAc`` by::

  obabel aspirin.smi  -O out.svg  --genalias  -xA 
  

 

