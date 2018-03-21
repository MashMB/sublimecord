"""
File name: payloads.py
Author: Maciej Bedra

File that contains templates of payloads that
can be send to Discord app via Discrod IPC socket.
"""

# Payload template for handshaking
handshake = {
	"v": 1,
	"client_id": None
}

# Json template for rpc assets section
rpc_assets = {
	"large_text": None,
	"large_image": None,
	"small_text": None,
	"small_image": None
}

# Json template for rpc timestamps section
rpc_timestamps = {
	"start": None
}

# Json template for rpc complex (full) activity section
rpc_complex_activity = {
	"details": None,
	"state": None,
	"timestamps": rpc_timestamps,
	"assets": rpc_assets
}

# Json template for rpc simple activity section
rpc_simple_activity = {
	"details": None,
	"state": None,
	"timestamps": rpc_timestamps
}

# Json template for rpc args section
rpc_args = {
	"activity": None,
	"pid": None
}

# Payload template for Discord Rich Presence
rpc = {
	"cmd": "SET_ACTIVITY",
	"args": rpc_args,
	"nonce": None
}