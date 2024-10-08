from main import *

HELP_MESSAGE = f"""WOT ({colorama.Fore.RED}Who's Out There?{colorama.Fore.WHITE}):
A simple tool for host discovery.

[Required]:
{colorama.Style.DIM}[{colorama.Style.RESET_ALL}-t{colorama.Style.DIM}]{colorama.Style.RESET_ALL} Define the target for the scan.
{colorama.Style.DIM}[{colorama.Style.RESET_ALL}-i{colorama.Style.DIM}]{colorama.Style.RESET_ALL} Define the desired network interface.

[Optional]:
{colorama.Style.DIM}[{colorama.Style.RESET_ALL}-h{colorama.Style.DIM}]{colorama.Style.RESET_ALL} Print the help display."""

REQUIRED = [ '-t', '-i' ]

try:
	parameters = { 'Help': False, 'Target': None, 'Interface': None }

	if '-h' in sys.argv:
		PrintHelp(HELP_MESSAGE)

	if not VerifyRequired(sys.argv, REQUIRED):
		PrintMessage("Failure to verify provided flags. Please ensure you have included required criteria.")
		sys.exit()

	parameters = PopulateParameters(parameters, sys.argv)

	discovery = Discovery(
		parameters["Target"], 
		parameters["Interface"]
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
except OSError:
	PrintMessage("There was an operating system failure detected.")
except ValueError:
	PrintMessage("There was an error with one of the fields provided.")