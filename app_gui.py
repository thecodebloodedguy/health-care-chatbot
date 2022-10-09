
from chat import chatter
from tkinter import *
import tkinter
import pyttsx3
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"



BG_GRAY = "#66ffe0"
BG_COLOR = "#00ffaa"
TEXT_COLOR = "#000000"
 
# import speech_recognition as sr

def _on_enter_pressed(event):
    msg=msg_entry.get()
    _insert_message(msg,"You")

# def _voice_input(event):
#     r = sr.Recognizer()
    
#     try:

#         with sr.Microphone() as source: 
#             r.adjust_for_ambient_noise(source,duration=1)               
#             audio = r.listen(source)

#         msg=r.recognize(audio) 
#         msg=msg_entry.get()
#         _insert_message(msg,"You")
#     except:
#         msg="__NO__"
#         msg=msg_entry.get()
#         _insert_message(msg,"You")

    


window=tkinter.Tk()
window.title("Chat")
window.resizable(width=True,height=True)
window.configure(width=490,height=650,bg=BG_COLOR)    


head_label= Label(window,bg=BG_COLOR,fg=TEXT_COLOR,text="PharmDroid-Your Personal Doctor",font=FONT_BOLD,pady=10)
head_label.place(relwidth=1)
        
line= Label(window,width=450,bg=BG_GRAY)
line.place(relwidth=1,rely=0.07,relheight=0.012)
        
        
text_widget = Text(window,width=20,height=2,bg=BG_COLOR,fg=TEXT_COLOR,font=FONT,padx=5,pady=5)
text_widget.place(relheight=0.800,relwidth=1,rely=0.08)
text_widget.configure(cursor="arrow",state=DISABLED)
        
scrollbar =Scrollbar(text_widget)
scrollbar.place(relheight=1,relx=0.975)
scrollbar.configure(command=text_widget.yview)
        
bottom_label = Label(window,bg=BG_GRAY,height=80)
bottom_label.place(relwidth=1,rely=0.825)
        
msg_entry= Entry(bottom_label,bg="#2c3e50",fg=TEXT_COLOR,font=FONT)
msg_entry.place(relwidth=0.74,relheight=0.032,rely=0.008,relx=0.011)
msg_entry.focus()
msg_entry.bind("<Return>",_on_enter_pressed)#,_voice_input
        
        
send_button = Button(bottom_label,text="Send",font=FONT_BOLD,width=20,bg=BG_GRAY,command=lambda:_on_enter_pressed(None))
send_button.place(relx=0.77,rely=0.008,relheight=0.03,relwidth=0.22)
msg=msg_entry.get()

# mic_button = Button(bottom_label,text="Voice",font=FONT_BOLD,width=20,bg=BG_GRAY,command=lambda:_voice_input(None))
# mic_button.place(relx=0.77,rely=0.05,relheight=0.03,relwidth=0.22)
# msg=msg_entry.get()


def _insert_message(msg,sender):
        if not msg:
            return
        msg_entry.delete(0,END)
        msg1=f"\n{sender}:\n{msg}\n\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END,msg1)
        text_widget.configure(state=DISABLED)
        resp=chatter(msg)
        msg2=f"\nTanu:\n{resp}\n\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END,msg2)
        text_widget.configure(state=DISABLED)
        text_widget.see(END)
        engine=pyttsx3.init()
        voice = engine.getProperty('voices')
        engine.setProperty('voice', voice[1].id)
        engine.say(resp)
        engine.runAndWait()

window.mainloop()