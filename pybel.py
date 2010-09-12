"""
**pybel** - A Python module that simplifies access to the Open Babel API

Global variables:
  :data:`informats`, :data:`outformats`, :data:`descs`,
  :data:`fps`, :data:`forcefields`, :data:`operations`

Functions:
  :func:`readfile`, :func:`readstring`

Classes:
  :class:`Atom`, :class:`Molecule`, :class:`Outputfile`, :class:`Fingerprint`,
  :class:`Smarts`, :class:`MoleculeData`

.. note::

  The ``openbabel.py`` module can be accessed through the :data:`ob` global
  variable.

"""

import math
import os.path
import tempfile

try:
    import oasa
    import oasa.cairo_out
except ImportError: #pragma: no cover
    oasa = None

try:
    import Tkinter as tk
    import Image as PIL
    import ImageTk as piltk
except ImportError: #pragma: no cover
    tk = None

def _formatstodict(list):
    broken = [x.replace("[Read-only]", "").replace("[Write-only]","").split(" -- ") for x in list]
    broken = [(x,y.strip()) for x,y in broken]
    return dict(broken)
informats = {}
"""A dictionary of supported input formats"""
outformats = {}
"""A dictionary of supported output formats"""

def _getplugins(findplugin, names):
    plugins = dict([(x, findplugin(x)) for x in names if findplugin(x)])
    return plugins

descs = ['LogP', 'MR', 'TPSA']
"""A list of supported descriptors"""
fps = ['FP2', 'FP3', 'FP4']
"""A list of supported fingerprint types"""
forcefields = ['uff', 'mmff94', 'ghemical']
"""A list of supported forcefields"""
operations = ['Gen3D']
"""A list of supported operations"""

def readfile(format, filename):
    """Iterate over the molecules in a file.

    Required parameters:
       **format** -- chemical file format
                      See the :data:`informats` variable for a list
                      of available input formats
                      
       **filename**

    You can access the first molecule in a file using the :func:`next()` method
    of the iterator::
    
        mol = readfile("smi", "myfile.smi").next()
        
    You can make a list of the molecules in a file using::
    
        mols = list(readfile("smi", "myfile.smi"))
        
    You can iterate over the molecules in a file as shown in the
    following code snippet:
    
    >>> atomtotal = 0
    >>> for mol in readfile("sdf", "head.sdf"):
    ...     atomtotal += len(mol.atoms)
    ...
    >>> print atomtotal
    43
    """
    obconversion = ob.OBConversion()
    formatok = obconversion.SetInFormat(format)
    if not formatok:
        raise ValueError("%s is not a recognised OpenBabel format" % format)
    if not os.path.isfile(filename):
        raise IOError("No such file: '%s'" % filename)
    obmol = ob.OBMol()
    notatend = obconversion.ReadFile(obmol,filename)
    while notatend:
        yield Molecule(obmol)
        obmol = ob.OBMol()
        notatend = obconversion.Read(obmol)

def readstring(format, string):
    """Read in a molecule from a string.

    Required parameters:
       **format** -- chemical file format
                      See the :data:`informats` variable for a list
                      of available input formats
                      
       **string**

    Example::
    
        >>> input = "C1=CC=CS1"
        >>> mymol = readstring("smi", input)
        >>> len(mymol.atoms)
        5
    """
    obmol = ob.OBMol()
    obconversion = ob.OBConversion()

    formatok = obconversion.SetInFormat(format)
    if not formatok:
        raise ValueError("%s is not a recognised OpenBabel format" % format)

    success = obconversion.ReadString(obmol, string)
    if not success:
        raise IOError("Failed to convert '%s' to format '%s'" % (
            string, format))
    return Molecule(obmol)

