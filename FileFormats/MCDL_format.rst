.. _MCDL_format:

MCDL format (mcdl)
==================

**Modular Chemical Descriptor Language**


As described in Gakh A.A., Burnett M.N.,
Modular Chemical Descriptor Language (MCDL):
Composition, Connectivity and Supplementary Modules
J.Chem.Inf.Comput.Sci, 2001, 41, 1494-1499

Here's an example conversion from SMILES to MCDL::

  obabel -:"CC(=O)Cl" -omcdl
  CHHH;COCl[2]


