CSharp and OBDotNet
===================

**OBDotNet** is a compiled assembly that allows Open Babel to be used from the various .NET  languages (e.g. Visual Basic, C#, IronPython, IronRuby, and J#) on Windows, Linux and MacOSX. The current version is OBDotNet 0.4. 

Installation
------------

Windows
~~~~~~~

The :file:`OBDotNet.dll` assembly provided on Windows was compiled using the .NET framework v3.5 for the x86 platform. To use it, you will need to compile your code using .NET v3.5 or newer and you will also need to target x86 (``/platform:x86``).

The following instructions describe how to compile a simple C# program that uses OBDotNet:

   1. First you need to download and install the :program:`OpenBabelGUI version 2.3.1`
   2. Next create an example CSharp program that uses the Open Babel API (see below for one or use `this link`_). Let's call this :file:`example.cs`.
   3. Copy :file:`OBDotNet.dll` from the Open Babel installation into the same folder as :file:`example.cs`.
   4. Open a command prompt at the location of :file:`example.cs` and compile it as follows::

              C:\Work> C:\Windows\Microsoft.NET\Framework\v3.5\csc.exe
                                         /reference:OBDotNet.dll /platform:x86 example.cs

   5. Run the created executable, :program:`example.exe`, to discover the molecule weight of propane::

              C:\Work> example.exe
              44.09562

If you prefer to use the MSVC# GUI, note that the Express edition does not have the option to choose x86 as a target. This will be a problem if you are using a 64-bit operating system. There's some information at `Coffee Driven Development`_ on how to get around this.

.. _this link: http://openbabel.svn.sf.net/viewvc/openbabel/openbabel/tags/openbabel-2-2-1/scripts/csharp/example.cs?revision=2910
.. _Coffee Driven Development: http://coffeedrivendevelopment.blogspot.com/2008/06/hacking-vs-c-2008-express.html

MacOSX and Linux
~~~~~~~~~~~~~~~~

On Linux and MacOSX you need to use Mono, the open source implementation of the .NET framework, to compile the bindings. The following instructions describe how to compile and use these bindings:

  1. :file:`OBDotNet.dll` is included in the Open Babel source distribution in :file:`scripts/csharp`. To compile a CSharp application that uses this (e.g. the example program shown below), use a command similar to the following::

       gmcs example.cs /reference:../openbabel-2.3.1/scripts/csharp/OBDotNet.dll
     
  2. To run this on MacOSX or Linux you need to compile the CSharp bindings as described in the section :ref:`Compile bindings`. This creates :file:`lib/libopenbabel_csharp.so` in the build directory.

  3. Add the location of :file:`OBDotNet.dll` to the environment variable MONO_PATH. Add the location of :file:`libopenbabel_csharp.so` to the environment variable LD_LIBRARY_PATH. Additionally, if you have not installed Open Babel globally you should set BABEL_LIBDIR to the location of the Open Babel library and BABEL_DATADIR to the :file:`data` directory.

  4. Run :file:`example.exe`::

       $ ./example.exe
       44.09562 

OBDotNet API
------------

The API is almost identical to the Open Babel :ref:`C++ API <API>`. Differences are described here.

.. rubric:: Using iterators

In OBDotNet, iterators are provided as methods of the relevant class. The full list is as follows:

* **OBMol** has ``.Atoms()``, ``.Bonds()``, ``.Residues()``, and ``.Fragments()``. These correspond to :obapi:`OBMolAtomIter`, :obapi:`OBMolBondIter`, :obapi:`OBResidueIter` and :obapi:`OBMolAtomDFSIter` respectively.
* **OBAtom** has ``.Bonds()`` and ``.Neighbours()``. These correspond to :obapi:`OBAtomBondIter` and :obapi:`OBAtomAtomIter` respectively. 

.. highlight:: c#

Such iterators are used as follows::

        foreach (OBAtom atom in myobmol.Atoms())
            System.Console.WriteLine(atom.GetAtomType());

Other iterators in the C++ API not listed above can still be used through their IEnumerator methods.

.. rubric:: Handling OBGenericData

To cast :obapi:`OBGenericData` to a specific subclass, you should use the ``.Downcast <T>`` method, where ``T`` is a subclass of **OBGenericData**.

.. rubric:: Open Babel Constants

Open Babel constants are available in the class ``openbabelcsharp``.

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

