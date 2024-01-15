######################
### Modulos a Usar ###
######################
##Para la ventana
import tkinter as tk 
from tkinter import ttk
from PIL import Image, ImageTk

##Para validaciones
import re

##Para DataFrame
import pandas as pd

##Para guardar datos en firebase
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("app-1-tkinter-3748e-587c25ce8bc6.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

##Para guardar datos en el excel de drive
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = 'python-sheet-tesel-408702-fd8b27b9ef62.json'
SPREADSHEET_ID = '1BLicKmushOSY6XFjbhykXtDb7xyN0gS3nK6jcEII6Ew'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

##############################
### Creacion de la Ventana ###
##############################
root=tk.Tk()
root.geometry("800x500+20+20")
root.resizable(False, False)
root.title("Subir Datos Prueba 1")

#######################
### IMAGEN DE FONDO ###
#######################
##Creacion del Canva
canvas1 = tk.Canvas(root, width=800, height=500)
canvas1.pack(fill="both", expand=True)

##Imagen de Fondo
def resize_image(image_path, width, height):
  original_image = Image.open(image_path)
  resized_image = original_image.resize((width, height))
  return ImageTk.PhotoImage(resized_image)

resized_bg = resize_image("IMFONDO1.jpg", 800,500)
canvas1.create_image(0, 0, image=resized_bg, anchor=tk.NW)

#######################################
### INSERTAR LABELS, ENTRY, BUTTONS ###
#######################################
valor_0, valor_1 = 40, 140
LG, A = 30, 420

ID_label=tk.Label(root,
                  text="ID",
                  width=10,
                  height=1,
                  #bd=1.5,
                  font=("Arial",20),
                  #relief="solid",
                  bg="#F50743"
                )
ID_label_1=canvas1.create_window(valor_0,valor_1,anchor=tk.NW,
                                 window=ID_label)
ID=tk.Entry(root,
            textvar=tk.StringVar(),
            width=LG,
            #height=1,
            #bd=1.5,
            font=("Arial",20)
            )
entry1_ID=canvas1.create_window(valor_0+A,valor_1+(2*10),anchor=tk.CENTER, 
                                 window=ID)

def BorrarID(): ID.delete(0,tk.END)
Button_ID=tk.Button(canvas1,
                    text="B",
                    width=4,
                    height=1,
                    font=("Arial",11),
                    command=BorrarID
                    )
Button_ID_1=canvas1.create_window(valor_0+(1.7*A), valor_1+(LG//6), 
                                anchor=tk.NE,
                                window=Button_ID )


valor_1+=50
Ap_label=tk.Label(root,
                  text="Apellido",
                  width=10,
                  height=1,
                  #bd=1.5,
                  font=("Arial",20),
                  #relief="solid",
                  bg="#F50743"
                  )
Ap_label_1=canvas1.create_window(valor_0,valor_1,anchor=tk.NW,
                                 window=Ap_label)
Ap=tk.Entry(root,
            textvar=tk.StringVar(),
            width=LG,
            #height=1,
            #bd=1.5,
            font=("Arial",20)
            )
entry1_Ap=canvas1.create_window(valor_0+A,valor_1+(2*10),anchor=tk.CENTER, 
                                 window=Ap)

def BorrarAp(): Ap.delete(0,tk.END)
Button_Ap=tk.Button(canvas1,
                    text="B",
                    width=4,
                    height=1,
                    font=("Arial",11),
                    command=BorrarAp
                    )
Button_Ap_1=canvas1.create_window(valor_0+(1.7*A), valor_1+(LG//6), 
                                anchor=tk.NE,
                                window=Button_Ap )

valor_1+=50
Nombre_label=tk.Label(root,
                  text="Nombre",
                  width=10,
                  height=1,
                  #bd=1.5,
                  font=("Arial",20),
                  #relief="solid",
                  bg="#F50743"
                  )
Nombre_label_1=canvas1.create_window(valor_0,valor_1,anchor=tk.NW,
                                 window=Nombre_label)
Name=tk.Entry(root,
            textvar=tk.StringVar(),
            width=LG,
            #height=1,
            #bd=1.5,
            font=("Arial",20)
            )
entry1_Name=canvas1.create_window(valor_0+A,valor_1+(2*10),anchor=tk.CENTER, 
                                 window=Name)
def BorrarName(): Name.delete(0,tk.END)
Button_Name=tk.Button(canvas1,
                    text="B",
                    width=4,
                    height=1,
                    font=("Arial",11),
                    command=BorrarName
                    )
Button_Name_1=canvas1.create_window(valor_0+(1.7*A), valor_1+(LG//6), 
                                anchor=tk.NE,
                                window=Button_Name )

valor_1+=50
Materia_label=tk.Label(root,
                  text="Materia",
                  width=10,
                  height=1,
                  #bd=1.5,
                  font=("Arial",20),
                  #relief="solid",
                  bg="#F50743"
                  )
Materia_label_1=canvas1.create_window(valor_0,valor_1,anchor=tk.NW,
                                 window=Materia_label)
Mat=tk.Entry(root,
            textvar=tk.StringVar(),
            width=LG,
            #height=1,
            #bd=1.5,
            font=("Arial",20)
            )
entry1_Mat=canvas1.create_window(valor_0+A,valor_1+(2*10),anchor=tk.CENTER, 
                                 window=Mat)
def BorrarMat(): Mat.delete(0,tk.END)
Button_Mat=tk.Button(canvas1,
                    text="B",
                    width=4,
                    height=1,
                    font=("Arial",11),
                    command=BorrarMat
                    )
Button_Mat_1=canvas1.create_window(valor_0+(1.7*A), valor_1+(LG//6), 
                                anchor=tk.NE,
                                window=Button_Mat )

##################################
### Botones para guardar datos ###
##################################
def AbrirDatos():
  data=[]
  docs=db.collection("Prueba 1 Parte 1").stream()
  for doc in docs:
    data.append(doc.to_dict())
  return pd.DataFrame(data)

def Advertencia():
   ventana1=tk.Toplevel(root)
   ventana1.geometry("200x100")
   ventana1.resizable(False, False)
   ventana1.title("Datos Ingresados Invalidos")
   
   etiqueta=tk.Label(ventana1, text="Cheque los datos ingresados")
   etiqueta.pack(padx=20, pady=20)
   
   ventana1.after(3000, ventana1.destroy) #3000 milisegundos (3 segundos)
   ventana1.focus()
   
def REGISTRADO():
   ventana1=tk.Toplevel(root)
   ventana1.geometry("200x100")
   ventana1.resizable(False, False)
   ventana1.title("Datos Ingresado")
   
   etiqueta=tk.Label(ventana1, text="Dato Ingresado en el sistema")
   etiqueta.pack(padx=20, pady=20)
   
   ventana1.after(3000, ventana1.destroy) #3000 milisegundos (3 segundos)
   ventana1.focus()

#def funcion_boton1():
#    print("Botón 1 presionado")

def mostrar_datos():
    ventana=tk.Toplevel(root)
    ventana.geometry("500x500")
    ventana.resizable(False, False)
    ventana.title("Datos")

    mostrar=ttk.Treeview(ventana)
    mostrar["columns"]=("ID","Apellido","Nombre","Materia")
    mostrar.column("#0", width=0, stretch=tk.NO)
    mostrar.column("ID", anchor=tk.W, width=100)
    mostrar.column("Apellido", anchor=tk.W, width=100)
    mostrar.column("Nombre", anchor=tk.W, width=100)
    mostrar.column("Materia", anchor=tk.W, width=100)
    
    mostrar.heading("#0",text="",anchor=tk.W)
    mostrar.heading("ID",text="ID",anchor=tk.W)
    mostrar.heading("Apellido",text="Apellido",anchor=tk.W)
    mostrar.heading("Nombre",text="Nombre",anchor=tk.W)
    mostrar.heading("Materia",text="Materia",anchor=tk.W)
    
    Bd = AbrirDatos()
    for j, (iD, appe, nam, subj) in enumerate(zip(Bd["ID"], Bd["Apellido"], Bd["Nombre"], Bd["Materia"])):
        mostrar.insert("", j, values=(iD, appe, nam, subj))
    
    mostrar.pack(padx=20, pady=20)
    
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)
#    boton1 = tk.Button(frame_botones, 
#                       text="Eliminar", 
#                       font=("Arial", 20), 
#                       command=funcion_boton1)
#    boton1.pack(side=tk.LEFT, padx=10, pady=10)

    boton2 = tk.Button(frame_botones, 
                       text="Volver", 
                       font=("Arial", 20), 
                       command=ventana.destroy)
    boton2.pack(side=tk.LEFT, padx=10, pady=10)

class User:
  def __init__(self, id,ap,nom,mat):
    self.id=id
    self.ap=ap
    self.nom=nom
    self.mat=mat
  
  def Subir(self):
    pattern_id=r"^[0-9]{8}$"
    pattern_ap_nom=r"^[A-Z À-ÿ]+[á-é a-z]+(?:\s[A-Z À-ÿ]+[á-é a-z]+)*$"
    valor_booleano=re.match(pattern_id,self.id) and re.match(pattern_ap_nom,self.ap) and re.match(pattern_ap_nom, self.nom)
    
    Bd=AbrirDatos()
    if len(self.id)==8 and valor_booleano and self.id not in Bd["ID"]:
      values = [[self.id, self.ap, self.nom,self.mat]]
      sheet.values().append( spreadsheetId=SPREADSHEET_ID,
      range="prueba 1 parte 3!A2", 
      valueInputOption='USER_ENTERED',
      body={'values': values}).execute()
      
      datos_dict = { "ID": self.id, "Apellido": self.ap,
            "Nombre": self.nom, "Materia":self.mat }
      #db.collection("Prueba 1 Parte 1").add(datos_dict)
      db.collection("Prueba 1 Parte 1").document(self.id).set(datos_dict)
      
      ID.delete(0,tk.END)
      Ap.delete(0,tk.END)
      Name.delete(0,tk.END)
      Mat.delete(0,tk.END)

      REGISTRADO()
      
    else:
      ID.delete(0,tk.END)
      Ap.delete(0,tk.END)
      Name.delete(0,tk.END)
      Mat.delete(0,tk.END)
      
      Advertencia()
      
def registro():
  iD=ID.get()
  ape=Ap.get()
  name=Name.get()
  mate=Mat.get()
  
  Persona=User(iD,ape,name,mate)
  Persona.Subir()
      
valor_1+=50
Button_Save=tk.Button(root,
                  text="Guardar",
                  width=10,
                  height=1,
                  #bd=1.5,
                  font=("Arial",20),
                  #relief="solid",
                  #bg="#F50743",
                  command=registro
                  )
Button_Save_1=canvas1.create_window(valor_0+(1*100),valor_1,anchor=tk.NW,
                                 window=Button_Save)

Button_Viz=tk.Button(root,
                  text="Ver Datos",
                  width=10,
                  height=1,
                  #bd=1.5,
                  font=("Arial",20),
                  #relief="solid",
                  #bg="#F50743",
                  command=mostrar_datos
                  )
Button_Viz_1=canvas1.create_window(valor_0+(3*100),valor_1,anchor=tk.NW,
                                 window=Button_Viz)

def LIMPIEZA():
  ID.delete(0, tk.END)
  Ap.delete(0, tk.END)
  Name.delete(0, tk.END)
  Mat.delete(0, tk.END)                           

def deleTe():
    Eliminate=ID.get()
    try:
        db.collection("Prueba 1 Parte 1").document(Eliminate).delete()
        ID.delete(0,tk.END)
    except Exception as e:
        ID.delete(0,tk.END)

Button_Clear=tk.Button(root,
                  text="Eliminar",
                  width=10,
                  height=1,
                  #bd=1.5,
                  font=("Arial",20),
                  #relief="solid",
                  #bg="#F50743",
                  command=deleTe
                  )
Button_Clear_1=canvas1.create_window(valor_0+(5*100),valor_1,anchor=tk.NW,
                                 window=Button_Clear)

root.mainloop()