from gtts import gTTS
from tkinter import *
#voice generater functions
def generate():
    tts = gTTS(text.get(),lang='ru')
    t = name.get()
    tts.save(t+'.mp3')

def EngGen():
    tts = gTTS(text.get(),lang='en')
    t = name.get()
    tts.save(t+'.mp3')

#window and buttons
window = Tk()
window.title('озвучка текста')
window.geometry('430x200')
window.resizable(width=False, height=False)
but = Button(window,text='озвучить',command=generate,fg='#eee',bg='#333')
ButEng = Button(window,text='озвучить английский текст',command=EngGen,fg='#eee',bg='#333') 
#text input windows
text = Entry(width=30)
name = Entry(width=30)

textlab = Label(text='Что нужно озвучить',fg='#eee',bg='#333')#what needs to be voiced
namelab = Label(text='название файла',fg='#eee',bg='#333')#file name

authorLab = Label(text='Автор програмы и програмист Илья Околелов 12ф',fg='#eee',bg='#333')

namelab.place(x=0,y=18)
textlab.place(x=0,y=0)              
text.pack()
name.pack()
but.place(x=120,y=50)
ButEng.place(x=120,y=70)
authorLab.place(x=0,y=180)

window.mainloop()
