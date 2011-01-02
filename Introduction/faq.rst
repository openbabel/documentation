Frequently Asked Questions
==========================

General
-------

.. rubric:: What is Open Babel?

Put simply, Open Babel is a free, open-source version of the Babel chemistry file translation program. Open Babel is a project designed to pick up where Babel left off, as a cross-platform program and library designed to interconvert between many file formats used in molecular modeling, computational chemistry, and many related areas.

Open Babel includes two components, a command-line utility and a C++ library. The command-line utility is intended to be used as a replacement for the original babel program, to translate between various chemical file formats. The C++ library includes all of the file-translation code as well as a wide variety of utilities to foster development of other open source scientific software.

.. rubric:: How does this relate to BabelChat, BabelFish, Babel IM, etc. ...?

It doesn't. Not surprisingly, "babel" is used frequently in a lot of software names. 

.. rubric:: Is it Open Babel or OpenBabel?

Your choice. It's probably easier to call it Open Babel since that's what it is--an open version of Babel. But if you like one-word, mixed-case project names, then go for OpenBabel. In that case, the space is just too small to be printed.

.. rubric:: How does this relate to the original Babel and OELib, the "next" Babel?

The original Babel was written by Pat Walters and Matt Stahl, based on the "convert" program by Ajay Shah, and is still a remarkable application. Both Pat and Matt have moved on to other work. The original Babel is hosted by Smog.com on a `Babel homepage`_, by the `Computational Chemistry List`_ (CCL) and of course by Open Babel at `SourceForge.net`_.


Along the way, the two original authors started a rewrite of Babel into C++ they called OBabel, which was never really publicly released. But Matt used some of these ideas in OELib, which was generously released under the GNU GPL by his employer, OpenEye Software, and the last known version of this OELib is still available from our `file repository`_.

.. _Babel homepage: http://smog.com/chem/babel/
.. _Computational Chemistry List: http://ccl.net/cca/software/UNIX/babel/
.. _file repository:
.. _SourceForge.net: http://sourceforge.net/project/showfiles.php?group_id=40728&package_id=100796

OpenEye decided that for their purposes OELib needed a rewrite (now called OEChem_), but this would be closed-source to include some advanced algorithms. So the GPL'ed version of OELib would not be maintained. Instead, the free version of OELib was renamed and has become "Open Babel" with the blessing of Matt and other contributors.

.. _OEChem: http://www.eyesopen.com/products/toolkits/oechem.html

Open Babel has evolved quite a lot since its birth in 2001.

.. rubric:: What's the latest version?

As of this writing, the latest version is Open Babel |release|. This is a stable version suitable for widespread use and development.

.. rubric:: Can I use Open Babel code in a personal project?

One common misconception about the GNU GPL license for Open Babel is that it requires users to release any code that uses the Open Babel library. This is completely untrue. There are no restrictions on use of Open Babel code for personal projects, regardless of where you work (academia, industry, ... wherever).

However, if you intend on releasing a software package that uses Open Babel code, the GPL requires that your package be released under the GNU GPL license. The distinction is between use and distribution. See :ref:`Why contribute` below for more on the licensing issues.

.. rubric:: How do I cite Open Babel in a paper?

If you would like to reference Open Babel in an academic paper, we suggest using both of the following references at the moment:

* Guha et al. [ghh2006]_

.. [ghh2006] Rajarshi Guha, Michael T. Howard, Geoffrey R. Hutchison, Peter Murray-Rust, Henry Rzepa, Christoph Steinbeck, Joerg Kurt Wegner, Egon Willighagen.
   **The Blue Obelisk -- Interoperability in Chemical Informatics.**
   *J. Chem. Inf. Model.* **2006**, *46*, 991-998.
   [`Link <http://dx.doi.org/10.1021/ci050400b>`_] 

* The Open Babel Package, version 2.2.3 http://openbabel.org (accessed Feb 2010) 

The first is a paper on the `Blue Obelisk`_ initiative, which includes Open Babel and other open source chemistry projects, and the second is one way to cite a software package at a particular URL. Obviously, you should include the version number of Open Babel you used, and the date you downloaded the software or installed Open Babel.

.. _Blue Obelisk: http://blueobelisk.org

Features, Formats, Roadmap
--------------------------

.. rubric:: Why don't you support file format X?

The file formats currently supported are some of the more common file formats and, admittedly, those we use in our work. If you'd like to see other file formats added, we need one of:

    * documentation on the file format
    * working code to read the file format or translate it
    * example files in the new file format and in some other format 

The latter obviously is the easiest with text file formats. Binary files take some time to reverse engineer without documentation or working code. Also consider pointing developers to this FAQ and the "What's in it for me?" section.

