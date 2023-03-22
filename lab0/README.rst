========================
**Tasks: Mastering Git**
========================

**1. Initialize a repository.**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new directory:

.. code-block:: bash

	$ mkdir python-course
	$ cd python-course
	
Initialize a new repository in the created directory:

.. code-block:: bash

	$ git init

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

**3. Create a new branch and modify README.md.**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new branch named first_branch and switch to it:

.. code-block:: bash

	$ git branch first_branch
	$ git checkout first_branch

Modify the README.md: add a list of console commands to solve the 1st subtask:

.. code-block:: bash

	$ nano lab0/README.rst
	$ git add lab0/README.rst

Display the state of the working directory and the staging area:

.. code-block:: bash

	$ git status

Commit all changes:

.. code-block:: bash

	$ git commit -m "feat(lab0): update README.rst"

**4. Switch back to the master branch and modify README.md.**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Switch back to the master branch:

.. code-block:: bash

	$ git checkout master

Modify the README.md: add a list of console commands to solve the 2nd subtask:

.. code-block:: bash

	$ nano lab0/README.rst
	$ git add lab0/README.rst

Commit all changes:

.. code-block:: bash

	$ git commit -m "feat(lab0): update README.rst"

Display the project history:

.. code-block:: bash

	$ git log
