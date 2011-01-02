.. _error handling:

Errors and Warnings
===================

Errors and warnings in Open Babel are handled internally by a flexible system motivated by a few factors:

* End users often do not wish to be deluged by debugging or other messages during operation.
* Other developers may wish to redirect or filter error/warning output (e.g., in a GUI).
* The operation of Open Babel should be open to developers and users alike to monitor an "audit trail" of operations on files and molecules, and debug the program and library itself when the need arises. 

Multiple error/warning levels exist and should be used by code. These are defined in the :obapi:`obMessageLevel` enum as follows:

* ``obError`` -- for critical errors (e.g., cannot read a file)
* ``obWarning`` -- for non-critical problems (e.g., molecule appears empty)
* ``obInfo`` -- for informative messages (e.g., file is a non-standard format)
* ``obAuditMsg`` -- for messages auditing methods which destroy or perceive molecular data (e.g., kekulization, atom typing, etc.)
* ``obDebug`` -- for messages only useful for debugging purposes 

The default filter level is set to ``obWarning``, which means that users are told of critical errors, but not non-standard formatting of input files. For more information, please see the API documentation for the :obapi:`OBMessageHandler` class.

.. highlight:: c++

A global error handler :obapi:`obErrorLog` (an instance of :obapi:`OBMessageHandler`) is defined and can be used as illustrated below::

    if (atomIndex < 1 || atomIndex > mol.NumAtoms() )
        obErrorLog.ThrowError(__FUNCTION__, "Requested Atom Out of Range", obDebug);

     stringstream errorMsg;
     errorMsg << " Could not parse line in type translation table types.txt"
              << " -- incorrect number of columns";
     errorMsg << " found " << vc.size() << " expected " << _ncols << ".";
     obErrorLog.ThrowError(__FUNCTION__, errorMsg.str(), obInfo);

The ``__FUNCTION__`` builtin is defined by many compilers (e.g., GCC) but can be defined to an empty string on some platforms without this compiler extension. It is currently used to provide information about which function is yielding the error or debugging information. This extension should eventually be replaced in the Open Babel code by ``__func__`` which is now part of the C99 standard. 

