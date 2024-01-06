import socket

def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports): #goes through 1 port to number of specified ports
		scan_port(target,port)

def scan_port(ipaddress, port): #function performed for each individual port
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
		pass #doesnt print closed ports

targets = input("[*] Enter Targets To Scan (split them by ,): ") #input target(s)
ports = int(input("[*] Enter How Many Ports To Scan: ")) #input and specify amount of ports
if ',' in targets: #take inputs and check if multiple targets specified
	print("[*] Scanning Multiple Targets")
	for ip_addr in targets.split(','): #splitting multiple targets with comma
		scan(ip_addr.strip(' '), ports) #scan individual ips
else: #if specified only one ip
	scan(targets,ports)