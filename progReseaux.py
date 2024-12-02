from netmiko import ConnectHandler
#information de connexion
router = {
	"device_type":"cisco ios"
	"host" : "sandbox-iosxe-latest-1.cisco.com"
	"user_name":"admin"
	"port":22
}
#connexion au router
conn=ConnectHandler(**router)
#show l'heure
clock=conn.send_command("show clock")
print(clock)
#affichage les interfaces 
interface=conn.send_command(sh ip int br)
with open ('interfaces.txt','w') as file
file.write(interface)
print (interface.txt)
#configuration interface loopback ip 
commands=[
	"interfaces loopback 8",
	"ip address 10.8.8.8 255.255.255.240"
	"no shutdown"
]
configuration conn.send config set (commands)
print (configuration)
