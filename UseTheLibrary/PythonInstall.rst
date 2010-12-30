Install Python bindings
~~~~~~~~~~~~~~~~~~~~~~~

Windows
-------

Install the bindings
^^^^^^^^^^^^^^^^^^^^

#. First you need to download and install the
   `OpenBabelGUI <http://openbabel.org/wiki/Install>`_ version 2.3.0
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
sure that BABEL\_DATADIR is set correctly to the :file:`data` folder of the
Open Babel installation (at a command prompt, type *echo %BABEL\_DATADIR%*).
If not, carefully delete any existing System environment variables
with the name BABEL\_DATADIR, and correct the value of the User
environment variable BABEL\_DATADIR (if necessary).

Install OASA (optional)
^^^^^^^^^^^^^^^^^^^^^^^

If you wish to draw 2D depictions using Pybel, you need the
`OASA library <http://bkchem.zirael.org/oasa_en.html>`_ by Beda
Kosata. This is installed as follows:


-  Install
   `Python Imaging Library (PIL) <http://www.pythonware.com/products/pil/#pil117>`_
   for your version of Python
-  Download and unzip the Windows package of
   `OASA <http://bkchem.zirael.org/oasa_en.html>`_. There is a version for
   Python 2.5 and 2.6.
-  Copy the two folders :file:`oasa` and :file:`cairo` to the :file:`site-packages`
   folder of your Python distribution (on my system, this is
   :file:`C:\\Program Files\\Python25\\Lib\\site-packages`)

Test the installation
^^^^^^^^^^^^^^^^^^^^^

Open a Windows command prompt, and type the following commands to
make sure that everything is installed okay. If you get an error
message, there's something wrong and you should email the mailing
list with the output from these commands.

::

    C:\Documents and Settings\Noel> babel -V
    Open Babel 2.2.1 -- Dec 31 2008 -- 12:51:03
    
    C:\Documents and Settings\Noel> babel -Hsdf
    sdf  MDL MOL format
     Reads and writes V2000 and V3000 versions
     Write Options, e.g. -x3
      3  output V3000 not V2000 (used for >999 atoms/bonds)
      m  write no properties
    
    Specification at: http://www.mdl.com/downloads/public/ctfile/ctfile.jsp
    
    C:\Documents and Settings\Noel>dir "%BABEL_DATADIR%"\mr.txt
     Volume in drive C has no label.
     Volume Serial Number is 68A3-3CC9
    
     Directory of C:\Program Files (x86)\OpenBabel-2.3.0\data

    26/10/2010  16:37             4,295 mr.txt
                   1 File(s)          4,295 bytes
                   0 Dir(s)  58,607,575,040 bytes free
    
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

See :ref:`Compile bindings` for information on how to configure CMake to compile the Python bindings. This can be done either globally or locally.

You may need to add the location of :file:`libopenbabel.so` (on my system, the location is :file:`/usr/local/lib`) to the environment variable LD\_LIBRARY\_PATH if you get the following error when you try to import the OpenBabel library at the Python prompt:

::

    $ python
    >>> import openbabel 
    Traceback (most recent call last):
      File "<stdin>", line 1, in
      File "/usr/lib/python2.4/site-packages/openbabel.py", line 9, in
       import _openbabel
    ImportError: libopenbabel.so.3: cannot open shared object file: No such file or directory

Install OASA (optional)
^^^^^^^^^^^^^^^^^^^^^^^

If you wish to draw 2D depictions using Pybel, you need the
`OASA library <http://bkchem.zirael.org/oasa_en.html>`_ by Beda
Kosata. This is installed as follows:


-  Download `OASA <http://bkchem.zirael.org/oasa_en.html>`_,
   unzip it, and add the resulting oasa directory to the PYTHONPATH.
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
