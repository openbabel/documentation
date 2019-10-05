.. _obabel:

obabel - Convert, Filter and Manipulate Chemical Data
=====================================================

:command:`obabel` is a command-line program for interconverting between many file formats used in molecular modeling and computational chemistry and related areas. It can also be used for filtering molecules and for simple manipulation of chemical data.

Synopsis
--------

.. hlist::

   * ``obabel [-H <help-options>]``
   * ``obabel [-i <input-ID>] infile [-o <output-ID>] [-O outfile] [OPTIONS]``

.. _babel options:

Options
-------

.. rubric:: Information and help

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
    List plugin types (``charges``, ``descriptors``, ``fingerprints``, ``forcefields``, ``formats``, ``loaders`` and ``ops``)
-L <plugin type>
    List plugins of this type. For example, ``obabel -L formats`` gives the list of file formats.
-L <plugin-ID>
    Details of a particular plugin (of any plugin type). For example, ``obabel -L cml`` gives details on the CML file format.
-V
    Output version number

.. rubric:: Conversion options

* ``obabel [-i <input-ID>] infile [-o <output-ID>] [-O outfile] [OPTIONS]``
* ``obabel -:"<text>"  [-i <input-ID>] [-o <output-ID>] [-O outfile] [OPTIONS]``

.. note::

  If only input and output files are given, Open Babel will guess the file type from the filename extension. For information on the file formats supported by Open Babel, please see :ref:`file formats`. If text is provided using the ``-:`` notation, SMILES are assumed by default if an input format is not specified.

-a <options>
    Format-specific input options. Use ``-H <format-ID>`` to see options
    allowed by a particular format, or see the appropriate section in
    :ref:`file formats`.
--add <list>
    Add properties (for SDF, CML, etc.) from descriptors in list. Use
    ``-L descriptors`` to see available descriptors.
--addfilename
    Add the input filename to the title.
--addinindex
    Append input index to title (that is, the index `before` any filtering)
--addoutindex
    Append output index to title (that is, the index `after` any filtering)
--addpolarh
    Like ``-h``, but only adds hydrogens to polar atoms.
--addtotitle <text>
    Append the text after each molecule title
--append <list>
    Append properties or descriptor values appropriate for a molecule to its title. For more
    information, see :ref:`append option`.
-b
    Convert dative bonds (e.g. ``[N+]([O-])=O`` to ``N(=O)=O``)
-c
    Center atomic coordinates at (0,0,0)
-C
    Combine molecules in first file with others having the same name
--canonical
    Canonicalize the atom order. If generating canonical SMILES, do not use
    this option. Instead use the :ref:`Canonical_SMILES_format`.
--conformer <options>
    Conformer searching to generate low-energy or diverse
    conformers. For more information, see :ref:`conformers`.
-d
    Delete hydrogens (make all hydrogen implicit)
--delete <list>
    Delete properties in list
-e
    Continue to convert molecules after errors
--energy <options>
     Forcefield energy evaluation. See :ref:`minimize option`.
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
--fillUC <param>
    For a crystal structure, add atoms to fill the entire unit cell based
    on the unique positions, the unit cell and the spacegroup. The parameter
    can either be ``strict`` (the default), which only keeps atoms inside the
    unit cell, or ``keepconnect``, which fills the unit cell but keeps the
    original connectivity.
--filter <criteria>
    Filter based on molecular properties. See
    :ref:`filter options` for examples and a list of
    criteria.
--gen2d
    Generate 2D coordinates
--gen3d
    Generate 3D coordinates. You can specify the speed of prediction. See :ref:`specify_speed`.
-h
    Add hydrogens (make all hydrogen explicit)
--highlight <substructure color>
    Highlight substructures in 2D depictions. Valid 
    colors are black, gray, white, red, green, blue, yellow,
    cyan, purple, teal and olive. Additional colors may be
    specified as hexadecimal RGB values preceded by ``#``.
    Multiple substructures and corresponding colors may be
    specified.
-i <format-ID>
    Specifies input format. See :ref:`file formats`.
-j, --join
    Join all input molecules into a single output molecule entry
-k
    Translate computational chemistry modeling keywords. See
    the computational chemistry formats (:ref:`Computational chemistry`),
    for example :ref:`GAMESS_Input` and :ref:`Gaussian_98_or_03_Input`.
