Sublimecord
===========

Sublime Text 3 commands, event handler and connection to Discord via Discord IPC wrapper.

.. py:class:: Sublimecord

	Singleton class that gives all necessary tools
	to send Discord Rich Presence with data
	taken from Sublime Text 3.

	.. py:method:: get_instance()

		Get Sublimecord instance if exists in other situation, create new instance.

		:returns: Sublimecord instance
		:rtype: Sublimecord

	.. py:method:: __init__(self)

		Sublimecord constructor.

	.. py:method:: get_file_size(self, characters)

		Converting characters quantity to size on which computer operate.

		:param characters: characters to convert quantity
		:type characters: int
		:returns: size on which computer operate with proper size definition
		:rtype: string

	.. py:method:: connect_to_discord(self)

		Connect to Discord and send initial Discord Rich Presence.

	.. py:method:: disconnect_from_discord(self)

		Disconnect from Discord and reset ipc object.

	.. py:method:: get_file_properties(self, view)

		Getting opened file name, extension and size.

		:param view: Sublime Text view instance
		:type view: View

	.. py:method:: get_project_name(self, window)

		Getting opened project name (opened folder).

		:param window: Sublime Text window instance
		:type window: Window

	.. py:method:: change_status(self)

		Check variables content, prepare titles and
		send Discord Rich Presence.

.. py:class:: ConnectCommand(sublime_plugin.WindowCommand)

	Command that allows connect to Discord via Discord IPC socket and send initial Discord Rich Presence status.

	:param: class is extending WindowCommand class from sublime_plugin package
	:type WindowCommand: WindowCommand

	.. py:method:: run(self)

		Get project name, file name, file extension, connect to Discord and send initial Discord Rich Presence. WindowCommand overriden method.

.. py:class:: DisconnectCommand(sublime_plugin.WindowCommand)

	.. py:method:: run(self)

		Proper way to disconnect from Discord. WindowCommand overriden method.

.. py:class:: EventHandler(sublime_plugin.ViewEventListener)

	Event handler, sends Discord Rich Presence on specific action.

	:param ViewEventListener: class is extending ViewEventListener class from sublime_plugin package
	:type ViewEventListener: ViewEventListener

	.. py:method:: on_activated(self)

		Update Discord Rich Presence status every time when Sublime Text 3 is connected and view gains focus.