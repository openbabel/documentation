.. _MDL_RXN_format:

MDL RXN format (rxn)
====================

**The MDL reaction format is used to store information on chemical reactions.**


Output Options, e.g. -xA
 A  output in Alias form, e.g. Ph, if present
 G <option> how to handle any agents present

            One of the following options should be specifed:

            - agent - Treat as an agent (default). Note that some programs
                      may not read agents in RXN files.
            - reactant - Treat any agent as a reactant
            - product - Treat any agent as a product
            - ignore - Ignore any agent
            - both - Treat as both a reactant and a product



