obabel vs Chemistry Toolkit Rosetta
-----------------------------------

The `Chemistry Toolkit Rosetta`_ is the brainchild of Andrew Dalke. It is a website that illustrates how to program various chemical toolkits to do a set of tasks. To make it easily understandable, these tasks are probably on the simpler side of those in the real world. The Rosetta already contains several examples of using the Open Babel Python bindings to carry out tasks.

Here we focus on the use of the command line application :command:`obabel` to accomplish the tasks listed in the Rosetta. Inevitably we will struggle with more complicated tasks; however this section is intended to show how far you can go simply using :command:`obabel`, and to illustrate some of its less common features. Some of the tasks cannot be done exactly as specified, but they are are usually close enough to useful.

.. _Chemistry Toolkit Rosetta: http://ctr.wikia.com/wiki/Chemistry_Toolkit_Rosetta_Wiki

Note that except for the examples involving piping, the GUI could also be used. Also the copy output format at present works only for files with Unix line endings.

Heavy atom counts from an SD file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *For each record from the benzodiazepine  file, print the total number of heavy atoms in each record (that is, exclude hydrogens). The output is one output line per record, containing the count as an integer. If at all possible, show how to read directly from the gzip'ed input SD file.*

::

  obabel benzodiazepine.sdf.gz -otxt --title "" --append atoms -d -l5

The :ref:`txt format <Title_format>` outputs only the title but we set that to nothing and then append the result. The *atoms* descriptor counts the number of atoms after the ``-d`` option has removed the hydrogens. The ``-l5`` limits the output to the first 5 molecules, in case you really didn't want to print out results for all 12386 molecules.

Convert a SMILES string to canonical SMILES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *Parse two SMILES strings and convert them to canonical form. Check that the results give the same string.*

::

  obabel -:"CN2C(=O)N(C)C(=O)C1=C2N=CN1C" -:"CN1C=NC2=C1C(=O)N(C)C(=O)N2C" -ocan

giving::

  Cn1cnc2c1c(=O)n(C)c(=O)n2C
  Cn1cnc2c1c(=O)n(C)c(=O)n2C
  2 molecules converted


Report how many SD file records are within a certain molecular weight range
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

  *Read the benzodiazepine file and report the number of records which contain a molecular weight between 300 and 400.*

::

  obabel benzodiazepine.sdf.gz -onul --filter "MW>=300 MW<=400"
  3916 molecules converted