class Outputfile(object):
    """Represent a file to which *output* is to be sent.
    
    Although it's possible to write a single molecule to a file by
    calling the :func:`~Molecule.write()` method of a :class:`Molecule`, if
    multiple molecules are to be written to the same file you
    should use the :class:`Outputfile` class.
    
    Required parameters:
       **format** -- chemical file format
                      See the :data:`outformats` variable for a list
                      of available output formats
                      
       **filename** 

    Optional parameters:
       **overwrite** -- overwrite the output file if it already exists?
                   Default is ``False``
                   
    Methods:
       :func:`write()`, :func:`close()`
    """
    def __init__(self, format, filename, overwrite=False):
        self.format = format
        self.filename = filename
        if not overwrite and os.path.isfile(self.filename):
            raise IOError("%s already exists. Use 'overwrite=True' to overwrite it." % self.filename)
        self.obConversion = ob.OBConversion()
        formatok = self.obConversion.SetOutFormat(self.format)
        if not formatok:
            raise ValueError("%s is not a recognised OpenBabel format" % format)
        self.total = 0 # The total number of molecules written to the file
    
    def write(self, molecule):
        """Write a molecule to the output file.
        
        Required parameters:
           **molecule** -- A :class:`Molecule`
        """
        if not self.filename:
            raise IOError("Outputfile instance is closed.")

        if self.total==0:
            self.obConversion.WriteFile(molecule.OBMol, self.filename)
        else:
            self.obConversion.Write(molecule.OBMol)
        self.total += 1

    def close(self):
        """Close the output file to further writing."""
        self.obConversion.CloseOutFile()
        self.filename = None

