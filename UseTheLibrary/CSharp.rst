CSharp and OBDotNet
===================

**OBDotNet** is a compiled assembly that allows OpenBabel to be used from the various .NET  languages (e.g. Visual Basic, C#, IronPython, IronRuby, and J#) on Windows, Linux and MacOSX. The current version is OBDotNet 0.4. 

Installation
------------

Windows
~~~~~~~

The OBDotNet.dll assembly provided on Windows was compiled using the .NET framework v3.5 for the x86 platform. To use it, you will need to compile your code using .NET v3.5 or newer and you will also need to target x86 (``/platform:x86``).

The following instructions describe how to compile a simple C# program that uses OBDotNet:

   1. First you need to download and install the :program:`OpenBabelGUI version 2.3.0`
   2. Download and extract OBDotNet-0.4.zip_. There should be an example CSharp program included, :program:`example.cs`.
   3. Open a command prompt wherever you unzipped OBDotNet and compile :program:`example.cs` as follows::

              C:\Tools\OBDotNet-0.4> C:\Windows\Microsoft.NET\Framework\v3.5\csc.exe /reference:OBDotNet.dll /platform:x86 example.cs

   4. Run the created executable, :program:`example.exe`, to discover the molecule weight of propane::

              C:\Tools\OBDotNet-0.4> example.exe
              44.09562

If you prefer to use the MSVC# GUI, note that the Express edition does not have the option to choose x86 as a target. This will be a problem if you are using a 64-bit operating system. There's some information at `Coffee Driven Development`_ on how to get around this.

.. _OBDotNet-0.4.zip : http://sf.net/projects/openbabel/files/OBDotNet/0.4/OBDotNet-0.4.zip/download
.. _example program: http://openbabel.svn.sf.net/viewvc/openbabel/openbabel/tags/openbabel-2-2-1/scripts/csharp/example.cs?revision=2910
.. _Coffee Driven Development: http://coffeedrivendevelopment.blogspot.com/2008/06/hacking-vs-c-2008-express.html

Running under Mono
~~~~~~~~~~~~~~~~~~

For Linux or MacOSX, instructions will one day appear here. **TODO**

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

