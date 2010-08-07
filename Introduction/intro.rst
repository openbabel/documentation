Goals of the Open Babel project
===============================

Open Babel is a project to facilitate the interconversion of chemical data from one format to another -- including file formats of various types. While this likely seems mundane to some, it reflects several realistic points:

* Multiple programs are often required in realistic workflows. These may include databases, modeling or computational programs, visualization programs, etc.
* Many programs have individual data formats, and/or support only a small subset of other file types.
* Chemical representations often vary considerably:
   * Some programs are 2D. Some are 3D. Some use fractional k-space coordinates.
   * Some programs use bonds and atoms of discrete types. Others use only atoms and electrons.
   * Some programs use symmetric representations. Others do not.
   * Some programs specify all atoms. Others use "residues" or omit hydrogen atoms. 
* Individual implementations of even standardized file formats are often buggy, incomplete or do not completely match published standards. 

As a free, and open source project, Open Babel improves by way of helping others. It gains by way of its users, contributors, developers, related projects, and the general chemical community. We must continually strive to support these constituencies.

We gratefully accept contributions in many forms -- from bug reports, complaints, and critiques, which help us improve what we do poorly, to feature suggestions, code contributions, and other efforts, which direct our future development.

* For end users, we seek to provide a range of utility, from simple (or complex) file interconversion, to indexing, databasing, and transforming chemical and molecular data.
* For developers, we seek to provide an easy-to-use free and open source chemical library. This assists a variety of chemical software, from molecular viewers and visualization tools and editors to databases, property prediction tools, and in-house development. 

To this end, we hope that our tools reflect several key points:

* As much chemical information and files should be read and understood by Open Babel. This means that we should always strive to support as many concepts as possible in a given file format, and support for additional file formats is beneficial to the community as a whole.
* Releases should be made to be "as good as we can make it" each and every time.
* Improving our code and our community to bring in additional contributions in many forms helps both developers and end-users alike. Making development easy for new contributors will result in better tools for users as well. 
