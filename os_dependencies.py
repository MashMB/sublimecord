"""
File name: os_dependencies.py
Author: Maciej Bedra

File that contains expected localizations to 
Discord IPC socket on specific platforms.
"""

# Supported platforms
supported = ["windows", "linux", "darwin"]

# Localizations for specific platforms where Discord IPC socket can be found
localizations = {
	"windows": "\\\\?\\pipe",
	"unix": {
		"XDG_RUNTIME_DIR",
		"TMPDIR",
		"TMP",
		"TEMP"
	}
}

# Expected socket name
socket_name = ["discord-ipc-0"]