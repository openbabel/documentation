.. _Multilevel_Neighborhoods_of_Atoms_(MNA):

Multilevel Neighborhoods of Atoms (MNA) (mna)
=============================================

**Iteratively generated 2D descriptors suitable for QSAR**

Multilevel Neighborhoods of Atoms (MNA) descriptors are
2D molecular fragments suitable for use in QSAR modelling [fpbg99]_.
The format outputs a complete descriptor fingerprint per
molecule. Thus, a 27-atom (including hydrogen) molecule would
result in 27 descriptors, one per line.

MNA descriptors are generated recursively. Starting at the origin,
each atom is appended to the descriptor immediately followed by a
parenthesized list of its neighbours. This process iterates until the
specified distance from the origin, also known as the depth of the
descriptor.

Elements are simplified into 32 groups. Each group has a representative
symbol used to stand for any element in that group:

==== ========
Type Elements
==== ========
H    H
C    C
N    N
O    O
F    F
Si   Si
P    P
S    S
Cl   Cl
Ca   Ca
As   As
Se   Se
Br   Br
Li   Li, Na
B    B, Re
Mg   Mg, Mn
Sn   Sn, Pb
Te   Te, Po
I    I, At
Os   Os, Ir
Sc   Sc, Ti, Zr
Fe   Fe, Hf, Ta
Co   Co, Sb, W
Sr   Sr, Ba, Ra
Pd   Pd, Pt, Au
Be   Be, Zn, Cd, Hg
K    K, Rb, Cs, Fr
V    V, Cr, Nb, Mo, Tc
Ni   Ni, Cu, Ge, Ru, Rh, Ag, Bi
In   In, La, Ce, Pr, Nd, Pm, Sm, Eu
Al   Al, Ga, Y, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Tl
R    R, He, Ne, Ar, Kr, Xe, Rn, Ac, Th, Pa, U, Np, Pu, Am, Cm, Bk, Cf, Es, Fm, Md, No, Lr, Db, Jl
==== ========

Acyclic atoms are preceded by a hyphen "-" mark.

Here's the multi-level neighborhood for the molecule
represented by the SMILES string CC(=O)Cl::

 # The contents of this file were derived from
 # Title = acid chloride
 -C(-H(-C)-H(-C)-H(-C)-C(-C-O-Cl))
 -C(-C(-H-H-H-C)-O(-C)-Cl(-C))
 -O(-C(-C-O-Cl))
 -Cl(-C(-C-O-Cl))
 -H(-C(-H-H-H-C))
 -H(-C(-H-H-H-C))
 -H(-C(-H-H-H-C))

.. [fpbg99] Dmitrii Filimonov, Vladimir Poroikov, Yulia Borodina, and
            Tatyana Gloriozova. **Chemical Similarity Assessment through
            Multilevel Neighborhoods of Atoms: Definition and Comparison with
            the Other Descriptors.** *J. Chem. Inf. Comput. Sci.* **1999**, *39*, 666-670.
            [`Link <http://dx.doi.org/10.1021/ci980335o>`_]



.. note:: This is a write-only format.

Write Options
~~~~~~~~~~~~~ 

-L <num>  *Levels (default = 2)*


