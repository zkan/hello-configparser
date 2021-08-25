import configparser


parser = configparser.ConfigParser()
parser.read("main.conf")

sections = parser.sections()
print("Sections:", sections)

default = parser["DEFAULT"]
print(default)

server_alive_interval = parser["DEFAULT"]["ServerAliveInterval"]
print("ServerAliveInterval:", server_alive_interval)

another_server_alive_interval = parser.get("DEFAULT", "ServerAliveInterval")
print("Another ServerAliveInterval:", another_server_alive_interval)

bitbucket_user = parser.get("bitbucket.org", "User")
print("Bitbucket User:", bitbucket_user)

bitbucket_server_alive_interval = parser.get("bitbucket.org", "ServerAliveInterval")
print("Bitbucket ServerAliveInterval:", bitbucket_server_alive_interval)

bitbucket_forward_x11 = parser.get("bitbucket.org", "ForwardX11")
print("Bitbucket ForwardX11:", bitbucket_forward_x11)

topsecret_port = parser.get("topsecret.server.com", "Port")
print("Topsecret Port:", topsecret_port)

topsecret_forward_x11 = parser.get("topsecret.server.com", "ForwardX11")
print("Topsecret ForwardX11:", topsecret_forward_x11)
