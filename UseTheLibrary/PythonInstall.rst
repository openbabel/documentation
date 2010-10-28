Install Python bindings
~~~~~~~~~~~~~~~~~~~~~~~

Windows
-------

Install the bindings
^^^^^^^^^^^^^^^^^^^^


#. First you need to download and install the
   `OpenBabelGUI </wiki/Install>`_ version 2.3.0
#. Next, download and install the OpenBabel Python bindings
   (version 1.6) for your Python version, either
   `2.5 <http://sourceforge.net/projects/openbabel/files/openbabel-python/1.6/openbabel-python-1.6.py25.exe/download>`_
   or
   `2.6 <http://sourceforge.net/projects/openbabel/files/openbabel-python/1.6/openbabel-python-1.6.py26.exe/download>`_,
   `2.7 <http://sourceforge.net/projects/openbabel/files/openbabel-python/1.6/openbabel-python-1.6.py27.exe/download>`_
   or
   `3.1 <http://sourceforge.net/projects/openbabel/files/openbabel-python/1.6/openbabel-python-1.6.py31.exe/download>`_.

**Note**: If you are **upgrading** from an earlier version of the
Python bindings, you should uninstall that first (using Add/Remove
Programs) and then follow steps 1 and 2 above. You should also make
sure that BABEL\_DATADIR is set correctly to the directory of the
OpenBabelGUI (at a command prompt, type *echo %BABEL\_DATADIR%*).
If not, carefully delete any existing System environment variables
with the name BABEL\_DATADIR, and correct the value of the User
environment variable BABEL\_DATADIR (if necessary).

Install OASA (optional)
^^^^^^^^^^^^^^^^^^^^^^^

If you wish to draw 2D depictions using Pybel, you need the
`OASA library <http://bkchem.zirael.org/oasa_en.html>`_ by Beda
Kosata. This is installed as follows:


-  Install
   `Python Imaging Library (PIL) <http://www.pythonware.com/products/pil/#pil116>`_
   for your version of Python
-  Download and unzip the Windows package of
   `OASA <http://bkchem.zirael.org/oasa_en.html>`_
-  Copy the two folders 'oasa' and 'cairo' to the site-packages
   folder of your Python distribution (on my system, this is
   C:\\Program Files\\Python25\\Lib\\site-packages)
-  If you are using Python 2.5, you are finished!
-  If you are using Python 2.4, go into the 'site-packages/cairo'
   folder, delete '\_cairo.pyd', and rename '\_cairo.pyd2.4' to
   '\_cairo.pyd'

Test the installation
^^^^^^^^^^^^^^^^^^^^^

Open a Windows command prompt, and type the following commands to
make sure that everything is installed okay. If you get an error
message, there's something wrong and you should email the mailing
list (see the main `Python </wiki/Python>`_ page) with the output
from these commands.