class Molecule(object):
    """Represent a Pybel Molecule.

    Required parameter:
       **OBMol** -- an Open Babel :obapi:`OBMol` or any type of Cinfony Molecule
    
    Attributes:
       :attr:`atoms`, :attr:`charge`, :attr:`conformers`, :attr:`data`,
       :attr:`dim`, :attr:`energy`, :attr:`exactmass`, :attr:`formula`, 
       :attr:`molwt`, :attr:`spin`, :attr:`sssr`, :attr:`title`, :attr:`unitcell`.
    
    Methods:
       :func:`addh()`, :func:`calcfp()`, :func:`calcdesc()`, :func:`draw()`,
       :func:`localopt()`, :func:`make3D()`, :func:`removeh()`, :func:`write()`
      
    The underlying Open Babel :obapi:`OBMol` can be accessed using the attribute:
       :attr:`OBMol`

    An iterator (:func:`__iter__()`) is provided that iterates over the
    atoms of the molecule. This allows constructions such as the following::
        
           for atom in mymol:
               print atom       
    """
    _cinfony = True

    def __init__(self, OBMol):
        
        if hasattr(OBMol, "_cinfony"):
            a, b = OBMol._exchange
            if a == 0:
                mol = readstring("smi", b)
            else:
                mol = readstring("mol", b)
            OBMol = mol.OBMol

        self.OBMol = OBMol
 
    @property
    def atoms(self):
        "A list of atoms of the molecule"
        return [ Atom(self.OBMol.GetAtom(i+1)) for i in range(self.OBMol.NumAtoms()) ]
    @property
    def charge(self):
        "The charge on the molecule"
        return self.OBMol.GetTotalCharge()
    @property
    def conformers(self):
        """Conformers of the molecule"""
        return self.OBMol.GetConformers()
    @property
    def data(self):
        """Access the molecule's data through a dictionary-like object,
        :class:`MoleculeData`."""
        return MoleculeData(self.OBMol)
    @property
    def dim(self):
        "Are the coordinates 2D, 3D or 0D?"
        return self.OBMol.GetDimension()
    @property
    def energy(self):
        """The molecule's energy"""
        return self.OBMol.GetEnergy()
    @property
    def exactmass(self):
        """The exact mass"""
        return self.OBMol.GetExactMass()
    @property
    def formula(self):
        """The molecular formula"""
        return self.OBMol.GetFormula()
    @property
    def molwt(self):
        """The molecular weight"""
        return self.OBMol.GetMolWt()
    @property
    def spin(self):
        """The spin multiplicity"""
        return self.OBMol.GetTotalSpinMultiplicity()
    @property
    def sssr(self):
        """The Smallest Set of Smallest Rings (SSSR)"""
        return self.OBMol.GetSSSR()
    def _gettitle(self): return self.OBMol.GetTitle()
    def _settitle(self, val): self.OBMol.SetTitle(val)
    title = property(_gettitle, _settitle, doc="The molecule title")
    @property
    def unitcell(self):
        """Access any unit cell data"""
        unitcell = self.OBMol.GetData(ob.UnitCell)
        if unitcell:
            return ob.toUnitCell(unitcell)
        else:
            raise AttributeError("Molecule has no attribute 'unitcell'")
    @property
    def _exchange(self):
        if self.OBMol.HasNonZeroCoords():
            return (1, self.write("mol"))
        else:
            return (0, self.write("can").split()[0])

    def __iter__(self):
        """Iterate over the Atoms of the Molecule.
        
        This allows constructions such as the following::
        
           for atom in mymol:
               print atom
        """
        return iter(self.atoms)

    def calcdesc(self, descnames=[]):
        """Calculate descriptor values.

        Optional parameter:
           **descnames** -- a list of names of descriptors
                            See the :data:`descs` variable for a
                            list of available descriptors.

        If `descnames` is not specified, all available descriptors are
        calculated. 
        """
        if not descnames:
            descnames = descs
        ans = {}
        for descname in descnames:
            try:
                desc = _descdict[descname]
            except KeyError:
                raise ValueError("%s is not a recognised Open Babel descriptor type" % descname)
            ans[descname] = desc.Predict(self.OBMol)
        return ans
    
    def calcfp(self, fptype="FP2"):
        """Calculate a molecular fingerprint.
        
        Optional parameters:
           **fptype** -- the fingerprint type (default is ``FP2``).
                         See the :data:`fps` variable for a list of
                         of available fingerprint types.
        """
        fp = ob.vectorUnsignedInt()
        try:
            fingerprinter = _fingerprinters[fptype]
        except KeyError:
            raise ValueError("%s is not a recognised Open Babel Fingerprint type" % fptype)
        fingerprinter.GetFingerprint(self.OBMol, fp)
        return Fingerprint(fp)

    def write(self, format="smi", filename=None, overwrite=False):
        """Write the molecule to a file or return a string.
        
        Optional parameters:
           **format** -- chemical file format
                         See the :data:`outformats` variable for a list
                         of available output formats (default is ``smi``)
                         
           **filename** -- default is ``None``
           
           **overwrite** -- overwrite the output file if it already exists?
                       Default is ``False``.

        If a `filename` is specified, the result is written to a file.
        Otherwise, a string is returned containing the result.

        To write multiple molecules to the same file you should use
        the :class:`Outputfile` class.
        """
        obconversion = ob.OBConversion()
        formatok = obconversion.SetOutFormat(format)
        if not formatok:
            raise ValueError("%s is not a recognised OpenBabel format" % format)

        if filename:
            if not overwrite and os.path.isfile(filename):
                raise IOError("%s already exists. Use 'overwrite=True' to overwrite it." % filename)
            obconversion.WriteFile(self.OBMol,filename)
            obconversion.CloseOutFile()
        else:
            return obconversion.WriteString(self.OBMol)

    def localopt(self, forcefield="mmff94", steps=500):
        """Locally optimize the coordinates.
        
        Optional parameters:
           **forcefield** -- default is ``mmff94``.
                             See the :data:`forcefields` variable for a
                             list of available forcefields.
                             
           **steps** -- default is 500

        If the molecule does not have any coordinates, :func:`make3D()` is
        called before the optimization. Note that the molecule needs
        to have explicit hydrogens. If not, call :func:`addh()`.
        """
        forcefield = forcefield.lower()
        if self.dim != 3:
            self.make3D(forcefield)
        ff = _forcefields[forcefield]
        success = ff.Setup(self.OBMol)
        if not success:
            return
        ff.SteepestDescent(steps)
        ff.GetCoordinates(self.OBMol)
    
