Babel - Convert, Filter and Manipulate Chemical Data
====================================================

Babel is a cross-platform program designed to interconvert between
many file formats used in molecular modeling and computational
chemistry and related areas.

Synopsis
--------

``babel [-H <help-options>]``

``babel [OPTIONS] [-i <input-format-ID>] infile [-o <output-format-ID>] outfile``

If only input and ouput files are given, Open Babel will guess the
file type from the
filename extension. For information on the file formats supported by Open Babel, please see :ref:`file formats`.

Options
-------

-a <options>
    Format-specific input options. See ``-H <format-ID>`` for options
    allowed by a particular format
--addtotitle 
    Append text after the current molecule title
--addformula 
    Append the molecular formula after the current molecule title

--append <property list> 
    Append properties values to the current molecule title. For more
    information, see :ref:`append option`.
-b 
    Convert dative bonds (e.g. ``[N+]([O-])=O`` to ``N(=O)=O``)
-c 
    Center atomic coordinates at (0,0,0)
-C 
    Combine molecules in first file with others having the same name
-d 
    Delete Hydrogens
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
-F 
    Output the available fingerprint types
--filter <criteria> 
    Filter based on molecular properties. See
    :ref:`filter options` for examples and a list of
    criteria.
-h 
    Add hydrogens
-H 
    Output usage information
-H <format-ID> 
    Output formatting information and options for
    `format </wiki/Category:Formats>`_ specified
-Hall 
    Output formatting information and options for all
    `formats </wiki/Category:Formats>`_
-i <format-ID> 
    Specifies input format, see below for the available
    `formats </wiki/Category:Formats>`_
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
    Specifies output format, see below for the available
    `formats </wiki/Category:Formats>`_
-p <pH> 
    Add Hydrogens appropriate for pH (use transforms in phmodel.txt)
--property 
    Add or replace a property (for example, in an SD file, :ref:`MDL MOL format`)
-s <SMARTS>
    Convert only molecules matching the SMARTS
    pattern specified
--separate 
    Separate disconnected fragments into individual molecular records
-t
    All input files describe a single molecule
--title <title> 
    Add or replace molecular title
-x <options> 
    Format-specific output options. See ``-H <format-ID>`` for options
    allowed by a particular format
-v <SMARTS>
    Convert only molecules **NOT** matching the SMARTS
    pattern specified
-V 
    Output version number and exit
-z 
    Compress the output with gzip


Examples
--------

Standard conversion::

    babel -ixyz ethanol.xyz -opdb ethanol.pdb

Conversion from a SMI file in STDIN to a Mol2 file written to
STDOUT::

    babel -ismi -omol2

Split a multi-molecule file into new1.smi, new2.smi, etc.::

    babel infile.mol new.smi -m

Format Options
--------------

Individual file formats may have additional formatting options. These are listed in the documentation for the individual formats (see :ref:`file formats`) or can be shown using the ``-H <format-Id>`` option, e.g. ``-H cml``.

To use these additional options, input format options are preceded by ``-a``, e.g. ``-as``. Output format options are preceded by ``-x``, e.g. ``-xn``.

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

  In addition, if you are converting SDF files and are filtering based on the title, you should consider using ``-as`` (see :ref:`MDL_MOL_format`). Rather than perceiving the chemistry of the entire molecule, this option will only read in the title.

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
