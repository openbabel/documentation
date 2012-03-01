.. _Add plugins:

Adding plugins
==============

Open Babel uses a plugin architecture for file formats, 'operations', charge models, forcefields, fingerprints and descriptors. The general idea behind plugins is described on Wikipedia_. When you start an application that uses the Open Babel library, it searches for available plugins and loads them. This means, for example, that plugins could be distributed separately to the Open Babel distribution.

.. _Wikipedia: http://en.wikipedia.org/wiki/Plug-in_%28computing%29

In fact, even the plugin types are themselves plugins; this makes it easy to add new categories of plugin. The different types of plugins can be listed using::

        C:\>babel -L
        charges
        descriptors
        fingerprints
        forcefields
        formats
        loaders
        ops

To list the plugins of a particular type, for example, charge models, just specify the plugin type::

        C:\>babel -L charges
        gasteiger    Assign Gasteiger-Marsili sigma partial charges
        mmff94       Assign MMFF94 partial charges
        qeq    Assign QEq (charge equilibration) partial charges (Rappe and Goddard, 199
        1)
        qtpie    Assign QTPIE (charge transfer, polarization and equilibration) partial
        charges (Chen and Martinez, 2007)

To add a new plugin of any type, the general method is very simple:

1. Make a copy of an existing plugin .cpp file
2. Edit it so that it does what you want
3. Add the name of the .cpp file to the appropriate :file:`CMakeLists.txt`.

The following sections describe in depth how to add support for a new file format or operation to Open Babel. Remember that if you do add a new plugin, please contribute the code back to the Open Babel project.

.. toctree::

   AddFileFormat.rst
   AddingNewOptions.rst
   AddNewDescriptor.rst
