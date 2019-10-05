.. _migrating_to_3.0:

Updating to Open Babel 3.0 from 2.x
===================================

Open Babel 3.0 breaks the API in a number of cases, and introduces some new behavior behind-the-scenes. These changes were necessary to fix some long standing issues impacting chemical accuracy as well as performance.

Here we describe the main changes, and how to change existing code to adapt.

Removal of babel
----------------

The ``babel`` executable has been removed, and ``obabel`` should be used instead. Typically the only change needed is to place ``-O`` before the output filename::

  $ babel -ismi tmp.smi -omol out.mol
  $ obabel -ismi tmp.smi -omol -O out.mol

Python module
-------------

In OB 3.x, both ``openbabel.py`` and ``pybel.py`` live within the ``openbabel`` module::

   # OB 2.x
   import openbabel as ob
   import pybel

   # OB 3.0
   from openbabel import openbabel as ob
   from openbabel import pybel

While more verbose, the new arrangement is in line with standard practice and helps avoid conflict with a different Python project, PyBEL.

Handling of elements and related information
--------------------------------------------

The API for interconverting atomic numbers and element symbols has been replaced for performance reasons. The ``OBElementTable`` class has been removed and its associated functions are now available through the ``OBElements`` namespace:

.. code-block: c++

::

  // OB 2.x
  OBElementTable etab;
  const char *elem = etab.GetSymbol(6);
  unsigned int atomic_num = etab.GetAtomicNum(elem);

  // OB 3.0
  #include <openbabel/elements.h>
  const char *elem = OBElements::GetSymbol(6);
  unsigned int atomic_num = OBElements::GetAtomicNum(elem);

Furthermore, the OBAtom API convenience functions for testing for particular elements (e.g. ``IsHydrogen()``) have been removed. Instead, ``OBAtom::GetAtomicNum()`` should be used along with an element constant or atomic number:

::

  // OB 2.x
  if (atom->IsCarbon()) {...

  // OB 3.0
  if (atom->GetAtomicNum() == OBElements.Carbon) {...
  //   or
  if (atom->GetAtomicNum() == 6) {...

Handling of isotope information now longer uses ``OBIsotopeTable`` but is accessed through the ``OBElements`` namespace::

  // OB 2.x
  OBIsotopeTable isotab;
  isotab.GetExactMass(6, 14);

  // OB 3.0
  double exact = OBElements.GetExactMass(OBElements.Carbon, 14);

.. (TMI?) Finally, the OBElement::CorrectedBondRad() method was removed.

Atom classes
------------

In OB 2.x, atom class information was stored as part of an ``OBAtomClassData`` object attached to an ``OBMol`` and accessed via ``OBMol.GetData("Atom Class")``. In OB 3.0, atom class information is instead stored as an ``OBPairInteger`` associated with an ``OBAtom`` and accessed via ``OBAtom.GetData("Atom Class")``.

OBAtom valence and degree methods
---------------------------------

OB 2.x referred to the function that returned the explicit degree of an atom as ``GetValence()``. This was confusing, at best. To find the explicit valence, the ``BOSum()`` method was required. OB 3.0 avoids this confusion by renaming methods associated with degree or valence:

* ``OBAtom::GetExplicitValence()`` (OB 2.x ``BOSum()``)
* ``OBAtom::GetExplicitDegree()`` (OB 2.x ``GetValence()``)
* ``OBAtom::GetHvyDegree()`` (OB 2.x ``GetHvyValence()``)
* ``OBAtom::GetHeteroDegree()`` (OB 2.x ``GetHeteroValence()``)

Molecule, atom and bond flags
-----------------------------

The "Unset" methods for molecule, atom and bond flags have been removed. Instead, a value of ``false`` should be passed to the corresponding "Set" method. For example, ``OBMol::UnsetAromaticPerceived()`` in OB 2.x is now ``OBMol::SetAromaticPerceived(false)``.

Removal of deprecated methods
-----------------------------

Several deprecated methods have been removed. For the most part, an equivalent function with a different name is present in the API:

* ``OBBond::GetBO()``/``SetBO()`` removed. ``OBBond::GetBondOrder()``/``SetBondOrder()`` should be used instead.
* ``OBAtom::GetCIdx()`` removed. ``OBAtom::GetCoordinateIdx()`` should be used instead.
* ``OBBitVec::Empty()`` removed. ``OBBitVec::IsEmpty()`` should be used instead.
* ``OBBitVec::BitIsOn()`` removed. ``OBBitVec::BitIsSet()`` should be used instead.

Handling of implicit hydrogens
------------------------------

With OB 3.0, the number of implicit hydrogens is stored as a property of the atom. This value can be interrogated and set independently of any other property of the atom. This is how other mature cheminformatics toolkits handle implicit hydrogens. In contrast, in OB 2.x this was a derived property worked out from valence rules and some additional flags set on an atom to indicate non-standard valency. 

From the point of view of the user, the advantage of the 2.x approach was that the user never needed to consider the implicit hydrogens; their count was calculated based on the explicit atoms (a behavior known as "floating valence"). The disadvantage was that it was difficult for the user to specify non-standard valencies, may have papered-over problems with the data, gave rise to subtle bugs which were not easily addressed and had poorer performance.

As an example of how the behavior has changed, let's look at creating a bond. If we read the SMILES string ``C.C``, create a bond between the two atoms and write out the SMILES string, we get different answers for OB 2.x (``CC``) versus OB 3.0 (``[CH4][CH4]``). OB 2.x just works out the count based on standard valence rules. With OB 3.0, there were four implicit hydrogens on each carbon before we made the bond, and there still are four - they didn't go anywhere and weren't automatically adjusted. 

While this may seem like a major change, adapting code to handle the change should be straightforward: adding or removing a bond should be accompanied by incrementing or decrementing the implicit hydrogen count by the bond order. This also applies to deleting an atom, since this deletes any bonds connected to it. Note that care should be taken not to set the hydrogen count to a negative value when decrementing.

::

  unsigned int bondorder = 1;
  mol->AddBond(1, 2, bondorder);
  OBAtom* start = mol->GetAtom(1);
  unsigned int hcount = start->GetImplicitHCount();
  start->SetImplicitHCount(bondorder >= hcount ? 0 : hcount - bondorder);
  OBAtom* end = mol->GetAtom(2);
  hcount = end->GetImplicitHCount();
  end->SetImplicitHCount(bondorder >= hcount ? 0 : hcount - bondorder);

For the particular case of creating a new atom, it is worth noting that the implicit hydrogen count defaults to zero and that users must set it themselves if necessary. To help with this situation a convenience function has been added to OBAtom that sets the implicit hydrogen count to be consistent with normal valence rules. TODO

Regarding specific API functions, the following have been removed:

* ``OBAtom::SetImplicitValence()``, ``GetImplicitValence()``
* ``OBAtom::IncrementImplicitValence()``, ``DecrementImplicitValence()``
* ``OBAtom::ForceNoH()``, ``HasNoHForce()``, ``ForceImplH()``, ``HasImplHForced()``
* ``OBAtom::ImplicitHydrogenCount()``

The following have been added:

* ``OBAtom::SetImplicitHCount()``, ``GetImplicitHCount()``

Handling of aromaticity
-----------------------

Molecule modification no longer clears the aromaticity perception flag. If the user wishes to force reperception after modification, then they should call ``OBMol::SetAromaticPerceived(false)``.

..
        Kekulization
        ------------
        The following API functions have been removed as part of this rewrite.
        * OBAtom::KBOSum()
        * OBBond::SetKSingle(), SetKDouble(), SetKTriple()
        * OBBond::UnsetKekule()
        * OBBond::IsSingle(), IsDouble(), IsTriple().
        * OBBond::IsKSingle(), IsKDouble(), IsKTriple()
        Regarding ``OBBond::IsSingle()`` etc., the user should replaced these with ``OBBond::GetBondOrder()==1`` if that is their intention. The original IsSingle(), etc. returned ``false`` for aromatic bonds - this can be tested with a call to ``OBBond::IsAromatic()``.
