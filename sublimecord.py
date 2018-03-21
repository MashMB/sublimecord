"""
File name: sublimecord.py
Author: Maciej Bedra

Sublime Text 3 commands, event handler
and connection to Discord via Discord IPC wrapper.
"""

import os
import re
import sublime
import sublime_plugin
import sys

sys.path.insert(0, os.path.dirname(__file__))
import discord_ipc
import extensions

class Sublimecord:
	"""
	Singleton class that gives all necessary tools
	to send Discord Rich Presence with data
	taken from Sublime Text 3.
	"""

	__instance = None

	@staticmethod
	def get_instance():
		"""
		Get Sublimecord instance if exists
		in other situation, create new instance.

		:returns: Sublimecord instance
		:rtype: Sublimecord
		"""

		if Sublimecord.__instance == None:
			Sublimecord()

		return Sublimecord.__instance

	def __init__(self):
		"""
		Sublimecord constructor.
		"""

		if Sublimecord.__instance != None:
			raise Exception("Cannot create more instances of Sublimecord")
		else:
			Sublimecord.__instance = self

		self.project_name = None
		self.file_name = None
		self.file_extension = None
		self.file_size = None
		self.ipc = None
		self.sublimecord_settings = sublime.load_settings("Sublimecord.sublime-settings")

	def get_file_size(self, characters):
		"""
		Converting characters quantity to size
		on which computer operate.

		:param characters: characters to convert quantity
		:type characters: int
		:returns: size on which computer operate
		with proper size definition
		:rtype: string
		"""

		if characters < 1024:
			return str(int(characters)) + "B"
		elif characters >= 1024:
			return str(int(characters / 1024)) + "kB"
		elif characters >= 1048576:
			return str(int(characters / 1048576)) + "MB"
		elif characters >= 1073741824:
			return str(int(characters / 1073741824)) + "GB"

	def connect_to_discord(self):
		"""
		Connect to Discord and send initial Discord Rich Presence.
		"""

		if self.ipc == None:
			self.ipc = discord_ipc.DiscordIPC("417649998252081154")
			self.ipc.connect()
			self.change_status()

	def disconnect_from_discord(self):
		"""
		Disconnect from Discord and reset ipc object.
		"""

		if self.ipc != None:
			self.ipc.disconnect()
			self.ipc = None

	def get_file_properties(self, view):
		"""
		Getting opened file name, extension and size.

		:param view: Sublime Text view instance
		:type view: View
		"""

		path = view.file_name()

		if path != None:
			splitted_path = re.split('\\\\|/', path)
			self.file_name = splitted_path[-1]
			splitted_file_name = self.file_name.split(".")
			self.file_extension = splitted_file_name[-1].lower()
			self.file_size = self.get_file_size(view.size())
		else:
			self.file_name = None
			self.file_extension = None
			self.file_size = None

	def get_project_name(self, window):
		"""
		Getting opened project name (opened folder).

		:param window: Sublime Text window instance
		:type window: Window
		"""

		folders = window.folders()

		if len(folders) != 0:
			path = folders[0]
			splitted_path = re.split('\\\\|/', path)
			self.project_name = splitted_path[-1]
		else:
			self.project_name = None

	def change_status(self):
		"""
		Check variables content, prepare titles and
		send Discord Rich Presence.
		"""

		if self.ipc != None:
			project_status = None
			file_status = None

			if self.sublimecord_settings.get("hide_project_name") == False:
				if self.project_name != None:
					project_status = "Working on: " + self.project_name
				else:
					project_status = "No project opened"
			else:
				project_status = "Top secret project"

			if self.sublimecord_settings.get("hide_file_name") == False:
				if self.file_name != None:
					file_status = "File: " + self.file_name
				else:
					file_status = "No file opened"
			else:
				if self.file_size != None:
					file_status = "File size: " + self.file_size
				else:
					file_status = "File size: 0B"

			if self.file_extension in extensions.supported:
				self.ipc.send_rich_presence(extensions.sublime_text["header"],
							extensions.sublime_text["logo"],
							extensions.supported[self.file_extension],
							self.file_extension,
							project_status,
							file_status)
			else:
				self.ipc.send_rich_presence(extensions.sublime_text["header"],
							extensions.sublime_text["logo"],
							extensions.unknown["header"],
							extensions.unknown["icon"],
							project_status,
							file_status)

class ConnectCommand(sublime_plugin.WindowCommand):
	"""
	Command that allows connect to Discord
	via Discord IPC socket and send initial
	Discord Rich Presence status.

	:param: class is extending WindowCommand class from
	sublime_plugin package
	:type WindowCommand: WindowCommand
	"""

	def run(self):
		"""
		Get project name, file name, file extension,
		connect to Discord and send initial Discord Rich Presence.
		WindowCommand overriden method.
		"""

		sublimecord = Sublimecord.get_instance()
		sublimecord.get_project_name(self.window)
		sublimecord.get_file_properties(self.window.active_view())
		sublimecord.connect_to_discord()

class DisconnectCommand(sublime_plugin.WindowCommand):
	"""
	Command created to properly disconnect from Discord
	(Discord Rich Presence will be still visible, it will disappear
	after closing Sublime Text 3).

	:param: class is extending WindowCommand class from
	sublime_plugin package
	:type WindowCommand: WindowCommand
	"""

	def run(self):
		"""
		Proper way to disconnect from Discord.
		WindowCommand overriden method.
		"""

		sublimecord = Sublimecord.get_instance()
		sublimecord.disconnect_from_discord()

class EventHandler(sublime_plugin.ViewEventListener):
	"""
	Event handler, sends Discord Rich Presence on specific action.

	:param ViewEventListener: class is extending ViewEventListener class from
	sublime_plugin package
	:type ViewEventListener: ViewEventListener
	"""


	def on_activated(self):
		"""
		Update Discord Rich Presence status every time
		when Sublime Text 3 is connected and view gains
		focus.
		"""

		sublimecord = Sublimecord.get_instance()
		sublimecord.get_project_name(sublime.active_window())
		sublimecord.get_file_properties(self.view)
		sublimecord.change_status()