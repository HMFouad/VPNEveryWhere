import Tkinter as tk
from Tkinter import *
import tkFileDialog
from socket import *
import os
from Scan import *
from CreateFileConfig import *

TITLE_FONT = ("Helvetica", 18, "bold")
color="red" # Cercle color = red
ConfigFilePath=""
port1 = 0
NbThread = 0

"""def rec_port():

    port = scanSocket("fdn.fr",port1)
    return port
port = rec_port()"""

class VPN_GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Principal_Frame, PageOne, PageTwo, PageThree, PageFour):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Principal_Frame")

    def drawcircle(self,Frame4,x,y,rad,color):
        canvas = tk.Canvas(Frame4, width=580, height=140)
        canvas.pack(expand="yes", fill="both")
        canvas.create_oval(x-rad,y-rad,x+rad,y+rad, width=0,fill=color)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def Open(self):         #to select confiration file
        fo = open ("FileConfigEmplacement.txt", "w")
        original = tkFileDialog.askopenfilename(filetypes = [("All", "*"),("Configuration file","*.cube;*.txt")])
        fo.write(os.path.split(original)[0]);
        ConfigFilePath=(os.path.split(original)[0])+("/")+(os.path.basename(original))
        fo.write("/");
        fo.write(os.path.basename(original));
        fo.close()
        print(ConfigFilePath)
        """choose_filepath(ConfigFilePath, port)"""
        return ConfigFilePath
    
    def connect(self):
        #chemin = VPN_GUI.Open(self,ConfigFilePath)
        chemin = 'ConfigFile.ovpn'  #Name of fileCofig in the workspace
        lanch(chemin)
        color="green"
        
        """Principal_Frame.afterVoyant(color)"""
        
        
    
