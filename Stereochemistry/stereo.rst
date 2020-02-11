Stereochemistry
===============

Open Babel stores stereochemistry as the relative arrangement of a set of atoms in space. For example, for a tetrahedral stereocenter, we store information like "looking from atom 2, atoms 4, 5 and 6 are arranged clockwise around atom 3". This section describes how a user can work with or manipulate this information. This might be useful to invert a particular center, replace a substituent at a stereocenter, enumerate stereoisomers or determine the number of unspecified stereocenters.

Although Open Babel has data structures to support a variety of forms of stereochemistry, currently little use is made of any stereochemistry other than tetrahedral and cis/trans (and square planar to a certain degree).

We will look first of all at how stereochemistry information is stored and accessed, and then at how this information is converted to/from particular file formats.

Accessing stereochemistry information
-------------------------------------

Each record of stereochemistry information around an atom or bond is stored as StereoData associated with the OBMol. First of all, let's look at direct access to the StereoData. The following code counts the number of tetrahedral centers with specified stereochemistry, as well as the number of double bonds with specified cis/trans stereochemistry::

        num_cistrans = 0
        num_tetra = 0

        mol = pybel.readstring("smi", "F/C=C/C[C@@H](Cl)Br")
        m = mol.OBMol

        for genericdata in m.GetAllData(ob.StereoData):
            stereodata = ob.toStereoBase(genericdata)
            stereotype = stereodata.GetType()

            if stereotype == ob.OBStereo.CisTrans:
                cistrans = ob.toCisTransStereo(stereodata)
                if cistrans.IsSpecified():
                    num_cistrans += 1

            elif stereotype == ob.OBStereo.Tetrahedral:
                tetra = ob.toTetrahedralStereo(stereodata)
                if tetra.IsSpecified():
                    num_tetra += 1

.. sidebar:: Atom and Bond Ids

        All of the stereo handling code uses Ids to reference atoms and bonds, rather than indices. An Open Babel atom has an index (``OBAtom::GetIdx()``) and an Id (``OBAtom::GetId()``). The former runs from 1 to the number of atoms. The latter can be anything (don't assume it's the Idx-1), but is unique within the molecule. If you delete an atom, the indices change, but the Ids do not. For this reason, all stereo is stored using Ids so that stereo information is not invalidated by changes to the molecule. When the stereochemistry description involves implicit hydrogens or lone pairs, the special atom Id ``OBStereo::ImplicitRef`` (numerically, ``-2`` or ``4294967294`` if accessed via the bindings) is used.

The code above is quite verbose, and requires iteration through all of the stereo data. To make it simpler to access stereo data for a particular atom or bond, a facade class OBStereoFacade can instead be used, which provides convenience functions for these operations.::

        num_cistrans = 0
        num_tetra = 0

        mol = pybel.readstring("smi", "F/C=C/C[C@@H](Cl)Br")
        m = mol.OBMol

        facade = ob.OBStereoFacade(m)

        for atom in ob.OBMolAtomIter(m):
            mid = atom.GetId()
            if facade.HasTetrahedralStereo(mid):
                tetra = facade.GetTetrahedralStereo(mid)
                if tetra.IsSpecified():
                    num_tetra += 1

        for bond in ob.OBMolBondIter(m):
            mid = bond.GetId()
            if facade.HasCisTransStereo(mid):
                cistrans = facade.GetCisTransStereo(mid)
                if cistrans.IsSpecified():
                    num_cistrans += 1

Note that every time you create a new OBStereoFacade, a certain amount of work is done building up the correspondance between atoms/bonds and stereo data. For this reason, a single OBStereoFacade should be created for a molecule and reused.

The stereo configuration
------------------------

The examples above introduce the Config object, which contains the description of the stereochemistry. The contents of this object will be different depending on the specific type of stereochemistry, e.g. ``OBCisTransStereo::Config`` (``OBCisTransConfig`` from Python) records the begin and end Ids of the associated bond, the Ids of the attached atoms, the spatial relationship of those atoms, and whether stereo is specified.

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

