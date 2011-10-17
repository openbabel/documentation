Install Open Babel
==================

Open Babel runs on Windows, Linux and MacOSX. You can either :ref:`install a binary package <Install binaries>` (the easiest option) or :ref:`compile Open Babel yourself <Compiling Open Babel>` (also easy, but much more geek cred).

.. _Install binaries:

Install a binary package
------------------------

Windows
~~~~~~~

Open Babel is available as a `binary installer`_ for Windows. It includes several command-line tools as well as a graphical user interface (GUI).

.. _binary installer: http://sourceforge.net/projects/openbabel/files/openbabel/2.3.1/OpenBabel2.3.1_Windows_Installer.exe/download

Advanced users may be interested in compiling Open Babel themselves (see :ref:`Compiling Open Babel`).

Linux
~~~~~

Open Babel binary packages are available from many Linux distributions including Ubuntu, OpenSUSE and Fedora.

In general, we recommend using the latest release of Open Babel (currently |release|). If this is not available for your Linux distribution, you should :ref:`compile Open Babel yourself <Compiling Open Babel>`.

.. _Compiling Open Babel:

Compiling Open Babel
--------------------

Open Babel is written in C++. Compiling is the process of turning this C++ into instructions that the computer's processor can understand, machine code.

Although pre-compiled (or "binary") packages are available for several platforms, there are several reasons you might want to compile Open Babel yourself:

- The current release (|release|) of Open Babel is not available for your platform. We recommend always using the latest release.
- You want more control over the features available. For example, perhaps you want the Python bindings but these were not included in your distribution.
- You want to use the latest development code.
- You want to add a new feature. It is easy to add new formats or operations to Open Babel as it has a plugin architecture (see :ref:`Add plugins`).
- You just want to compile stuff yourself. We understand.

Open Babel can be compiled on Linux, MacOSX, BSDs and other Unixes, and also on Windows (with Cygwin, MinGW or MSVC).

.. _requirements:

Requirements
~~~~~~~~~~~~

To build Open Babel, you **need** the following:

* The `source code <http://sourceforge.net/projects/openbabel/files/openbabel/2.3.1/openbabel-2.3.1.tar.gz/download>`__ for the latest release of Open Babel
* A C++ compiler

    Open Babel is written in standards-compliant C++. The best-supported compilers are GCC 4 and MSVC++ 2008, but it also compiles with Clang and Intel Compiler 11. 

* CMake 2.4 or newer

    Open Babel uses CMake as its build system. CMake is an open source cross-platform build system from KitWare.

    You need to install CMake 2.4 or newer. This is available as a binary package from the KitWare website; alternatively, it may be available through your package manager (on Linux). If necessary, you can also compile it yourself from the source code.

If you want to build the GUI (Graphical User Interface), you **need** the following in addition:

* wxWidgets 2.8 (or newer)
  
    Binary packages may be available through your package manager (*wx-common* and *wx2.8-headers* on Ubuntu) or from http://www.wxwidgets.org/downloads/. Otherwise, you could try compiling it yourself from the source code.

The following are **optional** when compiling Open Babel, but if not available some features will be missing:

* :program:`libxml2` development headers are required to read/write CML files and other XML formats (the *libxml2-dev* package in Ubuntu) 
* :program:`zlib` development libraries are required to support reading gzipped files (the *zlib1g-dev* package in Ubuntu) 
* :program:`Eigen` version 2 is **required** if using the language bindings in the release. In addition, if it not present, some API classes (OBAlign, OBConformerSearch) and plugins (the QEq and QTPIE charge models, the conformer operation) will not be available.

  Eigen may be available through your package manager (the *libeigen2-dev* package in Ubuntu). Alternatively, Eigen is available from http://eigen.tuxfamily.org. It doesn't need to be compiled or installed. Just unzip it and specify its location when configuring :program:`cmake` (see below) using ``-DEIGEN2_INCLUDE_DIR=whereever``.

* If using GCC 3.x to compile (and not GCC 4.x), then the Boost headers are required for certain formats (CML, Chemkin, Chemdraw CDX, MDL RXN and RSMI) 

If you want to use Open Babel using one of the supported **language bindings**, then the following notes may apply:

* You need the the Python development libraries to compile the Python bindings (package *python-dev* in Ubuntu)
* You need the the Perl development libraries to compile the Perl bindings (package *libperl-dev* in Ubuntu)
 

Basic build procedure
~~~~~~~~~~~~~~~~~~~~~

The basic build procedure is the same for all platforms and will be described first. After this, we will look at variations for particular platforms.

.. highlight:: console

1. The recommended way to build Open Babel is to use a separate source and build directory; for example, :file:`openbabel-2.3.1` and :file:`build`. The first step is to create these directories::

        $ tar zxf openbabel-2.3.1.tar.gz   # (this creates openbabel-2.3.1)
        $ mkdir build

2. Now you need to run :program:`cmake` to configure the build. The following will configure the build to use all of the default options::

        $ cd build
        $ cmake ../openbabel-2.3.1

