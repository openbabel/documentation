Install Open Babel
==================

Open Babel runs on Windows, Linux and MacOSX. You can either `install a binary package`_ (the easiest option) or `compile OpenBabel yourself`_ (also easy, but much more geek cred).

Install a binary package
------------------------

Windows
~~~~~~~

Open Babel is available as a `binary installer`_ for Windows. It includes several command-line tools as well as a graphical user interface (GUI).

.. _binary installer: http://sourceforge.net/projects/openbabel/files/openbabel/2.3.3/OpenBabel2.3.3_Windows_Installer.exe/download

Advanced users may be interested in compiling OpenBabel themselves (see :ref:`Compiling Open Babel`).

Linux
~~~~~

Open Babel binary packages are available from many Linux distributions including Ubuntu, OpenSUSE and Fedora.

In general, we recommend using the latest release of Open Babel (currently |release|). If this is not available for your Linux distribution, you should :ref:`compile OpenBabel yourself <Compiling Open Babel>`.

.. _Compiling Open Babel

Compiling Open Babel
--------------------

OpenBabel is written in C++. Compiling is the process of turning this C++ into instructions that the computer's processor can understand, machine code.

Although pre-compiled (or "binary") packages are available for several platforms, there several reasons you might want to compile OpenBabel yourself:

- The current release (|release|) of Open Babel is not available for your platform. We recommend always using the latest release.
- You want more control over the features available. For example, perhaps you want the Python bindings but these were not included in your distribution.
- You want to use the latest development code.
- You want to add a new feature. It is easy to add new formats or operations to Open Babel as it has a plugin architecture.
- You just want to compile stuff yourself. We understand.

Open Babel can be compiled on Linux, MacOSX, BSDs and other Unixes, and also on Windows (with Cygwin, MinGW or MSVC).

Requirements
~~~~~~~~~~~~

To build Open Babel, you **need** the following:

* The `source code <http://sourceforge.net/project/showfiles.php?group_id=40728&package_id=32894>`__ for the latest release of Open Babel
* A C++ compiler

    Open Babel is written in standards-compliant C++. The best-supported compilers are GCC 4 and MSVC++ 2008, but it also compiles with Clang and Intel Compiler 11. 

* CMake 2.4 or newer

    Open Babel uses CMake as its build system. CMake is a open source cross-platform build system from KitWare.

    You need to install CMake 2.4 or newer. This is available as a binary package from the KitWare website; alternatively, it may be available through your package manager (on Linux). If necessary, you can also compile it yourself from the source code.

The following are optional when compiling Open Babel, but if not available some features will be missing:

.. todo:: This section needs to be updated

* libxml2 development headers are required to read/write CML files (the libxml2-dev package in Ubuntu) 
* zlib.h is required to support reading gzipped files (the zlib1g-dev package in Ubuntu) 
* If using GCC 3.x to compile (and not GCC 4.x), then the Boost headers are required for certain formats (CML, Chemkin, Chemdraw CDX, MDL RXN and RSMI) 


Basic build procedure
~~~~~~~~~~~~~~~~~~~~~

The basic build procedure is the same for all platforms and will be described first. After this, we will look at variations for particular platforms.

.. highlight:: bash

1. The recommended way to build Open Babel is to use a separate source and build directory; for example, :file:`src` and :file:`build`. The first step is to create these directories::

        $ tar zxf openbabel-2.3.0.tar.gz
        $ mv openbabel-2.3.0 src
        $ mkdir build

2. Now you need to run :program:`cmake` to configure the build. The following will configure the build to use all of the default options::

        $ cd build
        $ cmake ../src

3. If you need to specify an option, use the ``-D`` switch to :program:`cmake`. For example, the following line sets the value of ``CMAKE_INSTALL_PREFIX`` and ``BUILD_TYPE``::

        $ cmake ../src -DCMAKE_INSTALL_PREFIX=~/Tools -DBUILD_TYPE=DEBUG

   We will discuss various possible options later.

4. At this point, it would be a good idea to compile Open Babel::

        $ make

5. And finally, as root (or using ``sudo``) you should install it::

        # make install

Local build
~~~~~~~~~~~

.. sidebar:: Look Ma, no install!

  With the right sort of environment variable magic, you can actually use Open Babel straight from the build folder. But life is a bit easier if you install it somewhere, either system-wide or locally.

By default, Open Babel is installed in :file:`/usr/local/` on a Unix-like system. This requires root access (or ``sudo``). Even if you do have root access, you may not want to overwrite an existing installation or you may want to avoid conflicts with a version of Open Babel installed by your package manager.

The solution to all of these problems is to do a local install into a directory somewhere in your home folder. 
An additional advantage of a local install is that if you ever want to uninstall it, all you need to do is delete the installation directory; removing the files from a global install is more tricky.
To configure :cmake: to install into :file:`~/Tools/openbabel-install`, for example, you would do the following::

        $ cmake ../src -DCMAKE_INSTALL_PREFIX=~/Tools/openbabel-install

Then you can run :command:`make` and :command:`make install` without needing root access::

        $ make && make install

 
Compile language bindings
~~~~~~~~~~~~~~~~~~~~~~~~~

Linux
-----



Windows
~~~~~~~

TODO
