#
#This program is a simple sort program just made with the intent of making life a bit easier for people with messy desktops mainly.
#This program can also be used for other files than the desktop.
#

from datetime import datetime 
from mimetypes import guess_type
import shutil
from glob import glob
from os import getcwd, makedirs, path, chdir
from sys import exit
from tkinter import filedialog, Button, Tk, Label, messagebox, ttk, Listbox, Scrollbar

#abspath = path.abspath("PySort.py")
#dname = path.dirname(abspath)

Executables = []
Audios = []
Videos = []
Images = []
Docs = []
HTML = []
Compress = []
Text = []
PyScripts = []
Nokia = []
Torrent = []
ISO = []
Short = []
Un = []
mainlist = [Executables,Audios,Videos,Images,Docs,HTML,Compress,Text,PyScripts,Nokia,Torrent,ISO,Short,Un]
mainlistn = ["Executables moved:\n","Audio files moved:\n","Videos moved:\n","Images moved:\n","Documents moved:\n","Webpages moved:\n","Compressed files moved:\n","Text files moved:\n","Python scripts moved:\n","Nokia files moved:\n","Torrent files moved:\n","ISO files moved:\n","Shortcuts moved:\n","Unknown files moved:\n"]
Errors = []


#===========================================MAIN CLASSES=====================================================


class Create():
    def __init__(self, obj, filename):
        try:
            makedirs(str(filename))
        except OSError:
            pass
        try:
            shutil.move(obj, str(filename))
        except (shutil.Error, WindowsError):
            Errors.append(str(obj))
            pass
class fors:
    def __init__(self, vari, globstr, foldern, tlist):
        for vari in glob(globstr):
            Create(vari, foldern)
            tlist.append(vari)


#===========================================MAIN OPERATION===================================================


def identify():
    for mn in glob('*'):
        m = guess_type(mn, strict=True)
        isdir = path.isdir(mn)
        new = (str(m))
    
#Executables
        if new == "('application/octet-stream', None)" or glob(mn) == glob("*.msi"):
            Create(mn, "Executables")
            Executables.append(mn)

#Videos
        elif new == "('video/x-msvideo', None)" or new == "('video/mp4', None)" or glob(mn) == glob('*.webm') or glob(mn) == glob('*.flv'):
            Create(mn, "Video")
            Videos.append(mn)
            
#Images
        elif new == "('image/x-png', None)" or new == "('image/pjpeg', None)" or new == "('image/gif', None)" or new == "('image/jpeg', None)":
            Create(mn, "Images")
            Images.append(mn)

#Audio Basic
        elif new == "('audio/x-mpg', None)" or new == "('audio/x-wav', None)" or new == "('audio/x-ms-wma', None)" or new == "('midi/mid', None)":
            Create(mn, "Audio")
            Audios.append(mn)

#Documents
        elif new == "('application/vnd.openxmlformats-officedocument.wordprocessingml.document', None)" or new == "('application/x-msexcel', None)" or new == "('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', None)" or new == "('application/x-mspowerpoint', None)" or new == "('application/x-mspowerpoint.12', None)" or new == "('application/msword', None)" or new == "('application/pdf', None)":
            Create(mn, "Documents")
            Docs.append(mn)

#Web Pages
        elif new == "('text/html', None)":
            Create(mn, "Web Pages")
            HTML.append(mn)

#Compressed
        elif new == "('application/x-tar', 'gzip')" or new == "('application/zip', None)" or glob(mn) == glob('*.rar') or glob(mn) == glob('*.7z'):
            Create(mn, "Compressed")
            Compress.append(mn)

#Text
        elif new == "('text/plain', None)":
            Create(mn, "Text")
            Text.append(mn)

#Python Scripts :)
        elif new == "('text/x-python', None)":
            if mn == "PySort.py":
                pass
            else:
                Create(mn, "Python Scripts")
                PyScripts.append(mn)
			
#Torrent files, you naughty dog :P
        elif new == "('application/x-bittorrent', None)":
            Create(mn, "Bit Torrent")
            Torrent.append(mn)

#Shortcuts
    for j in glob('*.lnk'):
        if j == "PySort.lnk":
            pass
        else:
            Create(j, "Shortcuts")
            Short.append(j)

#Audio advanced
    fors("Audio", "*.flac", "Audio", Audios)
    #fors("Audio", "*.FLAC", "Audio", Audios)
    
#Nokia files
    fors("nok1", "*.sis", "Nokia Apps", Nokia)
    fors("nok2", "*.sisx", "Nokia Apps", Nokia)

#Disk Images
    #fors("iso", "*.iso", "Disk Images", ISO)
    fors("iso1", "*.ISO", "Disk Images", ISO)
    #fors("iso2", "*.img", "Disk Images", ISO)
    fors("iso3", "*.IMG", "Disk Images", ISO)
    #fors("iso4", "*.nrg", "Disk Images", ISO)
    fors("iso5", "*.NRG", "Disk Images", ISO)
    #fors("iso6", "*.mds", "Disk Images", ISO)
    fors("iso7", "*.MDS", "Disk Images", ISO)
    #fors("iso8", "*.mdf", "Disk Images", ISO)
    fors("iso9", "*.MDF", "Disk Images", ISO)
    #fors("iso10", "*.cdi", "Disk Images", ISO)
    fors("iso11", "*.CDI", "Disk Images", ISO)
    #fors("iso12", "*.dvd", "Disk Images", ISO)
    fors("iso13", "*.DVD", "Disk Images", ISO)
    #fors("iso14", "*.ima", "Disk Images", ISO)
    fors("iso15", "*.IMA", "Disk Images", ISO)
    