How do I know that I'm looking from atom Id 0, and that the atom Ids are arranged clockwise? From the documentation for ``OBTetrahedralStereo::GetConfig``, which states that this is the default. It is worth pointing out that you should never need to test the value of the winding, the direction, or the from/towards atom; the values of these will be whatever you asked for. If you instead ask for the anticlockwise arrangement of atoms looking *towards* the atom with Id 0, you can get that as follows::

   config = tetstereo.GetConfig(0, ob.OBStereo.AntiClockwise, ob.OBStereo.ViewTowards)
   print("Looking towards atom Id {0}, the atoms Ids {1} are arranged anticlockwise".format(config.from_or_towards, config.refs))

Which prints::

  Looking towards atom Id 0, the atoms Ids (2, 3, 4) are arranged anticlockwise

It should be noted that the Config objects returned by GetConfig() are *copies* of the stereo configuration. That is, modifying them has no affect on the stereochemistry of the molecule (see the next section). As a result, it is straightforward to keep a copy of the stereo configuration, modify the molecule, and then check whether the modification has altered the stereochemistry using the equality operator of the Config.

Modifying the stereochemistry
-----------------------------

We will talk later about the interaction between 2D and 3D structural information and how stereochemistry is perceived and recorded. For now, let's avoid these issues by using a 0D structure and modifying its stereochemistry.::

        from openbabel import pybel
        ob = pybel.ob

        mol = pybel.readstring("smi", "C[C@@H](Cl)F")
        print(mol.write("smi", opt={"nonewline": True}))

        # Invert the stereo
        m = mol.OBMol
        facade = ob.OBStereoFacade(m)
        tetstereo = facade.GetTetrahedralStereo(m.GetAtom(2).GetId())
        config = tetstereo.GetConfig()
        config.winding = ob.OBStereo.AntiClockwise
        tetstereo.SetConfig(config)
        print(mol.write("smi", opt={"nonewline": True}))

        config.specified = False
        tetstereo.SetConfig(config)
        print(mol.write("smi", opt={"nonewline": True}))

which prints...::

        C[C@@H](Cl)F
        C[C@H](Cl)F
        CC(Cl)F

How did I know that setting the relative arrangement to anti-clockwise would invert the stereo? Again, as described above, by default GetConfig() returns the atoms in clockwise order. Another way to invert the stereo would be to swap two of the refs, or to set the direction from 'from' to 'towards'.

Stereo perception
-----------------

Until now we have not mentioned where this stereo information came from; we have read a SMILES string and somehow the resulting molecule has stereo data associated with it.

Stereo perception is the identification of stereo centers from the molecule and its associated data, which may include 3D coordinates, stereobonds and existing stereo data. Passing an OBMol to the global function ``PerceiveStereo`` triggers stereo perception, and sets a flag marking stereo as perceived (``OBMol::SetChiralityPerceived(true)``). If, in the first place, stereo was already marked as perceived then stereo perception is not performed. Any operations that require stereo information should call PerceiveStereo before accessing stereo information.

Behind the scenes, the code for stereo perception is quite different depending on the dimensionality (``OBMol::GetDimension()``) of the molecule.

.. rubric:: 3D structures

Perhaps the most straightforward is when the structure has 3D coordinates. In this case, a symmetry analysis identifies stereogenic centers and their stereoconfigurations are perceived from the coordinates. Some file formats such as the MOL file allow atoms and double bonds to be marked as have unspecified stereochemistry, and this information is applied to the detected stereocenters. For the specific case of the MOL file, the atom flag that marks this is ignored by default (as required by the specification) but an option (``s``) is provided to read it::

        $ obabel -:"I/C=C/C[C@@](Br)(Cl)F" --gen3d -omol | obabel -imol -osmi
        I/C=C/C[C@@](Br)(Cl)F
        $ obabel -:"IC=CCC(Br)(Cl)F" --gen3d -omol | obabel -imol -osmi
        IC=CC[C@@](Br)(Cl)F
        $ obabel -:"IC=CCC(Br)(Cl)F" --gen3d -omol | obabel -imol -as -osmi
        IC=CCC(Br)(Cl)F