##    def globalopt(self, forcefield="MMFF94", steps=1000):
##        if not (self.OBMol.Has2D() or self.OBMol.Has3D()):
##            self.make3D()
##        self.localopt(forcefield, 250)
##        ff = _forcefields[forcefield]
##        numrots = self.OBMol.NumRotors()
##        if numrots > 0:
##            ff.WeightedRotorSearch(numrots, int(math.log(numrots + 1) * steps))
##        ff.GetCoordinates(self.OBMol)
    
    def make3D(self, forcefield = "mmff94", steps = 50):
        """Generate 3D coordinates.
        
        Optional parameters:
           **forcefield** -- default is ``mmff94``.
                             See the :data:`forcefields` variable
                             for a list of available forcefields.
                             
           steps -- default is ``50``

        Once coordinates are generated, hydrogens are added and a quick
        local optimization is carried out with 50 steps and the
        MMFF94 forcefield. Call :func:`localopt()` if you want
        to improve the coordinates further.
        """
        forcefield = forcefield.lower()
        _builder.Build(self.OBMol)
        self.addh()
        self.localopt(forcefield, steps)

    def addh(self):
        """Add hydrogens."""
        self.OBMol.AddHydrogens()

    def removeh(self):
        """Remove hydrogens."""
        self.OBMol.DeleteHydrogens()
        
    def __str__(self):
        return self.write()

    def draw(self, show=True, filename=None, update=False, usecoords=False):
        """Create a 2D depiction of the molecule.

        Optional parameters:
        
          **show** -- display on screen (default is ``True``)
          
          **filename** -- write to file (default is ``None``)
          
          **update** -- update the coordinates of the atoms
                        This sets the atom coordinates to those
                        determined by the structure diagram generator
                        (default is ``False``)
                        
          **usecoords** -- use the current coordinates
                           This causes the current coordinates to be used
                           instead of calculating new 2D coordinates
                           (default is ``False``)

        OASA is used for 2D coordinate generation and depiction. Tkinter and
        Python Imaging Library are required for image display.
        """
        etab = ob.OBElementTable()

        if not oasa:
            errormessage = ("OASA not found, but is required for 2D structure "
                            "generation and depiction. OASA is part of BKChem. "
                            "See installation instructions for more "
                            "information.")
            raise ImportError(errormessage)
        mol = oasa.molecule()
        for atom in self.atoms:
            v = mol.create_vertex()
            v.symbol = etab.GetSymbol(atom.atomicnum)
            v.charge = atom.formalcharge
            if usecoords:
                v.x, v.y, v.z = atom.coords[0] * 30., atom.coords[1] * 30., 0.0
            mol.add_vertex(v)

        for bond in ob.OBMolBondIter(self.OBMol):
            e = mol.create_edge()
            e.order = bond.GetBO()
            if bond.IsHash():
                e.type = "h"
            elif bond.IsWedge():
                e.type = "w"
            mol.add_edge(bond.GetBeginAtomIdx() - 1,
                         bond.GetEndAtomIdx() - 1,
                         e)
        # I'm sure there's a more elegant way to do the following, but here goes...
        # let's set the stereochemistry around double bonds
        self.write("can") # Perceive UP/DOWNness
        for bond in ob.OBMolBondIter(self.OBMol):
            ends = bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()
            if bond.GetBO() == 2:
                stereobonds = [[b for b in ob.OBAtomBondIter(self.OBMol.GetAtom(x)) if b.GetIdx() != bond.GetIdx() and (b.IsUp() or b.IsDown())]
                               for x in ends]
                if stereobonds[0] and stereobonds[1]: # Needs to be defined at either end
                    if stereobonds[0][0].IsUp() == stereobonds[1][0].IsUp():
                        # Either both up or both down
                        stereo = oasa.stereochemistry.cis_trans_stereochemistry.SAME_SIDE
                    else:
                        stereo = oasa.stereochemistry.cis_trans_stereochemistry.OPPOSITE_SIDE
                    atomids = [(b[0].GetBeginAtomIdx(), b[0].GetEndAtomIdx()) for b in stereobonds]
                    extremes = []
                    for id, end in zip(ends, atomids):
                        if end[0] == id:
                            extremes.append(end[1])
                        else:
                            extremes.append(end[0])
                    center = mol.get_edge_between(mol.atoms[ends[0] - 1], mol.atoms[ends[1] - 1])
                    st = oasa.stereochemistry.cis_trans_stereochemistry(
                              center = center, value = stereo,
                              references = (mol.atoms[extremes[0] - 1], mol.atoms[ends[0] - 1],
                                            mol.atoms[ends[1] - 1], mol.atoms[extremes[1] - 1]))
                    mol.add_stereochemistry(st)
        
        mol.remove_unimportant_hydrogens()
        if not usecoords:
            oasa.coords_generator.calculate_coords(mol, bond_length=30)
            if update:
                newcoords = [(v.x / 30., v.y / 30., 0.0) for v in mol.vertices]
                for atom, newcoord in zip(ob.OBMolAtomIter(self.OBMol), newcoords):
                    atom.SetVector(*newcoord)
        if filename or show:
            maxx = max([v.x for v in mol.vertices])
            minx = min([v.x for v in mol.vertices])
            maxy = max([v.y for v in mol.vertices])
            miny = min([v.y for v in mol.vertices])
            maxcoord = max(maxx - minx, maxy - miny)
            fontsize = 16
            bondwidth = 6
            linewidth = 2
            if maxcoord > 270: # 300  - margin * 2
                for v in mol.vertices:
                    v.x *= 270. / maxcoord
                    v.y *= 270. / maxcoord
                fontsize *= math.sqrt(270. / maxcoord)
                bondwidth *= math.sqrt(270. / maxcoord)
                linewidth *= math.sqrt(270. / maxcoord)
            if filename:
                filedes = None
            else:
                filedes, filename = tempfile.mkstemp()
            
            canvas = oasa.cairo_out.cairo_out()
            canvas.show_hydrogens_on_hetero = True
            canvas.font_size = fontsize
            canvas.bond_width = bondwidth
            canvas.line_width = linewidth
            canvas.mol_to_cairo(mol, filename)
            if show:
                if not tk:
                    errormessage = ("Tkinter or Python Imaging "
                                    "Library not found, but is required for image "
                                    "display. See installation instructions for "
                                    "more information.")
                    raise ImportError(errormessage)
                root = tk.Tk()
                root.title((hasattr(self, "title") and self.title)
                           or self.__str__().rstrip())
                frame = tk.Frame(root, colormap="new", visual='truecolor').pack()
                image = PIL.open(filename)
                imagedata = piltk.PhotoImage(image)
                label = tk.Label(frame, image=imagedata).pack()
                quitbutton = tk.Button(root, text="Close", command=root.destroy).pack(fill=tk.X)
                root.mainloop()
            if filedes:
                os.close(filedes)
                os.remove(filename)

