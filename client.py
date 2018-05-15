import xmlrpc
import xmlrpc.client
import socket
import datetime
import os

def title_bar(host_id):
    
    os.system('clear')

    print("--------------------------------------")
    print("  Big Computational Image Processing  ")
    print("--------------------------------------")
    print("Hello ",host_id)

def load_images():
    # Implement load image in client-side
    print("Please load image first before going to next menu..")
    filename = input('Input your image filename (include file extensions) : ')
    # For uploading image to server
    with open(filename, 'rb') as handle:
        data = xmlrpc.client.Binary(handle.read())
        handle.close()
        result = proxy.image_upload(data, date, host_id)

def user_menu():
    # Client menu program
    print("1. Rotate Image")
    print("2. Blur Image")
    print("3. Convert image to grayscale")
    print("4. Convert image to binary")
    print("5. Download the image file")
    print("6. Remove image")
    print("7. Exit")

    return input("Choose menu : ")


# Change the ip address port location in the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

# Get computer client hostname and date
host_id = str(socket.gethostname())
date = str(datetime.datetime.now().date())

# Main client program
choice = 0
title_bar(host_id)
load_images()

while(choice != '6'):
    choice = user_menu()
    # Respond user choice
    if (choice == '1'):
        title_bar(host_id)
        degree = int(input("Please input your angle in degree : "))
        # Run image rotation function in server
        try:
            proxy.imrotate(date, host_id, degree)
            print("Image rotation success!")
        except:
            # Catch if image failed to rotate
            print("Image rotation failed!")
    elif (choice == '2'):
        title_bar(host_id)
        kernel = int(input("Please input the blur intensity : "))
        # Run image blur function in server
        try:
            proxy.imblur(date, host_id, kernel)
            print("Image successfully blurred!")
        except:
            # Catch if image blur function is failed
            print("Image blurring is failed!")
    elif (choice == '3'):
        title_bar(host_id)
        # Convert image from rgb to grayscale in server
        try:
            proxy.im2gray(date, host_id)
            print("Color successfully convert in grayscale!")
        except:
            # Catch if color conversion is failed
            print("Color conversion is failed!")
    elif (choice == '4'):
        title_bar(host_id)
        # Convert image from rgb to binary image in server
        try:
            proxy.imthresh(date, host_id)
            print("Image successfully convert in binary!")
        except:
            # Catch if convert image to binary is failed
            print("Convert image to binary failed!")
    elif (choice == '5'):
        title_bar(host_id)
        # Download image from server
        new_filename = input("Please write the new image filename (include file extensions) : ")
        try:
            handle = open(new_filename, "wb")
            handle.write(proxy.image_download(date, host_id).data)
            handle.close()
            print("Image successfully downloaded!")
        except:
            # Catch if download function is failed
            print("Image download failed!")
    elif (choice == '6'):
        # Delete files in server-side
        proxy.remove_files(date, host_id)
    elif (choice == '7'):
        title_bar(host_id)
        print("Thank you for using this application")
        # Delete files after client exit the program
        proxy.remove_files(date, host_id)