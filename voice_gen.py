from gtts import gTTS
import customtkinter
import sys
from tkinter import *
#voice generater functions

def escape():
	sys.exit()

def generate():
    tts = gTTS(text.get(),lang='ru')
    t = name.get()
    tts.save(t+'.mp3')



#window and buttons
window = Tk()
window.title('Генерация речи из текста')#title name
window.geometry('900x500')
window.resizable(width=False, height=False)
window['bg'] = '#2d2d2d'
customtkinter.set_appearance_mode('dark')

but = customtkinter.CTkButton(master=window,text='Озвучить',command=generate)
exit_but = customtkinter.CTkButton(master=window,text='Выход',command=escape)
#text input windows
text = customtkinter.CTkEntry(master=window,width=100)
name = customtkinter.CTkTextbox(master=window,width=600)

textlab = customtkinter.CTkLabel(master=window,text='Текст')#what needs to be voiced
namelab = customtkinter.CTkLabel(master=window,text='Название файла')#file name

authorLab = customtkinter.CTkLabel(master=window,text='Автор Илья Околелов')

namelab.place(relx=0.25, 
	          rely=0.05,
	          anchor=CENTER)

textlab.place(relx=0.13, 
	          rely=0.32,
	          anchor=CENTER)             

text.place(relx=0.38, 
	      rely=0.05,
	      anchor=CENTER)

name.place(relx=0.5, 
	      rely=0.3,
	      anchor=CENTER)

but.place(relx=0.5, 
	      rely=0.6,
	      anchor=CENTER)

exit_but.place(relx=0.5, 
	           rely=0.75,
	           anchor=CENTER)

authorLab.place(relx=0.01, 
	      		rely=0.98,
	      		anchor=SW)

window.mainloop()