#Unknown
    for u in glob("*"):
        mime = guess_type(u)
        isdir = path.isdir(u)
        if str(mime) == "(None, None)" and isdir == False and u not in Errors:
            Create(u, "Unknown")
            Un.append(u)

    if len(Errors) > 0:
        messagebox.showinfo("ERRORS OCCURED!", (str(len(Errors)))+" file(s) were not moved.") #file(s) were not moved because they are already in the destination folders:\n"+'\n'.join(Errors))
    return("Complete!")




#===========================================GUI==============================================================


root = Tk()                                 #Create the root windows.
root.title("PSFW 0.5b")                     #Names the title of the window.
root.geometry("400x370")                    #Sets the size of the windows you've chosen.
root.resizable(0,0)                         #This, in my case, sets the windows to non-resizable.
root.wm_iconbitmap('Folder-Options.ico')    #This changes the icon of the GUI window.
lab = Label(root, text = "Welcome to PySort! An application from a lazy guy to all lazy people!\nYou are currently in: %s" %str(getcwd()))
#^ This creates a label on the main windows(root) which just prints text.) ^
lab.pack()                                  #The pack feature needs to be used on any object created on the root windows. This is to tell pyhton to place the object on the screen.

def prints(inpt):
    n = 0
    count = 0
    for lists in mainlist:
        if len(lists) == 0:
            count += 1
        elif len(lists) > 0:
            b = ''
            for i in lists:
                if i in Errors:
                    pass
                else:
                    i = i+'\n '
                    b += i
            inpt.write(mainlistn[count]+" "+b)
            #print(mainlistn[count]+" "+b)
            n += 1
            count += 1
   
def butt():
    listbox.delete(1, "end")
    newdir = filedialog.askdirectory() #This  is a method in filedialog(class in tkinter) that makes a folder selection screen.
    if newdir == "":
        pass
    else:
        b = newdir[0]
        notallowed = "C:/Windows/"
        try:
            if newdir == (b+":/Windows/") or newdir[3:9] == notallowed[3:9]:
                messagebox.showerror("PySort", "Do not select that directory!") #Messagebox prints a popup message on the screen, depending on the method (in this case, showerror.)
            else:
                chdir(newdir)
                lab.config(text = "Welcome to PySort! An application from a lazy guy to all lazy people!\nYou are currently in: %s" %str(getcwd()))
                #^The config method changes the properties of an object.
        except WindowsError:
            pass

def clear():
    del Errors[:]
    ok()
    
def ok():
    date = datetime.now()
    origdir = str(getcwd())
    listbox.delete(1, "end")
    del (Executables[:],Audios[:],Videos[:],Images[:],Docs[:],HTML[:],Compress[:],Text[:],PyScripts[:],Nokia[:],Torrent[:],ISO[:],Short[:],Un[:])
    mainlist = [Executables,Audios,Videos,Images,Docs,HTML,Compress,Text,PyScripts,Nokia,Torrent,ISO,Short,Un]
    #bar = progress()
    aski = messagebox.askyesno(message='Are you sure you want to sort this folder?', title='Confirmation')
    if aski == True:
        buttonquit.config(state = "disabled")
        #^This messagebox makes a notification, not an error.
        b = identify()
        if b == "Complete!":
#            if len(Errors) > 0:
#                for numa in range(len(Errors)):
#                    listbox.insert((numa+2), Errors[numa])
#            else:
#                listbox.insert(2, "None")
#            chdir(str(dname)+"\\logs")
#            try:
#                datedir = makedirs(str(date)[:10])
#                chdir(str(datedir))
#            except WindowsError:
#                datedir = chdir(str(date)[:10])
#            filename = str(str(date)[11:19]+":.txt")
#            filename = filename.replace(":","h ", 1).replace(":","m ", 1).replace(":","s", 1)
#            logfile = open(filename, "w")
#            #logfile.write("Moved files:\n"+str(prints())+"\n\n"+"Errors:\n"+str(Errors))
#            #logfile.close()
#            prints(logfile)
#            chdir(origdir)
            print(str(date)[11:19])
            messagebox.showinfo("PySort", b)
            buttonquit.config(state = "active")
            
    else:
        pass

def bye():
    root.destroy()
    #^Destroy is used to terminate the window.
    try:
        exit()
    except SystemExit:
        pass

scrollbar = Scrollbar(root, orient='vertical')
listbox = Listbox(root, width = 44, height= 18, yscrollcommand=scrollbar.set)
scrollbar.pack(side='right', fill='y')
scrollbar.config(command=listbox.yview)
listbox.pack()
listbox.place(x=115, y =47)
listbox.insert(1, "===ERRORS - NOT MOVED IN LAST SESSION===")
listbox.insert(2, "Not Run")
#buttonprint = Button(root, text="SAVE TO LOG",borderwidth=3, command = prints)
#buttonprint.pack(side="bottom")
buttonchoose = Button(root, text = "Change Directory", height = 5, width = 14,borderwidth=3, command = butt)
buttonchoose.pack()                 #The pack() feature is used to tell python to place the object on the GUI(window).
buttonchoose.place(y = 48)         #place allows you to put the object where you want on the screen.
buttonok = Button(root, text = "SORT",height = 5,width = 14,borderwidth=3, command = clear)
buttonok.pack()
buttonok.place(y = 148)
buttonquit = Button(root, text = "Exit", height = 5, width = 14,borderwidth=3, command = bye)
buttonquit.pack()
buttonquit.place(y = 250)
root.mainloop()                     #This starts the GUI screen(main window, or windows you've specified).