3. If you need to specify an option, use the ``-D`` switch to :program:`cmake`. For example, the following line sets the value of ``CMAKE_INSTALL_PREFIX`` and ``CMAKE_BUILD_TYPE``::

        $ cmake ../openbabel-2.3.1 -DCMAKE_INSTALL_PREFIX=~/Tools -DCMAKE_BUILD_TYPE=DEBUG

   We will discuss various possible options later.

4. At this point, it would be a good idea to compile Open Babel::

        $ make

   Have a coffee while the magic happens. If you have a multi-processor machine and would prefer an expresso, try a parallel build instead::

        $ make -j4    # parallel build across 4 processors

5. And finally, as root (or using ``sudo``) you should install it::

        # make install

Local build
~~~~~~~~~~~

.. sidebar:: Look Ma, no install!

  With the right sort of environment variable magic (see :ref:`below <environment variables>`), you can actually use Open Babel straight from the build folder. But life is a bit easier if you install it somewhere, either system-wide or locally.

By default, Open Babel is installed in :file:`/usr/local/` on a Unix-like system. This requires root access (or ``sudo``). Even if you do have root access, you may not want to overwrite an existing installation or you may want to avoid conflicts with a version of Open Babel installed by your package manager.

The solution to all of these problems is to do a local install into a directory somewhere in your home folder. 
An additional advantage of a local install is that if you ever want to uninstall it, all you need to do is delete the installation directory; removing the files from a global install is more work.

1. To configure :program:`cmake` to install into :file:`~/Tools/openbabel-install`, for example, you would do the following::

        $ cmake ../openbabel-2.3.1 -DCMAKE_INSTALL_PREFIX=~/Tools/openbabel-install

2. Then you can run :command:`make` and :command:`make install` without needing root access::

        $ make && make install

Compile the GUI
~~~~~~~~~~~~~~~

The GUI is built using the wxWidgets toolkit. Assuming that you have already installed this (see :ref:`requirements` above), you just need to configure :program:`cmake` as follows::

        $ cmake ../openbabel-2.3.1 -DBUILD_GUI=ON

When you run ``make`` and ``make install``, the GUI will be automatically built and installed alongside the main Open Babel library and tools.
 
.. _Compile bindings:

Compile language bindings
~~~~~~~~~~~~~~~~~~~~~~~~~

.. sidebar:: Eigen2 required

  If you wish to compile the language bindings supplied in the release, Eigen2 is required (see :ref:`requirements` above).

1. When configuring CMake, include options such as ``-DPYTHON_BINDINGS=ON -DRUBY_BINDINGS=ON`` for whichever bindings you wish to build (valid names are ``PYTHON``, ``CSHARP``, ``PERL``, ``JAVA`` or ``RUBY``). The bindings will then be built and installed along with the rest of Open Babel. You should note any warning messages in the CMake output.

2. If CMake cannot find Java, you should set the value of the environment variable ``JAVA_HOME`` to the directory containing the Java :file:`bin` and :file:`lib`  directories. For example, if you download the JDK from Sun and run the self-extracting .bin file, it creates a directory :file:`jdk1.6.0_21` (or similar); you should set ``JAVA_HOME`` to the full path to this directory.

3. If CMake cannot find the Perl libraries (which happens on Ubuntu 9.10, surprisingly), you need to configure CMake with something like ``-DPERL_LIBRARY=/usr/lib/libperl.so -DPERL_INCLUDE_PATH=/usr/lib/perl/5.10.0/CORE``.

4. If you are compiling the CSharp bindings, you should specify the CSharp compiler to use with something like ``-DCSHARP_EXECUTABLE=C:\Windows\Microsoft.NET\Framework\v3.5\csc.exe``.

5. With Java and CSharp, the bindings will be installed by default to the same location as the Open Babel libraries.
  
6. For Ruby, Python and Perl, the library files are installed to a subdirectory of wherever the Open Babel libraries are installed: something like :file:`python2.6/site-packages/` or `dist-packages` in the case of Python, :file:`perl/5.8.7` for Perl, and :file:`site_ruby/1.8/linux-i486` for Ruby. If you wish to install the bindings somewhere else, configure CMake with the option ``-DPYTHON_PREFIX=wherever`` for Python, or something similar for Perl (``OBPERL_PREFIX``) or Ruby (``RUBY_PREFIX``).

7. To tell Python where to find the bindings, add the directory containing ``openbabel.py`` to the front of the PYTHONPATH environment variable (if it is not there already). Similarly add the ``perl`` subdirectory (where the bindings were installed) to the front of the PERL5LIB variable; for Ruby add the directory containing :file:`openbabel.so` to RUBYLIB; for Java, add the location of ``openbabel.jar`` to the CLASSPATH.

For example, for Python::

        $ cmake ../openbabel-2.3.1 -DPYTHON_BINDINGS=ON
        $ make
        # make install
        $ export PYTHONPATH=/usr/local/lib/python2.6/site-packages:$PYTHONPATH

Cygwin
~~~~~~
The basic build instructions up above work just fine so long as you use the CMake provided by Cygwin rather than a native Windows installation.