As just described, the flow of information is from the 3D coordinates to Open Babel's internal record of stereo centers, and this flow is triggered by calling stereo perception (which does nothing if the stereo is marked as already perceived). It follows from this that altering the coordinates *after* stereo perception (e.g. by reflecting through an axis, thereby inverting chirality) has no affect on the internal stereo data. If operations are performed on the molecule that require stereo is be reperceived, then ``OBMol::SetChiralityPerceived(false)`` should be called.

It should also be clear from the discussion above that changing the stereodata (e.g. using SetConfig() to invert a tetrahedral stereocenter) has no affect on the molecule's coordinates (though it may affect downstream processing, such as the information written to a SMILES string). If this is needed, the user will have to manipulate the coordinates themselves, or generate coordinates for the whole molecule using the associated library functions (e.g. the ``--gen3d`` operation).

.. rubric:: 2D structures

2D structures represent a depiction of a molecule, and stereochemistry is indicated by wedge or hash bonds, or by adopting particular conventions (e.g. Fischer or Haworth projection of monosaccharides). Open Babel does not support any of these conventions, nor does it support the use of wedge or hash bonds for perspective drawing (e.g. where a thick bond is support by two wedges). This may change in future, of course, but it's worth noting that Open Babel is not the only toolkit with these limitations and so what you think you are storing in your database may not be what the 'computer' thinks it is.

Stereo centers are identified based on a symmetry analysis, and their configuration inferred either from the geometry (for cis/trans bonds) or from bonds marked as wedge/hash (tetrahedral centers). File format readers record information about which bonds were marked as wedges or hashes and this can be accessed with OBBond:IsWedge/IsHash, where the Begin atom of the bond is considered the origin of the wedge/hash. Similar to the situation with 3D perception, changing a bond from a wedge to a hash (or vice versa) has no affect on the stereo objects once stereo has been perceived, but triggering reperception will regenerate the desired stereo data.

It should also be noted that the file writers regenerate the wedges or hashes from the stereo data at the point of writing; in other words, the particular location of the wedge/hash or even whether it is present may change on writing. This was done to ensure that the written structure accurately represents Open Babel's internal view of the molecule; passing wedges/hashes through unchanged may not represent this (consider the case where a wedge bond is attached to a tetrahedral center which cannot be a stereocenter).

.. rubric:: 0D structures

A SMILES string is sometimes referred to as describing a 0.5D structure, as it can describe the relative arrangement of atoms around stereocenters. The SMILES reader simply reads and records this information as stereo data, and then the molecule is marked as having stereo perceived (unless the ``S`` option is passed - see below).

Being able to skip an explicit call to stereo perception means that SMILES strings can be read quickly - an important feature when dealing with millions or more. However, if you wish to identify additional stereocenters whose stereo configuration is unspecified, or the SMILES strings come from an untrusted source and stereo may have been incorrectly specified (e.g. on a tetrahedral center with two groups the same), then you may wish to trigger reperception.

Without any additional information, stereo cannot be perceived from a structure that has neither 2D nor 3D coordinates. Triggering stereo perception on such a structure will generate stereo objects where applicable, but their stereo will be marked as unspecified. However, where existing stereo data is present (e.g. after reading a SMILES string), the data will be retained if the stereocenter is identified by the perception routine as a true stereocenter. The ``S`` option to the SMILES reader tells it not to mark the stereo as perceived on reading; as a result, reperception will occur if triggered by a writer::

  $ obabel -:"F[C@@](F)(F)[C@@H](I)Br" -osmi
  F[C@@](F)(F)[C@@H](I)Br
  $ obabel -:"F[C@@](F)(F)[C@@H](I)Br" -aS -osmi
  FC(F)(F)[C@@H](I)Br

Miscellaneous stereo functions in the API
-----------------------------------------

* ``OBAtom::IsChiral`` - this is a convenience function that checks whether there is any tetrahedral stereo data associated with a particular atom. Its presence is for legacy reasons - like all convenience functions in the API, a future tidy-up may remove it.
