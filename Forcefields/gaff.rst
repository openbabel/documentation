.. _Generalized_Amber_Force_Field:

Generalized Amber Force Field (gaff)
=============================

The `AMBER force field <http://en.wikipedia.org/wiki/AMBER>`_ (or more
accurately, family of force fields used with the `AMBER software
<http://ambermd.org/>`_ are designed mainly for biomolecules (i.e.,
proteins, DNA, RNA, carbohydrates, etc.).

A general set of parameters for small organic molecules to allow
simulations of drugs and small molecule ligands in conjugtion with
biomolecules is provided by `GAFF
<http://ambermd.org/antechamber/gaff.html>`_. Parameters exist for
almost all molecules made of C, N, O, H, S, P, F, Cl, Br, and I, and
are compatible with the AMBER functional forms.

Typically, GAFF expects partial charges assigned using quantum
chemistry (i.e., HF/6-31G* RESP charges or AM1-BCC). The Open Babel
implementation can use other partial charges as available, although
with lower resulting accuracy.

In general, GAFF is expected to provide accuracy (in terms of geometry
and energies) on par or better than the :ref:`MMFF94_Force_Field`.

.. note:: If you use GAFF, you should cite the appropriate paper:
          Wang, J., Wolf, R. M.; Caldwell, J. W.;Kollman, P. A.;
          Case, D. A. "Development and testing of a general AMBER
          force field". *Journal of Computational Chemistry,* **2004**
          v. 25, 1157-1174.
