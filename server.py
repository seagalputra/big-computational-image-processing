"""
Tugas Besar Sistem Parallel dan Terdistribusi
"Big Computational Image Processing"

Amelia Anis Miranda - 1301154547
Dwiferdio Seagal Putra - 1301154323
Defa Eka Ardio - 1301154281
Fauzi Kurniawan - 1301154267

References :
    - https://docs.python.org/2/library/os.html (os - Miscellaneous operating system interfaces)
    - http://www.scipy-lectures.org/packages/scikit-image/index.html (Scikit-image: Image Processing)
    - https://docs.python.org/2/library/simplexmlrpcserver.html (SimpleXMLRPCServer - Basic XML-RPC server)
    - https://docs.python.org/3/library/xmlrpc.html (xmlrpc - XMLRPC server and client modules)
"""

from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import socket
import os
from skimage import io
from skimage import transform
from skimage import color
from skimage import filters
from skimage import img_as_uint

def image_upload(filedata, date, host_id):
    """Function for uploading image from client program to server
    
    Arguments:
        filedata {Image data} -- Read data from specify data file
        date {String} -- Date from computer's client
        host_id {String} -- Host id from computer's client
    
    Returns:
        N-Dimensional Matrix -- Return image file in server-side
    """

    with open(date+host_id+'.jpg', 'wb') as handle:
        data = filedata.data
        handle.write(data)
        handle.close()
        return True

def image_download(date, host_id):
    """Function to download image from server to client
    
    Arguments:
        date {String} -- Date from computer's client
        host_id {String} -- Host id from computer's client
    
    Returns:
        N-Dimensional Matrix -- Return image in client-side
    """

    handle = open(date+host_id+'.jpg', 'rb')
    return xmlrpc.client.Binary(handle.read())
    handle.close()

def imrotate(date, host_id, angle):
    """Function to rotate image using pecify angle in server
    
    Arguments:
        date {String} -- Date from computer's client 
        host_id {String} -- Host id from computer's client
        angle {integer} -- Specify angle to rotate image
    """

    image = io.imread(date+host_id+'.jpg')
    rotate = transform.rotate(image, angle)
    print('Image Rotated with', angle,' degree')
    io.imsave(date+host_id+'.jpg', rotate)

def imblur(date, host_id, s):
    """Function to blur the image
    
    Arguments:
        date {String} -- Date from computer's client
        host_id {String} -- Host id from computer's client
        s {integer} -- Sigma parameter for kernel blur
    """

    image = io.imread(date+host_id+'.jpg')
    blur = filters.gaussian(image, sigma=s)
    print('Image blur success')
    io.imsave(date+host_id+'.jpg', blur)

def im2gray(date, host_id):
    """Function for convert image to grayscale
    
    Arguments:
        date {String} -- Date from computer's client
        host_id {String} -- Host id from computer's client
    """

    image = io.imread(date+host_id+'.jpg')
    gray = color.rgb2gray(image)
    print('Image successfuly convert to grayscale')
    io.imsave(date+host_id+'.jpg', gray)

def imthresh(date, host_id):
    """Function to convert image into binary image
    
    Arguments:
        date {String} -- Date from computer's client
        host_id {String} -- Host id from computer's client
    """

    image = io.imread(date+host_id+'.jpg')
    gray = color.rgb2gray(image)
    thresh = filters.threshold_otsu(gray)
    binary = gray > thresh
    print("Image successfully threshold!")
    io.imsave(date+host_id+'.jpg', img_as_uint(binary))

def remove_files(date, host_id):
    """Function to remove image files
    
    Arguments:
        date {String} -- Date from computer's client
        host_id {String} -- Host id from computer's client
    """

    os.remove(date+host_id+'.jpg')

# Main Server Program
# Change the ip address and port if necessary    
server = SimpleXMLRPCServer(('192.168.1.13', 8000), allow_none=True)
print('Listening on port 8000')

server.register_function(image_upload, 'image_upload')
server.register_function(image_download, 'image_download')
server.register_function(imrotate, 'imrotate')
server.register_function(imblur, 'imblur')
server.register_function(im2gray, 'im2gray')
server.register_function(imthresh, 'imthresh')
server.register_function(remove_files, 'remove_files')
server.serve_forever()