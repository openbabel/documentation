Descriptors
===========

.. INSERT AUTOMATICALLY GENERATED CONTENT BELOW

Numerical descriptors
---------------------

.. rubric:: Number of atoms (atoms)

Add or remove hydrogens to count total or heavy atoms
SMARTS: \*

.. rubric:: Number of bonds (bonds)

Add or remove hydrogens to count total or bonds between heavy atoms
SMARTS: \*~\*

.. rubric:: Number of Hydrogen Bond Donors (JoelLib) (HBD)

SMARTS: [!#6;!H0]

.. rubric:: Number of Hydrogen Bond Acceptors 1 (JoelLib) (HBA1)

Identification of Biological Activity Profiles Using Substructural
Analysis and Genetic Algorithms -- Gillet, Willett and Bradshaw,
U. of Sheffield and Glaxo Wellcome.
Presented at Random & Rational: Drug Discovery via Rational Design
and Combinitorial Chemistry, Strategic Research Institute, Princeton
NJ, Sept. 1995
SMARTS: [$([!#6;+0]);!$([F,Cl,Br,I]);!$([o,s,nX3]);!$([Nv5,Pv5,Sv4,Sv6])]

.. rubric:: Number of Hydrogen Bond Acceptors 2 (JoelLib) (HBA2)

SMARTS: [$([$([#8,#16]);!$(\*=N~O);!$(\*~N=O);X1,X2]),$([#7;v3;!$([nH]);!$(\*(-a)-a)])]

.. rubric:: Number of Fluorine Atoms (nF)

SMARTS: F

.. rubric:: octanol/water partition coefficient (logP)

Datafile: logp.txt

.. rubric:: Molecular Weight filter (MW)



.. rubric:: Number of triple bonds (tbonds)

SMARTS: \*#\*

.. rubric:: molar refractivity (MR)

Datafile: mr.txt

.. rubric:: Number of aromatic bonds (abonds)

SMARTS: \*:\*

.. rubric:: Number of single bonds (sbonds)

SMARTS: \*-\*

.. rubric:: Number of double bonds (dbonds)

SMARTS: \*=\*

.. rubric:: topological polar surface area (TPSA)

Datafile: psa.txt

.. rubric:: Rotatable bonds filter (rotors)



.. rubric:: Melting point (MP)

This is a melting point descriptor developed
by Andy Lang. For details see:
http://onschallenge.wikispaces.com/MeltingPointModel011
Datafile: mpC.txt

Textual descriptors
-------------------

.. rubric:: Canonical SMILES (cansmi)



.. rubric:: Canonical SMILES without isotopes or stereo (cansmiNS)



.. rubric:: IUPAC InChI identifier (InChI)



.. rubric:: InChIKey (InChIKey)



.. rubric:: Chemical formula (formula)



.. rubric:: For comparing a molecule's title (title)



Descriptors for filtering
-------------------------

.. rubric:: Lipinski Rule of Five (L5)

HBD<5 HBA1<10 MW<500 logP<5

.. rubric:: SMARTS filter (smarts)



.. rubric:: SMARTS filter (s)