-l <#>
    For multiple entry input, stop import with molecule # as the last
    entry
--largest <#N descriptor>
    Only convert the N molecules which have the largest values of the
    specified descriptor. Preceding the descriptor by ``~`` inverts
    this filter.
-m
    Produce multiple output files, to allow:

    -  Splitting one input file - put each molecule into consecutively
       numbered output files
    -  Batch conversion - convert each of multiple input files into a
       specified output format
--minimize <options>
     Forcefield energy minimization. See :ref:`minimize option`.
-o <format-ID>
    Specifies output format. See :ref:`file formats`.
-p <pH>
    Add hydrogens appropriate for pH (use transforms in :file:`phmodel.txt`)
--partialcharge <charge-method>
    Calculate partial charges by the specified method. List available methods
    using ``obabel -L charges``.
--property <name  value>
    Add or replace a property (for example, in an SD file)
-r
    Remove all but the largest contiguous fragment (strip salts)
--readconformer
    Combine adjacent conformers in multi-molecule input into a single molecule.
    If a molecule has the same structure as the preceding molecule, as
    determined from its SMILES, it is not output but its coordinates are
    added to the preceding molecule as an additional conformer. There can
    be multiple groups of conformers, but the molecules in each group must
    be adjacent.
-s <SMARTS>
    Convert only molecules matching the SMARTS pattern specified
-s <filename.xxx>
    Convert only molecules with the molecule in the file as a substructure
--separate
    Separate disconnected fragments into individual molecular records
--smallest <#N descriptor>
    Only convert the N molecules which have the smallest values of the
    specified descriptor. Preceding the descriptor by ``~`` inverts this
    filter.
--sort
    Output molecules ordered by the value of a descriptor. See :ref:`sorting option`.
--title <title>
    Add or replace molecular title
--unique, --unique <param>
    Do not convert duplicate molecules. See :ref:`removing duplicates`.
--writeconformers
    Output multiple conformers as separate molecules
-x <options>
    Format-specific output options. use ``-H <format-ID>`` to see options
    allowed by a particular format, or see the appropriate section in
    :ref:`file formats`.
-v <SMARTS>
    Convert only molecules **NOT** matching the SMARTS pattern specified
-z
    Compress the output with gzip (not on Windows)


Examples
--------

The examples below assume the files are in the current directory. Otherwise you may need to include the full path to the files e.g. :file:`/Users/username/Desktop/mymols.sdf` and you may need to put quotes around the filenames (especially on Windows, where they can contain spaces).

Standard conversion::

    obabel ethanol.xyz -O ethanol.pdb
    babel ethanol.xyz ethanol.pdb

Conversion if the files do not have an extension that describes their format::

    obabel -ixyz ethanol.aa -opdb -O ethanol.bb
    babel -ixyz ethanol.aa -opdb ethanol.bb

Molecules from multiple input files (which can have different formats) are normally combined in the output file::

    obabel ethanol.xyz acetal.sdf benzene.cml -O allmols.smi

Conversion from a SMI file in STDIN to a Mol2 file written to STDOUT::

    obabel -ismi -omol2

Split a multi-molecule file into :file:`new1.smi`, :file:`new2.smi`, etc.::

    obabel infile.mol -O new.smi -m

In Windows this can also be written::

    obabel infile.mol -O new*.smi

Multiple input files can be converted in batch format too. To convert all files ending in .xyz (``*.xyz``) to PDB files, you can type::

    obabel *.xyz -opdb -m

Open Babel will not generate coordinates unless asked, so while a conversion from SMILES to SDF will generate a valid SDF file, the resulting file will not contain coordinates. To generate coordinates, use either the ``--gen3d`` or  the ``--gen2d`` option::

     obabel infile.smi -O out.sdf --gen3d

If you want to remove all hydrogens (i.e. make them all implicit) when doing the conversion the command would be::

     obabel mymols.sdf -osmi -O outputfile.smi -d

If you want to add hydrogens (i.e. make them all explicit) when doing the conversion the command would be::

     obabel mymols.sdf -O outputfile.smi -h

If you want to add hydrogens appropriate for pH7.4 when doing the conversion the command would be::

     obabel mymols.sdf -O outputfile.smi -p

The protonation is done on an atom-by-atom basis so molecules with multiple ionizable centers will have all centers ionized.

