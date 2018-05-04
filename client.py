import xmlrpc
import xmlrpc.client
import socket
import datetime
import os

def title_bar(host_id):
    os.system('clear')

    print("--------------------------------------")
    print("Hello ",host_id)

def load_images():
    print("Please load image first before going to next menu..")
    filename = input('Input your image filename (with file extensions) : ')
    # For uploading image to server
    with open(filename, 'rb') as handle:
        data = xmlrpc.client.Binary(handle.read())
        handle.close()
        result = proxy.image_upload(data, date, host_id)

def user_menu():
    print("1. Rotate Image")
    print("2. Blur Image")
    print("3. Convert image to grayscale")
    print("4. Download the image file")
    print("5. Exit")

    return input("Choose menu : ")


# Change the ip address port location in the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

host_id = str(socket.gethostname())
date = str(datetime.datetime.now().date())

# Main client program
choice = 0
title_bar(host_id)
load_images()

while(choice != '5'):
    choice = user_menu()
    # Respond user choice
    if (choice == '1'):
        degree = int(input("Please input your angle in degree : "))
        # Run image rotate function in the server
        proxy.imrotate(date, host_id, degree)
    elif (choice == '2'):
        kernel = int(input("Please input the blur intensity"))
        # Run image blur function in server
        proxy.imblur(date, host_id, kernel)
    elif (choice == '3'):
        # Code here
        print('Converted to grayscale')
    elif (choice == '4'):
        handle = open("new_image.jpg", "wb")
        handle.write(proxy.image_download(date, host_id).data)
        handle.close()
    elif (choice == '5'):
        print("Thank you for using this application")