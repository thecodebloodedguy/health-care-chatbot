
from chat import chatter
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
from tkinter import *
import tkinter
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


def _on_enter_pressed(event):
       msg=msg_entry.get()
       _insert_message(msg,"You")

window=tkinter.Tk()
window.title("Chat")
window.resizable(width=False,height=False)
window.configure(width=470,height=550,bg=BG_COLOR)    


head_label= Label(window,bg=BG_COLOR,fg=TEXT_COLOR,text="Welcome",font=FONT_BOLD,pady=10)
head_label.place(relwidth=1)
        
line= Label(window,width=450,bg=BG_GRAY)
line.place(relwidth=1,rely=0.07,relheight=0.012)
        
        
text_widget = Text(window,width=20,height=2,bg=BG_COLOR,fg=TEXT_COLOR,font=FONT,padx=5,pady=5)
text_widget.place(relheight=0.745,relwidth=1,rely=0.08)
text_widget.configure(cursor="arrow",state=DISABLED)
        
scrollbar =Scrollbar(text_widget)
scrollbar.place(relheight=1,relx=0.974)
scrollbar.configure(command=text_widget.yview)
        
bottom_label = Label(window,bg=BG_GRAY,height=80)
bottom_label.place(relwidth=1,rely=0.825)
        
msg_entry= Entry(bottom_label,bg="#2C3E50",fg=TEXT_COLOR,font=FONT)
msg_entry.place(relwidth=0.74,relheight=0.06,rely=0.008,relx=0.011)
msg_entry.focus()
msg_entry.bind("<Return>",_on_enter_pressed)
        
        
send_button = Button(bottom_label,text="Send",font=FONT_BOLD,width=20,bg=BG_GRAY,command=lambda:_on_enter_pressed(None))
send_button.place(relx=0.77,rely=0.008,relheight=0.06,relwidth=0.22)
msg=msg_entry.get()

def _insert_message(msg,sender):
        if not msg:
            return
        
        msg_entry.delete(0,END)
        msg1=f"{sender}:{msg}\n\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END,msg1)
        text_widget.configure(state=DISABLED)
        
        msg2=f"bot:{chatter(msg)}\n\n"
        text_widget.configure(state=NORMAL)
        text_widget.insert(END,msg2)
        text_widget.configure(state=DISABLED)
        
        text_widget.see(END)

window.mainloop()