.. _MMFF94_Force_Field:

MMFF94 Force Field (mmff94)
=============================

The MMFF94 force field (and the related MMFF94s) were developed by
Merck and are sometimes called the Merck Molecular Force Field,
although MMFF94 is no longer considered an acronym.

The method provides good accuracy across a range of organic and
*drug-like* molecules. The core parameterization was provided by
high-quality quantum calculations, rather than experimental data,
across ~500 test molecular systems.

The method includes parameters for a wide range of atom types
including the following common organic elements: C, H, N, O, F, Si, P,
S, Cl, Br, and I. It also supports the following common ions: Fe\
:sup:`+2`\ , Fe\ :sup:`+3`\ , F\ :sup:`-`\ , Cl\ :sup:`-`\ , Br\
:sup:`-`\ , Li\ :sup:`+`\ , Na\ :sup:`+`\ , K\ :sup:`+`\ , Zn\
:sup:`+2`\ , Ca\ :sup:`+2`\ , Cu\ :sup:`+1`\ , Cu\ :sup:`+2`\ ,
and Mg\ :sup:`+2`\ . The Open Babel implementation should
automatically perform atom typing and recognize these elements.

MMFF94 performs well at optimizing geometries, bond lengths, angles,
etc. and includes electrostatic and hydrogen-bonding effects.

.. note:: If you use MMFF94 you should cite the appropriate papers:

   1. Thomas A. Halgren, *J. Comput. Chem.,* 17, 490-519 **(1996).**
   2. Thomas A. Halgren, *J. Comput. Chem.,* 17, 520-552 **(1996).**
   3. Thomas A. Halgren, *J. Comput. Chem.,* 17, 553-586 **(1996).**
   4. Thomas A. Halgren and Robert B. Nachbar, *J. Comput. Chem.,* 17, 587-615 **(1996).**
   5. Thomas A. Halgren, *J. Comput. Chem.,* 17, 616-641 **(1996).**

Some experiments and most theoretical calculations show significant
pyramidal "puckering" at nitrogens in isolated structures. The MMFF94s
(static) variant has slightly different out-of-plane bending and
dihedral torsion parameters to planarize certain types of delocalized
trigonal N atoms, such as aromatic aniline. This provides a better
match to the time-average molecular geometry in solution or crystal
structures.

If you are comparing force-field optimized molecules to crystal
structure geometries, we recommend using the MMFF94s variant for this
reason. All other parameters are identical.

However, if you are perfoming "docking" simulations, consideration of
active solution conformations, or other types of computational
studies, we recommend using the MMFF94 variant, since one form or
another of the N geometry will predominate.

.. note:: If you use MMFF94s, you should also cite the following paper that details that method:

    6. Thomas A. Halgren, *J. Comput. Chem.*, 20, 720-729 **(1999).**