::

    Microsoft Windows XP [Version 5.1.2600]
    (C) Copyright 1985-2001 Microsoft Corp.
    
    C:\Documents and Settings\Noel> babel -V
    Open Babel 2.2.1 -- Dec 31 2008 -- 12:51:03
    
    C:\Documents and Settings\Noel> babel -Hsdf
    sdf  MDL MOL format
     Reads and writes V2000 and V3000 versions
     Write Options, e.g. -x3
      3  output V3000 not V2000 (used for >999 atoms/bonds)
      m  write no properties
    
    Specification at: http://www.mdl.com/downloads/public/ctfile/ctfile.jsp
    
    C:\Documents and Settings\Noel>dir "%BABEL_DATADIR%"\OBGUI.exe
     Volume in drive C has no label.
     Volume Serial Number is 68A3-3CC9
    
     Directory of C:\Program Files\OpenBabel-2.2.1
    
    31/12/2008  12:53         1,253,376 OBGUI.exe
                   1 File(s)      1,253,376 bytes
                   0 Dir(s)  39,672,901,632 bytes free
    
    C:\Documents and Settings\Noel> C:\Python24\python
    Python 2.4.3 - Enthought Edition 1.0.0 (#69, Aug  2 2006, 12:09:59) [MSC v.1310
    32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pybel
    >>> mol = pybel.readstring("smi", "CC(=O)Br")
    >>> mol.make3D()
    >>> print(mol.write("sdf"))
    
     OpenBabel01010918183D
    
      7  6  0  0  0  0  0  0  0  0999 V2000
        1.0166   -0.0354   -0.0062 C   0  0  0  0  0
        2.5200   -0.1269    0.0003 C   0  0  0  0  0
        3.0871   -1.2168    0.0026 O   0  0  0  0  0
        3.2979    1.4258    0.0015 Br  0  0  0  0  0
        0.6684    1.0007    0.0052 H   0  0  0  0  0
        0.6255   -0.5416    0.8803 H   0  0  0  0  0
        0.6345   -0.5199   -0.9086 H   0  0  0  0  0
      1  2  1  0  0  0
      1  5  1  0  0  0
      1  6  1  0  0  0
      1  7  1  0  0  0
      2  4  1  0  0  0
      2  3  2  0  0  0
    M  END
    $$$$
    >>> mol.draw() # If you installed OASA, this will display its structure
    >>> (Hit CTRL+Z followed by Enter to exit)

Linux and MacOSX
----------------

The first step is to download and compile the latest version of
OpenBabel. Follow the instructions on the
`OpenBabel Install </wiki/Install_(source_code)>`_ page to install
OpenBabel either globally or locally.

Next, you need to compile and install the Python bindings. This can
be done either globally or locally as described below. The
following instructions refer to OpenBabel 2.1.0 and Python 2.4.
Remember to correct the PATHs for your versions of OpenBabel and
Python.

Install the Python bindings globally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(A1) Compiling the bindings may require an extra Python package
depending on your Linux distribution. For example, for Debian you
need the 'python-dev' package (installed using 'apt-get'); for
SUSE, you need 'python-devel' (installed using YaST).

Change directory to 'openbabel-2.1.0/scripts/python' and run:

::

    python setup.py build

(A2) To install the python interface globally, as root type:

::

    python setup.py install

(A3) You may need to add the location of libopenbabel.so (on my
system, the location is /usr/local/lib) to the environment variable
LD\_LIBRARY\_PATH if you get the following error when you try to
import the OpenBabel library at the Python prompt:

::

    $ python
    >>> import openbabel 
    Traceback (most recent call last):
      File "<stdin>", line 1, in
      File "/usr/lib/python2.4/site-packages/openbabel.py", line 9, in
       import _openbabel
    ImportError: libopenbabel.so.3: cannot open shared object file: No such file or directory

Install the Python bindings locally
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(B1) To compile the Python extension, follow Step A1 above.

(B2) To install the Python extension, instead of Step B2 above, use
the 'prefix' option to setup.py:

::

    python setup.py install --prefix=/home/noel/tree

This installs the Python extension into something like
/home/noel/tree/lib/python2.4/site-packages, so you need to add
this directory to your PYTHONPATH in your startup scripts (that is,
.bashrc, or whatever):

::

    export PYTHONPATH=$PYTHONPATH:/home/noel/tree/lib/python2.4/site-packages

(B3) As described in Step B3 above, you will probably also have to
edit the variable LD\_LIBRARY\_PATH as follows:

::

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/noel/tree/lib

Advanced Notes
^^^^^^^^^^^^^^


-  When compiling the Python extension, if you want to link to a
   version of Open Babel that is not in ../../src (relative to
   setup.py), /usr/local or /usr (this is the order in which these
   locations are searched), you should set OPENBABEL\_INSTALL to point
   to the alternative location. There should be an
   "include/openbabel-2.0" and a "lib" directory at the location
   pointed to by OPENBABEL\_INSTALL.


-  If you are compiling a development version of OpenBabel, then
   you need to create the SWIG bindings yourself. Make sure you have
   the latest version of SWIG installed, and at Step A2 above, run
   configure as follows: ``./configure --enable-maintainer-mode``

Install OASA (optional)
^^^^^^^^^^^^^^^^^^^^^^^

If you wish to draw 2D depictions using Pybel, you need the
`OASA library <http://bkchem.zirael.org/oasa_en.html>`_ by Beda
Kosata. This is installed as follows:


-  Download `OASA 0.12.1 <http://bkchem.zirael.org/oasa_en.html>`_,
   unzip it, and add the oasa-0.12.1 directory to the PYTHONPATH.
-  OASA requires Cairo and its Python bindings which are included
   in Debian as 'libcairo2' and 'python-cairo' respectively.
-  To display images on the screen (rather than just writing to a
   file), you also need:
   
   -  the
      `Python Imaging Library <http://www.pythonware.com/products/pil/>`_,
      available as the Debian packages 'python-imaging' and
      'python-imaging-tk',
   -  the Python Tkinter library. This should already be installed as
      part of a standard Python distribution. If not it's available as
      the Debian package 'python-tk'.
