Ruby
====

.. highlight:: irb

As with the other language bindings, just follow the instructions at :ref:`Compile bindings` to build the Ruby bindings.

Like any Ruby module, the Open Babel bindings can be used from a Ruby script or interactively using :program:`irb` as follows::

        $ irb
        irb(main):001:0> require 'openbabel'
        => true
        irb(main):002:0> c=OpenBabel::OBConversion.new
        => #<OpenBabel::OBConversion:0x2acedbadd020>
        irb(main):003:0> c.set_in_format 'smi'
        => true
        irb(main):004:0> benzene=OpenBabel::OBMol.new
        => #<OpenBabel::OBMol:0x2acedbacfa10>
        irb(main):005:0> c.read_string benzene, 'c1ccccc1'
        => true
        irb(main):006:0> benzene.num_atoms
        => 6

