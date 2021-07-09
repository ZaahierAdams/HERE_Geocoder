'''

Author: Zaahier Adams
https://github.com/ZaahierAdams


UI/ frontend for Curate
(1) GUI created with tkinter framework
(2) Link with backend (Backend.py)


First released: 07/06/2020
last updated:   07/06/2020

'''

import sys
from os import path as ospath 
from webbrowser import open as webBroswerOpen

import Backend 

from tkinter import *
from PIL import ImageTk, Image
from importlib import reload


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = ospath.abspath(".")

    return ospath.join(base_path, relative_path)

def Video_Tut():
    webBroswerOpen('https://youtu.be/hGmhmutrjnU')

def HERE_Website():
    webBroswerOpen('https://developer.here.com/sign-up?create=Freemium-Basic&keepState=true&step=account')
    
def Curate():
    API_key     = Entry_3_1.get()
    input_file  = Entry_3_2.get()
    Backend.Initiate(API_key, input_file)
    reload(Backend)
    
current_version = 'v1.00 (07.06.2020)'
app_name = 'Geocoder'

image_1 = 'Icon_2.ico'
image_2 = 'logos3.png'

root = Tk()
root.geometry("410x700")
root.title(app_name+' '+current_version)
root.resizable(True,True)
root.iconbitmap(resource_path(image_1))

Theme_1 = '#1C1C1C'
Theme_2 = '#60FFE4'
Theme_2_2='#1AFBD0'
#Theme_2 = '#D5A3DE'
#Theme_2_2='#D5A3DE'
Theme_3 = '#000000'
Theme_4 = '#FFFFFF'
Theme_5 = '#D5A3DE'
Theme_6 = '#BEFFFF'

def on_enter_2_1(e):
    Button_2_1['bg'] = Theme_6
def on_enter_2_2(e):
    Button_2_2['bg'] = Theme_6
def on_enter_3_1(e):
    Button_3_1['bg'] = Theme_6
    
def on_leave_2_1(e):
    Button_2_1['bg'] = Theme_2
def on_leave_2_2(e):
    Button_2_2['bg'] = Theme_2    
def on_leave_3_2(e):
    Button_3_1['bg'] = Theme_2
    
font_1 = 'Verdana'
font_2 = 'Helvetica'
font_3 = 'Verdana 16 bold'
font_4 = 'Verdana 16 bold'

font_size_1_1       = 60
font_size_1_2       = 11
#font_size_2_heading = 20
font_size_2_button  = 10
font_size_3_Descrip = 10
font_size_3_entry   = 9
font_size_3_button  = 16

height_label_1_1    = 1
height_label_1_2    = 2
height_label_2      = 1
height_label_3_1    = 2
height_label_3      = 1
height_button_2     = 2
height_button_3     = 1
height_entry_3      = 1
height_entry_3_5    = 2

height_empty_1      = 1
height_empty_2      = 1
height_empty_3_1    = 1
height_empty_3_2    = 2

width_label_1_1     = 10
width_label_1_2     = 100
width_label_2       = 10
width_label_3       = 100
width_button_2      = 30
width_button_3      = 16
width_entry_3       = 42

borderWidth_entry   = 0
borderWidth_button  = 0

text_label_1_1 = app_name+''
text_label_1_2 = 'Validates and Geocodes Addresses'
text_label_2_1 = '( Step 1 )'
text_label_2_2 = '( Step 2 )'
text_label_3_1 = 'HERE API key:'
text_label_3_2 = 'File Name:'
text_label_3_4 = 'Powered by:'
text_label_3_5 = ('Developed: Zaahier Adams (https://github.com/ZaahierAdams)'
                  + '\nDisclaimer: I am not affiliated or in any way officially connected with HERE')

text_button_2_1 = 'Watch this video tutorial'
text_button_2_2 = 'Create a HERE account\nand get an API key'
text_button_3_1 = 'Geocode now!'

