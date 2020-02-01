Stereochemistry
===============

As with most chemistry toolkits, Open Babel stores stereochemistry as the relative arrangement of atoms in space rather than using the IUPAC system of R/S (etc) to describe absolute stereochemistry. For example, for a tetrahedral stereocenter, we store information like "looking from atom 2, atoms 4, 5 and 6 are arranged clockwise around atom 3". At first, this might seem surprising and much more verbose; but the IUPAC system was designed for generating systematic IUPAC names and *not* for storing stereo information. In contrast, storing stereochemistry does not require any calculation (this information is provided by the file format), it is fairly simple to understand (unlike the IUPAC system), and it is unaffected by changes to other atoms in a molecule (unlike the IUPAC system). It is also the most common way for chemists to communicate stereo information - consider wedge/hash bonds and layout of double bonds in a chemical depiction.

In Open Babel, stereochemistry information is stored as a property of the molecule as StereoData. Often we are interested in the stereo associated with a particular atom or bond; to simplify access to this, a facade class OBStereoFacade is provided.

An Open Babel atom has an index (``OBAtom::GetIdx()``) and an Id (``OBAtom::GetId()``). The former runs from 1 to the number of atoms. The latter can be anything (don't assume it's the Idx-1), but are unique within the molecule. If you delete an atom, the indices change, but the Ids do not. For this reason, all stereo is stored using Ids so that stereo information is not invalidated by changes to the molecule. The key point here is that all methods related to stereo use atom Ids and not atom indices.

When the stereochemistry description involves implicit hydrogens or lone pairs, the special atom Id ``OBStereo::ImplicitRef`` (numerically, ``-2`` or ``4294967294`` if accessed via the bindings) is used.

Basic access
------------

Let's read the SMILES string ``F[C@@](Cl)(Br)I`` and access the stereo. When we read this SMILES string, the tetrahedral center will be the second atom, that with Idx 2.::

    smi = "F[C@@](Cl)(Br)I"
    mol = pybel.readstring("smi", smi).OBMol
    secondatom = mol.GetAtom(2)
    atomid = secondatom.GetId()

    stereofacade = ob.OBStereoFacade(mol)
    print("Does this atom have tet stereo info?", stereofacade.HasTetrahedralStereo(atomid))
    tetstereo = stereofacade.GetTetrahedralStereo(atomid)
    config = tetstereo.GetConfig()
    print("The stereocenter is at atom Id {}".format(config.center))
    print("Is the configuration specified? {}".format("Yes" if config.specified else "No")
    print("Looking from atom Id {0}, the atoms Ids {1} are arranged clockwise".format(config.from_or_towards, config.refs)) 

Which prints...::

        Does this atom have tet stereo info? True
        The stereocenter is at atom Id 1
        Is the configuration specified? Yes
        Looking from atom Id 0, the atoms Ids (2, 3, 4) are arranged clockwise

How do I know that I'm looking from atom Id 0, and that the atom Ids are arranged clockwise? From the documentation for GetConfig() for tetrahedral stereocenters, which states that this is the default. If you want instead the anticlockwise arrangement of atoms looking *towards* the atom with Id 0, you can get that as follows::

   config = tetstereo.GetConfig(0, ob.OBStereo.AntiClockwise, ob.OBStereo.ViewTowards)
   print("Looking towards atom Id {0}, the atoms Ids {1} are arranged anticlockwise".format(config.from_or_towards, config.refs))

Which prints::

  Looking towards atom Id 0, the atoms Ids (2, 3, 4) are arranged anticlockwise

Note that every time you create a new OBStereoFacade, a certain amount of work is done building up the correspondance between atoms/bonds and stereo data. For this reason, a single OBStereoFacade should be created for a molecule and reused.

SMILES strings
--------------

Open Babel's SMILES reader supports atom-based tetrahedral and bond-based cis/trans stereochemistry.

Modifying stereochemistry
-------------------------

.. rubric: Molecules without coordinates

The object returned by GetConfig() contains the full description of the stereochemistry of a particular atom or bond. This is a copy of the data associated with the OBMol, and so modifying it has no effect; instead, SetConfig() is used to copy the modified data back to the OBMol.
