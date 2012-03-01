.. _add-new-descriptor:

How to add a new descriptor
===========================

[Some text here]

Add a new group contribution descriptor
---------------------------------------

Group contribution descriptors are a common type of molecular descriptor whose value is a sum of contributions from substructures of the molecule. Such a descriptor can easily be added to Open Babel without the need to recompile the code. All you need is a set of SMARTS strings for each group, and their corresponding contributions to the descriptor value.

The following example shows how to add a new descriptor, *hellohalo*, whose value increments by 1, 2, 3 or 4 for each F, Cl, Br, and I (respectively) in the molecule.

1. Create a working directory, for example :file:`C:\\Work`.
2. Copy the plugin definition file, :file:`plugindefines.txt` to the working directory. This file can be found in the Open Babel data directory (typically in :file:`/usr/share/openbabel` on Linux systems, or :file:`C:\\ProgramData\\OpenBabel-2.3.1\\data` on Windows).
3. For the *hellohalo* descriptor, add the following to the end of :file:`plugindefines.txt` (make sure to include a blank line between it and other descriptor definitions)::

        OBGroupContrib
        hellohalo              # name of descriptor
        hellohalo_smarts.txt   # data file
        Count up the number of halogens (sort of)\n    # brief description
        This descriptor is not correlated with any\n   # longer description
        known property, living or dead.
    
4. Now create a file :file:`hellohalo_smarts.txt`, again in the working directory, containing the following SMARTS definitions and contribution values::

           # These are the SMARTS strings and contribution values
           # for the 'hellohalo' group contribution descriptor.
           ;heavy
           F    1  # This is for fluorines
           Cl   2  # And this is for chlorines
           Br   3  # Etc.
           I    4  # Ditto

That's it!

Now let's test it. Open a command prompt, and change directory to the working directory. We can find information on the new descriptor using :command:`obabel`'s ``-L`` option::

        C:\Work>obabel -L descriptors
        abonds    Number of aromatic bonds
        atoms    Number of atoms
        ...
        hellohalo    Count up the number of halogens (sort of)
        ...
        title    For comparing a molecule's title
        TPSA    topological polar surface area

        C:\Work>obabel -L hellohalo
        One of the descriptors
        hellohalo    Count up the number of halogens (sort of)
        This descriptor is not correlated with any
        known property, living or dead.
         Datafile: hellohalo_smarts.txt
        OBGroupContrib is definable

An easy way to test the descriptor is to use the title output format, and append the descriptor value to the title::

        C:\Work>obabel -:C(Cl)(Cl)I -otxt --append hellohalo
        4
        1 molecule converted

There are a couple of points to note about the pattern file:

1. Although a SMARTS string may match a substructure of a molecule, the descriptor contribution is only assigned to the first atom of the match.

2. Where several SMARTS strings assign values to the same atom, only the final assignment is retained. As an example, the following set of patterns will assign a contribution of 0.4 to all atoms except for carbon atoms, which have a value of 1.0::

        ;heavy
        [*]     0.4    # All atoms
        [#6]    1.0    # All carbon atoms

3. If you wish to take into account contributions from hydrogen atoms, you should precede the ``;heavy`` section by a ``;hydrogen`` section. The values for the contributions in the latter section are multiplied by the number of hydrogens attached to the matching atom. For example, consider the following set of patterns::

        ;hydrogen
        [*]  0.2   # Hydrogens attached to all atoms
        C    1.0   # Hydrogens attached to an aliphatic carbon
        ;heavy
        C   10.0   # An aliphatic carbon

   For ethanol, this gives a value of 25.2: two carbons (20.0), five hydrogens attached to a carbon (5.0), and one other hydrogen (0.2).

For further inspiration, check out :file:`psa.txt`, :file:`mr.txt` and :file:`logp.txt` in the :file:`data` directory. These are the group contribution descriptions for Polar Surface Area, Molar Refractivity and LogP.