Convert SMILES file to SD file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *Convert a SMILES file into an SD file. The conversion must do its best to use the MDL conventions for the SD file, including aromaticity perception. Note that the use of aromatic bond types in CTABs is only allowed for queries, so aromatic structures must be written in a Kekule form. Because the stereochemistry of molecules in SD files is defined solely by the arrangement of atoms, it is necessary to assign either 2D or 3D coordinates to the molecule before generating output. The coordinates do not have to be reasonable (i.e. it's ok if they would make a chemist scream in horror), so long as the resulting structure is chemically correct.*

::

  obabel infile.smi -O outfile.sdf --gen3D
  

Report the similarity between two structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *Report the similarity between "CC(C)C=CCCCCC(=O)NCc1ccc(c(c1)OC)O" (PubChem CID 1548943) and "COC1=C(C=CC(=C1)C=O)O" (PubChem CID 1183).*

Two types of fingerprint are used: the default FP2 path-based one, and FP4 which is structure key based::

  obabel -:"CC(C)C=CCCCCC(=O)NCc1ccc(c(c1)OC)O" -:"COC1=C(C=CC(=C1)C=O)O" -ofpt
  Tanimoto from first mol = 0.360465

  obabel -:"CC(C)C=CCCCCC(=O)NCc1ccc(c(c1)OC)O" -:"COC1=C(C=CC(=C1)C=O)O" -ofpt
         -xfFP4
  Tanimoto from first mol = 0.277778

                                  
Find the 10 nearest neighbors in a data set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *The data will come from the gzip'ed SD file of the benzodiazepine data set. Use the first structure as the query structure, and use the rest of the file as the targets to find the 10 most similar structures. The output is sorted by similarity, from most similar to least. Each target match is on its own line, and the line contains the similarity score in the first column in the range 0.00 to 1.00 (preferably to 2 decimal places), then a space, then the target ID, which is the title line from the SD file.*

A fastsearch index, using the default FP2 fingerprint, is prepared first::

  obabel benzodiazepine.sdf -ofs

The query molecule (first in the file) is extracted::

  obabel benzodiazepine.sdf -O first.sdf -l1

The similarity search of the index file for the 10 most similar molecules is done. The output is to :ref:`Title_format`, with the ``-aa`` option of :ref:`Fastsearch_format` adding the Tanimoto score::

  obabel benzodiazepine.fs -otxt -s first.sdf -at 10 -aa

  623918 1
  450820 1
  1688 1
  20351792 0.993007
  9862446 0.986111
  398658 0.97931
  398657 0.97931
  6452650 0.978873
  450830 0.978873
  3016 0.978873
  10 molecules converted

The Tanimoto coefficient comes second, rather than first as requested and is not formatted to two decimal places, but the information is still there.

Depict a compound as an image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *Depict the SMILES "CN1C=NC2=C1C(=O)N(C(=O)N2C)C" as an image of size 200x250 pixels. The image should be in PNG format if possible, otherwise in GIF format. If possible, give it the title "Caffeine". It should display the structure on a white background.*

Open Babel can output 2D structures as :ref:`PNG <PNG_2D_depiction>`. The ``-d`` makes hydrogen implicit. Width and height are set with the -xw and -xh options.::

  obabel -:"CN1C=NC2=C1C(=O)N(C(=O)N2C)C Caffeine" -O out.png -xw 200 -xh 250 -d

Open Babel also supports outputting :ref:`SVG <SVG_2D_depiction>`, which is resolution independent as a vector format.::

  obabel -:"CN1C=NC2=C1C(=O)N(C(=O)N2C)C Caffeine" -O out.svg -d

Highlight a substructure in the depiction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *Read record 3016 from the benzodiazepine SD file. Find all atoms which match the SMARTS "c1ccc2c(c1)C(=NCCN2)c3ccccc3" and highlight them in red. All other atoms must be drawn in black.*

  *The resulting image should be 200x250 pixels and on a white background. The resulting image file should be in PNG (preferred) or GIF format.*

::

  obabel benzodiazepine.sdf.gz -O out.png --filter "title=3016"
         -s "c1ccc2c(c1)C(=NCCN2)c3ccccc3 red" -xu -xw 200 -xh 250 -d

Open Babel can output 2D structures as :ref:`PNG <PNG_2D_depiction>`. The compressed data file can be used as input. The ``-d`` makes hydrogen implicit and the ``-xu`` removes the element-specific coloring. Width and height are set with the -xw and -xh options.

This is slow (about a minute) because each molecule is fully interpreted, although in most cases only the title is required. The task can be done 10 times faster by using the uncompressed file, converting only the title (the ``-aT`` option) and copying the SD text to standard out when a match occurs. This is piped to a second command which outputs the structure.::

  obabel benzodiazepine.sdf -ocopy --filter "title=3016" -aT |
         obabel -isdf -O out.png -s "c1ccc2c(c1)C(=NCCN2)c3ccccc3 red" -xu -xw 200 -xh 250 -d

Open Babel also supports outputting :ref:`SVG <SVG_2D_depiction>`, which is resolution independent as a vector format.::

  obabel benzodiazepine.sdf.gz -O out.svg --filter "title=3016"
         -s "c1ccc2c(c1)C(=NCCN2)c3ccccc3 red" -xu -d

  obabel benzodiazepine.sdf -ocopy --filter "title=3016" -aT |
         obabel -isdf -O out.svg -s "c1ccc2c(c1)C(=NCCN2)c3ccccc3 red" -xu -d


Align the depiction using a fixed substructure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *Use the first 16 structures of the benzodiazepine SD file to make a 4x4 grid of depictions as a single image. The first structure is in the upper-left corner, the second is to its right, and so on. Each depiction should include the title field of the corresponding record, which in this case is the PubChem identifier.*

  *Use "[#7]~1~[#6]~[#6]~[#7]~[#6]~[#6]~2~[#6]~[#6]~[#6]~[#6]~[#6]12" as the common SMARTS substructure. This is the fused ring of the benzodiazepine system but without bond type or atom aromaticity information. Use the first molecule as the reference depiction. All other depictions must have the depiction of their common substructure aligned to the reference.*

Since Open Babel 2.3.1 this can be done in one line::

  obabel benzodiazepine.sdf.gz -O out.png -l16 --align -d -xu -xw 400 -xh 400
         -s"[#7]~1~[#6]~[#6]~[#7]~[#6]~[#6]~2~[#6]~[#6]~[#6]~[#6]~[#6]12 green"

The depiction has some cosmetic tweaks: the substructure is highlighted in green; ``-d`` removes hydrogen; ``-xu`` removes the element specific coloring.
Open Babel also supports outputting :ref:`SVG <SVG_2D_depiction>`, which is resolution independent as a vector format.::

  obabel benzodiazepine.sdf.gz -O out.svg -l16 --align -d -xu
         -s"[#7]~1~[#6]~[#6]~[#7]~[#6]~[#6]~2~[#6]~[#6]~[#6]~[#6]~[#6]12 green"

In earlier versions the :command:`obfit` program can be used. First extract the first molecule for the reference and the first 16 to be displayed::

  obabel benzodiazepine.sdf.gz -O firstbenzo.sdf -l1
  obabel benzodiazepine.sdf.gz -O sixteenbenzo.sdf -l16

Then use the program :command:`obfit`, which is distributed with Open Babel::

  obfit "[#7]~1~[#6]~[#6]~[#7]~[#6]~[#6]~2~[#6]~[#6]~[#6]~[#6]~[#6]12"
        firstbenzo.sdf  sixteenbenzo.sdf > 16out.sdf

Display the 16 molecules (with implicit hydrogens) as :ref:`SVG <SVG_2D_depiction>` (earlier versions of Open Babel do not support :ref:`PNG <PNG_2D_depiction>`)::

  obabel 16out.sdf -O out.png -d -xw 400 -xh 400


Perform a substructure search on an SDF file and report the number of false positives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  *The sample database will be gzip'ed SD file of the benzodiazepine data set. The query structure will be defined as "C1C=C(NC=O)C=CC=1".*

The default FP2 fingerprint is sensitive to whether a bond is aromatic or not. So this Kekule structure needs to be converted to its aromatic form. As this happens automatically on conversion, the easiest way is to store the SMILES string in a file, and use this file to specify the search pattern.    

Prepare an index (of the unzipped data file)::

  obabel benzodiazepine.sdf -ofs

Do the substructure search. A very large number of molecules match the query, so the maximum number of hits has to be increased with the ``-al 9000`` option. By virtue of the ``~`` it is the false positives that are output (to nowhere) but their number is reported::

  obabel benzodiazepine.fs -onul -s ~substruct.smi -al 9000 
  8531 candidates from fingerprint search phase
  12 molecules converted 


Calculate TPSA
~~~~~~~~~~~~~~

  *The goal of this task is get an idea of how to do a set of SMARTS matches when the data comes in from an external table.*

  *Write a function or method named "TPSA" which gets its data from the file "tpsa.tab". The function should take a molecule record as input, and return the TPSA value as a float. Use the function to calculate the TPSA of "CN2C(=O)N(C)C(=O)C1=C2N=CN1C". The answer should be 61.82, which agrees exactly with Ertl's online TPSA tool but not with PubChem's value of 58.4.*

Open Babel's command line cannot parse tables with custom formats. But the TPSA descriptor, defined by a table in the file :file:`psa.txt`, is already present and can be used as follows::

  obabel -:CN2C(=O)N(C)C(=O)C1=C2N=CN1C -osmi --append TPSA

giving::

  Cn1c(=O)n(C)c(=O)c2c1ncn2C      61.82
  1 molecule converted 

The table in :file:`tpsa.tab` and Open Babel's :file:`psa.txt` have the same content but different formats. The first few rows of :file:`tpsa.tab` are::

  psa	SMARTS	description
  23.79	[N0;H0;D1;v3]	N#
  23.85	[N+0;H1;D1;v3]	[NH]=
  26.02	[N+0;H2;D1;v3]	[NH2]-

and the equivalent lines from Open Babel's :file:`psa.txt`::

  [N]#*	23.79
  [NH]=*	23.85
  [NH2]-*	26.02

It is possible to add new descriptors without having to recompile. If another property, *myProp*, could be calculated using a table in :file:`myprop.txt` with the same format as :file:`psa.txt`, then a descriptor could set up by adding the following item to :file:`plugindefines.txt`::

  OBGroupContrib
  myProp          # name of descriptor
  myprop.txt      # data file
  Coolness index  # brief description

The following would then output molecules in increasing order of *myProp* with the value added to the title::

  obabel infile.smi -osmi --sort myProp+


Working with SD tag data
~~~~~~~~~~~~~~~~~~~~~~~~  

  *The input file is SD file from the benzodiazepine data set. Every record contains the tags PUBCHEM_CACTVS_HBOND_DONOR, PUBCHEM_CACTVS_HBOND_ACCEPTOR and PUBCHEM_MOLECULAR_WEIGHT, and most of the records contain the tag PUBCHEM_XLOGP3.*

  *The program must create a new SD file which is the same as the input file but with a new tag data field named "RULE5". This must be "1" if the record passes Lipinski's rule, "0" if it does not, and "no logP" if the PUBCHEM_XLOGP3 field is missing.*

This exercise is a bit of a stretch for the Open Babel command-line. However, the individual lines may be instructional, since they are more like the sort of task that would normally be attempted. 
::

  obabel benzodiazepine.sdf.gz -O out1.sdf --filter "PUBCHEM_CACTVS_HBOND_DONOR<=5 & 
         PUBCHEM_CACTVS_HBOND_ACCEPTOR<=10 & PUBCHEM_MOLECULAR_WEIGHT<=500 &
         PUBCHEM_XLOGP3<=5"
         --property "RULE5" "1"

  obabel benzodiazepine.sdf.gz -O out2.sdf --filter "!PUBCHEM_XLOGP3"
         --property "RULE5" "no logP"

  obabel benzodiazepine.sdf.gz -O out3.sdf --filter "!PUBCHEM_XLOGP3 &
         !(PUBCHEM_CACTVS_HBOND_DONOR<=5 & PUBCHEM_CACTVS_HBOND_ACCEPTOR<=10 &
         PUBCHEM_MOLECULAR_WEIGHT<=500 & PUBCHEM_XLOGP3<=5)"
         --property "RULE5" "0"

The first command converts only molecules passing Lipinski's rule, putting them in :file:`out1.sdf`, and adding an additional property, *RULE5*, with a value of ``1``.

The second command converts only molecules that do not have a property *PUBCHEM_XLOGP3*.

The third command converts only molecules that do have a *PUBCHEM_XLOGP3* and which fail Lipinski's rule.

Use :command:`cat` or :command:`type` at the command prompt to concatenate the three files :file:`out1.sdf`, :file:`out2.sdf`, :file:`out3.sdf`.

These operations are slow because the chemistry of each molecule is fully converted. As illustrated below, the filtering alone could have been done more quickly using the uncompressed file and the ``-aP`` option, which restricts the reading of the SDF file to the title and properties only, and then copying the molecule's SDF text verbatim with ``-o copy``. But adding the additional property is not then possible::

  obabel benzodiazepine.sdf -o copy -O out1.sdf -aP --filter
         "PUBCHEM_CACTVS_HBOND_DONOR<=5 & PUBCHEM_CACTVS_HBOND_ACCEPTOR<=10 &
         PUBCHEM_MOLECULAR_WEIGHT<=500 & PUBCHEM_XLOGP3<=5"

Unattempted tasks
~~~~~~~~~~~~~~~~~

A number of the Chemical Toolkit Rosetta tasks cannot be attempted as the :command:`obabel` tool does not (currently!) have the necessary functionality. These include the following:

* Detect and report SMILES and SDF parsing errors
* Ring counts in a SMILES file
* Unique SMARTS matches against a SMILES string
* Find the graph diameter
* Break rotatable bonds and report the fragments
* Change stereochemistry of certain atoms in SMILES file

To handle these tasks, you need to use the Open Babel library directly. This is the subject of the next section.
