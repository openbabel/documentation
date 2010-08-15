Java
====

The :file:`openbabel.jar` file in the OpenBabel distribution allows you to use the OpenBabel C++ library from Java or any of the other JVM languages (Jython, JRuby, BeanShell, etc.). 

Quickstart Example
------------------

Let's begin by looking at an example program that uses OpenBabel. The following program carries out file format conversion, iteration over atoms and SMARTS pattern matching:

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
             
               vvInt matches = acidpattern.GetUMapList();
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

openbabel.jar is installed along with the OpenBabelGUI on Windows, typically in :file:`C:\Program Files\OpenBabel-2.2.1`. As an example of how to use openbabel.jar, download OBTest.java_ and compile and run it as follows::

        C:\> set CLASSPATH=C:\Program Files\OpenBabel-2.2.1\openbabel.jar;.
        C:\> "C:\Program Files\Java\jdk1.5.0_16\bin\javac.exe" OBTest.java
        C:\> "C:\Program Files\Java\jdk1.5.0_16\bin\java.exe" OBTest
        Running OBTest...
        Benzene has 6 atoms.
        C:\>

.. _OBTest.java: http://openbabel.svn.sf.net/viewvc/openbabel/openbabel/tags/openbabel-2-2-1/scripts/java/OBTest.java?revision=2910

Linux
~~~~~

.. highlight:: bash

::

        % javac *.java
        # assuming that jni.h is found in /usr/include/java
        % g++ -c -fpic openbabel_java.cpp -I../../include -I/usr/include/java
        # assuming that the C++ libopenbabel is in /usr/local/lib
        % g++ -shared -L/usr/local/lib openbabel_java.o -lopenbabel -o libopenbabel.so

To run Java programs, try::

        LD_PRELOAD=/usr/local/lib/libopenbabel.so java OBTest

Mac OS X
~~~~~~~~

::

        % javac *.java
        % g++ -c -I/System/Library/Frameworks/JavaVM.framework/Headers openbabel_java.cpp
        % g++ -dynamiclib -o libopenbabel.jnilib openbabel_java.o -framework JavaVM -L/usr/local/lib -lopenbabel

To run the OBTest program, try::

        % java OBTest

More information on compiling JNI libraries on Mac OS X can be found at the `Apple developer website`_.

.. _Apple developer website: http://developer.apple.com/documentation/Java/Conceptual/Java14Development/05-CoreJavaAPIs/CoreJavaAPIs.html#//apple_ref/doc/uid/TP40001902-210780-TPXREF144

API
---

:file:`openbabel.jar` provides direct access to the C++ Open Babel library from Java through the namespace **org.openbabel**. This binding is generated using the SWIG package and provides access to almost all of the Open Babel interfaces from Java, including the base classes :obapi:`OBMol`, :obapi:`OBAtom`, :obapi:`OBBond`, and :obapi:`OBResidue`, as well as the conversion framework :obapi:`OBConversion`.

Essentially any call in the C++ API is available to Java programs with very little difference in syntax. As a result, the principal documentation is the `Open Babel C++ API documentation`_. A few differences exist, however:

.. _Open Babel C++ API documentation: http://openbabel.org/api

.. highlight:: java

* Global variables, global functions and constants in the C++ API can be found in **org.openbabel.openbabel_java**. The variables are accessible through get methods.
* When accessing various types of :obapi:`OBGenericData`, you will need to cast them to the particular subclass using the global functions, *toPairData*, *toUnitCell*, etc.
* The Java versions of the iterator classes in the C++ API (that is, all those classes ending in *Iter*) implement the *Iterator* and *Iterable* interfaces. This means that the following *foreach* loop is possible::

        for(OBAtom atom : new OBMolAtomIter(mol)) {
            System.out.println(atom.GetAtomicNum());
        }

* To facilitate use of the :obapi:`OBMolAtomBFSIter`, *OBAtom* has been extended to incorporate a *CurrentDepth* value, accessible through *Get*::

        for(OBAtom atom : new OBMolAtomBFSIter(mol)) {
            System.out.println(atom.GetCurrentDepth());
        }