Of course you don't actually need to change the file type to modify the hydrogens. If you want to add all hydrogens the command would be::

     obabel mymols.sdf -O mymols_H.sdf -h

Some functional groups e.g. nitro or sulphone can be represented either as ``[N+]([O-])=O`` or ``N(=O)=O``. To convert all to the dative bond form::

     obabel mymols.sdf -O outputfile.smi -b

If you only want to convert a subset of molecules you can define them using ``-f`` and ``-l``. To convert molecules 2-4 of the file :file:`mymols.sdf` type::

     obabel mymols.sdf -f 2 -l 4 -osdf -O outputfile.sdf

Alternatively you can select a subset matching a SMARTS pattern, so to select all molecules containing bromobenzene use::

     obabel mymols.sdf -O selected.sdf -s "c1ccccc1Br"

You can also select the subset that do *not* match a SMARTS pattern, so to select all molecules not containing bromobenzene use::

     obabel mymols.sdf -O selected.sdf -v "c1ccccc1Br"

You can of course combine options, so to join molecules and add hydrogens type::

     obabel mymols.sdf -O myjoined.sdf -h -j

Files compressed with gzip are read transparently, whether or not they have a .gz suffix::

     obabel compressed.sdf.gz -O expanded.smi

On platforms other than Windows, the output file can be compressed with gzip, but note if you don't specify the .gz suffix it will not be added automatically, which could cause problems when you try to open the file::

     obabel mymols.sdf -O outputfile.sdf.gz -z

This next example reads the first 50 molecules in a compressed dataset and prints out the SMILES of those containing a pyridine ring, together with the index in the file, the ID (taken from an SDF property) as well as the output index::

    obabel chembl_02.sdf.gz -osmi -l 50 -s c1ccccn1 --append chebi_id
           --addinindex --addoutindex

For the test data (taken from ChEMBLdb), this gave::

    N1(CCN(CC1)c1c(cc2c3c1OCC(n3cc(c2=O)C(=O)O)C)F)C        3 100146 1
    c1(c(=O)c2c(n(c1)OC)c(c(N1CC(CC1)CNCC)c(c2)F)F)C(=O)O   6 100195 2
    S(=O)(=O)(Nc1ncc(cc1)C)c1c2c(c(N(C)C)ccc2)ccc1          22 100589 3
    c1([nH]c2c(c1)cccc2)C(=O)N1CCN(c2c(N(CC)CC)cccn2)CC1    46 101536 4

Format Options
--------------

Individual file formats may have additional formatting options. These are listed in the documentation for the individual formats (see :ref:`file formats`) or can be shown using the ``-H <format-Id>`` option, e.g. ``-H cml``.

To use these additional options, input format options are preceded by ``-a``, e.g. ``-as``. Output format options, which are much more common, are preceded by ``-x``, e.g. ``-xn``. So to read the 2D coordinates (rather than the 3D) from a :ref:`CML file <Chemical_Markup_Language>` and generate an :ref:`SVG file <SVG_2D_depiction>` displaying the molecule on a black background, the relevant options are used as follows::

      obabel mymol.cml out.svg -a2 -xb

.. _append option:

Append property values to the title
-----------------------------------

The command line option ``--append`` adds extra information to the title of the molecule.

The information can be calculated from the structure of the molecule or can originate from a property attached to the molecule (in the case of CML and SDF input files). It is used as follows::

 obabel infile.sdf -osmi --append "MW CAT_NO"

``MW`` is the ID of a descriptor which calculates the molecular weight of the molecule, and ``CAT_NO`` is a property of the molecule from the SDF input file. The values of these are added to the title of the molecule. For input files with many molecules these additions are specific to each molecule. (Note that the related option ``--addtotitle`` simply adds the same text to every title.)

The append option only takes one parameter, which means that it may be necessary to enclose all of the descriptor IDs or property names together in a single set of quotes.

If the name of the property in the SDF file (internally the Attribute in OBPairData) contains spaces, these spaces should be replaced by underscore characters, '_'. So the example above would also work for a property named ``CAT NO``.

By default, the extra items are added to the title separated by spaces. But if the first character in the parameter is a punctuation character other than '_', it is used as the separator instead. If the list starts with "\t", a tab character is used as a separator. 

.. _conformers:

Generating conformers for structures
------------------------------------

