.. include:: <isolat1.txt>

.. |kekule| replace:: Kekul\ |eacute|

Handling of aromaticity
=======================

The purpose of this section is to give an overview of how Open Babel handles aromaticity. Given that atoms can be aromatic, bonds can be aromatic, and that molecules have a flag for aromaticity perceived, it's important to understand how these all work together.

How is aromaticity information stored?
--------------------------------------

Like many other toolkits, Open Babel stores aromaticity information separate from bond order information. This means that there isn't a special bond order to indicate aromatic bond. Instead, aromaticity is stored as a flag on an atom as well as a flag on a bond. You can access and set this information using the following API functions:

* OBAtom::IsAromatic(), OBAtom::SetAromatic(), OBBond::UnsetAromatic()
* OBBond::IsAromatic(), OBBond::SetAromatic(), OBBond::UnsetAromatic()

There is a catch though, or rather a key point to note. OBMols have a flag to indicate whether aromaticity has been perceived. This is set via the following API functions:

* OBMol::SetAromaticPerceived(), OBMol::UnsetAromaticPerceived()

The value of this flag determines the behaviour of the OBAtom and OBBond IsAromatic() functions.

* If the flag is set, then IsAromatic() simply returns the corresponding value of the atom or bond flag. 
* If unset, then IsAromatic() triggers aromaticity perception (from scratch), and then returns the value of the flag.

Perception of aromaticity
-------------------------

It's convenient to use the term "perception", but what we mean is to apply an aromaticity model. Currently Open Babel only has a single aromaticity model, which is close to the Daylight aromaticity model. An aromaticity model describes how many pi electrons are contributed by each atom; if this sums to 4n+2 within a cycle, then all atoms and bonds in that cycle will be marked as aromatic.

Applying a model involves creating an instance of OBAromaticTyper(), and calling AssignAromaticFlags() passing an OBMol as a parameter. This wipes any existing flags, sets the atom and bond flags according to the model, and marks the aromaticity as perceived.

If you wish (and know what you are doing), you can apply your own aromaticity model by setting various atoms and bonds as aromatic and then marking the molecule as having aromaticity perceived. Naturally, not all models will make sense chemically. Even more problematic is the situation where no |kekule| form exists that corresponds to the aromatic form. And finally, there is the philosophical question of the meaning of an aromatic atom without aromatic bonds, and vice versa.

SMILES reading and writing
--------------------------

Putting the pieces together, let's look at the interaction between SMILES reading/writing and the handling of aromaticity.

.. rubric:: Writing SMILES

Unless |kekule| SMILES are requested (via the ``k`` output option), the SMILES writer will always write an aromatic SMILES string. IsAromatic() will be called on atoms and bonds to determine whether to use lowercase letters. As described earlier, this will trigger aromaticity perception according to the default model if the molecules is not marked as having its aromaticity perceived.

.. rubric:: Reading SMILES

The situation when reading SMILES is a bit more involved. If the SMILES string contains lowercase characters and aromatic bonds, this information is used to mark atoms and bonds as aromatic. The molecule is then kekulized to assign bond orders to aromatic bonds. Next, unless the ``a`` option is supplied, the molecule is marked as having its aromaticity unperceived.

That last step might seem strange. Why, after going to the trouble of reading the aromaticity and using it to kekulize, do we then effectively ignore it?

The reason is simply this: when writing an aromatic SMILES, we usually want to use our own aromaticity model and not that present in the input SMILES string. Otherwise, SMILES strings for the same molecule from different sources (that may use different aromaticity models) would not yield the same canonical SMILES string.

Of course, if the SMILES string came from Open Babel in the first place, we are doing unnecessary work when we keep reapplying the same aromaticity model. In this case, you can speed things up by using the ``a`` option, so that the aromaticity information present in the input is retained. The following examples show this in action::

  $ obabel -:cc -osmi
  C=C
  $ obabel -:cc -osmi -aa
  cc

Effect of modifying the structure
---------------------------------

Perhaps surprisingly, modifying the structure has no effect on the existing aromaticity flags; deleting an atom does not mark aromaticity as unperceived, nor indeed does any other change to the structure such as changing the atomic number of an atom or setting its charge; nor does the use of Begin/EndModify() affect the aromaticity flags. The only way to ensure that aromaticity is reperceived after modifying the structure is to explicitly mark it as unperceived.

The rationale for this is that an efficient toolkit should avoid unnecessary work. The toolkit does not know if a particular modification invalidates any aromaticity already perceived, or even if it did know, it cannot know whether the user actually wishes to invalidate it. It's up to the user to tell the toolkit. This places more responsibility in the hands of the user, but also more power.

To illustrate, let's consider what happens when the user reads benzene from the SMILES string ``c1ccccc1``, and then modifies the structure by deleting an aromatic atom.

As this is an aromatic SMILES string, the SMILES reader will mark all atoms and bonds as aromatic. Next, the molecule itself is marked as not having aromaticity perceived (see previous section). After reading, we can trigger aromaticity perception by calling IsAromatic() on an atom; now, in addition to the atoms and bonds being marked as aromatic, the molecule itself will be marked as having aromaticity perceived.

If at this point we delete a carbon and write out a SMILES string, what will the result be? You may expect something like ``[CH]=CC=C[CH]`` (or ``C=CC=CC`` if we also adjust the hydrogen count on the neighbor atoms) but instead it will be ``[cH]ccc[cH]`` (or ``ccccc`` if hydrogens were adjusted).

This follows from the discussion above - structural modifications have no effect on aromaticity flags. If instead the user wishes the SMILES writer to reperceive aromaticity, all that is necessary is to mark the molecule as not having aromaticity perceived, in which case the |kekule| form will instead be obtained.
