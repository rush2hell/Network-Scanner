import subprocess as sp
import optparse as op
import scapy.all as scapy
import socket, sys
from threading import Thread

def get_arguments():
	parser = op.OptionParser()
	parser.add_option("-n", dest="ip", help="Show all device connected to network")
	parser.add_option("-i", dest="interface", help="Interface to change its MAC Address")
	parser.add_option("-m", dest="new_mac", help="New MAC Address")
	parser.add_option("-s", dest="host", help="Host Address to scan")
	parser.add_option("-a", dest="startPort", help="Start Port number to be scan")
	parser.add_option("-z", dest="endPort", help="End Port number to be scan")
	(options, arguments) = parser.parse_args()
	if (options.interface and options.new_mac):
		change_mac(options.interface,options.new_mac)
	elif options.ip:
		scan(options.ip)
	elif (options.host and options.startPort and options.endPort):
		port_scan(options.host,options.startPort,options.endPort)
	else:
		print("[-] Please enter valid arguments.")
	return options


def change_mac(interface, new_mac):
	print("[+]....Changing MAC Address for [ "+interface+" ] to "+new_mac)
	sp.call(["ifconfig", interface, "down"])
	sp.call(["ifconfig", interface, "hw", "ether", new_mac])
	sp.call(["ifconfig", interface, "up"])

def port_scan(host,startPort,endPort):
	threads = []
	timeout = 10.0
	print(host)
	try:
		hostIP = socket.gethostbyname(host)
	except KeyboardInterrupt:
		print("\n\n[*]User requested an interrupt[*]")
		sys.exit()
	except socket.gaierror:
		print("\n\n[*]Hostname unresolvable[*]")
		sys.exit()
	except socket.error:
		print("\n\n[*]Unable to connect to target[*]")
		sys.exit()

	print ("-" * 50)
	print ("Scanning Target: ", hostIP)
	print ("-" * 50)

    # Scanning and open port display
	def scanner(port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(timeout)
		result = sock.connect_ex((hostIP, port))
		if result == 0:
			print("[*] Port {}: Open".format(port))
		sock.close()

    # Setup threading and calling the scan
	sp = int(startPort)
	ep = int(endPort)
	for i in range(sp, ep+1):
		thread = Thread(target=scanner, args=(i,))
		threads.append(thread)
		thread.start()
	[x.join() for x in threads]
	print ("-" * 50)
	print ("Scanning completed!")
	print ("-" * 50)

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

	print("IP\t\t\tMAC Address\n")
	clients_list = []
	for element in answered_list:
		clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
		clients_list.append(clients_dict)
		print(element[1].psrc + "\t\t" + element[1].hwsrc)
		print(clients_list)
options = get_arguments()
