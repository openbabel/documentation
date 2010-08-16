Pybel
=====

.. highlight:: python

Pybel provides convenience functions and classes that make it
simpler to use the Open Babel libraries from Python, especially for
file input/output and for accessing the attributes of atoms and
molecules. The Atom and Molecule classes used by Pybel can be
converted to and from the OBAtom and OBMol used by the
``openbabel`` module. These features are discussed in more detail
below.

The rationale and technical details behind Pybel are described in O'Boyle et al [omh2008]_. To support further development of Pybel, please cite this paper if you use Pybel to obtain results for publication:

Information on the Pybel API can be found at the interactive Python
prompt using the ``help()`` function, and is also available in 
Appendix 1 (see :ref:`Pybel API`).

To use Pybel, use ``import pybel`` or ``from pybel import *``.

.. [omh2008] N.M. O'Boyle, C. Morley and G.R. Hutchison.
   **Pybel: a Python wrapper for the OpenBabel cheminformatics toolkit.**
   *Chem. Cent. J.* **2008**, *2*, 5.
   [`Link <http://dx.doi.org/10.1186/1752-153X-2-5>`_]

Atoms and Molecules
^^^^^^^^^^^^^^^^^^^

A
:class:`~pybel.Molecule`
can be created in any of three ways:


#. From an :obapi:`OBMol`, using ``Molecule(myOBMol)``
#. By reading from a file (see :ref:`Input Output`
   below)
#. By reading from a string (see :ref:`Input Output`
   below)

An :class:`~pybel.Atom`
be created in two different ways:


#. From an :obapi:`OBAtom`, using ``Atom(myOBAtom)``
#. By accessing the :attr:`~pybel.Molecule.atoms` attribute of a :class:`~pybel.Molecule`

.. sidebar:: Using Pybel with openbabel.py 

        It is always possible to access the OBMol or OBAtom on which a
        Molecule or Atom is based, by accessing the appropriate attribute,
        either ``.OBMol`` or ``.OBAtom``. In this way, it is easy to
        combine the convenience of ``pybel`` with the many additional
        capabilities present in ``openbabel``. See
        :ref:`Combining`
        below.

