.. The contents of this file will be copied to the start of
   Overview.rst when you run UpdateFileFormats.py. Don't
   edit Overview.rst directly - instead, edit this file.

.. _file formats:

Supported File Formats and Options
==================================

Chemists are an imaginative bunch. They keep thinking of new file formats.

OpenBabel has support for X formats in total. It can read Y formats and can write Z formats. These formats are identified by a name (for example, "ShelX format") and one or more short codes (in this case, "ins" or "res"). The titles of each section provide this information (for example, :ref:`ShelX_format`).

The short code is used when using ``babel`` to convert files from one format to another::

  babel -iins myfile.ins -ocml

converts from ShelX format to Chemical Markup Language (in this case, no output file is specified and the output will be written to screen [stdout]). In fact, if the filename extension is the same as the file format code, then there is no need to specify the code. In other words, the following command will behave identically::

  babel myfile.ins -ocml

As well as the general conversion options described elsewhere (?), each format may have its own options for either reading or writing. For example, the ShelX format has two options that affect reading of files, ``s`` and ``b``. To set a file format option:

* For **Read Options**, precede the option with ``-a`` in the babel commandline
* For **Write Options**, precede the option with ``-x``

For example, if we wanted to set all bonds to single bonds when reading a Shelx format file, we could specify the ``s`` option::

  babel -iins myfile.ins -ocml -as

More than one read (or write) option can be specified, either using separate terms (e.g. ``-ax -ay -az``) or together in one term (as ``-axyz``).

**Developer Note**
  To set the file formats for an ``OBConversion`` object, use ``SetInAndOutFormat(InCode, OutCode)``. To set a Read Option ``s``, use ``SetOptions("s", OBConversion::INOPTIONS)``.



.. toctree::
   :maxdepth: 2

   Common_cheminformatics.rst
   Utility.rst
   Other_cheminformatics.rst
   Computational_chemistry.rst
   Crystallography.rst
   Reactions.rst
   Images.rst
   2D_drawing.rst
   3D_viewers.rst
   Kinetics_and_Thermodynamics.rst
   Molecular_dynamics_and_docking.rst
   Volume_data.rst
   Miscellaneous.rst
   Biological_data.rst
   I_have_no_idea_what_this_is.rst
