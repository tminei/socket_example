import socket
import json
import datetime
with open("settings.json", "r") as f:
    settings = json.loads(f.read())["client"]

with open(settings["send"], "r") as f:
    data = f.read()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((settings["ip"], settings["port"]))
client.send(data.encode())
from_server = client.recv(settings["recv"])
client.close()
print(from_server.decode())
if settings["historyPolitics"]["save"]:
    with open(settings["historyPolitics"]["file"], "a") as f:
        f.write(f"{datetime.datetime.now()} > {from_server.decode()}\n")