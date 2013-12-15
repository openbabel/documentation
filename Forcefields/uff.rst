.. _Universal_Force_Field:

Universal Force Field (uff)
=============================

One problem with traditional force fields is a limited set of elements
and atom types. The Universal Force Field (UFF) was developed to
provide a set of rules and procedures for producing appropriate
parameters across the entire periodic table.

While some implementations of UFF use the QEq partial charge model,
the original manuscript and authors of UFF determined the
parameterization without an electrostatic model. Consequently, by
default the Open Babel implementation does not use electrostatic
interactions.

.. note:: If you use UFF, you should cite the appropriate paper:

          Rappe, A. K.; Casewit, C. J.; Colwell, K. S.;
          Goddard, W. A. III;  Skiff, W. M.; "UFF, a full periodic
          table force field for molecular mechanics and molecular
          dynamics simulations." *J Am Chem Soc*, **1992** v. 114,
          10024-10039.
