Examples
========

Output Molecular Weight for a Multi-Molecule SDF File
-----------------------------------------------------

Let's say we want to print out the molecular weights of every
molecule in an SD file. Why? Well, we might want to plot a
histogram of the distribution, or see whether the average of the
distribution is significantly different (in the statistical sense)
compared to another SD file.

.. rubric:: openbabel.py

::

    from openbabel import *
    
    obconversion = OBConversion()
    obconversion.SetInFormat("sdf")
    obmol = OBMol()
    
    notatend = obconversion.ReadFile(obmol,"../xsaa.sdf")
    while notatend:
        print obmol.GetMolWt()
        obmol = OBMol()
        notatend = obconversion.Read(obmol)

.. rubric:: Pybel

::

    from pybel import *
    
    for molecule in readfile("sdf","../xsaa.sdf"):
        print molecule.molwt

Find information on all of the atoms and bonds connected to a particular atom
-----------------------------------------------------------------------------

First of all, look at all of the Classes in the Open Babel API that
end with "Iter". You should use these whenever you need to do
something like iterate over all of the atoms or bonds connected to
a particular atom, iterate over all the atoms in a molecule,
iterate over all of the residues in a protein, and so on.

As an example, let's say we want to find information on all of the
bond orders and atoms connected to a particular OBAtom called
'obatom'. The idea is that we iterate over the neighbouring atoms
using OBAtomAtomIter, and then find the bond between the
neighbouring atom and 'obatom'. Alternatively, we could have
iterated over the bonds (OBAtomBondIter), but we would need to look
at the indices of the two atoms at the ends of the bond to find out
which is the neighbouring atom:

::

    for neighbour_atom in openbabel.OBAtomAtomIter(obatom):
       print neighbour_atom.GetAtomicNum()
       bond = obatom.GetBond(neighbour_atom)
       print bond.GetBondOrder()

Examples from around the web
----------------------------

-  Noel O'Blog -
   `Hack that SD file <http://baoilleach.blogspot.com/2007/07/pybel-hack-that-sd-file.html>`_,
   Just How Unique are your Molecules
   `Part I <http://baoilleach.blogspot.com/2007/07/pybel-just-how-unique-are-your.html>`_
   and
   `Part II <http://baoilleach.blogspot.com/2007/07/pybel-just-how-unique-are-your_12.html>`_,
   `Calculate circular fingerprints with Pybel <http://baoilleach.blogspot.com/2008/02/calculate-circular-fingerprints-with.html>`_,
   `Molecular Graph-ics with Pybel <http://baoilleach.blogspot.com/2008/10/molecular-graph-ics-with-pybel.html>`_,
   and
   `Generating InChI's Mini-Me, the InChIKey <http://baoilleach.blogspot.com/2008/10/generating-inchis-mini-me-inchikey.html>`_.
-  `Filter erroneous structures from the ZINC database <http://blur.compbio.ucsf.edu/pipermail/zinc-fans/2007-September/000293.html>`_
-  Quantum Pharmaceuticals -
   `Investigation of datasets for hERG binding <http://drugdiscoverywizzards.blogspot.com/2007/12/how-good-are-biological-experiments.html>`_
-  cclib - Given the coordinates, charge, and multiplicity,
   `how to create the corresponding OBMol <http://cclib.svn.sourceforge.net/viewvc/cclib/tags/cclib-0.8/src/cclib/bridge/cclib2openbabel.py?view=markup>`_
-  Florian Nigsch wrote an implementation of `Murcko fragments <http://flo.nigsch.com/?p=29>`_ using Pybel
-  Andrew Dalke's `Chemical Toolkit Rosetta <http://ctr.wikia.com/wiki/Chemistry_Toolkit_Rosetta_Wiki>`_ contains several examples of Python code using openbabel.py and pybel

Invert a particular stereocenter in a series of molecules
---------------------------------------------------------

The following was a request on the
`CCL.net <http://www.ccl.net/cgi-bin/ccl/message-new?2008+03+20+005>`__
list:

    I am looking for any program which can specifically change or
    invert the stereocenter. I have a lot of compounds to work with.
    All those compounds have more than one stereocenters. I want to
    invert one stereocenter which is common in all compounds. So,
    precisely, my problem is to change a carbon's stereocenter from "S"
    to "R" and need to do this thing for all of compounds in database.

OBAtom has methods to interrogate and alter an atom's
stereochemistry. If you use a SMARTS query to find the target atom,
it's easy to change it.:

::

    import pybel
    
    smarts = pybel.Smarts("C[C@](O)CC(=O)O")
    inverse = pybel.Smarts("C[C@@](O)CC(=O)O")
    
    outputfile = pybel.Outputfile("sdf", "output.sdf")
    for mol in pybel.readfile("smi", "3_p0.smi"):
       matches = smarts.findall(mol)
       if matches:
           firstmatch = matches[0]
           matchingatom = firstmatch[1]
           mol.OBMol.GetAtom(matchingatom).SetClockwiseStereo()
           assert inverse.findall(mol), "Hasn't been inverted!"
           outputfile.write(mol)
    outputfile.close()

Split an SDF file using the molecule titles
-------------------------------------------

The following was a request on the
`CCL.net <http://ccl.net/cgi-bin/ccl/message-new?2009+10+22+002>`__
list:

    Hi all, Does anyone have a script to split an SDFfile into single
    sdfs named after each after each individual molecule as specified
    in first line of parent multi file?

The solution is simple...

::

    import pybel
    for mol in pybel.readfile("sdf", "bigmol.sdf"):
       mol.write("sdf", "%s.sdf" % mol.title)

An implementation of RECAP
--------------------------

TJ O'Donnell (of `gNova <http://www.gnova.com/>`_) has written an
implementation of the RECAP fragmentation algorithm in 130 lines of
Python. The code is at `[1] <http://gist.github.com/95387>`_.

TJ's book,
"`Design and Use of Relational Databases in Chemistry <http://www.amazon.com/Design-Use-Relational-Databases-Chemistry/dp/1420064428/ref=sr_1_1?ie=UTF8&s=books&qid=1221754435&sr=1-1>`_",
also contains examples of Python code using Open Babel to create and
query molecular databases (see for example the link to Open Babel
code in the `Appendix <http://www.gnova.com/book/>`_).
