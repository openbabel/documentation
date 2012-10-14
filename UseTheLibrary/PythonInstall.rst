Install Python bindings
~~~~~~~~~~~~~~~~~~~~~~~

Windows
-------

Install the bindings
^^^^^^^^^^^^^^^^^^^^

#. First you need to download and install the
   `OpenBabelGUI <http://openbabel.org/wiki/Install>`_ version 2.3.2
#. Next, download and install the OpenBabel Python bindings
   (version 1.7) for your Python version, either
   `2.5 <http://sourceforge.net/projects/openbabel/files/openbabel-python/1.7/openbabel-python-1.7.py25.exe/download>`_
   `2.6 <http://sourceforge.net/projects/openbabel/files/openbabel-python/1.7/openbabel-python-1.7.py26.exe/download>`_,
   `2.7 <http://sourceforge.net/projects/openbabel/files/openbabel-python/1.7/openbabel-python-1.7.py27.exe/download>`_
   `3.1 <http://sourceforge.net/projects/openbabel/files/openbabel-python/1.7/openbabel-python-1.7.py31.exe/download>`_,
   or
   `3.2 <http://sourceforge.net/projects/openbabel/files/openbabel-python/1.7/openbabel-python-1.7.py32.exe/download>`_.

**Note**: If you are **upgrading** from an earlier version of the
Python bindings, you should uninstall that first (using Add/Remove
Programs) and then follow steps 1 and 2 above. You should also make
sure that BABEL\_DATADIR is set correctly to the :file:`data` folder of the
Open Babel installation (at a command prompt, type *echo %BABEL\_DATADIR%*).
If not, carefully delete any existing System environment variables
with the name BABEL\_DATADIR, and correct the value of the User
environment variable BABEL\_DATADIR (if necessary).

Install Python Imaging Library (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to display 2D depictions using Pybel (rather than just write to 
a file), you need the `Python Imaging Library (PIL) <http://www.pythonware.com/products/pil/#pil117>`_
by Fredrik Lundh. Unfortunately, at the time of writing (Oct 2011), there is still not an official
release for Python 3.

Test the installation
^^^^^^^^^^^^^^^^^^^^^

Open a Windows command prompt, and type the following commands to
make sure that everything is installed okay. If you get an error
message, there's something wrong and you should email the mailing
list with the output from these commands.

::

    C:\Documents and Settings\Noel> obabel -V
    Open Babel 2.3.2 -- Oct 13 2012 -- 17:57:01
    
    C:\Documents and Settings\Noel> obabel -Hsdf
    sdf  MDL MOL format
    Reads and writes V2000 and V3000 versions

    Read Options, e.g. -as
     s  determine chirality from atom parity flags
    ...
    ...
    
    C:\Documents and Settings\Noel> dir "%BABEL_DATADIR%"\mr.txt
     Volume in drive C has no label.
     Volume Serial Number is 68A3-3CC9
    
     Directory of C:\Users\Noel\AppData\Roaming\OpenBabel-2.3.2\data

    26/10/2010  16:37             4,295 mr.txt
                   1 File(s)          4,295 bytes
                   0 Dir(s)  58,607,575,040 bytes free
    
    C:\Documents and Settings\Noel> C:\Python26\python
    Python 2.6.5 (r265:79096, Mar 19 2010, 21:48:26) [MSC v.1500 32 bit (Intel)] on
    win32
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
    >>> mol.draw() # If you installed PIL, this will display its structure
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

Install Python Imaging Library (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to display 2D depictions using Pybel (rather than just write to 
a file), you need the `Python Imaging Library (PIL) <http://www.pythonware.com/products/pil/#pil117>`_
by Fredrik Lundh, and the Python Tkinter library (part of the standard library).
These should be available through
your package manager, e.g. on Debian, PIL is provided by 'python-imaging' and
'python-imaging-tk', while Tkinter is provided by 'python-tk'. Unfortunately,
at the time of writing (Oct 2011), there is still not an official
release of PIL for Python 3.
