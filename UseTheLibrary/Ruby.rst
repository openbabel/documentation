Ruby
====

As with the other language bindings, the Ruby bindings are auto-generated and include a Makefile that uses extconf.rb. These bindings are only available for Linux and MacOSX. (We would welcome help in making them available on Windows also.)

To generate the :file:`Makefile` and run it, use something like the following::

        % ruby extconf.rb --with-openbabel-include=/usr/local/include/openbabel-2.0
        % make

Like any Ruby module, the Open Babel bindings can be used from a Ruby script or interactively using :program:`irb` as follows::

        % irb
        irb(main):001:0> require 'openbabel'

