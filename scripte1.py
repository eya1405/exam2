from netmiko import ConnectHandler
#information de connextion
router = {
	"device_type": "cisco_ios",
	"host":"sanbox-iosxe-latest-1.cisco.com",
	"username":"admin",
	"password":"cisco12345",
	"port":22
}
#connexion au router
conn= ConnectHandler(**router)
#affiche l'heur
clock = conn.send_command("show clock")
print(clock)
#affiche les interfaces
interfac = conn.send_command("sh ip int br")
with open ("interfaces.txt","w") as files:
	file.write(interfac)
print('interfac.txt')
#cofiguration interfaces loopback avec ip 
commands = [
	"interface loopback 8",
	"ip address 10.8.8.8 255.255.255.240",
	"no shutdown"
]
configuration = conn.send_config_set(commands)
print(configuration)
