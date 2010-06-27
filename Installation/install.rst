Install OpenBabel
=================

OpenBabel runs on Windows, Linux and MacOSX. You can either `install a binary package`_ (the easiest option) or `compile OpenBabel yourself`_ (also easy, but much more geek cred).

Install a binary package
------------------------

Windows
~~~~~~~

OpenBabel is available as a `binary installer`_ for Windows. It includes several command-line tools as well as a graphical user interface (GUI).

.. _binary installer: http://sourceforge.net/projects/openbabel/files/openbabel/2.3.3/OpenBabel2.3.3_Windows_Installer.exe/download

Advanced users may be interested in compiling OpenBabel themselves (see `Compiling OpenBabel`_).

Linux
~~~~~

OpenBabel binary packages are available from many Linux distributions including Ubuntu, OpenSUSE and Fedora.

In general, we recommend using the latest release of OpenBabel (currently |release|). If this is not available for your Linux distribution, you should `compile OpenBabel yourself`_.

.. _compile OpenBabel yourself: `Compiling OpenBabel`_

Compiling OpenBabel
-------------------

OpenBabel is written in C++. Compiling is the process of turning this C++ into instructions that the computer's processor can understand, machine code.

Although pre-compiled (or "binary") packages are available for several platforms, there several reasons you might want to compile OpenBabel yourself:

- The current release (|release|) of OpenBabel is not available for your platform. We recommend always using the latest release.
- You want more control over the features available. For example, perhaps you want the Python bindings but these were not included in your distribution.
- You want to use the latest development code.
- You want to add a new feature. It is easy to add new formats or operations to OpenBabel as it has a plugin architecture.
- You just want to compile stuff yourself. We understand.

OpenBabel is written in standards-compliant C++. The best-supported compilers are GCC 4 and MSVC++ 2008, but it also compiles with Intel Compiler 11. 

Windows
~~~~~~~

TODO
