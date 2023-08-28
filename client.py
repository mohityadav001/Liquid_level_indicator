from opcua import Client
import time
import base64
import subprocess


# create a client object
client = Client("server url")


with open('outimg_0.png', 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read())
# connect to the server
client.connect()


node = client.get_node("ns=3;s=1007")
# write the base64 string to the OPC UA server
node.set_value(encoded_string)

# disconnect from the server
client.disconnect()
# subprocess.run(["jupyter", "Untitled.ipynb"])
