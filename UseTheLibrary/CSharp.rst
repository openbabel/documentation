CSharp and OBDotNet
===================

**OBDotNet** is a compiled assembly that allows OpenBabel to be used from the various .NET  languages (e.g. Visual Basic, C#, IronPython, IronRuby, and J#) on Windows, Linux and MacOSX. The current version is OBDotNet 0.3. 

Installation
------------

C# and Visual Basic
~~~~~~~~~~~~~~~~~~~

The following instructions describe how to use OBDotNet in a C# project using Microsoft Visual C# 2008 Express Edition. You should be able to apply these instructions to more recent compilers, and also to Visual Basic projects.

   1. First you need to download and install the :program:`OpenBabelGUI version 2.2.3`
   2. Download and extract OBDotNet-0.3.zip_
   3. Start :program:`Microsoft Visual C# Express Edition` and create a new new project, for example a console application
   4. Replace the code in :file:`Program.cs` by this `example program`_ and save the project somewhere
   5. Copy and paste the entire contents of the extracted :file:`OBDotNet-0.3.zip` folder into the project directory in :file:`bin/Debug`
   6. Right click on References in the right hand pane and choose the Browse Tab to add a reference to :file:`OBDotNet.dll` in the :file:`bin/Debug` directory.
   7. If you build the project now, it should work.
   8. Uncomment the final line, and run it under :guilabel:`Debug`/:guilabel:`Start Debugging`. You should see the output of 44.0952, the molecular weight of propane.
   9. To run the program at the command line, you just type the full path to the exe located in the :file:`Debug` folder. 

.. _OBDotNet-0.3.zip : http://sf.net/projects/openbabel/files/OBDotNet/0.3/OBDotNet-0.3.zip/download
.. _example program: http://openbabel.svn.sf.net/viewvc/openbabel/openbabel/tags/openbabel-2-2-1/scripts/csharp/example.cs?revision=2910

Running under Mono
~~~~~~~~~~~~~~~~~~

For Linux or MacOSX follow the instructions in the :file:`README` file in :file:`scripts/csharp`.

OBDotNet API
------------

The API is almost identical to the Open Babel `C++ API`_. Differences are described here.

.. _C++ API: http://openbabel.org/api

.. rubric:: Using iterators

In OBDotNet, iterators are provided as methods of the relevant class. The full list is as follows:

* **OBMol** has ``.Atoms()``, ``.Bonds()``, ``.Residues()``, and ``.Fragments()``. These correspond to :obapi:`OBMolAtomIter`, :obapi:`OBMolBondIter`, :obapi:`OBMolResidueIter` and :obapi:`OBMolAtomDFSIter` respectively.
* **OBAtom** has :obapi:`.Bonds()` and :obapi:`.Neighbours()`. These correspond to :obapi:`OBAtomBondIter` and :obapi:`OBAtomAtomIter` respectively. 

.. highlight:: c#

Such iterators are used as follows::

        foreach (OBAtom atom in myobmol.Atoms())
            System.Console.WriteLine(atom.GetAtomType());

Other iterators in the C++ API not listed above can still be used through their IEnumerator methods.

.. rubric:: Handling OBGenericData

To cast :obapi:`OBGenericData` to a specific subclass, you should use the ``.Downcast <T>`` method, where ``T`` is a subclass of **OBGenericData**.

.. rubric:: Open Babel Constants

OpenBabel constants are available in the class ``openbabelcsharp``.

Examples
--------

The following sections show how the same example application would be programmed in C#, Visual Basic and IronPython. The programs print out the molecular weight of propane (represented by the SMILES string "CCC").

.. rubric:: C#

::

        using System;
        using OpenBabel;

        namespace MyConsoleApplication
        {
            class Program
            {
                static void Main(string[] args)
                {
                    OBConversion obconv = new OBConversion();
                    obconv.SetInFormat("smi");
                    OBMol mol = new OBMol();
                    obconv.ReadString(mol, "CCC");
                    System.Console.WriteLine(mol.GetMolWt());
                }
            }
        }

.. rubric:: Visual Basic

.. code-block:: vb.net

        Imports OpenBabel

        Module Module1

            Sub Main()
                Dim OBConv As New OBConversion()
                Dim Mol As New OBMol()

                OBConv.SetInFormat("smi")
                OBConv.ReadString(Mol, "CCC")
                System.Console.Write("The molecular weight of propane is " & Mol.GetMolWt())
            End Sub

        End Module

.. rubric:: IronPython

.. code-block:: python

        import clr
        clr.AddReference("OBDotNet.dll")

        import OpenBabel as ob

        conv = ob.OBConversion()
        conv.SetInFormat("smi")
        mol = ob.OBMol()
        conv.ReadString(mol, "CCC")
        print mol.GetMolWt()