root.configure(background= Theme_1)
Frame_1 = Frame(root, bg = Theme_1)             
Frame_2 = Frame(root, bg = Theme_2)
Frame_3 = Frame(root, bg = Theme_1)

Label_1_1 = Label(Frame_1, 
                  
                  width     = width_label_1_1, 
                  height    = height_label_1_1, 
                  
                  bg        = Theme_1, 
                  fg        = Theme_2_2, 
                  
                  text      = text_label_1_1, 
                  font      = (font_1, font_size_1_1), 
                  
                  anchor    = S
                  )

Label_1_2 = Label(Frame_1, 
                  
                  width     = width_label_1_2, 
                  height    = height_label_1_2, 
                  
                  bg        = Theme_1, 
                  fg        = Theme_4, 
                  
                  text      = text_label_1_2, 
                  font      = (font_2, font_size_1_2), 
                  
                  anchor    = N
                  )

Label_2_1 = Label(Frame_2, 
                  
                  width     = width_label_2, 
                  height    = height_label_2, 
                  
                  bg        = Theme_2, 
                  fg        = Theme_3, 
                  
                  text      = text_label_2_1, 
                  font      = font_3, 
                  
                  anchor    = CENTER
                  )

Label_2_2 = Label(Frame_2, 
                  
                  width     = width_label_2, 
                  height    = height_label_2,
                  
                  bg        = Theme_2, 
                  fg        = Theme_3,  
                  
                  text      = text_label_2_2, 
                  font      = font_3, 
                  
                  anchor    = CENTER
                  )

Label_3_1 = Label(Frame_3, 
                  
                  width     = width_label_3, 
                  height    = height_label_3_1,
                  
                  bg        = Theme_1, 
                  fg        = Theme_4, 
                  
                  text      = text_label_3_1, 
                  font      = (font_2, font_size_3_Descrip), 
                  
                  anchor    = S
                  )

Label_3_2 = Label(Frame_3, 
                  
                  width     = width_label_3, 
                  height    = height_label_3, 
                  
                  bg        = Theme_1, 
                  fg        = Theme_4, 
                  
                  text      = text_label_3_2, 
                  font      = (font_2, font_size_3_Descrip), 
                  
                  anchor    = S
                  )

Label_3_4 = Label(Frame_3, 
                  
                  width     = width_label_3, 
                  height    = height_label_3,
                  
                  bg        = Theme_1, 
                  fg        = Theme_3, 
                  
                  text      = text_label_3_4, 
                  font      = (font_2, 8), 
                  
                  anchor    = S
                  )

Label_3_5 = Label(Frame_3, 
                  
                  width     = width_label_3, 
                  height    = height_entry_3_5,
                  
                  bg        = Theme_1, 
                  fg        = Theme_4, 
                  
                  text      = text_label_3_5, 
                  font      = (font_2, 8), 
                  
                  anchor    = S
                  )

Label_empty_1 = Label(Frame_1, 
                  
                  width     = width_label_3, 
                  height    = height_empty_1,
                  
                  bg        = Theme_1, 
                  )

Label_empty_2_1 = Label(Frame_2, 
                  
                  width     = width_label_3, 
                  height    = height_empty_2,
                  
                  bg        = Theme_2, 
                  )

Label_empty_2_2 = Label(Frame_2, 
                  
                  width     = width_label_3, 
                  height    = height_empty_2,
                  
                  bg        = Theme_2, 
                  )

Label_empty_3_1 = Label(Frame_3, 
                  
                  width     = width_label_3, 
                  height    = height_empty_3_1,
                  
                  bg        = Theme_1, 
                  )

Label_empty_3_2 = Label(Frame_3, 
                  
                  width     = width_label_3, 
                  height    = height_empty_3_2,
                  
                  bg        = Theme_1, 
                  )


