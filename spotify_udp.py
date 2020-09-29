import argparse, random, socket, sys, datetime

class server:
	MAX_BYTES = 65535

	def __init__(self, interface, port):
		self.interface = interface
		self.port = port

	def run(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.bind((self.interface, self.port))
		print("Server socket: ", sock.getsockname())
		while True:
			data, address = sock.recvfrom(self.MAX_BYTES)
			text = data.decode('ascii')
			print(f"The client at {address} says {text}. ")
			message = "I received your message. "
			sock.sendto(message.encode('ascii'), address)

class client:
	MAX_BYTES = 655535

	def __init__(self, hostname, port):
		self.hostname = hostname
		self.port = port

	def run(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.connect((self.hostname, self.port))
		print("Client socket: ", sock.getsockname())
		delay = 0.1
		text = "This message is sent to the server by the client. "
		data = text.encode('ascii')
		while True:
			sock.send(data)
			print(f"Waiting up to {delay} seconds. ")
			sock.settimeout(delay)
			try:
				data = sock.recv(self.MAX_BYTES)
			except socket.timeout:
				today = datetime.datetime.now().date()
				time1 = datetime.time(12,00).replace(second = 0, microsecond = 0)
				time2 = datetime.time(17,00).replace(second = 0, microsecond = 0)
				time3 = datetime.time(23, 59).replace(second = 0, microsecond = 0)
				current_time = datetime.datetime.now().time().replace(second = 0, microsecond = 0)
				t = datetime.datetime.combine(today, current_time)
				t1 = datetime.datetime.combine(today, time1)
				t2 = datetime.datetime.combine(today, time2)
				t3 = datetime.datetime.combine(today, time3)

				if t >= t1 and t < t2:
					delay *= 2
					if delay > 2.0:
						raise RuntimeError("Server is down. ")

				elif t >= t2 and t < t3:
					delay *= 3
					if delay > 4.0:
						raise RuntimeError("Server is down. ")

				else:
					delay *=2
					if delay > 1.0:
						raise RuntimeError("Server is down. ")

			else:
				break
		print("Server says: ", data.decode('ascii'))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description = "sending data by UDP")
	choices = {"client": client, "server": server}
	parser.add_argument("role", choices = choices, help = "either server or client")
	parser.add_argument("host", help = "server interface")
	parser.add_argument("-p", metavar = 'PORT', type = int, default = 4337, help = "UDP port")

	args = parser.parse_args()
	classname = choices[args.role]
	endpoint = classname(args.host, args.p)
	endpoint.run()
