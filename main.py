import os
import image

os.system('clear')
menu = 0
print('--------------------------------------')
print('  Big Computational Image Processing  ')
print('--------------------------------------')
print('1. Load Images')
print('2. Basic Function')
print('3. Filter')
print('4. Exit')
print('--------------------------------------')
print('Choose menu : ', end='')
menu = int(input())

if (menu == 1):
    print('Please input the image filename and extensions : ', end='')
    filename = input()
    img = image.read_images(filename)
    image.show_images(img)
    
elif (menu == 2):
    print('Menu 2')
elif (menu == 3):
    print('Menu 3')
else:
    print('Bye.. Bye..')