The command line option ``--conformer`` allows performing conformer
searches using a range of different algorithms and options:

* ``--log`` -           output a log of the energies (default = no log)
* ``--nconf #`` -       number of conformers to generate

Forcefield-based methods for finding stable conformers:

* ``--systematic`` - systematically (exhaustively) generate all conformers
* ``--random`` - randomly generate conformers
* ``--weighted`` - weighted rotor search for lowest energy conformer
* ``--ff <name>`` - select a forcefield (default = MMFF94)

Genetic algorithm based methods (default):

* ``--children #`` - number of children to generate for each parent (default = 5)
* ``--mutability #`` - mutation frequency (default = 5)
* ``--converge #`` - number of identical generations before convergence is reached
* ``--score #`` - scoring function [rmsd|energy] (default = rmsd)

You can use them like this (to generate 50 conformers, scoring with
MMFF94 energies but default genetic algorithm options)::

  obabel EtOT5D.cml -O EtOT5D0.xyz --conformer --nconf 50 --score energy

or if you also wish to generate 3D coordinates, followed by conformer
searching try something like this::

  obabel ligand.babel.smi -O ligand.babel.sdf --gen3d --conformer --nconf 20 --weighted

.. _filter options:

Filtering molecules from a multimolecule file
---------------------------------------------

Six of the options above can be used to filter molecules:

* ``-s`` - convert molecules that match a SMARTS string
* ``-v`` - convert molecules that don't match a SMARTS string
* ``-f`` and ``-l`` - convert molecules in a certain range
* ``--unique`` - only convert unique molecules (that is, remove duplicates)
* ``--filter`` - convert molecules that meet specified chemical (and other) criteria

This section focuses on the ``--filter`` option, which is very versatile and can select a subset of molecules based either on properties imported with the molecule (as from a SDF file) or from calculations made by Open Babel on the molecule.

The aim has been to make the option flexible and intuitive to use; don't be put off by the long description.

You use it like this::

  obabel filterset.sdf -osmi --filter "MW<130 ROTATABLE_BOND > 2"