class Atom(object):
    """Represent an atom.

    Required parameter:
       **OBAtom** -- an Open Babel :obapi:`OBAtom`
        
    Attributes:
       :attr:`atomicmass`, :attr:`atomicnum`, :attr:`coords`,
       :attr:`exactmass`,
       :attr:`formalcharge`, :attr:`heavyvalence`, :attr:`heterovalence`,
       :attr:`hyb`, :attr:`idx`,
       :attr:`implicitvalence`, :attr:`isotope`, :attr:`partialcharge`,
       :attr:`spin`, :attr:`type`,
       :attr:`valence`, :attr:`vector`.
    
    The underlying Open Babel :obapi:`OBAtom` can be accessed
    using the attribute:
       :attr:`OBAtom`
    """
    
    def __init__(self, OBAtom):
        self.OBAtom = OBAtom
        
    @property
    def coords(self):
        """Coordinates of the atom"""
        return (self.OBAtom.GetX(), self.OBAtom.GetY(), self.OBAtom.GetZ())
    @property
    def atomicmass(self):
        "Atomic mass"
        return self.OBAtom.GetAtomicMass()
    @property
    def atomicnum(self):
        "Atomic number"
        return self.OBAtom.GetAtomicNum()
    @property
    def exactmass(self):
        "Exact mass"
        return self.OBAtom.GetExactMass()
    @property
    def formalcharge(self):
        "Formal charge"
        return self.OBAtom.GetFormalCharge()
    @property
    def heavyvalence(self):
        "Number of non-hydrogen atoms attached"
        return self.OBAtom.GetHvyValence()
    @property
    def heterovalence(self):
        "Number of heteroatoms attached"
        return self.OBAtom.GetHeteroValence()
    @property
    def hyb(self):
        """The hybridization of this atom: 1 for sp, 2 for sp2, 3 for sp3, ...

        For further details see :obapi:`OBAtom::GetHyb() <OpenBabel::OBAtom::GetHyb>`"""
        return self.OBAtom.GetHyb()
    @property
    def idx(self):
        "The index of the atom in the molecule (starts at 1)"
        return self.OBAtom.GetIdx()
    @property
    def implicitvalence(self):
        "The maximum number of connections expected for this molecule"
        return self.OBAtom.GetImplicitValence()
    @property
    def isotope(self):
        "The isotope for this atom if specified; 0 otherwise."
        return self.OBAtom.GetIsotope()
    @property
    def partialcharge(self):
        "Partial charge"
        return self.OBAtom.GetPartialCharge()
    @property
    def spin(self):
        "Spin multiplicity"
        return self.OBAtom.GetSpinMultiplicity()
    @property
    def type(self):
        "Atom type"
        return self.OBAtom.GetType()
    @property
    def valence(self):
        "Number of explicit connections"
        return self.OBAtom.GetValence()
    @property
    def vector(self):
        "Coordinates as a :obapi:`vector3` object."
        return self.OBAtom.GetVector()

    def __str__(self):
        c = self.coords
        return "Atom: %d (%.2f %.2f %.2f)" % (self.atomicnum, c[0], c[1], c[2])

