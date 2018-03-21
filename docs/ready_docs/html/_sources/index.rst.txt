Welcome to documentation of Sublimecord!
========================================

Sublimecord is a Sublime Text 3 plugin that integrates your favourite text editor with Discord and allows you to share your work status with Discord community via Discord Rich Presence.

.. image:: ../img/sublimecord_plugin.png
	:align: center

Sublimecord has support for 55 programming languages that are also supported by Sublime Text 3. If you want to include more languages, just post it on `GitHub issues page <https://github.com/MashMB/sublimecord/issues>`_.

=============
How it works?
=============

Sublimecord is based on my other opensource project posted on GitHub (`discord_rpc_client <https://github.com/MashMB/discord_rpc_client>`_) that ensures communication with Discord. Plugin identifies opened file and folder name, sets activity timer.

Plugin works **only when Discord app is opened on client PC** (Discord Rich Presence mechanism enforces this) and supports all common platforms (Windows, Linux and MacOS).

To activate plugin, just use **command palette**:

.. image:: ../img/sublimecord_commands.png
	:align: center

After executing **connect** command, your status on Discord should be changed.

In plugin settings you can find options to hide project and file name.

====================================
Why there is no autoconnect feature?
====================================

There is no autoconnect feature because Discord app is not always opened when editor is (as it is written above, plugin needs Discord app to be opened on client PC) and we do not want to see error messages on screen. What is more, we do not always want to share our status while programming. It is not a big deal to use **command palette**.

===========================================================
Why Sublime Text 3 must be closed after disconnect command?
===========================================================

It is a little bit tricky. Sublime Text 3 uses it's own Python interpreter. Sublimecord plugin gets Sublime Text 3 process PID and sends it to Discord. Discord will show your status to the moment when process with given PID disappears. It can be achived only by closing editor and can not be tricked easily (there is option to do it by subprocess but client need to have Python installed on their machine so I do not see any sense to add this feature).

For people that wants to know how plugin works under the hood I prepared complex documentation that can be found here: `Welcome to documentation of Sublimecord! <https://github.com/MashMB/sublimecord/docs/ready_docs/html>`_

============
Installation
============

Sublimecord is not available to download from main **Package Control** channel.

Plugin installation is simple, just use a **command palette** and type:

.. code-block:: shell

	Package Control: Add Repository


Nextly paste link to the GitHub repo:

.. code-block:: shell

	https://github.com/MashMB/sublimecord

The last step is to find **Sublimecord** plugin on the list after using **command palette** command:

.. code-block:: shell

	Package Control: Install Package

There is known error with SSL certificate while downloading plugins from custom repositories (GitHub security update), so if above instructions do not work, install plugin manually, just download the repository and unpack it in Sublime Text 3 packages folder as follow:

Windows:

.. code-block:: shell

	C:\Users\<username>\AppData\Roaming\Sublime Text 3\Packages\

Linux:

.. code-block:: shell

	/home/<username>/.config/sublime-text-3/Packages/

MacOS:

.. code-block:: shell

	~/Library/Application Support/Sublime Text 3/Packages/

===============
Bugs and issues
===============

If you find any bugs or issues, I will be really happy to fix them, just post problem description on `GitHub issues page <https://github.com/MashMB/sublimecord/issues>`_. You can make it easier for me if you change only two lines of code in file **discord_ipc.py** that can be found in Sublime Text 3 packages folder named **sublimecord** (localization of packages is given above in **Install** section of this document).

Replace line 25 with this code:

.. code-block:: python

	logger_level = "DEBUG" 


Also line 30 with this code:

.. code-block:: python

	logger.disabled = True

After code replacement, restart Sublime Text 3 and open Sublime Text 3 console with **ctrl + `** shortcut. Try to connect to Discord, copy the console output that matches file **discord_ipc.py** and paste it on `GitHub issues page <https://github.com/MashMB/sublimecord/issues>`_.

As I am working all time on something new, do not be mad if fix will take some time.

=======
License
=======

The MIT License (MIT)

Copyright (c) 2018 Maciej Bedra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

.. toctree::
	:maxdepth: 2
	:hidden: 

	Sublimecord <docs/sublimecord>
	Extensions <docs/extensions>
	Discord IPC Wrapper <docs/discord_ipc>