import xmlrpc
import xmlrpc.client
import socket
import datetime

proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

host_id = str(socket.gethostname())
date = str(datetime.datetime.now().date())

# For upload image data
with open("gambar.jpg", 'rb') as handle:
    data = xmlrpc.client.Binary(handle.read())
    handle.close()
    result = proxy.image_upload(data, date, host_id)

# For download image data
# handle = open("gambar_baru.jpg", "wb")
# handle.write(proxy.image_download(host_id).data)
# handle.close()

# Run image rotate function in server
# proxy.imrotate(date, host_id, 90)

# Run image blur function in server
# proxy.imblur(date, host_id, 1)