It takes one parameter which probably needs to be enclosed in double quotes to avoid confusing the shell or operating system. (You don't need the quotes with the Windows GUI.) The parameter contains one or more conditional tests. By default, these have all to be true for the molecule to be converted. As well as this implicit AND behaviour, you can write a full Boolean expression (see below). As you can see, there can be spaces or not in sensible places and the conditional tests could be separated by a comma or semicolon.

You can filter on two types of property:

* An SDF property, as the identifier ROTATABLE_BOND could be. There is no need for it to be previously known to Open Babel.
* A descriptor name (internally, an ID of an OBDescriptor object). This is a plug-in class so that new objects can easily be added. MW is the ID of a descriptor which calculates molecular weight. You can see a list of available descriptors using::

    obabel -L descriptors

  or from a menu item in the GUI.

.. sidebar:: Faster filtering

  Open Babel provides a number of utility file formats (see :ref:`file formats`). Of these, using the *copy format* as the output format is particularly useful when filtering (see :ref:`Copy_raw_text`). This copies the content of the molecular file directly from input to output. If you are not converting the molecules between different formats, this procedure is much faster and avoids any possibility of information loss.

  In addition, if you are converting SDF files and are filtering based on the title, you should consider using ``-aT`` (see :ref:`MDL_MOL_format`). Rather than perceiving the chemistry of the entire molecule, this option will only read in the title.

The descriptor names are case-insensitive. With the property names currently, you need to get the case right. Both types of identifier can contain letters, numbers and underscores, '_'. Properties can contain spaces, but then when writing the name in the filter parameter, you need to replace them with underscores. So in the example above, the test would also be suitable for a property 'ROTATABLE BOND'.

Open Babel uses a SDF-like property (internally this is stored in the class OBPairData) in preference to a descriptor if one exists in the molecule. So with the example file, which can be found here_::

  obabel filterset.sdf -osmi --filter "logP>5"

converts only a molecule with a property logP=10.900, since the others do not have this property and logP, being also a descriptor, is calculated and is always much less than 5.

.. _here: https://raw.githubusercontent.com/openbabel/openbabel/master/test/files/filterset.sdf

If a property does not have a conditional test, then it returns true only if it exists. So::

  obabel filterset.sdf -osmi --filter "ROTATABLE_BOND MW<130"

converts only those molecules with a ROTATABLE_BOND property and a molecular weight less than 130. If you wanted to also include all the molecules without ROTATABLE_BOND defined, use::

  obabel filterset.sdf -osmi --filter "!ROTATABLE_BOND || (ROTATABLE_BOND & MW<130)"

The ! means negate. AND can be & or &&, OR can be | or ||. The brackets are not strictly necessary here because & has precedent over | in the normal way. If the result of a test doesn't matter, it is parsed but not evaluated. In the example, the expression in the brackets is not evaluated for molecules without a ROTATABLE_BOND property. This doesn't matter here, but if evaluation of a descriptor involved a lot of computation, it would pay to include it late in the boolean expression so that there is a chance it is skipped for some molecules.

Descriptors must have a conditional test and it is an error if they don't. The default test, as used by MW or logP, is a numerical one, but the parsing of the text, and what the test does is defined in each descriptor's code (a virtual function in the OBDescriptor class). Three examples of this are described in the following sections.

String descriptors
~~~~~~~~~~~~~~~~~~

::

  obabel filterset.sdf -osmi --filter "title='Ethanol'"

The descriptor *title*, when followed by a string (here enclosed by single quotes), does a case-sensitive string comparison. ('ethanol' wouldn't match anything in the example file.) The comparison does not have to be just equality::

  obabel filterset.sdf -osmi --filter "title>='D'"

converts molecules with titles Dimethyl Ether and Ethanol in the example file.

It is not always necessary to use the single quotes when the meaning is unambiguous: the two examples above work without them. But a numerical, rather than a string, comparison is made if both operands can be converted to numbers. This can be useful::

  obabel filterset.sdf -osmi --filter "title<129"

will convert the molecules with titles 56 123 and 126, which is probably what you wanted.

::

  obabel filterset.sdf -osmi --filter "title<'129'"

converts only 123 and 126 because a string comparison is being made.

String comparisons can use ``*`` as a wildcard if used as the first or last character of the string (anywhere else a ``*`` is a normal character). So ``--filter "title='*ol'"`` will match molecules with titles 'methanol', 'ethanol' etc. and ``--filter "title='eth*'`` will match 'ethanol', 'ethyl acetate', 'ethical solution' etc. Use a ``*`` at both the first and last characters to test for the occurrence of a string, so ``--filter "title='*ol*'"`` will match 'oleum', 'polonium' and 'ethanol'.

SMARTS descriptor
~~~~~~~~~~~~~~~~~

This descriptor will do a SMARTS test (substructure and more) on the molecules. The smarts ID can be abbreviated to s and the = is optional. More than one SMARTS test can be done::

  obabel filterset.sdf -osmi --filter "s='CN' s!='[N+]'"

This provides a more flexible alternative to the existing ``-s`` and ``-v`` options, since the SMARTS descriptor test can be combined with other tests.

InChI descriptor
~~~~~~~~~~~~~~~~

::

  obabel filterset.sdf -osmi --filter "inchi='InChI=1/C2H6O/c1-2-3/h3H,2H2,1H3'"

will convert only ethanol. It uses the default parameters for InChI comparison, so there may be some messages from the InChI code. There is quite a lot of flexibility on how the InChI is presented (you can miss out the non-essential bits)::

  obabel filterset.sdf -osmi --filter "inchi='1/C2H6O/c1-2-3/h3H,2H2,1H3'"
  obabel filterset.sdf -osmi --filter "inchi='C2H6O/c1-2-3/h3H,2H2,1H3'"
  obabel filterset.sdf -osmi --filter "inchi=C2H6O/c1-2-3/h3H,2H2,1H3"
  obabel filterset.sdf -osmi --filter "InChI=1/C2H6O/c1-2-3/h3H,2H2,1H3"

all have the same effect.

The comparison of the InChI string is done only as far as the parameter's length. This means that we can take advantage of InChI's layered structure::

  obabel filterset.sdf -osmi --filter "inchi=C2H6O"

will convert both Ethanol and Dimethyl Ether.

Substructure and similarity searching
-------------------------------------

For information on using :command:`obabel` for substructure searching and similarity searching, see :ref:`fingerprints`.

.. _sorting option:

Sorting molecules
-----------------

The ``--sort`` option is used to output molecules ordered by the value of a descriptor::

 obabel  infile.xxx  outfile.xxx  --sort desc

If the descriptor desc provides a numerical value, the molecule with the smallest value is output first. For descriptors that provide a string output the order is alphabetical, but for the InChI descriptor a more chemically informed order is used (e.g. "CH4" is before than "C2H6", "CH4" is less than "ClH" hydrogen chloride).

The order can be reversed by preceding the descriptor name with ``~``, e.g.::

 obabel  infile.xxx  outfile.yyy  --sort ~logP

As a shortcut, the value of the descriptor can be appended to the molecule name by adding a ``+`` to the descriptor, e.g.::

 obabel  aromatics.smi  -osmi  --sort ~MW+
  c1ccccc1C=C	styrene 104.149
  c1ccccc1C	toluene 92.1384
  c1ccccc1	benzene 78.1118

.. _removing duplicates:

Remove duplicate molecules
---------------------------

The ``--unique`` option is used to remove, i.e. not output, any chemically identical molecules during conversion::

 obabel  infile.xxx  outfile.yyy  --unique [param]

The optional parameter *param* defines what is regarded as "chemically identical". It can be the name of any descriptor, although not many are likely to be useful. If *param* is omitted, the InChI descriptor is used. Other useful descriptors are 'cansmi' and 'cansmiNS' (canonical SMILES, with and without stereochemical information),'title' and truncated InChI (see below).

A message is output for each duplicate found::

      Removed methyl benzene - a duplicate of toluene (#1)

Clearly, this is more useful if each molecule has a title. The ``(#1)`` is the number of duplicates found so far.

If you wanted to identify duplicates but not output the unique molecules, you could use the :ref:`null format <Outputs_nothing>`::

 obabel  infile.xxx  -onul  --unique

Truncated InChI
~~~~~~~~~~~~~~~

It is possible to relax the criterion by which molecules are regarded as "chemically identical" by using a truncated InChI specification as *param*. This takes advantage of the layered structure of InChI. So to remove duplicates, treating stereoisomers as the same molecule::

 obabel  infile.xxx  outfile.yyy  --unique /nostereo

Truncated InChI specifications start with ``/`` and are case-sensitive. *param* can be a concatenation of these e.g. ``/nochg/noiso``::

 /formula   formula only
 /connect   formula and connectivity only
 /nostereo  ignore E/Z and sp3 stereochemistry
 /nosp3     ignore sp3 stereochemistry
 /noEZ      ignore E/Z stereoochemistry
 /nochg     ignore charge and protonation
 /noiso     ignore isotopes

Multiple files
~~~~~~~~~~~~~~

The input molecules do not have to be in a single file. So to collect all the unique molecules from a set of MOL files::

 obabel  *.mol  uniquemols.sdf  --unique

If you want the unique molecules to remain in individual files::

 obabel  *.mol  U.mol  -m  --unique

On the GUI use the form::

 obabel  *.mol  U*.mol  --unique

Either form is acceptable on the Windows command line.

The unique molecules will be in files with the original name prefixed by 'U'. Duplicate molecules will be in similar files but with zero length, which you will have to delete yourself.

Aliases for chemical groups
---------------------------------

There is a limited amount of support for representing common chemical groups by an alias, e.g. benzoic acid as ``Ph-COOH``, with two alias groups. Internally in Open Babel, the molecule usually has a 'real' structure with the alias names present as only an alternative representation. For MDL MOL and SD files alias names can be read from or written to an 'A' line. The more modern RGroup representations are not yet recognized. Reading is transparent; the alias group is expanded and the 'real' atoms given reasonable coordinates if the the molecule is 2D or 3D. Writing in alias form, rather than the 'real' structure, requires the use of the ``-xA`` option.  SVGFormat will also display any aliases present in a molecule if the ``-xA`` option is set.

The alias names that are recognized are in the file :file:`superatoms.txt` which can be edited.

Normal molecules can have certain common groups given alternative alias representation using the ``--genalias`` option. The groups that are recognized and converted are a subset of those that are read. Displaying or writing them still requires the ``-xA`` option. For example, if :file:`aspirin.smi` contained ``O=C(O)c1ccccc1OC(=O)C``, it could be displayed with the  aliases ``COOH`` and ``OAc`` by::

  obabel aspirin.smi  -O out.svg  --genalias  -xA

.. _minimize option:

Forcefield energy and minimization
----------------------------------

Open Babel supports a number of forcefields which can be used for energy evaluation as well as energy minimization. The available forcefields as listed as follows::

  C:\>obabel -L forcefields
  GAFF    General Amber Force Field (GAFF).
  Ghemical    Ghemical force field.
  MMFF94    MMFF94 force field.
  MMFF94s    MMFF94s force field.
  UFF    Universal Force Field.

To evaluate a molecule's energy using a forcefield, use the ``--energy`` option. The energy is put in an OBPairData object "Energy" which is accessible via an SDF or CML property or ``--append`` (to title). Use ``--ff <forcefield_id>`` to select a forcefield (default is Ghemical) and ``--log`` for a log of the energy calculation. The simplest way to output the energy is as follows::

   obabel infile.xxx -otxt --energy --append "Energy"

To perform forcefield minimization, the ``--minimize`` option is used. The following shows typical usage::

  obabel infile.xxx -O outfile.yyy --minimize --steps 1500 --sd

The available options are as follows::

--log        output a log of the minimization process (default= no log)
--crit <converge>     set convergence criteria (default=1e-6)
--sd         use steepest descent algorithm (default = conjugate gradient)
--newton     use Newton2Num linesearch (default = Simple)
--ff <forcefield-id>       select a forcefield (default = Ghemical)
--steps <number>    specify the maximum number of steps (default = 2500)
--cut        use cut-off (default = don't use cut-off)
--rvdw <cutoff>     specify the VDW cut-off distance (default = 6.0)
--rele <cutoff>     specify the Electrostatic cut-off distance (default = 10.0)
--freq <steps>     specify the frequency to update the non-bonded pairs (default = 10)

Note that for both ``--energy`` and ``--minimize``, hydrogens are made explicit before energy evaluation.

Aligning molecules or substructures
-----------------------------------

The ``--align`` option aligns molecules to the first molecule provided. 
It is typically used with the ``-s`` option to specify an alignment
based on a substructure::

    obabel pattern.www  dataset.xxx  -O outset.yyy  -s SMARTS  --align

Here, only molecules matching the specified SMARTS pattern are converted
and are aligned by
having all their atom coordinates modified. The atoms that are
used in the alignment are those matched by SMARTS in the first
output molecule. The subsequent molecules are aligned so that
the coordinates of atoms equivalent to these are as nearly as
possible the same as those of the pattern atoms.
The atoms in the various molecules can be in any order.
Tha alignment ignores hydrogen atoms but includes symmetry.
Note that the standalone program :program:`obfit` has similar functionality.

The first input molecule could also be part of the data set::

    obabel dataset.xxx  -O outset.yyy  -s SMARTS  --align

This form is useful for ensuring that a particular substructure always
has the same orientation in a 2D display of a set of molecules.
0D molecules, for example from SMILES, are given 2D coordinates before
alignment.

See documentation for the ``-s`` option for its other possible
parameters. For example, the matching atoms could be those
of a molecule in a specified file.

If the ``-s`` option is not used, all of the atoms in the first molecule
are used as pattern atoms. The order of the atoms must be the same
in all the molecules.

The output molecules have a property (represented internally as
OBPairData) called ``rmsd``, which is a measure of the quality
of the fit. To attach it to the title of each molecule use
``--append rmsd``.

To output the two conformers closest to the first conformer in a dataset::

    obabel dataset.xxx  -O outset.yyy  --align  --smallest 2 rmsd

.. _specify_speed:

Specifying the speed of 3D coordinate generation
---------------------------------------------------
When you use the ``--gen3d`` option, you can specify the speed and quality. The following shows typical usage::

     obabel infile.smi -O out.sdf --gen3d fastest

The available options are as follows:

=================  ======================
option             description
=================  ======================
``fastest``        No cleanup
``fast``           Force field cleanup (100 cycles)
``med`` (default)  Force field cleanup (100 cycles) + Fast rotor search (only one permutation)
``slow``           Force field cleanup (250 cycles) + Fast rotor search (permute central rotors)            
``slowest``        Force field cleanup (500 cycles) + Slow rotor search
``better``         Same as ``slow``
``best``           Same as ``slowest``
``dist``, ``dg``   Use distance geometry method (unstable)
=================  ======================

You can also specify the speed by an integer from ``1`` (slowest) to ``5`` (fastest).
