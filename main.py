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
		return socket.gethostbyaddr(host)[0]

def PrintMessage(message):
		print(f"{colorama.Style.DIM}[{colorama.Style.RESET_ALL}*{colorama.Style.DIM}]{colorama.Style.RESET_ALL} {message}")

def PrintHelp(message):
	print(message)
	sys.exit()

def PopulateParameters(parameters, arguments):
	temporary = parameters
	for argument in range(0, len(arguments)):
		match arguments[argument]:
			case '-t':
				temporary['Target'] = arguments[argument + 1]
			case '-i':
				temporary['Interface'] = arguments[argument + 1]
	return temporary

def VerifyRequired(arguments, required):
	for argument in required:
		if argument not in arguments:
			return False
	return True