from scapy.all import ARP, srp, Ether
import sys, colorama, socket

class Discovery:
	def __init__(self, target, interface):
		self.target = target
		self.interface = interface

	def GetHosts(self):
		packet = Ether(dst="FF:FF:FF:FF:FF:FF") / ARP(pdst=self.target)
		replies = srp(packet, iface=self.interface, timeout=1, verbose=False)[0]

		if not replies:
			return []

		addresses = []
		for reply in range(0, len(replies)):
			addresses.append(replies[reply][1].psrc)
		return addresses

	def ReverseDNS(self, host):
		try:
			hostname = socket.gethostbyaddr(host)[0]
			return hostname
		except socket.herror:
			return

def PrintMessage(message):
	print("{}[{}*{}]{} {}".format(
		colorama.Style.DIM,
		colorama.Style.RESET_ALL,
		colorama.Style.DIM,
		colorama.Style.RESET_ALL,
		message
	))

def PopulateParameters(arguments, flags, dictionary):
	try:
		temporary = dictionary
		for argument in range(0, len(arguments)):
			if arguments[argument] in flags:
				dictionary[arguments[argument]] = arguments[argument + 1]
		return temporary
	except TypeError:
		PrintMessage("There was an error whilst populating the parameter list.")
		sys.exit()

def VerifyRequired(arguments, required):
	for argument in required:
		if argument not in arguments:
			return False
	return True