Molecules have the following attributes: :attr:`~pybel.Molecule.atoms`, :attr:`~pybel.Molecule.charge`, :attr:`~pybel.Molecule.data`, :attr:`~pybel.Molecule.dim`,
:attr:`~pybel.Molecule.energy`, :attr:`~pybel.Molecule.exactmass`, :attr:`~pybel.Molecule.formula`, :attr:`~pybel.Molecule.molwt`, :attr:`~pybel.Molecule.spin`, :attr:`~pybel.Molecule.sssr`, :attr:`~pybel.Molecule.title`
and :attr:`~pybel.Molecule.unitcell` (if crystal data). The :attr:`~pybel.Molecule.atoms` attribute provides a
list of the Atoms in a Molecule. The :attr:`~pybel.Molecule.data` attribute returns a
dictionary-like object for accessing and editing the data fields
associated with the molecule (technically, it's a
:class:`~pybel.MoleculeData`
object, but you can use it like it's a regular dictionary). The
:attr:`~pybel.Molecule.unitcell` attribute gives access to any unit cell data
associated with the molecule (see
:obapi:`OBUnitCell`).
The remaining attributes correspond directly to attributes of
OBMols: e.g. :attr:`~pybel.Molecule.formula` is equivalent to
:obapi:`OpenBabel::OBMol::GetFormula()`. For more information on what these
attributes are, please see the Open Babel C++ documentation for
:obapi:`OBMol`.

For example, let's suppose we have an SD file containing descriptor
values in the data fields:

::

    >>> mol = readfile("sdf", "calculatedprops.sdf").next() # (readfile is described below)
    >>> print mol.molwt
    100.1
    >>> print len(mol.atoms)
    16
    >>> print mol.data.keys()
    {'Comment': 'Created by CDK', 'NSC': 1, 'Hydrogen Bond Donors': 3, 'Surface Area': 342.43, .... }
    >>> print mol.data['Hydrogen Bond Donors']
    3
    >>> mol.data['Random Value'] = random.randint(0,1000) # Add a descriptor containing noise

Molecules have a
``<a href="http://openbabel.sourceforge.net/pybel.html#Molecule-write" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Molecule-write" rel="nofollow">.write()</a>``
method that writes a representation of a Molecule to a file or to a
string. See `Input/Output <#Input.2FOutput>`_ below. They also have
a
``<a href="http://openbabel.sourceforge.net/pybel.html#Molecule-calcfp" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Molecule-calcfp" rel="nofollow">.calcfp()</a>``
method that calculates a molecular fingerprint. See
`Fingerprints <#Fingerprints>`_ below.

The
``<a href="http://openbabel.sourceforge.net/pybel.html#Molecule-draw" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Molecule-draw" rel="nofollow">.draw()</a>``
method of a Molecule generates 2D coordinates and a 2D depiction of
a molecule. It uses the
`OASA library <http://bkchem.zirael.org/oasa_en.html>`_ by Beda
Kosata to do this (see the section below on
`Installing OASA </wiki/Python#Installing_OASA>`_). The default
options are to show the image on the screen (``show=True``), not to
write to a file (``filename=None``), to calculate 2D coordinates
(``usecoords=False``) but not to store them (``update=False``).

The
``<a href="http://openbabel.sourceforge.net/pybel.html#Molecule-addh" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Molecule-addh" rel="nofollow">.addh()</a>``
and
``<a href="http://openbabel.sourceforge.net/pybel.html#Molecule-removeh" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Molecule-removeh" rel="nofollow">.removeh()</a>``
methods allow hydrogens to be added and removed.

If a molecule does not have 3D coordinates, they can be generated
using the
``<a href="http://openbabel.sourceforge.net/pybel.html#Molecule-make3D" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Molecule-make3D" rel="nofollow">.make3D()</a>``
method. By default, this includes 50 steps of a geometry
optimisation using the MMFF94 forcefield. The list of available
forcefields is stored in the
`forcefields <http://openbabel.sourceforge.net/pybel.html#forcefields>`_
variable. To further optimise the structure, you can use the
``<a href="http://openbabel.sourceforge.net/pybel.html#Molecule-localopt" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Molecule-localopt" rel="nofollow">.localopt()</a>``
method, which by default carries out 500 steps of an optimisation
using MMFF94. Note that hydrogens need to be added before calling
``localopt()``.

The
``<a href="http://openbabel.sourceforge.net/pybel.html#Molecule-calcdesc" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Molecule-calcdesc" rel="nofollow">.calcdesc()</a>``
method of a Molecule returns a dictionary containing descriptor
values for LogP, Polar Surface Area ("TPSA") and Molar Refractivity
("MR"). A list of the available descriptors is contained in the
variable
``<a href="http://openbabel.sourceforge.net/pybel.html#descs" class="external text" title="http://openbabel.sourceforge.net/pybel.html#descs" rel="nofollow">descs</a>``.
If only one or two descriptor values are required, you can specify
the names as follows: ``calcdesc(["LogP", "TPSA"])``. Since the
``.data`` attribute of a Molecule is also a dictionary, you can
easily add the result of ``calcdesc()`` to an SD file (for example)
as follows:

::

    mol = readfile("sdf", "without_desc.sdf").next()
    descvalues = mol.calcdesc()
    # In Python, the update method of a dictionary allows you
    # to add the contents of one dictionary to another
    mol.data.update(descvalues)
    output = Outputfile("sdf", "with_desc.sdf")
    output.write(mol)
    output.close()

For convenience, a Molecule provides an iterator over its Atoms.
This is used as follows:

::

    for atom in myMolecule:
       # do something with atom

Atoms have the following attributes: atomicmass, atomicnum, cidx,
coords, coordidx, exactmass, formatcharge, heavyvalence,
heterovalence, hyb, idx, implicitvalence, index, isotope,
partialcharge, spin, type, valence, vector. The ``.coords``
attribute provides a tuple (x, y, z) of the atom's coordinates. The
remaining attributes are as for
`OBAtom <http://openbabel.sourceforge.net/api/current/classOpenBabel_1_1OBAtom.shtml>`_.

.. _Input Output:

Input/Output
^^^^^^^^^^^^

One of the strengths of Open Babel is the number of chemical file
formats that it can handle. Pybel provides a dictionary of the
input and output formats in the variables
`informats <http://openbabel.sourceforge.net/pybel.html#formats>`_
and
`outformats <http://openbabel.sourceforge.net/pybel.html#formats>`_,
where the keys are the three-letter codes for each format (e.g.
'pdb') and the values are the descriptions (e.g. 'Protein Data Bank
format').

Pybel greatly simplifies the process of reading and writing
molecules to and from strings or files. There are two functions for
reading Molecules:


#. ``<a href="http://openbabel.sourceforge.net/pybel.html#-readstring" class="external text" title="http://openbabel.sourceforge.net/pybel.html#-readstring" rel="nofollow">readstring(format, string)</a>``
   reads a Molecule from a string
#. ``<a href="http://openbabel.sourceforge.net/pybel.html#-readfile" class="external text" title="http://openbabel.sourceforge.net/pybel.html#-readfile" rel="nofollow">readfile(format, filename)</a>``
   provides an iterator over the Molecules in a file

Here are some examples of their use. Note in particular the use of
``.next()`` to access the first (and possibly only) molecule in a
file:

::

    >>> mymol = readstring("smi", "CCCC")
    >>> print mymol.molwt
    58
    >>> for mymol in readfile("sdf", "largeSDfile.sdf")
    ... print mymol.molwt
    >>> singlemol = readfile("pdb", "1CRN.pdb").next()

If a single molecule is to be written to a molecule or string, the
``<a href="http://openbabel.sourceforge.net/pybel.html#Molecule-write" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Molecule-write" rel="nofollow">.write()</a>``
method of the Molecule should be used:


#. ``mymol.write(format)`` returns a string
#. ``mymol.write(format, filename)`` writes the Molecule to a file.
   An optional additional parameter, ``overwrite``, should be set to
   ``True`` if you wish to overwrite an existing file.

For files containing multiple molecules, the
`Outputfile <http://openbabel.sourceforge.net/pybel.html#Outputfile>`_
class should be used instead. This is initialised with a format and
filename (and optional ``overwrite`` parameter). To write a
Molecule to the file, the
``<a href="http://openbabel.sourceforge.net/pybel.html#Outputfile-write" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Outputfile-write" rel="nofollow">.write()</a>``
method of the Outputfile is called with the Molecule as a
parameter. When all molecules have been written, the
``<a href="http://openbabel.sourceforge.net/pybel.html#Outputfile-close" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Outputfile-close" rel="nofollow">.close()</a>``
method of the Outputfile should be called.

Here are some examples of output using the Pybel methods and
classes:

::

    >>> print mymol.write("smi")
    'CCCC'
    >>> mymol.write("smi", "outputfile.txt")
    >>> largeSDfile = Outputfile("sdf", "multipleSD.sdf")
    >>> largeSDfile.write(mymol)
    >>> largeSDfile.write(myothermol)
    >>> largeSDfile.close()

Fingerprints
^^^^^^^^^^^^

A
`Fingerprint <http://openbabel.sourceforge.net/pybel.html#Fingerprint>`_
can be created in either of two ways:


#. From a vector returned by the OpenBabel GetFingerprint() method,
   using ``Fingerprint(myvector)``
#. By calling the
   ``<a href="http://openbabel.sourceforge.net/pybel.html#Molecule-calcfp" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Molecule-calcfp" rel="nofollow">.calcfp()</a>``
   method of a Molecule

The ``.calcfp()`` method takes an optional argument, ``fptype``,
which should be one of the fingerprint types supported by OpenBabel
(see `Tutorial:Fingerprints </wiki/Tutorial:Fingerprints>`_). The
list of supported fingerprints is stored in the variable
``<a href="http://openbabel.sourceforge.net/pybel.html#fps" class="external text" title="http://openbabel.sourceforge.net/pybel.html#fps" rel="nofollow">fps</a>``.
If unspecified, the default fingerprint ("FP2") is calculated.

Once created, the Fingerprint has two attributes: ``fp`` gives the
original OpenBabel vector corresponding to the fingerprint, and
``bits`` gives a list of the bits that are set.

The Tanimoto coefficient of two Fingerprints can be calculated
using the "\|" operator.

Here is an example of its use:

::

    >>> import pybel
    >>> smiles = ['CCCC', 'CCCN']
    >>> mols = [pybel.readstring("smi", x) for x in smiles] # Create two molecules from the SMILES
    >>> fps = [x.calcfp() for x in mols] # Calculate their fingerprints
    >>> print fps[0].bits, fps[1].bits
    [261, 385, 671] [83, 261, 349, 671, 907]
    >>> print fps[0] | fps[1] # Print the Tanimoto coefficient
    0.3333

SMARTS matching
^^^^^^^^^^^^^^^

Pybel also provides a simplified API to the Open Babel SMARTS
pattern matcher. A
`Smarts <http://openbabel.sourceforge.net/pybel.html#Smarts>`_
object is created, and the
``<a href="http://openbabel.sourceforge.net/pybel.html#Smarts-findall" class="external text" title="http://openbabel.sourceforge.net/pybel.html#Smarts-findall" rel="nofollow">.findall()</a>``
method is then used to return a list of the matches to a given
Molecule.

Here is an example of its use:

::

    >>> mol = readstring("smi","CCN(CC)CC") # triethylamine
    >>> smarts = Smarts("[#6][#6]") # Matches an ethyl group
    >>> print smarts.findall(mol) 
    [(1, 2), (4, 5), (6, 7)]

.. _Combining:

Combining Pybel with openbabel.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is easy to combine the ease of use of Pybel, with the
comprehensive coverage of the Open Babel toolkit that
``openbabel.py`` provides. Pybel is really a wrapper around
``openbabel.py``, with the result that the OBAtom and OBMol used by
openbabel.py can be interconverted to the Atom and Molecule used by
Pybel.

The following example shows how to read a molecule from a PDB file
using Pybel, and then how to use openbabel.py to add hydrogens. It
also illustrates how to find out information on what methods and
classes are available, while at the interactive Python prompt.

::

    >>> import pybel
    >>> mol = pybel.readfile("pdb", "1PYB").next()
    >>> help(mol)
    Help on Molecule in module pybel object:
    ...
     |  Attributes:
     |     atoms, charge, dim, energy, exactmass, flags, formula,
     |     mod, molwt, spin, sssr, title.
    ...
     |  The original Open Babel molecule can be accessed using the attribute:
     |     OBMol
    ...
    >>> print len(mol.atoms), mol.molwt
    3430 49315.2
    >>> dir(mol.OBMol) # Show the list of methods provided by openbabel.py
    ['AddAtom', 'AddBond', 'AddConformer', 'AddHydrogens', 'AddPolarHydrogens', ... ]
    >>> mol.OBMol.AddHydrogens()
    >>> print len(mol.atoms), mol.molwt
    7244 49406.0

The next example is an extension of one of the ``openbabel.py``
examples at the top of this page. It shows how a molecule could be
created using ``openbabel.py``, and then written to a file using
Pybel:

::

    import openbabel, pybel
    
    mol = openbabel.OBMol()
    a = mol.NewAtom()
    a.SetAtomicNum(6)   # carbon atom
    a.SetVector(0.0, 1.0, 2.0) # coordinates
    b = mol.NewAtom()
    mol.AddBond(1, 2, 1)   # atoms indexed from 1
    
    pybelmol = pybel.Molecule(mol)
    pybelmol.write("sdf", "outputfile.sdf")

For more examples of using Open Babel from Python, see the links on
the main `Python </wiki/Python>`_ page.
