import tkinter as tk
import random
from playsound import playsound

window=tk.Tk()
window.title('ROCK PAPER SCISSOR')
window.geometry("1200x900")
#window.configure(background='blue')

my_score=0
comp_score=0
counter=20

def clickrock():
    global my_score
    global comp_score
    global counter
    if counter==0:
        gameup=tk.Label(text="GAME UP...!!!",font=('Arial',30))
        gameup.grid(column=3,row=3)
        if my_score>comp_score:
            winner=tk.Label(text="YOU WON..HURRAYYY.!!!",font=('Arial',30))
            winner.grid(column=3,row=4)
            playsound('F:/media/notify.wav')
        else:
            winner=tk.Label(text="COMPUTER WON!!!",font=('Arial',30))
            winner.grid(column=3,row=4)
            playsound('F:/media/chord.wav')
        return
    clickrocklabel=tk.Label(text='rock',font=('Arial',15), height=5, width=5)
    clickrocklabel.grid(column=1,row=2)
    computer=random.choice(['rock','paper','scissor'])
    compchoosenlabel=tk.Label(text=computer,font=('Arial',15), height=5, width=5)
    compchoosenlabel.grid(column=4,row=2)
    if clickrocklabel.cget('text')=='rock' and computer=='rock':
        tieresult=tk.Label(text="TIE...!!!")
        tieresult.grid(column=2,row=4)
    elif clickrocklabel.cget('text')=='rock' and computer=='paper':
        tieresult=tk.Label(text='            ')
        tieresult.grid(column=2,row=4)
        my_score=my_score
        comp_score=comp_score+1
        myscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        myscoredisplay.grid(column=2,row=2)
        myscoredisplay.insert(tk.END, my_score)
        compscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        compscoredisplay.grid(column=3,row=2)
        compscoredisplay.insert(tk.END, comp_score)
    elif clickrocklabel.cget('text')=='rock' and computer=='scissor':
        tieresult=tk.Label(text='            ')
        tieresult.grid(column=2,row=4)
        my_score=my_score+1
        comp_score=comp_score
        myscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        myscoredisplay.grid(column=2,row=2)
        myscoredisplay.insert(tk.END, my_score)
        compscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        compscoredisplay.grid(column=3,row=2)
        compscoredisplay.insert(tk.END, comp_score)
    counter=counter-1
    
    
    

def clickpaper():
    global my_score
    global comp_score
    global counter
    if counter==0:
        gameup=tk.Label(text="GAME UP...!!!",font=('Arial',30))
        gameup.grid(column=3,row=3)
        if my_score>comp_score:
            winner=tk.Label(text="YOU WON..HURRAYYY.!!!",font=('Arial',30))
            winner.grid(column=3,row=4)
            playsound('F:/media/notify.wav')
        else:
            winner=tk.Label(text="COMPUTER WON!!!",font=('Arial',30))
            winner.grid(column=3,row=4)
            playsound('F:/media/chord.wav')
        return
    clickrocklabel=tk.Label(text='paper',font=('Arial',15), height=5, width=5)
    clickrocklabel.grid(column=1,row=2)
    computer=random.choice(['rock','paper','scissor'])
    compchoosenlabel=tk.Label(text=computer,font=('Arial',15), height=5, width=5)
    compchoosenlabel.grid(column=4,row=2)
    if clickrocklabel.cget('text')=='paper' and computer=='paper':
        tieresult=tk.Label(text="TIE...!!!")
        tieresult.grid(column=2,row=4)
    elif clickrocklabel.cget('text')=='paper' and computer=='rock':
        tieresult=tk.Label(text='            ')
        tieresult.grid(column=2,row=4)
        my_score=my_score+1
        comp_score=comp_score
        myscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        myscoredisplay.grid(column=2,row=2)
        myscoredisplay.insert(tk.END, my_score)
        compscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        compscoredisplay.grid(column=3,row=2)
        compscoredisplay.insert(tk.END, comp_score)
    elif clickrocklabel.cget('text')=='paper' and computer=='scissor':
        tieresult=tk.Label(text='            ')
        tieresult.grid(column=2,row=4)
        my_score=my_score
        comp_score=comp_score+1
        myscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        myscoredisplay.grid(column=2,row=2)
        myscoredisplay.insert(tk.END, my_score)
        compscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        compscoredisplay.grid(column=3,row=2)
        compscoredisplay.insert(tk.END, comp_score)
    counter=counter-1

