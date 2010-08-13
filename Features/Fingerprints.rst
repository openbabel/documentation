.. _fingerprints:

Molecular fingerprints and similarity searching
===============================================

Molecular fingerprints encode molecular structure in a series of binary digits (bits) that represent the presence or absence of particular substructures in the molecule. Comparing fingerprints will allow you to determine the similarity between two molecules, search databases, etc., but does not include full structural data (such as coordinates). 

The Open Babel fingerprints can be accessed through the following Utility file formats:

* :ref:`Fingerprint_format`: the path-based fingerprint FP2; substructure based fingerprints FP2, FP3 and MACCS; user-defined substructures 
* :ref:`Multilevel_Neighborhoods_of_Atoms_(MNA)`: a circular fingerprint
* :ref:`MolPrint2D_format`: a circular fingerprint

Here we will focus on the first one, the *fingerprint format*. For the others, please see the relevant sections listed above.

Available fingerprints
----------------------

You can see the available fingerprints by typing the following command::

        $ babel -L fingerprints
        FP2    Indexes linear fragments up to 7 atoms.
        FP3    SMARTS patterns specified in the file patterns.txt
        FP4    SMARTS patterns specified in the file SMARTS_InteLigand.txt
        MACCS    SMARTS patterns specified in the file MACCS.txt

At present there are four types of fingerprints:

* **FP2**, a path-based fingerprint which indexes small molecule fragments based on linear segments of up to 7 atoms (somewhat similar to the Daylight fingerprints):

    A molecule structure is analysed to identify linear fragments of length from 1-7 atoms. Single atom fragments of C, N, and O are ignored. A fragment is terminated when the atoms form a ring.

    For each of these fragments the atoms, bonding and whether they constitute a complete ring is recorded and saved in a set so that there is only one of each fragment type. Chemically identical versions, (i.e. ones with the atoms listed in reverse order and rings listed starting at different atoms) are identified and only a single canonical fragment is retained.

    Each remaining fragment is assigned a hash number from 0 to 1020 which is used to set a bit in a 1024 bit vector 
  
* **FP3** uses a series of SMARTS queries stored in :file:`patterns.txt`
* **FP4** uses a series of SMARTS queries stored in :file:`SMARTS_InteLigand.txt`
* **MACCS** uses the SMARTS patterns in :file:`MACCS.txt`

.. note::

        Note that you can tailor the latter three fingerprints to your own needs by adding your own SMARTS queries to these files. On UNIX and Mac systems, these files are frequently found in :file:`/usr/local/share/openbabel` under a directory for each version of Open Babel. 

Similarity searching
--------------------

Small datasets
~~~~~~~~~~~~~~