Button_2_1 = Button(Frame_2, 
                    
                    width   = width_button_2, 
                    height  = height_button_2, 
                    
                    bg      = Theme_2, 
                    fg      = Theme_3, 
                    
                    text    = text_button_2_1, 
                    font    = (font_2, font_size_2_button), 
                    
                    anchor    = N,
                                       
                    borderwidth = borderWidth_button , 
                    command = Video_Tut )

Button_2_2 = Button(Frame_2, 
                    
                    width   = width_button_2, 
                    height  = height_button_2, 
                    
                    bg      = Theme_2, 
                    fg      = Theme_3, 
                    
                    text    = text_button_2_2, 
                    font    = (font_2, font_size_2_button), 
                    
                    anchor    = N,
                                       
                    borderwidth = borderWidth_button,
                    
                    command = HERE_Website )

Button_3_1 = Button(Frame_3, 
                    
                    width   = width_button_3, 
                    height  = height_button_3, 
                    
                    bg      = Theme_2, 
                    fg      = Theme_3, 
                    
                    text    = text_button_3_1, 
                    font    = font_4, 
                                       
                    borderwidth = borderWidth_button ,
                    
                    command = lambda: Curate() )

Entry_3_1 = Entry(Frame_3,
                  
                  width     = width_entry_3, 
                    
                  bg        = Theme_4, 
                  fg        = Theme_3, 
                  
                  font      = (font_1, font_size_3_entry ),
                  justify   = CENTER,
                  
                  bd        = borderWidth_entry
                  )

Entry_3_2 = Entry(Frame_3,
                  
                  width     = width_entry_3, 
                    
                  bg        = Theme_4, 
                  fg        = Theme_3, 
                  
                  font      = (font_1, font_size_3_entry ),
                  justify   = CENTER,
                  
                  bd        = borderWidth_entry
                  )

Canvas_3 = Canvas(Frame_3, 
                
                  width     = 200, 
                  height    = 80, 
                
                  bg        = Theme_1,
                  
                  bd        = 0,
                  highlightthickness=0
                  )

image_location1 = resource_path(image_2)
image1 = ImageTk.PhotoImage(Image.open(image_location1))
Canvas_3.create_image(100, 80, anchor = S, image=image1)

Text_3 = Text(Frame_3, 
              
              width     = 100, 
              height    = 3, 
              
               bg       = Theme_1, 
               fg       = Theme_4, 
               
               font     = (font_2, 8),  
               
               bd       = 0, 
               highlightthickness=0, 
               
               padx     = 0, 
               pady     = 0,
               
               wrap = CHAR
               )
Text_3.insert(INSERT, '\n'+text_label_3_5)
Text_3.insert(END,"")
Text_3.tag_configure("center", justify='center')
Text_3.tag_add("center", 1.0, "end")
Text_3.configure(state="disabled")


Button_2_1.bind("<Enter>", on_enter_2_1)
Button_2_1.bind("<Leave>", on_leave_2_1)
Button_2_2.bind("<Enter>", on_enter_2_2)
Button_2_2.bind("<Leave>", on_leave_2_2)
Button_3_1.bind("<Enter>", on_enter_3_1)
Button_3_1.bind("<Leave>", on_leave_3_2)

Label_empty_1.pack()
Label_1_1.pack()
Label_1_2.pack()

Label_empty_2_1.pack()
Label_2_1.pack()
Button_2_1.pack()
Label_2_2.pack()
Button_2_2.pack()
Label_empty_2_2.pack()

Label_3_1.pack()
Entry_3_1.pack()
Label_3_2.pack()
Entry_3_2.pack()
Label_empty_3_1.pack()
Button_3_1.pack()
Label_empty_3_2.pack()
Label_3_4.pack()
Canvas_3.pack()#side = RIGHT)
#Label_3_5.pack()
Text_3.pack()

Frame_1.pack(fill=X)
Frame_2.pack(fill=X)
Frame_3.pack(fill=X)            

root.mainloop()