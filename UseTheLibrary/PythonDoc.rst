.. _openbabel python module:

The openbabel module
====================

The **openbabel** module provides direct access to the C++ Open
Babel library from Python. This binding is generated using the SWIG
package and provides access to almost all of the Open Babel
interfaces via Python, including the base classes OBMol, OBAtom,
OBBond, and OBResidue, as well as the conversion framework
OBConversion. As such, essentially any call in the C++ API is
available to Python scripts with very little difference in syntax.
As a result, the principal documentation is the
:ref:`C++ API documentation <API>`.

Examples
^^^^^^^^

Here we give some examples of common Python syntax for the
``openbabel`` module and pointers to the appropriate sections of
the API documentation.

The example script below creates atoms and bonds one-by-one using
the
:obapi:`OBMol`, :obapi:`OBAtom`, and :obapi:`OBBond` classes.

.. highlight:: python

::

     from openbabel import openbabel
    
     mol = openbabel.OBMol()
     print(mol.NumAtoms()) #Should print 0 (atoms)
    
     a = mol.NewAtom()
     a.SetAtomicNum(6)   # carbon atom
     a.SetVector(0.0, 1.0, 2.0) # coordinates
    
     b = mol.NewAtom()
     mol.AddBond(1, 2, 1)   # atoms indexed from 1
     print(mol.NumAtoms()) #Should print 2 (atoms)
     print(mol.NumBonds()) Should print 1 (bond)
    
     mol.Clear();

More commonly, Open Babel can be used to read in molecules using
the :obapi:`OBConversion`
framework. The following script reads in molecular information (a
SMI file) from a string, adds hydrogens, and writes out an MDL file
as a string.

::

    from openbabel import openbabel
    
    obConversion = openbabel.OBConversion()
    obConversion.SetInAndOutFormats("smi", "mdl")
     
    mol = openbabel.OBMol()
    obConversion.ReadString(mol, "C1=CC=CS1")
    
    print(mol.NumAtoms()) #Should print 5 (atoms)
    
    mol.AddHydrogens()
    print(mol.NumAtoms()) Should print 9 (atoms) after adding hydrogens
    
    outMDL = obConversion.WriteString(mol)

The following script writes out a file using a filename, rather
than reading and writing to a Python string.

::

    from openbabel import openbabel
    
    obConversion = openbabel.OBConversion()
    obConversion.SetInAndOutFormats("pdb", "mol2")
    
    mol = openbabel.OBMol()
    obConversion.ReadFile(mol, "1ABC.pdb.gz")   # Open Babel will uncompress automatically
    
    mol.AddHydrogens()
    
    print(mol.NumAtoms())
    print(mol.NumBonds())
    print(mol.NumResidues())
    
    obConversion.WriteFile(mol, '1abc.mol2')

Using iterators
^^^^^^^^^^^^^^^

A number of Open Babel toolkit classes provide iterators over
various objects; these classes are identifiable by the suffix
"Iter" in the
`list of toolkit classes <http://openbabel.sourceforge.net/api/current/annotated.shtml>`_
in the API:

-  `OBAtomAtomIter <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBAtomAtomIter.shtml>`_
   and
   `OBAtomBondIter <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBAtomBondIter.shtml>`_
   - given an OBAtom, iterate over all neighboring OBAtoms or OBBonds
-  `OBMolAtomIter <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBMolAtomIter.shtml>`_,
   `OBMolBondIter <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBMolBondIter.shtml>`_,
   `OBMolAngleIter <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBMolAngleIter.shtml>`_,
   `OBMolTorsionIter <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBMolTorsionIter.shtml>`_,
   `OBMolRingIter <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBMolRingIter.shtml>`_
   - given an OBMol, iterate over all OBAtoms, OBBonds, OBAngles,
   OBTorsions or OBRings.
-  `OBMolAtomBFSIter <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBMolAtomBFSIter.shtml>`_
   - given an OBMol and the index of an atom, OBMolAtomBFSIter
   iterates over all the neighbouring atoms in a breadth-first manner.
   It differs from the other iterators in that it returns two values -
   an OBAtom, and the 'depth' of the OBAtom in the breadth-first
   search (this is useful, for example, when creating circular
   fingerprints)
-  `OBMolPairIter <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBMolPairIter.shtml>`_
   - given an OBMol, iterate over all pairs of OBAtoms separated by
   more than three bonds
-  `OBResidueIter <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBResidueIter.shtml>`_
   - given an OBMol representing a protein, iterate over all
   OBResidues
