.. _add-file-format:

How to add a new file format
============================

Adding support for a new file format is a relatively easy process, particularly with Open Babel 2.3 and later. Here are several important steps to remember when developing a format translator:

   1. Create a file for your format in :file:`src/formats/` or :file:`src/formats/xml/` (for XML-based formats). Ideally, this file is self-contained, although several formats modules are compiled across multiple source code files.
   2. Add the name of the new .cpp file to an appropriate place in :file:`src/formats/CMakeLists.txt`. It will now be compiled as part of the build process.
   3. Take a look at other file format code, particularly :file:`exampleformat.cpp`, which contains a heavily-annotated description of writing a new format. XML formats need to take a different approach; see the code in :file:`xcmlformat.cpp` or :file:`pubchemformat.cpp`.
   4. When reading in molecules (and thus performing a lot of molecular modifications) call :obapi:`OBMol::BeginModify() <OpenBabel::OBMol::BeginModify>` at the beginning and :obapi:`OBMol::EndModify() <OpenBabel::OBMol::EndModify>` at the end. This will ensure that perception routines do not run while you read in a molecule and are reset after your code finishes.
   5. Currently, lazy perception does not include connectivity and bond order assignment. If your format does not include bonds, make sure to call :obapi:`OBMol::ConnectTheDots() <OpenBabel::OBMol::ConnectTheDots>` and :obapi:`OBMol::PerceiveBondOrders() <OpenBabel::OBMol::PerceiveBondOrders>` after :obapi:`OBMol::EndModify() <OpenBabel::OBMol::EndModify>` to ensure bonds are assigned.
   6. Consider various input and output options that users can set from the command-line or GUI. For example, many quantum mechanics formats (as well as other formats which do not recognize bonds) offer the following options (GUI programs often offer these as a sub-menu which appears when choosing the appropriate format):

     * -as Call only :obapi:`OBMol::ConnectTheDots() <OpenBabel::OBMol::ConnectTheDots>` (single bonds only)
     * -ab No bond perception 

   7. Make sure to use generic data classes like :obapi:`OBUnitCell` and others as appropriate. If your format stores any sort of common data types, consider adding a subclass of :obapi:`OBGenericData` for use by other formats and user code.
   8. Please make sure to add several example files to the test set repository. Ideally, these should work several areas of your import code -- in the end, the more robust the test set, the more stable and useful Open Babel will be. The test files should include at least one example of a correct file and one example of an invalid file (i.e., something which will properly be ignored and not crash babel).
   9. That's it! Contact the openbabel-discuss_ mailing list with any questions, comments, or to contribute your new format code. 

After the code is released in a new version, a new entry for your format should be added to this website under the formats category and to the list of extensions pages. See some of the examples for more information. 

.. _openbabel-discuss: http://lists.sourceforge.net/lists/listinfo/openbabel-discuss
