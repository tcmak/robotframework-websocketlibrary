
from websocket import create_connection

class WebSocketLibrary:

#	def __init__(self,URL=""):
#		if URL != "":
#			self._ws = create_connection(URL)

	def connect(self,URL,timeout=None, **options):
		self._ws = create_connection(URL,timeout,**options)

	def gettimeout(self):
		return self._ws.gettimeout()

	def settimeout(self, timeout):
		self._ws.settimeout(timeout)

	def getsubprotocol(self):
		return self._ws.getsubprotocol()

	def getstatus(self):
		return self._ws.getstatus()

	def getheaders(self):
		return self._ws.getheaders()

	def send(self,message):
		return self._ws.send(message)

	def send_binary(self,payload):
		return self._ws.send_binary(payload)

	def ping(self,payload=""):
		self._ws.ping(payload)

	def pong(self,payload=""):
		self._ws.pong(payload)

	def recv(self):
		return self._ws.recv()

	def recv_data(self, control_frame=False):
		return self._ws.recv_data(control_frame)

	def send_close(self):
		self._ws.send_close()

	def send_close_with_reason(self, status, reason):
		self._ws.send_close(status, reason)

	def close(self):
		self._ws.close()

	def close_with_reason(self, status, reason):
		self._ws.close(status, reason)

#	def __del__(self):
#		self._ws.close()