def _findbits(fp, bitsperint):
    """Find which bits are set in a list/vector.

    This function is used by the Fingerprint class.

    >>> _findbits([13, 71], 8)
    [1, 3, 4, 9, 10, 11, 15]
    """
    ans = []
    start = 1
    for x in fp:
        i = start
        while x > 0:
            if x % 2:
                ans.append(i)
            x >>= 1
            i += 1
        start += bitsperint
    return ans
        
class Fingerprint(object):
    """A molecular fingerprint.
    
    Required parameters:
       **fingerprint** -- a vector calculated by :obapi:`OBFingerprint::FindFingerprint() <OpenBabel::OBFingerprint::FindFingerprint>`

    Attributes:
       :attr:`bits`

    Methods:
       The ``|`` operator can be used to calculate the Tanimoto
       coefficient. For example, given two Fingerprints `a` and `b`,
       the Tanimoto coefficient is given by::
       
          tanimoto = a | b

    The underlying fingerprint object can be accessed using the
    attribute :attr:`fp`.
    """
    def __init__(self, fingerprint):
        self.fp = fingerprint
    def __or__(self, other):
        return ob.OBFingerprint.Tanimoto(self.fp, other.fp)
    @property
    def bits(self):
        """A list of bits set in the fingerprint"""
        return _findbits(self.fp, ob.OBFingerprint.Getbitsperint())    
    def __str__(self):
        return ", ".join([str(x) for x in self.fp])

