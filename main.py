from tkinter import*
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from requests import head

#colors
co0 = '#444466' #Black
co1 = '#feffff' #White
co2 = '#6f9fbd' #Blue
co3 = '#403d3d' #Ash

window = Tk()
window.title('')
window.geometry('550x510')
window.resizable(width=False, height=False)
window.configure(bg=co1)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

main_frame = Frame(window, width=500, height=305, bg=co1)
main_frame.grid(row=0, column=0, padx= 1, pady=1)

pok_name = Label(main_frame, text = 'Pokemon name', anchor = 'center', font=('Ivy 20 bold'), fg=co0)
pok_name.place(x=15, y=15)

pok_type = Label(main_frame, text = 'Pokemon type', anchor = 'center', font=('verdana 10 bold'), fg=co0)
pok_type.place(x=20, y=50)

pok_number = Label(main_frame, text = 'Pokemon number', anchor = 'center', font=('verdana 13 bold'), fg=co0)
pok_number.place(x=20, y=75)

#pokemon image===============================================================================================================

pokemon_image = Image.open('Images/pikachu.png')
pokemon_image = pokemon_image.resize((260, 260))
pokemon_image = ImageTk.PhotoImage(pokemon_image)

l_icon_l = Label(window, image=pokemon_image, bg=co1)
l_icon_l.place(x=60, y=50)

#Status===============================================================================================================

pok_status = Label(window, text = 'Status', font = ('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

pok_hp = Label(window, text = 'HP: 100', font = ('Verdana 10'), bg=co1, fg=co0)
pok_hp.place(x=15, y=360)

pok_Attack = Label(window, text = 'Attack: 300', font = ('Verdana 10'), bg=co1, fg=co0)
pok_Attack.place(x=15, y=385)

pok_Defence = Label(window, text = 'Defence: 500', font = ('Verdana 10'), bg=co1, fg=co0)
pok_Defence.place(x=15, y=410)

pok_Speed = Label(window, text = 'Speed: 100', font = ('Verdana 10'), bg=co1, fg=co0)
pok_Speed.place(x=15, y=435)

pok_Total = Label(window, text = 'Total: 100', font = ('Verdana 10 bold'), bg=co1, fg=co0)
pok_Total.place(x=15, y=460)

#Skills===============================================================================================================

pok_Skill = Label(window, text = 'Skills', font = ('Verdana 20'), bg=co1, fg=co0)
pok_Skill.place(x=180, y=310)

pok_hp1 = Label(window, text = 'Thunderbolt', font = ('Verdana 10'), bg=co1, fg=co0)
pok_hp1.place(x=180, y=360)

pok_hp2 = Label(window, text = 'Thunder Elite TM', font = ('Verdana 10'), bg=co1, fg=co0)
pok_hp2.place(x=180, y=385)

#Loading all Pokemons===============================================================================================================

img_pok_1 = Image.open('images/cabeca-pikachu.png')
img_pok_1 = img_pok_1.resize((40, 40))
img_pok_1 = ImageTk.PhotoImage(img_pok_1)

icon_1 = Button(window, text='Pikachu', width=150, image=img_pok_1, padx=5, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Verdana 12'), bg=co1, fg=co0)
icon_1.place(x=375, y=10)

window.mainloop()