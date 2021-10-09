import os
desktop = os.path.join(os.path.expanduser('~'),'Desktop') or os.environ['USERPROFILE']
os.chdir(desktop)
print("The video will be saved on the Desktop.\nCreate a folder on the desktop'n")
folder = str(input("Name of the folder to be created: \n"))
adr = str(input("Paste the link address of the youtube video you want to download: \n"))
os.system('sudo pip3 install youtube-dl') or os.system('pip install youtube-dl')
try:
    os.mkdir(folder)
    location = os.path.join(desktop,folder)
    os.chdir(location)
    print(os.getcwd())
    os.system('youtube-dl ' + adr)
except FileExistsError:
    location = os.path.join(desktop,folder)
    os.chdir(location)
    print(os.getcwd())
    os.system('youtube-dl ' + adr)


