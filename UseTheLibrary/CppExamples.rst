C++
===

How to use Open Babel from C++
------------------------------

Here's an example C++ program that uses the Open Babel toolkit to convert between two chemical file formats:

.. highlight:: c++

::

  #include <iostream>
  #include <openbabel/obconversion.h>
  using namespace std;

  int main(int argc,char **argv)
  {
    if(argc<3)
    {
      cout << "Usage: ProgrameName InputFileName OutputFileName";
      return 1;
    }

    ifstream ifs(argv[1]);
    if(!ifs)
    {
      cout << "Cannot open input file";
      return 1;
    }
    ofstream ofs(argv[2]);
    if(!ofs)
    {
      cout << "Cannot open output file";
      return 1;
    }
    OpenBabel::OBConversion conv(&ifs, &ofs);
    if(!conv.SetInAndOutFormats("CML","MOL"))
    {
      cout << "Formats not available" << "InputFileName";
      return 1;
    }
    int n = conv.Convert();
    cout << n << " molecules converted";

    return 0;
  }

Next, we'll look at how to compile this.

How to compile against the Open Babel library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using Makefiles
***************

The following Makefile can be used to compile the above example, assuming that it's saved as :file:`example.cpp`. You need to have already installed Open Babel somewhere. If the include files or the library are not automatically found when running :command:`make`, you can specify the location as shown by the commented out statements in CFLAGS and LDFLAGS below.

.. code-block:: makefile

  CC = g++
  CFLAGS = -c # -I /home/user/Tools/openbabel/install/include/openbabel-2.0
  LDFLAGS = -lopenbabel # -L /home/user/Tools/openbabel/install/lib

  all: example

  example: example.o
	$(CC) $(LDFLAGS) example.o -o example

  example.o: example.cpp
	$(CC) $(CFLAGS) $(LDFLAGS) example.cpp

  clean:
	rm -rf example.o example

Using CMake
***********

Rather than create a Makefile yourself, you can get CMake to do it for you. The nice thing about using CMake is that it can generate not only Makefiles, but also project files for MSVC++, KDevelop and Eclipse (among others). The following :file:`CMakeLists.txt` can be used to generate any of these. The commented out lines can be used to specify the location of the Open Babel library and include files if necessary.

.. code-block:: cmake

  cmake_minimum_required(VERSION 2.6)
  add_executable(example example.cpp)
  target_link_libraries(example openbabel)
  # target_link_libraries(example /home/user/Tools/openbabel/install/lib/libopenbabel.so)
  # include_directories(/home/user/Tools/openbabel/install/include/openbabel-2.0)

Further examples
~~~~~~~~~~~~~~~~

Output Molecular Weight for a Multi-Molecule SDF File
*****************************************************

Let's say we want to print out the molecular weights of every molecule in an SD file. Why? Well, we might want to plot a histogram of the distribution, or see whether the average of the distribution is significantly different (in the statistical sense) compared to another SD file.

::

  #include <iostream>

  #include <openbabel/obconversion.h>
  #include <openbabel/mol.h>

  int main(int argc,char **argv)
  {
    OBConversion obconversion;
    obconversion.SetInFormat("sdf");
    OBMol mol;

    bool notatend = obconversion.ReadFile(&mol,"../xsaa.sdf");
    while (notatend)
    {
      std::cout << "Molecular Weight: " << mol.GetMolWt() << std::endl;
      
      mol.Clear();
      notatend = obconversion.Read(&mol);
    }

    return(0);
  }

Properties from SMARTS Matches
******************************

Let's say that we want to get the average bond length or dihedral angle over particular types of atoms in a large molecule. So we'll use SMARTS to match a set of atoms and loop through the matches. The following example does this for sulfur-carbon-carbon-sulfur dihedral angles in a polymer and the carbon-carbon bond lengths between the monomer units::

  OBMol obMol;
  OBBond *b1;
  OBConversion obConversion;
  OBFormat *inFormat;
  OBSmartsPattern smarts;
  smarts.Init("[#16D2r5][#6D3r5][#6D3r5][#16D2r5]");

  string filename;
  vector< vector <int> > maplist;
  vector< vector <int> >::iterator matches;
  double dihedral, bondLength;

  for (int i = 1; i < argc; i++)
    {
      obMol.Clear();
      filename = argv[i];
      inFormat = obConversion.FormatFromExt(filename.c_str());
      obConversion.SetInFormat(inFormat);
      obConversion.ReadFile(&obMol, filename);
      
      if (smarts.Match(obMol))
	{
	  dihedral = 0.0;
          bondLength = 0.0;
	  maplist = smarts.GetUMapList();
	  for (matches = maplist.begin(); matches != maplist.end(); matches++)
	    {
	      dihedral += fabs(obMol.GetTorsion((*matches)[0],
						(*matches)[1],
						(*matches)[2],
						(*matches)[3]));
              b1 = obMol.GetBond((*matches)[1], (*matches)[2]);
              bondLength += b1->GetLength();
	    }
	  cout << filename << ": Average Dihedral " << dihedral / maplist.size()
	       << " Average Bond Length " << bondLength / maplist.size()
	       << " over " << maplist.size() <<  " matches\n";
	}
    }