class Principal_Frame(tk.Frame):
    port= 0

   
    def __init__(self, parent, controller):

        def Voyant(color):
            Frame4 = tk.Frame(self, borderwidth=2, relief="groove")
            Frame4.pack(padx=10, pady=10)

            circ = controller.drawcircle(Frame4,290,70,60,color)

            
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="VPN EveryWhere", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        Frame0 = tk.Frame(self, borderwidth=2, relief="groove")
        Frame0.pack(side="top", padx=20, pady=20)

        
       
        """--------------------------------------Scan----------------------------------------------------------------"""
        bouton_Connect = tk.Button(Frame0, text="Connect", borderwidth=2,width=15,height=2, command= lambda: controller.connect())
        bouton_Connect.pack(side="left", padx=50, pady=10)
        # port = scanSocket("fdn.fr",port1)

        """--------------------------------------FileConfig----------------------------------------------------------------"""




        """-------------------------------------------------------------------------------------------------------"""
        bouton_Config = tk.Button(Frame0, text="Config", borderwidth=2,width=15,height=2,
                                  command=lambda: controller.show_frame("PageOne"))
        bouton_Config.pack(side="left", padx=20, pady=30)


        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        """button1.pack()
        button2.pack()"""

        Frame2 = tk.Frame(self, borderwidth=2, relief="groove")
        Frame2.pack(side="top", padx=20, pady=20)     

        Frame3 = tk.Frame(Frame2, borderwidth=2, relief="groove")
        Frame3.pack(side="top", padx=0, pady=0)

        Frame31 = tk.Frame(Frame3, borderwidth=2, relief="groove")
        Frame31.pack(side="top", padx=10, pady=10)

        champ_label = tk.Label(Frame31, text="Niveau 0 :   ")
        champ_label.pack(side="left")
        bouton_Detail0 = tk.Button(Frame31, text="Detail")
        bouton_Detail0["command"] = lambda :controller.show_frame("PageFour")
        bouton_Detail0.pack(side="right")

        Frame32 = tk.Frame(Frame3, borderwidth=2, relief="groove")
        Frame32.pack(side="top", padx=10, pady=10)

        champ_label = tk.Label(Frame32, text="Niveau 1 :   ")
        champ_label.pack(side="left")
        bouton_Detail1 = tk.Button(Frame32, text="Detail")
        bouton_Detail1["command"] = lambda :controller.show_frame("PageFour")
        bouton_Detail1.pack(side="right")

        Frame33 = tk.Frame(Frame3, borderwidth=2, relief="groove")
        Frame33.pack(side="top", padx=10, pady=10)

        champ_label = tk.Label(Frame33, text="Niveau 2 :   ")
        champ_label.pack(side="left")
        bouton_Detail2 = tk.Button(Frame33, text="Detail")
        bouton_Detail2["command"] = lambda :controller.show_frame("PageFour")
        bouton_Detail2.pack(side="right")

        Voyant(color)
       

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #title("Config")
        #self.geometry("300x300+500+300")
        label = tk.Label(self, text="Config", font=TITLE_FONT)
        label.pack(side="top", padx=30, pady=30)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Principal_Frame"))
        button.pack(padx=30, pady=30)

        Frame0 = tk.Frame(self, borderwidth=2, relief="groove")
        Frame0.pack(padx=10, pady=10)

        Frame21 = tk.Frame(Frame0, borderwidth=2, relief="groove")
        Frame21.pack(side="top", padx=20, pady=20)
        champ_label = tk.Label(Frame21, text="Nombre de threads :   ")
        champ_label.pack(side="left")
        s = Spinbox(Frame21, from_=1, to=50)
        s.pack(side="left")
        bouton_OK = tk.Button(Frame21, text="OK")
        """bouton_OK["command"] = lambda :NbThread=s.get()"""
        bouton_OK.pack(side="left")

        def getLogin():
            Log=EntryLogin.get()
            Pass=EntryPassword.get()
            print EntryLogin.get()
            print EntryPassword.get()
            
            #chemin = controller.Open(ConfigFilePath)
            chemin = 'ConfigFile.ovpn'
            ChangeLogin(chemin,Log,Pass)


        Frame02 = tk.Frame(Frame0, borderwidth=2, relief="groove")
        Frame02.pack(side="left", padx=10, pady=10)

        Label_Login = tk.Label(Frame02, text="Config Login  ", font=TITLE_FONT)
        Label_Login.pack(side="top")

        Label_Login = tk.Label(Frame02, text="Login       :    ")
        Label_Login.pack(side="top")
        EntryLogin = tk.Entry(Frame02, width=20)
        EntryLogin.pack()

        Label_Password = tk.Label(Frame02, text="Password :    ")
        Label_Password.pack(side="top")

        EntryPassword = tk.Entry(Frame02, show="*", width=20)
        EntryPassword.pack()

        chemin = 'ConfigFile.ovpn'

        bouton_Ok = tk.Button(Frame02, text="OK")
        bouton_Ok["command"] = lambda: getLogin()
        bouton_Ok.pack(side="top", padx=20, pady=30)


        Frame03 = tk.Frame(Frame0, borderwidth=2, relief="groove")
        Frame03.pack(side="left", padx=10, pady=10)

        Label_Server = tk.Label(Frame03, text="Config Server  ", font=TITLE_FONT)
        Label_Server.pack(side="top")

        bouton_ConfigFile = tk.Button(Frame03, text="OpenConfigFile", borderwidth=2,width=15,height=2)
        bouton_ConfigFile["command"] = lambda: controller.Open()
        bouton_ConfigFile.pack(side="top", padx=30, pady=10)

        bouton_Server = tk.Button(Frame03, text="Config Server", borderwidth=2,width=15,height=2,
                                  command=lambda: controller.show_frame("PageThree"))
        bouton_Server.pack(side="top", padx=20, pady=30)




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Config File", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Principal_Frame"))
        button.pack()

        ConfigFile = tk.Entry(self, width=50)
        ConfigFile.pack(padx=30, pady=30)


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Server", font=TITLE_FONT)
        label.pack(side="top", padx=30, pady=30)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Principal_Frame"))
        button.pack(padx=30, pady=30)

        Frame0 = tk.Frame(self, borderwidth=2, relief="groove")
        Frame0.pack(side="top", padx=10, pady=10)

        Frame1 = tk.Frame(Frame0, borderwidth=2, relief="groove")
        Frame1.pack(side="top", padx=10, pady=10)

        Label_ServerName = tk.Label(Frame1, text="ServerName       :    ")
        Label_ServerName.pack(side="left")
        EntryServerName = tk.Entry(Frame1, width=20)
        EntryServerName.pack(side="left")

        def getServer():
            ip=EntryServerName.get()
            print EntryServerName.get()
            #chemin = controller.Open(ConfigFilePath)
            chemin = 'ConfigFile.ovpn'
            ChangeServer(chemin,ip)

        def getCertificat():
            Cert=Certificat.get(1.0, END)
            print Certificat.get(1.0, END)
            chemin = 'ConfigFile.ovpn'
            ChangeCertificat(chemin,Cert)
        
        bouton_AddServer = tk.Button(Frame1, text="Add Server")
        bouton_AddServer["command"] = lambda: getServer()
        bouton_AddServer.pack(side="left")

        Frame2 = tk.Frame(Frame0, borderwidth=0, relief="groove")
        Frame2.pack(side="top", padx=10, pady=10)
        
        Label_Certificat = tk.Label(Frame2, text="Certificat :    ")
        Label_Certificat.pack(side="left")

        chemin='ConfigFile.ovpn'
        
        bouton_parcourir = tk.Button(Frame2, text="Import")
        bouton_parcourir["command"] = lambda: ImportCertificat(controller.Open())
        bouton_parcourir.pack(side="left")

        Frame21 = tk.Frame(Frame0, borderwidth=0, relief="groove")
        Frame21.pack(side="top", padx=10, pady=10)
        Certificat = tk.Text(Frame21, width="30", height="15")
        """text.insert(END,"")"""
        Certificat.pack(side="top")
        
    

        bouton_AddCertificat = tk.Button(Frame0, text="Add Certificat", width="20")
        bouton_AddCertificat["command"] = lambda: getCertificat()
        bouton_AddCertificat.pack(side="bottom")

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Principal_Frame"))
        button.pack()

        text = tk.Text(self)
        text.insert(END,"Scan detail")
        text.pack()


if __name__ == "__main__":
    app = VPN_GUI()
    app.title("VPNEveryWhere")
    app.mainloop()
