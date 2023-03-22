========================
**Tasks: Mastering Git**
========================

**2. Create a project with an empty file README.md (or README.rst if you prefer).**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a project directory:

.. code-block:: bash

	$ touch README.rst
	
Add README.md:

.. code-block:: bash

	$ git add README.rst

Commit all changes:

.. code-block:: bash

	$ git commit -m "feat(repo): add README"

Create a directory lab0 with the file README.rst:

.. code-block:: bash

	$ mkdir lab0
	$ touch lab0/README.rst
	$ git add lab0/README.rst
	$ git commit -m "feat(lab0): add README"