class Smarts(object):
    """A Smarts Pattern Matcher

    Required parameters:
       **smartspattern** - A SMARTS pattern
    
    Methods:
       :func:`findall`
    
    Example:
    
    >>> mol = readstring("smi","CCN(CC)CC") # triethylamine
    >>> smarts = Smarts("[#6][#6]") # Matches an ethyl group
    >>> print smarts.findall(mol) 
    [(1, 2), (4, 5), (6, 7)]

    The numbers returned are the indices (starting from 1) of the atoms
    that match the SMARTS pattern. In this case, there are three matches
    for each of the three ethyl groups in the molecule.
    """
    def __init__(self,smartspattern):
        """Initialise with a SMARTS pattern."""
        self.obsmarts = ob.OBSmartsPattern()
        success = self.obsmarts.Init(smartspattern)
        if not success:
            raise IOError("Invalid SMARTS pattern")
    def findall(self,molecule):
        """Find all matches of the SMARTS pattern to a particular molecule.
        
        Required parameters:
           **molecule** - A :class:`Molecule`
        """
        self.obsmarts.Match(molecule.OBMol)
        return [x for x in self.obsmarts.GetUMapList()]
        
class MoleculeData(object):
    """Store molecule data in a dictionary-type object
    
    Required parameters:
      `obmol` -- an Open Babel :obapi:`OBMol`

    Methods and accessor methods are like those of a dictionary except
    that the data is retrieved on-the-fly from the underlying :obapi:`OBMol`.

    Example:
    
    >>> mol = readfile("sdf", 'head.sdf').next()
    >>> data = mol.data
    >>> print data
    {'Comment': 'CORINA 2.61 0041  25.10.2001', 'NSC': '1'}
    >>> print len(data), data.keys(), data.has_key("NSC")
    2 ['Comment', 'NSC'] True
    >>> print data['Comment']
    CORINA 2.61 0041  25.10.2001
    >>> data['Comment'] = 'This is a new comment'
    >>> for k,v in data.iteritems():
    ...    print k, "-->", v
    Comment --> This is a new comment
    NSC --> 1
    >>> del data['NSC']
    >>> print len(data), data.keys(), data.has_key("NSC")
    1 ['Comment'] False
    """
    def __init__(self, obmol):
        self._mol = obmol
    def _data(self):
        return [ob.toPairData(x) for x in self._mol.GetData() if x.GetDataType()==ob.PairData or x.GetDataType()==ob.CommentData]
    def _testforkey(self, key):
        if not key in self:
            raise KeyError("'%s'" % key)
    def keys(self):
        return [x.GetAttribute() for x in self._data()]
    def values(self):
        return [x.GetValue() for x in self._data()]
    def items(self):
        return zip(self.keys(), self.values())
    def __iter__(self):
        return iter(self.keys())
    def iteritems(self):
        return iter(self.items())
    def __len__(self):
        return len(self._data())
    def __contains__(self, key):
        return self._mol.HasData(key)
    def __delitem__(self, key):
        self._testforkey(key)
        self._mol.DeleteData(self._mol.GetData(key))
    def clear(self):
        for key in self:
            del self[key]
    def has_key(self, key):
        return key in self
    def update(self, dictionary):
        for k, v in dictionary.iteritems():
            self[k] = v
    def __getitem__(self, key):
        self._testforkey(key)
        return ob.toPairData(self._mol.GetData(key)).GetValue()
    def __setitem__(self, key, value):
        if key in self:
            pairdata = ob.toPairData(self._mol.GetData(key))
            pairdata.SetValue(str(value))
        else:
            pairdata = ob.OBPairData()
            pairdata.SetAttribute(key)
            pairdata.SetValue(str(value))
            self._mol.CloneData(pairdata)
    def __repr__(self):
        return dict(self.iteritems()).__repr__()

if __name__=="__main__": #pragma: no cover
    import doctest
    doctest.testmod(verbose=True)
