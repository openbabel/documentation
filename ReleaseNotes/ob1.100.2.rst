Open Babel 1.100.2
==================

Released on 2004-02-22.

What's new from 1.100.1
~~~~~~~~~~~~~~~~~~~~~~~

 - Shared library (version 0:0:0) built by default on POSIX systems
   (e.g. Linux, BSD, Mac OS X...)
 - Fixed installation of header files. The headers in the math/
   subdirectory were not installed alongside the other headers.
 - Added tools/ directory with small examples of using libopenbabel:
   * obgrep: Use SMARTS patterns to grep through multi-molecule files.
   * obfit:  Use SMARTS patterns to align molecules on substructures.
   * obrotate: Rotate a torsional bond matching a SMARTS pattern.
 - Improved PDB support: uses HETATM records more appropriately, attempts to
   determine chain/residue information if not available.
 - Fixed a variety of bugs in ShelX support.
 - Added support for handling atom and molecule spin multiplicity.
 - Updated documentation -- not yet complete, but significantly improved.
 - Fixed major omissions in CML readers and writers. All versions of CML are now
   supported (CML1/2 and array/nonArray). Also added \*.bat
   file for roundtripping between these formats for both 2- and 3-D data.
   Fixed bugs in test/cmltest/cs2a.mol.cml.
 - Building and running the test-suite in a build-directory other than the
   source-directory is now fully supported.
 - Support for the Intel C++ Compiler on GNU/Linux.
 - Miscellaneous fixes to make it easier to compile on non-POSIX machines.

New File Formats
~~~~~~~~~~~~~~~~

  -Export: Chemtool
           Chemical Resource Kit (CRK) 2D and 3D
           Parallel Quantum Solutions (PQS)
  -Import: CRK 2D and 3D
           PQS
