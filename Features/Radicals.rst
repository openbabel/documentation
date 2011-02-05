Radicals and SMILES extensions
==============================

The need for radicals and implicit hydrogen to coexist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hydrogen deficient molecules, radicals, carbenes, etc., are not
well catered for by chemical software aimed at pharmaceuticals. But
radicals are important reaction intermediates in living systems as
well as many other fields, such as polymers, paints, oils,
combustion and atmospheric chemistry. The examples given here are
small molecules, relevant to the last two applications.

Chemistry software to handle radicals is complicated by the common
use of implicit hydrogen when describing molecules. How is the
program to know when you type "O" whether you mean an oxygen atom
or water? This ambiguity leads some to say that hydrogens should
always be explicit in any chemical description. But this is not the
way that most chemists work. A straight paraffinic chain from which
a hydrogen had been abstracted might commonly be represented by
something like: |3-pentyl radical|

This uses implicit hydrogens and an explicit radical centre. But
sometimes the hydrogens are explicit and the radical centre
implicit, as when CH\ :sub:`3`\ is used to represent the methyl radical.

How Open Babel does it
~~~~~~~~~~~~~~~~~~~~~~

Open Babel accepts molecules with explicit or implicit hydrogens and
can convert between the two. It will also handle radicals (and
other hydrogen-deficient species) with implicit hydrogen by using
internally a property of an atom, `\_spinmultiplicity`, modelled on
the RAD property in MDL MOL files and also used in CML. This can be
regarded in the present context as a measure of the hydrogen
deficiency of an atom. Its value is:

* 0 for normal atoms,
* 2 for radical (missing one hydrogen) and
* 1 or 3 for carbenes and nitrenes (missing two hydrogens).

