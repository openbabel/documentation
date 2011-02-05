.. _testing:

Testing the Code
================

Testing is another important ongoing task for any large code base such as Open Babel. The following documentation is intended to give some idea as to the types of tests used by Open Babel and various tools available for debugging and testing.

Types of Tests
--------------

Unit tests
  These tests cover specific functionality of the library.
  
  Unit tests attempt to show that functions work as indicated (i.e. pass) and fail properly on unacceptable input. They are run after building the code by calling ``make test``. Ideally these tests should cover every public function in the :ref:`Open Babel API <API>`. Adding more tests to provide greater coverage is a high priority.

Regression tests
  These tests are associated with particular bug fixes.

  A regression test ensures that a bug, once fixed, stays fixed. If you have spent time fixing a bug, it's worthwhile to write an associated regression test. In fact, writing the test first is to a good way to prove that you have in fact fixed the problem.

Roundtrip tests
  Test file translation.

  These are run from the test file repository and test file translation to/from file formats.

"Dogfood" tests
   Using the development code.

   Many of the developers use the current development snapshots for their daily use. This is sometimes called eating your own dog food and ensures that bugs which impact common functionality are caught quickly.

Scripting language tests
   Perl and Python unit tests

   Both the Perl and Python language bindings have additional tests to ensure that these scripting language modules work. These tests not only stress the scripting modules themselves, but also the underlying library. 

Test dashboard
--------------

We have set up a test dashboard_ with nightly builds of Open Babel for several compilers and operating systems. The dashboard allows problems with particular SVN commits to be easily identified. Developers should check the dashboard after committing code and check whether the test suite has failed.

.. _dashboard: http://my.cdash.org/index.php?project=Open+Babel

We thank KitWare_ for providing dashboard resources.

.. _KitWare: http://www.kitware.com

Tools for software testing
--------------------------

A variety of tools can be used to help diagnose problems and debug errors:

.. rubric:: Debuggers

gdb_ (the GNU project debugger) is a basic debugger on UNIX systems.

* GDB can be run on the babel program like so: ``./libtool gdb src/babel``
* Several GDB commands are highly useful, including ``bt`` which gives a full backtrace of program execution upon error.
* The use of code optimization when compiling can make debugging with GDB and other debuggers extremely difficult. If needed, make sure Open Babel has been compiled, e.g. with ``CXXFLAGS="-g -O0"`` on UNIX. 

.. _gdb: http://www.gnu.org/software/gdb/

.. rubric:: Memory Checkers

Unlike languages like Java, which handle memory allocation and deletion, C++ requires that all code handle memory. In particular, this means if you use new or malloc or similar calls, you must be sure the memory will be properly freed when no longer needed. So-called "memory leaks" are cases where memory has been allocated, but never properly freed and are significant bugs in Open Babel.

Several tools can help find such errors:

* valgrind_ works on several platforms by carefully monitoring each memory access and allocation.
* LeakTracer_ works on a range of platforms by using C++ operator overloading.
* MallocDebug_ (Mac OS X only) is a graphic front-end to monitor memory use and incorrect memory usage. 
* `Visual Leak Detector`_ (Windows/MSVC only) is a very easy way to find memory leaks.

.. _valgrind: http://www.valgrind.org/
.. _LeakTracer: http://www.andreasen.org/LeakTracer/
.. _MallocDebug: http://developer.apple.com/documentation/Performance/Conceptual/ManagingMemory/Articles/FindingLeaks.html
.. _Visual Leak Detector: http://vld.codeplex.com/

.. rubric:: Code Profiling

To improve the speed of execution, it is often helpful to rely on tools which can

* gprof_ is used with the GCC compilers to produce profiling data including the number of calls to routines and the amount of time spent executing.
* Shark/Saturn (Mac OS X only) is a graphical front-ends to gprof and can sample programs while running. 
* callgrind is run through the valgrind_ virtual machine using ``valgrind --tool=callgrind ./myexe``. This works best (although slower) if the executable is compiled with debugging information.

.. _gprof: http://www.gnu.org/software/gprof/

.. rubric:: C++ Unscrambler

The symbols used by C++ compilers and exposed by debugging, profiling, and memory tools are "scrambled." The `c++filt <cppfilt>`_ program can be used to decode the symbol to a human-readable form.

.. _cppfilt: http://sources.redhat.com/binutils/docs-2.15/binutils/c--filt.html

