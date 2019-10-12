Open Babel 1.100.0
==================

Released on 2002-12-12.

What's new from 1.99
~~~~~~~~~~~~~~~~~~~~

 - Bond order typing is performed when importing from formats with no notion of
   bonds (quantum chemistry programs, XYZ, etc.).  -Now better conforms to the ISO
   C++ standard, should compile on most modern C++ compilers.
 - Improved test suite, including "roundtrip" testing, ensuring more accurate translations.
 - Support for the Chemical Markup Language (CML) and other file formats. (see below)
 - Improved PDB support -- should read PDB files more accurately and hew closer to the current PDB standard for export.
 - Improved Gaussian input generation.
 - Added support for the Chemical MIME standards, including command-line switches.
 - Added support for using the babel program as a pipe for a "translation filter" for other programs.
 - Can add hydrogen atoms based on pH.
 - Fixed a variety of memory leaks, sometimes causing other bugs.
 - Fixed a wide variety of bugs in various file formats.
 - Faster SMARTS matching and some overall speedups across the program.
 - API documentation using the Doxygen system.
 - Of course there are *many* other bug-fixes and improvements.

New File Formats
~~~~~~~~~~~~~~~~

  -Import: NWChem Output
  -Export: POV-Ray, NWChem Input
  -Both: CML, ViewMol, Chem3D