If you get an error about ``undefined reference to '_xmlFreeTextReader'``, you need to specify the location of the XML libraries with the ``-DLIBXML2_LIBRARIES`` option::

        $ cmake ../openbabel-2.3.1 -DLIBXML2_LIBRARIES=/usr/lib/libxml2.dll.a

The language bindings don't seem to work under Cygwin. If you can get them to work, let us know. Also remember that anything that uses Cygwin runs slower than a native build using MinGW or MSVC++, so if speed is an issue you might prefer to compile with MinGW or MSVC++.

MinGW
~~~~~
Open Babel builds out of the box with MinGW. It's an awkward system to set up though, so here are some step-by-step instructions...TODO

.. todo:: MinGW


Windows (MSVC)
~~~~~~~~~~~~~~
The main Windows build used by Open Babel uses the Microsoft Visual C++ compiler (MSVC).

1. Set up the following environment variables:

    a. Add the CMake :file:`bin` directory to the PATH.

    b. (Optional, see :ref:`requirements` above) Set EIGEN2_INCLUDE_DIR to the location of the top level Eigen directory (if installed).

    c. (Optional, required for GUI) Set WXWIN to the top level directory of wxWidgets (if installed).


2. Install the Microsoft Visual C++ 2008 (or newer) compiler.

   We use the Visual C++ 2008 (9.0) `Express Edition`_ (available for free). If you use MSVC++ 2010, open :file:`windows-vc2008/default_build.bat` in a text editor and change the ``Visual Studio 9 2008`` to ``Visual Studio 10``.

.. _Express Edition: http://www.microsoft.com/Express/VC/

3. Open a command prompt, and change directory to the :file:`windows-vc2008` subdirectory. To configure :program:`cmake`, and generate the VC++ project files, run :file:`default_build.bat`.

4. Double-click on :file:`windows-vc2008/build/openbabel.sln` to start MSVC++. At the top of the window just below the menu bar, choose `Release` in the drop-down box.

5. On the left-hand side, right-click on the ``ALL_BUILD`` target, and choose :guilabel:`Build`.

.. todo:: How to build the GUI

Troubleshooting build problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. rubric:: CMake caches some variables from run-to-run. How can I wipe the cache to start from scratch?

Delete :file:`CMakeCache.txt` in the build directory. This is also a very useful file to look into if you have any problems.

.. rubric:: How do I specify the location of the XML libraries?

CMake should find these automatically if they are installed system-wide. If you need to specify them, try using the ``-DLIBXML2_LIBRARIES=wherever`` option with CMake to specify the location of the DLL or SO file, and ``-DLIBXML2_INCLUDE_DIR=wherever`` to specify the location of the header files.

.. rubric:: How do I specify the location of the ZLIB libraries?

CMake should find these automatically if they are installed system-wide. If you need to specify them, try using the ``-DZLIB_LIBRARY=wherever`` option with CMake to specify the location of the DLL or SO file, and ``-DZLIB_INCLUDE_DIR=wherever`` to specify the location of the header files.

.. _environment variables:

.. rubric:: What environment variables affect how Open Babel finds formats, plugins and libraries?

**LD_LIBRARY_PATH** - Used to find the location of the :file:`libopenbabel.so` file.
  You should set this if you get error messages about not being able to find :file:`libopenbabel.so`.
**BABEL_LIBDIR** - Used to find plugins such as the file formats
  If ``obabel -L formats`` does not list any file formats, then you need to set this environment variable to the directory where the file formats were installed, typically :file:`/usr/local/lib/openbabel/`.
**BABEL_DATADIR** - Used to find the location of the data files used for fingerprints, forcefields, etc.
  If you get errors about not being able to find some .txt files, then you should set this to the name of the folder containing files such as :file:`patterns.txt` and :file:`MACCS.txt`. These are typically installed to :file:`/usr/local/share/openbabel`.

Advanced build options
~~~~~~~~~~~~~~~~~~~~~~
.. rubric:: How do I control whether the tests are built?

The CMake option ``-DENABLE_TESTS=ON`` or ``OFF`` will look after this. To actually run the tests, use ``make tests``.

.. rubric:: How do I do a debug build?

``-DCMAKE_BUILD_TYPE=Debug`` does a debug build (``gcc -g``). To revert to a regular build use ``-DCMAKE_BUILD_TYPE=Release``.

.. rubric:: How do I see what commands cmake is using to build?

Run Make as follows::
    
        $ VERBOSE=1 make

.. rubric:: How do I build one specific target?

Just specify the target when running Make. The following just builds the Python bindings::

        $ make _openbabel

To speed things up, you can ask Make to ignore dependencies::

        $ make _openbabel/fast

.. rubric:: How do I create the SWIG bindings?

Use the ``-DRUN_SWIG=ON`` option with CMake. This requires SWIG 2.0 or newer. If the SWIG executable is not on the PATH, you will need to specify its location with ``-DSWIG_EXECUTABLE=wherever``.

.. rubric:: How do I build the Doxygen documentation?

Use the ``-DBUILD_DOCS=ON`` option with CMake. If the Doxygen executable is not on the PATH, you will need to specify its location with ``-DDOXYGEN_EXECUTABLE=wherever``.
