Java
====

The :file:`openbabel.jar` file in the Open Babel distribution allows you to use the Open Babel C++ library from Java or any of the other JVM languages (Jython, JRuby, BeanShell, etc.). 

Quickstart Example
------------------

Let's begin by looking at an example program that uses Open Babel. The following program carries out file format conversion, iteration over atoms and SMARTS pattern matching:

.. code-block:: java

        import org.openbabel.*;

        public class Test {

           public static void main(String[] args) {
               // Initialise
               System.loadLibrary("openbabel_java");

               // Read molecule from SMILES string
               OBConversion conv = new OBConversion();
               OBMol mol = new OBMol();
               conv.SetInFormat("smi");
               conv.ReadString(mol, "C(Cl)(=O)CCC(=O)Cl");
             
               // Print out some general information
               conv.SetOutFormat("can");
               System.out.print("Canonical SMILES: " +
                 conv.WriteString(mol));
               System.out.println("The molecular weight is "
                 + mol.GetMolWt());
               for(OBAtom atom : new OBMolAtomIter(mol))
                   System.out.println("Atom " + atom.GetIdx()
                     + ": atomic number = " + atom.GetAtomicNum()
                     + ", hybridisation = " + atom.GetHyb());

               // What are the indices of the carbon atoms
               // of the acid chloride groups?
               OBSmartsPattern acidpattern = new OBSmartsPattern();
               acidpattern.Init("C(=O)Cl");
               acidpattern.Match(mol);
             
               vectorvInt matches = acidpattern.GetUMapList();
               System.out.println("There are " + matches.size() +
                                  " acid chloride groups");
               System.out.print("Their C atoms have indices: ");
               for(int i=0; i<matches.size(); i++)
                   System.out.print(matches.get(i).get(0) + " ");
           }
        }

	
Output::

        Canonical SMILES: ClC(=O)CCC(=O)Cl
        The molecular weight is 154.9793599
        Atom 1: atomic number = 6, hybridisation = 2
        Atom 2: atomic number = 17, hybridisation = 0
        Atom 3: atomic number = 8, hybridisation = 2
        Atom 4: atomic number = 6, hybridisation = 3
        Atom 5: atomic number = 6, hybridisation = 3
        Atom 6: atomic number = 6, hybridisation = 2
        Atom 7: atomic number = 8, hybridisation = 2
        Atom 8: atomic number = 17, hybridisation = 0
        There are 2 acid chloride groups
        Their C atoms have indices: 1 6 


Installation
------------

Windows
~~~~~~~

.. highlight:: bat

:file:`openbabel.jar` is installed along with the OpenBabelGUI on Windows, typically in :file:`C:/Program Files (x86)/OpenBabel-2.3.1`. As an example of how to use :file:`openbabel.jar`, download OBTest.java_ and compile and run it as follows::

        C:\> set CLASSPATH=C:\Program Files (x86)\OpenBabel-2.3.1\openbabel.jar;.
        C:\> "C:\Program Files\Java\jdk1.5.0_16\bin\javac.exe" OBTest.java
        C:\> "C:\Program Files\Java\jdk1.5.0_16\bin\java.exe" OBTest
        Running OBTest...
        Benzene has 6 atoms.
        C:\>

.. _OBTest.java: http://openbabel.svn.sf.net/viewvc/openbabel/openbabel/tags/openbabel-2-2-1/scripts/java/OBTest.java?revision=2910

MacOSX and Linux
~~~~~~~~~~~~~~~~

The following instructions describe how to compile and use these bindings on MacOSX and Linux:

  1. :file:`openbabel.jar` is included in the Open Babel source distribution in :file:`scripts/java`. To compile a Java application that uses this (e.g. the example program shown above), use a command similar to the following::

       javac Test.java -cp ../openbabel-2.3.1/scripts/java/openbabel.jar
     
  2. To run the resulting :file:`Test.class` on MacOSX or Linux you first need to compile the Java bindings as described in the section :ref:`Compile bindings`. This creates :file:`lib/libopenbabel_java.so` in the build directory.

  3. Add the location of :file:`openbabel.jar` to the environment variable CLASSPATH, not forgetting to append the location of :file:`Test.class` (typically ".")::

       export CLASSPATH=/home/user/Tools/openbabel-2.3.1/scripts/java/openbabel.jar:.
     
  4. Add the location of :file:`libopenbabel_java.so` to the environment variable LD_LIBRARY_PATH. Additionally, if you have not installed Open Babel globally you should set BABEL_LIBDIR to the location of the Open Babel library and BABEL_DATADIR to the :file:`data` directory.

  5. Now, run the example application. The output should be as shown above.

API
---

:file:`openbabel.jar` provides direct access to the C++ Open Babel library from Java through the namespace **org.openbabel**. This binding is generated using the SWIG package and provides access to almost all of the Open Babel interfaces from Java, including the base classes :obapi:`OBMol`, :obapi:`OBAtom`, :obapi:`OBBond`, and :obapi:`OBResidue`, as well as the conversion framework :obapi:`OBConversion`.

Essentially any call in the C++ API is available to Java programs with very little difference in syntax. As a result, the principal documentation is the :ref:`Open Babel C++ API documentation <API>`. A few differences exist, however:

.. highlight:: java

* Global variables, global functions and constants in the C++ API can be found in **org.openbabel.openbabel_java**. The variables are accessible through get methods.
* When accessing various types of :obapi:`OBGenericData`, you will need to cast them to the particular subclass using the global functions, *toPairData*, *toUnitCell*, etc.
* The Java versions of the iterator classes in the C++ API (that is, all those classes ending in *Iter*) implement the *Iterator* and *Iterable* interfaces. This means that the following *foreach* loop is possible::

        for(OBAtom atom : new OBMolAtomIter(mol)) {
            System.out.println(atom.GetAtomicNum());
        }

* To facilitate use of the :obapi:`OBMolAtomBFSIter`, *OBAtom* has been extended to incorporate a *CurrentDepth* value, accessible through a get method::

        for(OBAtom atom : new OBMolAtomBFSIter(mol)) {
            System.out.println(atom.GetCurrentDepth());
        }

