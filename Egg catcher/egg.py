from tkinter import *
from itertools import cycle
from random import randrange
from tkinter import Tk,Label,Canvas,messagebox,font

from tkinter.ttk import *


root = Tk()
remaining_liv=3
score=0
egg_speed=500
egg_interval=4000
egg_dif=0.90

root.geometry("300x200")
root['bg']='light blue'
label=Label(root,text="Click The Button To Start The Game",font=("ArialBlack"),background="light blue").pack(pady=10)
 
#new window pop up
def new():
        canvas_w=866
        canvas_h=500
        #making background 
       
        NewWindow=Toplevel(root)
        NewWindow.title("NewWindow")
        NewWindow.geometry("866x520")
        NewWindow.maxsize(width=866,height=520)
        NewWindow.minsize(width=866,height=520)
        BG=PhotoImage(file="img.png")
        canvas1=Canvas(NewWindow, width=866,height=520)
        canvas1.pack(fill="both",expand = True)
        canvas1.create_image(0,0,image=BG,anchor="nw")

        #making egg
       
        color_cycle=cycle(['red','pink','yellow','blue','green','orange','purple','lightgreen',''])
        egg_h=55
        egg_w=45
        egg_score=10
        egg_speed=500

        #making arc
        catcher_h=150
        catcher_w=100
        catcher_x1=canvas_w / 2 - catcher_w / 2
        catcher_y1=canvas_h - catcher_h - 20
        catcher_x2=catcher_x1 + catcher_w
        catcher_y2=catcher_y1 + catcher_h
        
        catcher=canvas1.create_arc(catcher_x1,catcher_y1,catcher_x2,catcher_y2,start=200, extent=140,style='arc',outline='yellow',width=5)
        
        #display score and lives
        score=0
        score_text=canvas1.create_text(20,10,anchor='nw',font=('Cambria',22,'bold'),fill='darkblue',text='SCORE : ' + str(score))

        remaining_liv=3
        live_text=canvas1.create_text(canvas_w - 300,10,anchor='nw',font=('Cambria',22,'bold'),fill='darkblue',text='REMAINING LIVES : ' + str(remaining_liv))

        #making egg move
        eggs=[]
        def create_egg ():
                global egg_interval,remaining_liv
                x=randrange(20,800)    
                y=40
                new_egg=canvas1.create_oval(x,y,x + egg_w,y+egg_h,fill=next(color_cycle),width=0)
                eggs.append(new_egg)
                if remaining_liv==0:
                        quit()
                else: 
                        NewWindow.after(egg_interval,create_egg)
                           


        def move_egg ():
                for egg in eggs:
                        (egg_x,egg_y,egg_x2,egg_y2)=canvas1.coords(egg)
                        canvas1.move(egg,0,20)
                        if egg_y2 > canvas_h :
                                egg_drop(egg) 
                NewWindow.after(egg_speed,move_egg)                

        def egg_drop(egg):
                eggs.remove(egg)
                canvas1.delete(egg)
                lose_a_live()
                global remaining_liv, score
                if remaining_liv ==0:
                        messagebox.showinfo('GAME OVER !','FINAL SCORE:'+ str(score))
                        create_egg(remaining_liv)   
                        NewWindow.destroy()

        def lose_a_live():
                global remaining_liv
                remaining_liv -=1
                canvas1.itemconfigure(live_text,text='Lives : '+str(remaining_liv))     

        def check_catch():
                (catcher_x, catcher_y, catcher_x2, catcher_y2) = canvas1.coords(catcher)
                for egg in eggs:
                        (egg_x, egg_y, egg_x2, egg_y2)= canvas1.coords(egg)
                        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 40:
                                  eggs.remove(egg)
                                  canvas1.delete(egg)
                                  increase_score(egg_score)
                NewWindow.after(100,check_catch)
    
        def increase_score(points):
                global score, egg_speed, egg_interval, egg_dif
                score +=points
                egg_speed = int(egg_speed * egg_dif)
                egg_interval = int(egg_interval* egg_dif)
                canvas1.itemconfigure(score_text, text='Score: '+str(score))
    
        def move_left(event):
                (x1,y1,x2,y2) = canvas1.coords(catcher)
                if x1 > 0:
                        canvas1.move(catcher, -20,0)
        
        def move_right(event):
                (x1, y1,x2,y2) = canvas1.coords(catcher)
                if x2<canvas_w:
                        canvas1.move(catcher,20,0)
        
        canvas1.bind('<Left>',move_left)
        canvas1.bind('<Right>',move_right)
        canvas1.focus_set()

        NewWindow.after(1000,create_egg)
        NewWindow.after(1000,move_egg)
        NewWindow.after(1000,check_catch)

        

        NewWindow.mainloop()


mybutton=Button(text="start",command=new).pack(pady=10)


root.mainloop()