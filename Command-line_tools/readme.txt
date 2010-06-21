The best solution for keeping the docs in synch with the man pages seems to be to do shallow parsing of the Options from the rst file (e.g. using a Python script) and stick the result into a template for the man page.

With a bit more work, other parts of the man page can also be taken from rst, for example, Sections with more in-depth discussions of particular options.
