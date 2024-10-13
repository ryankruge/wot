from main import *

REQUIRED = [ '-t', '-i' ]
CONFIGURABLE = [ '-t', '-i' ]

HELP_MESSAGE = f"""WOT ({colorama.Fore.RED}Who's Out There?{colorama.Fore.WHITE}):
A simple tool for host discovery.

[Required]:
{colorama.Style.DIM}[{colorama.Style.RESET_ALL}-t{colorama.Style.DIM}]{colorama.Style.RESET_ALL} Define the target for the scan.
{colorama.Style.DIM}[{colorama.Style.RESET_ALL}-i{colorama.Style.DIM}]{colorama.Style.RESET_ALL} Define the desired network interface.

[Optional]:
{colorama.Style.DIM}[{colorama.Style.RESET_ALL}-h{colorama.Style.DIM}]{colorama.Style.RESET_ALL} Print the help display."""

try:
	if '-h' in sys.argv:
		print(HELP_MESSAGE)
		sys.exit()

	if not VerifyRequired(sys.argv, REQUIRED):
		PrintMessage("Failure to verify provided flags. Please ensure you have included required criteria.")
		sys.exit()

	parameters = { '-t': None, '-i': None }
	parameters = PopulateParameters(sys.argv, CONFIGURABLE, parameters)

	discovery = Discovery(
		parameters['-t'], 
		parameters['-i']
	)

	hosts = discovery.GetHosts()
	if not hosts:
		PrintMessage("There was an error whilst attempting to scan the network.")

	for host in hosts:
		PrintMessage("Result for {}[{}{}{}]{}: {}({}{}{}){}".format(
			colorama.Style.DIM,
			colorama.Style.RESET_ALL,
			host,
			colorama.Style.DIM,
			colorama.Style.RESET_ALL,
			colorama.Style.DIM,
			colorama.Style.RESET_ALL,
			discovery.ReverseDNS(host),
			colorama.Style.DIM,
			colorama.Style.RESET_ALL
		))
except KeyboardInterrupt:
	PrintMessage("Received halt signal. Exiting gracefully.")
	sys.exit()