-  `OBResidueAtomIter <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBResidueAtomIter.shtml>`_
   - given an OBResidue, iterate over all OBAtoms

These iterator classes can be used using the typical Python syntax
for iterators:

::

    for obatom in openbabel.OBMolAtomIter(obmol):
        print(obatom.GetAtomicMass())

Note that OBMolTorsionIter returns atom IDs which are off by one.
That is, you need to add one to each ID to get the correct ID.
Also, if you add or remove atoms, you will need to delete the
existing TorsionData before using OBMolTorsionIter. This is done as
follows:
::

    mol.DeleteData(openbabel.TorsionData)

Calling a method requiring an array of C doubles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some Open Babel toolkit methods, for example :obapi:`OBMol::Rotate() <OpenBabel::OBMol::Rotate>`,
require an array of doubles. It's not possible to directly use a
list of floats when calling such a function from Python. Instead,
you need to first explicitly create a C array using the
*double\_array()* function:

::

    obMol.Rotate([1.0, -54.7, 3])
    # Error!
    myarray = openbabel.double_array([1.0, -54.7, 3])
    obMol.Rotate(myarray)
    # Works!

Accessing OBPairData, OBUnitCell and other OBGenericData
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to access any subclass of OBGenericData (such as :obapi:`OBPairData`
or :obapi:`OBUnitCell`)
associated with a molecule, you need to 'cast' the :obapi:`OBGenericData`
returned by :obapi:`OBMol.GetData() <OpenBabel::OBMol::GetData>` using the *toPairData()*, *toUnitCell()* (etc.)
functions:

::

    pairdata = [openbabel.toPairData(x) for x in obMol.GetData() 
                if x.GetDataType()==openbabel.PairData]
    print(pairdata[0].GetAttribute(), pairdata[0].GetValue())
    
    unitcell = openbabel.toUnitCell(obMol.GetData(openbabel.UnitCell))
    print(unitcell.GetAlpha(), unitcell.GetSpaceGroup())

Using FastSearch from Python
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Rather than use the :obapi:`FastSearch` class directly, it's easiest to use the :obapi:`OpenInAndOutFiles() <OpenBabel::OBConversion::OpenInAndOutFiles>` method as follows::

 >>> from openbabel import openbabel
 >>> conv=openbabel.OBConversion()
 >>> conv.OpenInAndOutFiles("1200mols.smi","index.fs")
 True
 >>> conv.SetInAndOutFormats("smi","fs")
 True
 >>> conv.Convert()
 This will prepare an index of 1200mols.smi and may take some time...
 It took 6 seconds
 1192
 >>> conv.CloseOutFile()
 >>> conv.OpenInAndOutFiles("index.fs","results.smi")
 True
 >>> conv.SetInAndOutFormats("fs","smi")
 True
 >>> conv.AddOption("s",conv.GENOPTIONS,"C=CC#N")
 >>> conv.Convert()
 10 candidates from fingerprint search phase
 1202
 >>> f=open("results.smi")
 >>> f.read()
 'OC(=O)C(=Cc1ccccc1)C#N\t298\nN#CC(=Cc1ccccc1)C#N\t490\nO=N(=O)c1cc(ccc1)C=C(C#N
 )C#N\t491\nClc1ccc(cc1)C=C(C#N)C#N\t492\nClc1ccc(c(c1)Cl)C=C(C#N)C#N\t493\nClc1c
 cc(cc1Cl)C=C(C#N)C#N\t494\nBrc1ccc(cc1)C=C(C#N)C#N\t532\nClc1ccccc1C=C(C#N)C#N\t
 542\nN#CC(=CC=Cc1occc1)C#N\t548\nCCOC(=O)C(C#N)=C(C)C\t1074\n'

Combining numpy with Open Babel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are using the Python numerical extension, numpy, and you try
to pass values from a numpy array to Open Babel, it may not work
unless you convert the values to Python built-in types first:

::

    import numpy
    from openbabel import openbabel
    
    mol = openbabel.OBMol()
    atom = mol.NewAtom()
    
    coord = numpy.array([1.2, 2.3, 4.6], "float32")
    atom.SetVector(coord[0], coord[1], coord[2])
    # Error
    
    atom.SetVector(float(coord[0]), float(coord[1]), float(coord[2]))
    # No error
    
    coord = numpy.array([1.2, 2.3, 4.6], "float64")
    atom.SetVector(coord[0], coord[1], coord[2])
    # No error either - not all numpy arrays will cause an error