def clickscissor():
    global my_score
    global comp_score
    global counter
    if counter==0:
        gameup=tk.Label(text="GAME UP...!!!",font=('Arial',30))
        gameup.grid(column=3,row=3)
        if my_score>comp_score:
            winner=tk.Label(text="YOU WON..HURRAYYY.!!!",font=('Arial',30))
            winner.grid(column=3,row=4)
            playsound('F:/media/notify.wav')
        else:
            winner=tk.Label(text="COMPUTER WON!!!",font=('Arial',30))
            winner.grid(column=3,row=4)
            playsound('F:/media/chord.wav')
        return
    clickrocklabel=tk.Label(text='scissor',font=('Arial',15), height=5, width=5)
    clickrocklabel.grid(column=1,row=2)
    computer=random.choice(['rock','paper','scissor'])
    compchoosenlabel=tk.Label(text=computer,font=('Arial',15), height=5, width=5)
    compchoosenlabel.grid(column=4,row=2)
    if clickrocklabel.cget('text')=='scissor' and computer=='scissor':
        tieresult=tk.Label(text="TIE...!!!")
        tieresult.grid(column=2,row=4)
    elif clickrocklabel.cget('text')=='scissor' and computer=='rock':
        tieresult=tk.Label(text='            ')
        tieresult.grid(column=2,row=4)
        my_score=my_score
        comp_score=comp_score+1
        myscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        myscoredisplay.grid(column=2,row=2)
        myscoredisplay.insert(tk.END, my_score)
        compscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        compscoredisplay.grid(column=3,row=2)
        compscoredisplay.insert(tk.END, comp_score)
    elif clickrocklabel.cget('text')=='scissor' and computer=='paper':
        tieresult=tk.Label(text='            ')
        tieresult.grid(column=2,row=4)
        my_score=my_score+1
        comp_score=comp_score
        myscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        myscoredisplay.grid(column=2,row=2)
        myscoredisplay.insert(tk.END, my_score)
        compscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
        compscoredisplay.grid(column=3,row=2)
        compscoredisplay.insert(tk.END, comp_score)
    counter=counter-1

def startagain():
    global my_score
    global comp_score
    global counter
    my_score=0
    comp_score=0
    counter=20
    myscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
    myscoredisplay.grid(column=2,row=2)
    myscoredisplay.insert(tk.END, my_score)
    compscoredisplay=tk.Text(master=window,height=1, width=2, font=('Arial',20))
    compscoredisplay.grid(column=3,row=2)
    compscoredisplay.insert(tk.END, comp_score)
    tieresult=tk.Label(text='            ')
    tieresult.grid(column=2,row=4)
    gameup=tk.Label(text="                                         ",font=('Arial',30))
    gameup.grid(column=3,row=3)
    winner=tk.Label(text="                                                  ",font=('Arial',30))
    winner.grid(column=3,row=4)
        
questionlabel=tk.Label(text='What do you choose ?',font=('Arial',15),bg='yellow')
questionlabel.grid(column=0,row=0)

rockbutton=tk.Button(text='rock',command=clickrock, height=2, width=10,font=('Arial',15),bg='light blue')
rockbutton.grid(column=0,row=1)

paperbutton=tk.Button(text='paper',command=clickpaper, height=2, width=10,font=('Arial',15),bg='light green')
paperbutton.grid(column=0,row=2)

scissorbutton=tk.Button(text='scissor',command=clickscissor, height=2, width=10,font=('Arial',15), bg='pink')
scissorbutton.grid(column=0,row=3)

scissorbutton=tk.Button(text='START AGAIN !!',command=startagain,bg="light gray")
scissorbutton.grid(column=0,row=5)


choicelabel=tk.Label(text='You Choosen .. ')
choicelabel.grid(column=1,row=1)

yourscorelabel=tk.Label(text='Your Score is:')
yourscorelabel.grid(column=2,row=1)

entry=tk.Text(height=1, width=1, font=('Arial',20))
entry.grid(column=2,row=2)

compscorelabel=tk.Label(text='Computer Score is:')
compscorelabel.grid(column=3,row=1)

compentry=tk.Text(height=1, width=1, font=('Arial',20))
compentry.grid(column=3,row=2)

compchoicelabel=tk.Label(text='Computer Choosen .. ')
compchoicelabel.grid(column=4,row=1)
             
window.mainloop()

