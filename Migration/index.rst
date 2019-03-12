Updating to Open Babel 3.x from 2.x
===================================

Open Babel 3.0 breaks the API in a number of cases, and introduces some new behavior behind-the-scenes. These changes were necessary to fix some long standing issues impacting chemical accuracy as well as performance.

Here we describe the main changes, how they may impact use of the API, and how to change existing code to adapt.

Handling of implicit hydrogens
------------------------------
With OB 3.0, the number of implicit hydrogens is stored as a property of the atom. This value can be interrogated and set independently of any other property of the atom. This is how other mature cheminformatics toolkits handle implicit hydrogens. In contrast, in OB 2.x this was a derived property worked out from valence rules and some additional flags set on an atom to indicate non-standard valency. 

From the point of view of the user, the advantage of the 2.x approach was that the user never needed to consider the implicit hydrogens; their count was calculated based on the explicit atoms (a behavior known as "floating valence"). The disadvantage was that it was difficult for the user to specify non-standard valencies, may have papered-over problems with the data, and gave rise to subtle bugs which were not easily addressed.

As an example of how the behavior has changed, let's look at creating a bond. If we read the SMILES string `C.C`, create a bond between the two atoms and write out the SMILES string, we get different answers for OB 2 (`CC`) versus OB 3 (`[CH4][CH4]`). OB 2 just works out the count based on standard valence rules. With OB 3, there were four implicit hydrogens on each carbon before we made the bond, and there still are four - they didn't go anywhere and weren't automatically adjusted. 

While this may seem like a major change, adapting code to handle the change should be straightforward: adding or removing a bond should be accompanied by incrementing or decrementing the implicit hydrogen count by the bond order. This also applies to deleting an atom, since this deletes any bonds connected to it.

For the particular case of creating a new atom, it is worth noting that the implicit hydrogen count defaults to zero and that the user must set it themself. To help with this situation a convenience function has been added to OBAtom that sets the implicit hydrogen count to be consistent with normal valence rules.

