from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import socket
from skimage import io
from skimage import transform
from skimage import color
from skimage import filters

def image_upload(filedata, date, host_id):
    with open(date+host_id+'.jpg', 'wb') as handle:
        data = filedata.data
        handle.write(data)
        handle.close()
        return True

def image_download(date, host_id):
    handle = open(date+host_id+'.jpg', 'rb')
    return xmlrpc.client.Binary(handle.read())
    handle.close()

def imrotate(date, host_id, angle):
    image = io.imread(date+host_id+'.jpg')
    rotate = transform.rotate(image, angle)
    print('Image Rotated with', angle,' degree')
    io.imsave(date+host_id+'.jpg', rotate)

def imblur(date, host_id, s):
    image = io.imread(date+host_id+'.jpg')
    blur = filters.gaussian(image, sigma=s)
    print('Image blur success')
    io.imsave(date+host_id+'.jpg', blur)

# Main Server Program
# Change the ip address and port if necessary    
server = SimpleXMLRPCServer(('localhost', 8000), allow_none=True)
print('Listening on port 8000')

server.register_function(image_upload, 'image_upload')
server.register_function(image_download, 'image_download')
server.register_function(imrotate, 'imrotate')
server.register_function(imblur, 'imblur')
server.serve_forever()