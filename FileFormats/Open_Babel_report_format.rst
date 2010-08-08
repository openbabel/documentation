.. _Open_Babel_report_format:

Open Babel report format (report)
=================================

**A detailed report on the geometry of a molecule**

The report format presents a report of various molecular information,
including:

* Filename / molecule title
* Molecular formula
* Mass
* Exact mass (i.e., for high-resolution mass spectrometry, the mass of the most abundant elements)
* Total charge (if not electrically neutral)
* Total spin (if not singlet)
* Interatomic distances
* Atomic charges
* Bond angles
* Dihedral angles
* Chirality information (including which atoms are chiral)
* Additional comments in the input file

Example for benzene::

 FILENAME: benzene.report
 FORMULA: C6H6
 MASS: 78.1118
 EXACT MASS: 78.0469502
 INTERATOMIC DISTANCES

               C   1      C   2      C   3      C   4      C   5      C   6
               ------------------------------------------------------------------
    C   1    0.0000
    C   2    1.3958     0.0000
    C   3    2.4176     1.3958     0.0000
    C   4    2.7916     2.4176     1.3958     0.0000
    C   5    2.4176     2.7916     2.4176     1.3958     0.0000
    C   6    1.3958     2.4176     2.7916     2.4176     1.3958     0.0000
    H   7    1.0846     2.1537     3.4003     3.8761     3.4003     2.1537
    H   8    2.1537     1.0846     2.1537     3.4003     3.8761     3.4003
    H   9    3.4003     2.1537     1.0846     2.1537     3.4003     3.8761
    H  10    3.8761     3.4003     2.1537     1.0846     2.1537     3.4003
    H  11    3.4003     3.8761     3.4003     2.1537     1.0846     2.1537
    H  12    2.1537     3.4003     3.8761     3.4003     2.1537     1.0846

               H   7      H   8      H   9      H  10      H  11      H  12
               ------------------------------------------------------------------
    H   7    0.0000
    H   8    2.4803     0.0000
    H   9    4.2961     2.4804     0.0000
    H  10    4.9607     4.2961     2.4803     0.0000
    H  11    4.2961     4.9607     4.2961     2.4803     0.0000
    H  12    2.4803     4.2961     4.9607     4.2961     2.4804     0.0000

 ATOMIC CHARGES
    C   1   -0.1000000000
    C   2   -0.1000000000
    C   3   -0.1000000000
    C   4   -0.1000000000
    C   5   -0.1000000000
    C   6   -0.1000000000
    H   7    0.1000000000
    H   8    0.1000000000
    H   9    0.1000000000
    H  10    0.1000000000
    H  11    0.1000000000
    H  12    0.1000000000

 BOND ANGLES
    7    1    2   HC  Car  Car    120.000
    1    2    3  Car  Car  Car    120.000
    1    2    8  Car  Car   HC    120.000
    8    2    3   HC  Car  Car    120.000
    2    3    4  Car  Car  Car    120.000
    2    3    9  Car  Car   HC    120.000
    9    3    4   HC  Car  Car    120.000
    3    4    5  Car  Car  Car    120.000
    3    4   10  Car  Car   HC    120.000
   10    4    5   HC  Car  Car    120.000
    4    5    6  Car  Car  Car    120.000
    4    5   11  Car  Car   HC    120.000
   11    5    6   HC  Car  Car    120.000
    5    6    1  Car  Car  Car    120.000
    5    6   12  Car  Car   HC    120.000
   12    6    1   HC  Car  Car    120.000
    6    1    2  Car  Car  Car    120.000
    6    1    7  Car  Car   HC    120.000
    2    1    7  Car  Car   HC    120.000
    3    2    8  Car  Car   HC    120.000
    4    3    9  Car  Car   HC    120.000
    5    4   10  Car  Car   HC    120.000
    6    5   11  Car  Car   HC    120.000
    1    6   12  Car  Car   HC    120.000

 TORSION ANGLES
    6    1    2    3      0.026
    6    1    2    8   -179.974
    7    1    2    3    179.974
    7    1    2    8     -0.026
    1    2    3    4     -0.026
    1    2    3    9   -179.974
    8    2    3    4    179.974
    8    2    3    9      0.026
    2    3    4    5      0.026
    2    3    4   10    179.974
    9    3    4    5    179.974
    9    3    4   10     -0.026
    3    4    5    6     -0.026
    3    4    5   11    179.974
   10    4    5    6   -179.974
   10    4    5   11      0.026
    4    5    6    1      0.026
    4    5    6   12    179.974
   11    5    6    1   -179.974
   11    5    6   12     -0.026
    5    6    1    2     -0.026
    5    6    1    7   -179.974
   12    6    1    2    179.974
   12    6    1    7      0.026

.. seealso::

  :ref:`Open_Babel_molecule_report`



.. note:: This is a write-only format.

