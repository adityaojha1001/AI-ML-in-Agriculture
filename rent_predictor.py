import pandas as pd
import tkinter as ttk
app =ttk.Tk()
app.title('Ghar ka price batane wala')
app.geometry('250x125')

ttk.Label(app, text='Income').grid(row=0,column=0)
inc=ttk.Variable(app)
ttk.Entry(app, textvariable = inc).grid(row=0,column=1)

ttk.Label(app, text='House-age').grid(row=1,column=0)
age=ttk.Variable(app)
ttk.Entry(app, textvariable = age).grid(row=1,column=1)

ttk.Label(app, text='Room').grid(row=2,column=0)
room=ttk.Variable(app)
ttk.Entry(app, textvariable = room).grid(row=2,column=1)

ttk.Label(app, text='Population').grid(row=3,column=0)
pop=ttk.Variable(app)
ttk.Entry(app, textvariable = pop).grid(row=3,column=1)

def prediction():
    income = eval(inc.get())
    house_age = eval(age.get())
    rooms = eval(room.get())
    population = eval(pop.get())
    
    m = pd.read_pickle('housePredictor.pkl')
    query_df = pd.DataFrame([[income, house_age, rooms, population]])
    pred = round(m.predict(query_df)[0])
    result.set(f'${pred}')
    
ttk.Button(app, text='Predict Price', command =prediction).grid(row=4,column=0)
result= ttk.Variable(app)
ttk.Label(app, textvariable= result).grid(row=4,column=1)

app.mainloop()
