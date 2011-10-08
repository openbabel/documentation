.. The contents of this file will be copied to the start of
   Overview.rst when you run UpdateFileFormats.py. Don't
   edit Overview.rst directly - instead, edit this file.

.. _file formats:

Supported File Formats and Options
==================================

Chemists are a very imaginative group. They keep thinking of new file formats.

OpenBabel has support for 118 formats in total. It can read 88 formats and can write 89 formats. These formats are identified by a name (for example, ``ShelX format``) and one or more short codes (in this case, ``ins`` or ``res``). The titles of each section provide this information (for example, :ref:`ShelX_format`).

The short code is used when using :command:`obabel` or :command:`babel` to convert files from one format to another::

  obabel -iins myfile.ins -ocml

converts from ShelX format to Chemical Markup Language (in this case, no output file is specified and the output will be written to screen [stdout]). In fact, if the filename extension is the same as the file format code, then there is no need to specify the code. In other words, the following command will behave identically::

  babel myfile.ins -ocml

As well as the general conversion options described elsewhere (see :ref:`babel options`), each format may have its own options for either reading or writing. For example, the ShelX format has two options that affect reading of files, ``s`` and ``b``. To set a file format option:

* For **Read Options**, precede the option with ``-a`` at the command line
* For **Write Options**, precede the option with ``-x``

.. sidebar:: Mnemonic

   To remember the correct switch for read or write options, think of "raw eggs": **r**\ ead is **a**, **w**\ rite is **x** ("eggs").

For example, if we wanted to set all bonds to single bonds when reading a ShelX format file, we could specify the ``s`` option::

  babel -iins myfile.ins -ocml -as

More than one read (or write) option can be specified (e.g. ``-ax -ay -az``). :command:`babel` (but not :command:`obabel`) also allows you to specify several options together (e.g. as ``-axyz``).

**Developer Note**
  To set the file formats for an ``OBConversion`` object, use ``SetInAndOutFormat(InCode, OutCode)``. To set a Read Option ``s``, use ``SetOptions("s", OBConversion::INOPTIONS)``.


.. toctree::
   :maxdepth: 2

   Common_cheminformatics_Formats.rst
   Utility_Formats.rst
   Other_cheminformatics_Formats.rst
   Computational_chemistry_Formats.rst
   Crystallography_Formats.rst
   Reaction_Formats.rst
   Image_Formats.rst
   2D_drawing_Formats.rst
   3D_viewer_Formats.rst
   Kinetics_and_Thermodynamics_Formats.rst
   Molecular_dynamics_and_docking_Formats.rst
   Volume_data_Formats.rst
   Miscellaneous_Formats.rst
   Biological_data_Formats.rst
   Obscure_Formats.rst