It happens that for some doubly deficient species, like carbene
CH\ :sub:`2` and oxygen atoms, the singlet and triplet species are fairly close
in energy and both may be significant in certain applications such
as combustion, atmospheric or preparative organic chemistry, so it
is convenient that they can be described separately. There are of
course an infinity of other electronic configurations of molecules
but Open Babel has no special descriptors for them. However, even
more hydrogen-deficient atoms are indicated by the highest possible
value of spinmultiplicity (C atom has spin multiplicity of 5).
(This extends MDL's RAD property which has a maximum value of 3.)

If the spin multiplicity of an atom is not input explicitly, it is
set (in :obapi:`OBMol::AssignSpinMultiplicity() <OpenBabel::OBMol::AssignSpinMultiplicity>`) when the input format is
MOL, SMI, CML or Therm. This routine is called after all the atoms
and bonds of the molecule are known. It detects hydrogen deficiency
in an atom and assigns spin multiplicity appropriately. But because
hydrogen may be implicit it only does this for atoms which have at
least one explicit hydrogen or on atoms which have had
:obapi:`ForceNoH() <OpenBabel::OBAtom::ForceNoH>` called for them - which is effectively zero explicit
hydrogens. The latter is used, for instance, when SMILES inputs ``[O]``
to ensure that it is seen as an oxygen atom (spin multiplicity=3)
rather than water. Otherwise, atoms with no explicit hydrogen are
assumed to have a spin multiplicity of 0, i.e with full complement
of implicit hydrogens.

In deciding which atoms should be have spin multiplicity assigned,
hydrogen atoms which have an isotope specification (D,T or even 1H)
do not count. So SMILES ``N[2H]`` is NH\ :sub:`2`\ D (spin multiplicity
left at 0, so with a full content of implicit hydrogens), whereas
``N[H]`` is NH (spin multiplicity=3). A deuterated radical like NHD is
represented by ``[NH][2H]``.

In radicals either the hydrogen or the spin multiplicity can be implicit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the spin multiplicity has been set on an atom, the hydrogens
can be implicit even if it is a radical. For instance, the
following mol file, with explicit hydrogens, is one way of
representing the ethyl radical:

::

    ethyl radical
     OpenBabel04010617172D
    Has explicit hydrogen and implicit spin multiplicity
      7  6  0  0  0  0  0  0  0  0999 V2000
        0.0000    0.0000    0.0000 C   0  0  0  0  0
        0.0000    0.0000    0.0000 C   0  0  0  0  0
        0.0000    0.0000    0.0000 H   0  0  0  0  0
        0.0000    0.0000    0.0000 H   0  0  0  0  0
        0.0000    0.0000    0.0000 H   0  0  0  0  0
        0.0000    0.0000    0.0000 H   0  0  0  0  0
        0.0000    0.0000    0.0000 H   0  0  0  0  0
      1  2  1  0  0  0
      1  3  1  0  0  0
      1  4  1  0  0  0
      1  5  1  0  0  0
      2  6  1  0  0  0
      2  7  1  0  0  0
    M  END

When read by Open Babel the spinmultiplicity is set to 2 on the C
atom 2. If the hydrogens are made implicit, perhaps by the ``-d``
option, and the molecule output again, an alternative
representation is produced:

::

    ethyl radical
     OpenBabel04010617192D
    Has explicit spin multiplicity and implicit hydrogen
      2  1  0  0  0  0  0  0  0  0999 V2000
        0.0000    0.0000    0.0000 C   0  0  0  0  0
        0.0000    0.0000    0.0000 C   0  0  0  0  0
      1  2  1  0  0  0
    M  RAD  1   2   2
    M  END

SMILES extensions for radicals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although radical structures can be represented in SMILES by
specifying the hydrogens explicitly, e.g. ``[CH3]`` is the methyl
radical, some chemists have apparently felt the need to devise
non-standard extensions that represent the radical centre
explicitly. Open Babel will recognize ``C[O.]`` as well as ``C[O]`` as the
methoxy radical CH\ :sub:`3`\ O during input, but the non-standard
form is not supported in output.

By default, radical centres are output in explict hydrogen form,
e.g. ``C[CH2]`` for the ethyl radical. All the atoms will be in explict
H form, i.e. ``[CH3][CH2]``, if :obapi:`AddHydrogens() <OpenBabel::OBMol::AddHydrogens>` or the ``-h`` option has
been specified. The output is always standard SMILES, although
other programs may not interpret radicals correctly.

Open Babel supports another SMILES extension for both input and
output: the use of lower case atomic symbols to represent radical
centres. (This is supported on the ACCORD Chemistry Control and
maybe elsewhere.) So the ethyl radical is ``Cc`` and the methoxy radical
is ``Co``. This form is input transparently and can be output by using
the ``-xr`` option "radicals lower case". It is a useful shorthand in
writing radicals, and in many cases is easier to read since the
emphasis is on the radical centre rather than the number of
hydrogens which is less chemically significant.

In addition, this extension interprets multiple lower case ``c``
without ring closure as a conjugated carbon chain, so that ``cccc`` is
input as 1,3-butadiene. Lycopene (the red in tomatoes) is
``Cc(C)cCCc(C)cccc(C)cccc(C)ccccc(C)cccc(C)cccc(C)CCcc(C)C`` (without
the stereochemical specifications). This conjugated chain form is
not used on output - except in the standard SMILES aromatic form,
``c1ccccc1`` benzene.

It is interesting to note that the lower case extension actually improves
the chemical representation in a few cases. The allyl radical C\ :sub:`3`\ H\ :sub:`5`
would be conventionally ``[CH2]=[CH][CH2]`` (in its explict H form),
but could be represented as ``ccc`` with the extended syntax. The
latter more accurately represents the symmetry of the molecule
caused by delocalisation.

This extension is not as robust or as carefully considered as standard
SMILES and should be used with restraint. A structure that uses ``c``
as a radical centre close to aromatic carbons can be confusing to
read, and Open Babel's SMILES parser can also be confused. For example, it
recognizes ``c1ccccc1c`` as the benzyl radical, but it doesn't like
``c1cc(c)ccc1``. Radical centres should not be involved in ring
closure: for cyclohexyl radical ``C1cCCCC1`` is ok, but ``c1CCCCC1`` is not.

.. |3-pentyl radical| image:: ../_static/Zigzag.png
