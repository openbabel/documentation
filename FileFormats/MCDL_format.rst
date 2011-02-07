.. _MCDL_format:

MCDL format (mcdl)
==================

**Modular Chemical Descriptor Language**


As described in [gb2001]_.

.. [gb2001] A.A. Gakh and M.N. Burnett. **Modular Chemical Descriptor
            Language (MCDL): Composition, Connectivity and
            Supplementary Modules.**
            *J. Chem. Inf. Comput. Sci.*, **2004**, *41*, 1491-1499.
            [`Link <http://dx.doi.org/10.1021/ci000108y>`_]

Here's an example conversion from SMILES to MCDL::

  obabel -:"CC(=O)Cl" -omcdl
  CHHH;COCl[2]