For relatively small datasets (<10,000's) it is possible to do similarity searches without the need to build a similarity index, however larger datasets (up to a few million) can be searched rapidly once a fastsearch index has been built.

On small datasets these fingerprints can be used in a variety of ways. The following command gives you the Tanimoto coefficient between a SMILES string in mysmiles.smi and all the molecules in mymols.sdf::

        babel  mysmiles.smi  mymols.sdf -ofpt

        MOL_00000067   Tanimoto from first mol = 0.0888889
        MOL_00000083   Tanimoto from first mol = 0.0869565
        MOL_00000105   Tanimoto from first mol = 0.0888889
        MOL_00000296   Tanimoto from first mol = 0.0714286
        MOL_00000320   Tanimoto from first mol = 0.0888889
        MOL_00000328   Tanimoto from first mol = 0.0851064
        MOL_00000338   Tanimoto from first mol = 0.0869565
        MOL_00000354   Tanimoto from first mol = 0.0888889
        MOL_00000378   Tanimoto from first mol = 0.0816327
        MOL_00000391   Tanimoto from first mol = 0.0816327
        11 molecules converted

The default fingerprint used is the FP2 fingerprint. You change the fingerprint using the ``f`` output option as follows::

        babel mymols.sdf -ofpt -xfFP3

The ``-s`` option of babel is used to filter by SMARTS string (see Babel). If you wanted to know the similarity only to the substituted bromobenzenes in mymols.sdf then you might combine commands like this (note: if the query molecule does not match the SMARTS string this will not work as expected, as the first molecule in the database that matches the SMARTS string will instead be used as the query)::

        babel mysmiles.smi mymols.sdf -ofpt -s c1ccccc1Br

        MOL_00000067   Tanimoto from first mol = 0.0888889
        MOL_00000083   Tanimoto from first mol = 0.0869565
        MOL_00000105   Tanimoto from first mol = 0.0888889

If you don't specify a query file, babel will just use the first molecule in the database as the query::

        babel mymols.sdf  -ofpt

        MOL_00000067
        MOL_00000083   Tanimoto from MOL_00000067 = 0.810811
        MOL_00000105   Tanimoto from MOL_00000067 = 0.833333
        MOL_00000296   Tanimoto from MOL_00000067 = 0.425926
        MOL_00000320   Tanimoto from MOL_00000067 = 0.534884
        MOL_00000328   Tanimoto from MOL_00000067 = 0.511111
        MOL_00000338   Tanimoto from MOL_00000067 = 0.522727
        MOL_00000354   Tanimoto from MOL_00000067 = 0.534884
        MOL_00000378   Tanimoto from MOL_00000067 = 0.489362
        MOL_00000391   Tanimoto from MOL_00000067 = 0.489362
        10 molecules converted 

Large datasets
~~~~~~~~~~~~~~

On larger datasets it is necessary to first build a fastsearch index. This is an new file that stores a database of fingerprints for the files indexed. You will still need to keep both the new .fs fastsearch index and the original files. However, the new index will allow significantly faster searching and similarity comparisons. The index is created with the following command::

        babel mymols.sdf -ofs

This builds mymols.fs with the default fingerprint (unfolded). The following command uses the index to find the 5 most similar molecules to the molecule in query.mol::

        babel mymols.fs results.sdf -squery.mol -at5

or to get the matches with Tanimoto>0.6 to 1,2-dicyanobenzene::

        babel mymols.fs results.sdf -sN#Cc1ccccc1C#N -at0.6

Substructure searching
----------------------

Small datasets
~~~~~~~~~~~~~~

This command will find all molecules containing 1,2-dicyanobenzene and return the results as SMILES strings::

        babel mymols.sdf -sN#Cc1ccccc1C#N results.smi

If all you want output are the molecule names then adding ``-xt`` will return just the molecule names::

        babel mymols.sdf -sN#Cc1ccccc1C#N results.smi -xt

The parameter of the -s option in these examples is actually SMARTS, which allows a richer matching specification, if required. It does mean that the aromaticity of atoms and bonds is significant; use `[#6]` rather than `C` to match both aliphatic and aromatic carbon.

The -s option's parameter can also be a file name with an extension. The file must contain a molecule, which means only substructure matching is possible (rather than full SMARTS). The matching is also slightly more relaxed with respect to aromaticity.

Large datasets
~~~~~~~~~~~~~~

First of all, you need to create a fastsearch index (see above). The index is created with the following command::

        babel mymols.sdf -ofs

Substructure searching is as for small datasets, except that the fastsearch index is used instead of the original file. This command will find all molecules containing 1,2-dicyanobenzene and return the results as SMILES strings::

        babel mymols.fs -ifs -sN#Cc1ccccc1C#N results.smi

If all you want output are the molecule names then adding ``-xt`` will return just the molecule names::

        babel mymols.fs -ifs -sN#Cc1ccccc1C#N results.smi -xt

Case study: Search ChEMBLdb
---------------------------

This case study uses a combination of the techniques described above for similarity searching using large databases and using small databases. Note that we are using the default fingerprint for all of these analyses. The default fingerprint is FP2, a path-based fingerprint (somewhat similar to the Daylight fingerprints).

(1) Download Version 2 of ChEMBLdb from ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/.

(2) After unzipping it, make a fastsearch index (this took 18 minutes on my machine, for the 500K+ molecules)::

        babel chembl_02.sdf -ofs

(3) Let's use the first molecule in the sdf file as a query. Using Notepad (or on Linux, ``head -79 chembl_02.sdf``) extract the first molecule and save it as :file:`first.sdf`. Note that the molecules in the ChEMBL sdf do not have titles; instead, their IDs are stored in the "chebi_id" property field.

(4) This first molecule is 100183. Check its `ChEMBL page`_. It's pretty weird, but is there anything similiar in ChEMBLdb? Let's find the 5 most similar molecules::

        babel chembl_02.fs mostsim.sdf -s first.sdf -at5

.. _ChEMBL page: http://www.ebi.ac.uk/chembldb/index.php/compound/inspect/100183

(5) The results are stored in :file:`mostsim.sdf`, but how similar are these molecules to the query?::

        babel first.sdf mostsim.sdf -ofpt
        >
        >   Tanimoto from first mol = 1
        Possible superstructure of first mol
        >   Tanimoto from first mol = 0.986301
        >   Tanimoto from first mol = 0.924051
        Possible superstructure of first mol
        >   Tanimoto from first mol = 0.869048
        Possible superstructure of first mol
        >   Tanimoto from first mol = 0.857143
        6 molecules converted
        76 audit log messages

(6) That's all very well, but it would be nice to show the ChEBI IDs. Let's set the title field of :file:`mostsim.sdf` to the content of the "chebi_id" property field, and repeat step 5::

        babel mostsim.sdf mostsim_withtitle.sdf --append "chebi_id"
        babel first.sdf mostsim_withtitle.sdf -ofpt
        >
        >100183   Tanimoto from first mol = 1
        Possible superstructure of first mol
        >124893   Tanimoto from first mol = 0.986301
        >206983   Tanimoto from first mol = 0.924051
        Possible superstructure of first mol
        >207022   Tanimoto from first mol = 0.869048
        Possible superstructure of first mol
        >607087   Tanimoto from first mol = 0.857143
        6 molecules converted
        76 audit log messages

(7) Here are the ChEMBL pages for these molecules: 100183_, 124893_, 206983_, 207022_, 607087_. I think it is fair to say that they are pretty similiar. In particular, the output states that 206983 and 207022 are possible superstructures of the query molecule, and that is indeed true. 

.. _100183: http://www.ebi.ac.uk/chembldb/index.php/compound/inspect/100183
.. _124893: http://www.ebi.ac.uk/chembldb/index.php/compound/inspect/124893
.. _206983: http://www.ebi.ac.uk/chembldb/index.php/compound/inspect/206983
.. _207022: http://www.ebi.ac.uk/chembldb/index.php/compound/inspect/207022
.. _607087: http://www.ebi.ac.uk/chembldb/index.php/compound/inspect/607087

(8) How many of the molecules in the dataset are superstructures of the molecule in `first.sdf`? To do this and to visualize the large numbers of molecules produced, we can output to `SVGFormat` ::

        obabel chembl_02.fs  -O out.svg  -s first.sdf

Note that :program:`obabel` has been used here because of its more flexible option handling.
This command does a substructure search and puts the 47 matching structures in the file out.svg. This can be viewed in a browser like Firefox, Opera or Chrome (but not Internet Explorer). The display will give an overall impression of the set of molecules but details can be seen by zooming in with the mousewheel and panning by dragging with a mouse button depressed.

(9) The substructure that is being matched can be highlighted in the output molecules by adding another parameter to the -s option. Just for variety, the display is also changed to a black background, 'uncolored' (no element-specific coloring), and terminal carbon not shown explicitly. (Just refresh your browser to see the modified display.)

        obabel chembl_02.fs  -O out.svg  -s first.sdf green  -xb -xu -xc

This highlighting option also works when  the -s option is used without fastsearch on small datasets.

(10) The substructure search here has two stages.  The indexed fingerprint search quickly produces 62 matches from the 500K+ molecules in the dataset. Each of these is then checked by a slow detailed isomorphism check. There are 12 false positives from the fingerprint stage. These are of no significance, but you can see them by ::
 
        obabel chembl_02.fs  -O out.svg  -s ~first.sdf