.. rubric:: When I convert from SMILES to MOL2/PDB/etc., why are all of the coordinates zero?

The SMILES format contains 2D information on the molecule. That is, it says which atoms are connected to which other atoms, and what type of bonds are present. MOL2, PDB and several other formats contain 3D coordinate information not present in the SMILES format. Since Open Babel does not attempt to generate 3D structure by default, all of the coordinates are set to zero. However, it is possible to generate 3D structure with the release of Open Babel 2.2.0 using the ``--gen3d`` option.

.. rubric:: What doesn't Open Babel support yet?

A couple of things. See the proposed roadmap (**TODO**) for examples of things we'd like to see in future versions.

.. todo:: Need to add the roadmap, or else remove this comment.

.. rubric:: What sorts of features will be added in the future?

It's an open project, so if features are suggested or donated, they'll be considered as much as anything else on the drawing board. Some things are pretty clear from the roadmap.

.. _Why contribute:

What's in it for me to contribute?
----------------------------------

.. rubric:: What's in it for my chemistry software company?

If your product is closed-source or otherwise incompatible with the GPL, you unfortunately cannot link directly to the code library. You can, however, distribute Open Babel in unmodified form with your products to use the command-line interface. This is fairly easy because the Open Babel babel program allow reading from the standard input and writing to the standard output (functioning as a POSIX pipe).

If you decide to distribute binaries, you should either offer users the source if they want, or point them to the Open Babel website. Note that if you modify the source, you obviously can't point back to the Open Babel website -- the GPL requires that you distribute the changed source. (Or you can convince us to incorporate the changes and point back to us.)

What's not to like with this deal? You can have Open Babel translate foreign file formats for you and can point users at the website for distribution. You don't need to write tons of code for all these formats and bug reports can be passed back to us.

Of course, there's one catch. You'll most likely need to add feature-rich support for your file formats. So if you contribute a small amount of code under the GPL to read/write your files, everything else is handled by Open Babel.

It's a win-win for everyone. The community benefits by having feature-rich translation code and open file formats. Your company and its programs benefit by the ability to read just about every format imaginable. Users benefit by using the programs they need for the tasks they need.

.. rubric:: What's in it for me as an academic?

If you're an academic developer, you certainly should read the previous answer too. It takes little work on your part to interface with Open Babel and you get a lot in return.

But even if you're just an academic user, there's a lot of reasons to contribute. Most of us deal with a variety of file formats in our work. So it's useful to translate these cleanly. If a format isn't currently supported by Open Babel, see question 2.1 above. If you find bugs please report them. Since it's open source, you can patch the code yourself, recompile and have the problem fixed very quickly.

If you're inclined to write code, the GPL is an excellent option for the academic. You're the original copyright holder, so you can do whatever you want with the code, in addition to selling it. But if you've also licensed it under the GPL, no one can distribute it proprietarily (i.e., closed-source) without your agreement. Fellow acadmics can use it directly, learn from it, improve it and contribute back to you. Isn't that why many of us went into science?

Once licensed under the GPL, the code must remain free to interested parties. If someone modifies it, that code must still remain under the GPL, free for all.

.. rubric:: What's in it for an open-source software project?

Certainly the answers for closed-source software and academics also apply for you. Beyond that, if your code is compatible with the GPL, you can directly use Open Babel and all of the API. This is already happening with the Ghemical molecular editor, available under the GPL and many others (see `related projects`_). There's a lot of code in Open Babel beyond file translation and more to come. Why reinvent the wheel?

.. _related projects: http://openbabel.org/wiki/Related

.. rubric:: Why is this covered under the GPL instead of license X?

The short answer is that `OpenEye Scientific Software`_ employs Matt Stahl, one of the authors of the original Babel. They released a library called OELib under the GPL that did many things that Babel did. Later they decided to release the next version of OELib as a closed-source project--their choice for their code. We took the version of OELib still under GPL and went from there.

.. _OpenEye Scientific Software: http://www.eyesopen.com

If you'd like to see Open Babel licensed differently, we'd suggest asking OpenEye if they'd consider releasing the old code under a new license, e.g. the LGPL. At that point, we'd consider whether Open Babel should be relicensed or not. Obviously all copyright holders must agree to the new license.

It's worth noting that since OpenEye is developing a closed-source library called OEChem_ and implies one reason for purchase is in closed-source development products. So we think it's highly unlikely that OpenEye would allow Open Babel to become a competitor by relicensing under the LGPL.

.. rubric:: Where can I read more about the GNU GPL?

The Free Software Foundation maintains a FAQ_ list about the GNU GPL. The FAQ attempts to address common questions in an easy-to-read (i.e., not in legal language) form. 

.. _FAQ: http://www.fsf.org/licenses/gpl-faq.html
