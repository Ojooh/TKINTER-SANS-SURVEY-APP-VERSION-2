from tkinter import *
from itertools import zip_longest
import functools
import json
import random
import collections
import os


#global variables
counter = []
user_answers = []
numbering = []
issues = []

with open('db/questions_answers.json', 'r+') as questions_answers_file:
    questions_answers = json.load(questions_answers_file)

if os.path.exists("db/user_responses.json"):
    with open("db/user_responses.json", 'r+') as user_responses_file:
        user_responses = json.load(user_responses_file) 
else :
    with open("db/user_responses.json", 'w+') as user_responses_file:
        json.dump([], user_responses_file )

    with open("db/user_responses.json", 'r+') as user_responses_file:
        user_responses = json.load(user_responses_file)

def clear(event):
    for element in root.winfo_children():
        element.destroy()
def close(warning, window):
    warning.destroy()
    window.destroy()

def exit(window):
    root_exit = Tk()
    root_exit.title('Exit Application')
    root_exit.geometry('300x150')
    root_exit.iconbitmap("images/halo_shield.ico")
    root_exit['bg'] = "#ffffff"

    warning = Label(
        root_exit, 
        text= "You are about to close this application, all answers will not be saved", 
        font = ('Bookman Old Style', 14, 'bold'),
        fg='red',
        bg = '#ffffff',
        wraplength=300, 
    )
    warning.pack()

    OK_button = Button(
        root_exit, 
        bg='light yellow', 
        activebackground='light yellow', 
        text='OK', 
        command=functools.partial(close, root_exit, window)
    )
    OK_button.pack()
    
    root_exit.mainloop()


#<--------open admin window ------->
def adminOpen():
    # for exe uncomment the below line of code
    # os.system('"admin.exe"')
    # for exe comment the below line of code
    os.system("python admin.py")
#<--------open admin window End------->



#<!----------get position window ------------->
def getPosition():
    clear(root)
    root.geometry("1290x600")
    root.title("Cyber User Awareness Test")
    root.iconbitmap("images/halo_shield.ico")
    global v


    labeltext = Label(
      root,
      text = "Please, select a category that best describes your job",
      font = ("Bookman Old Style", 18, "bold"),
      justify="center",
      background = "#ffffff",
      wraplength = 1200
    )
    labeltext.pack()

    v = StringVar()
    v.set(-1)
    for value in questions_answers: 
        r = questions_answers.index(value)

        if(r % 2 == 0):
            Radiobutton(
                root, 
                text = value, 
                variable = v, 
                font = ("Bookman Old Style", 16),
                value = value,
                background= "#ffffff",
            ).pack(side = TOP, ipady = 5)
        
    img3 = PhotoImage(file="images/nextbutton.png")
    btnnext = Button(
        root,
        image=img3,
        relief=FLAT,
        border=0,
        command=functools.partial(categorySelected, v)
    )
    btnnext.image = img3
    btnnext.place(x=800, y=400)

    imgexit = PhotoImage(file='images/exitbutton.png')
    btnexit = Button(
        root,
        image=imgexit,
        relief=FLAT,
        border=0,
        command=functools.partial(exit, root),

    )
    btnexit.image = imgexit
    btnexit.place(x=100, y=400)

    
#<!----------get position window End ------------->







#<!----------Select Level window ------------->

def categorySelected(user_r):
    search = user_r.get()
    indexLevel = questions_answers.index(search)
    limit = len(questions_answers[indexLevel + 1])
    if((limit == 0) or (limit % 2 != 0)):
        clear(root)
        root.geometry("1300x700")
        root.title("Cyber User Awareness Test")
        root.iconbitmap("images/halo_shield.ico") 
        
        label_empty = Label(
            root,
            text="No Questions Have been set yet for this category",
            font=("Bookman Old Style", 24, "bold"),
            background="#ffffff",
            width=500,
            justify="center",
            wraplength=1000,
        )
        label_empty.pack()

        imgexit41 = PhotoImage(file='images/exitbutton.png')
        btnexit = Button(
            root,
            image=imgexit41,
            relief=FLAT,
            border=0,
            command=functools.partial(exit, root),
        )
        btnexit.image = imgexit41
        btnexit.place(x=50, y=540)


        img42 = PhotoImage(file='images/backbutton.png')
        btnback = Button(
            image=img42,
            relief=FLAT,
            border=0,
            command=getPosition,
        )
        btnback.image = img42
        btnback.place(x=900, y=540)

    else:
        selected(indexLevel + 1, "next")
#<!----------Select Level window End------------->






#<!----------get question number window------------->
def selected(k, mode):
    if len(counter) == 0:
            counter.append(1)
            level = k 
            que_val = int(counter[0])
            que_no = counter[0] - counter[0]
            numbering.append(1)
            questionShow(level, que_val, que_no)
    else:
        if mode == "next":
            selected_option = radiovar.get()
            if(selected_option == -1):
                level = k
                que_val = int(counter[0])
                que_no = counter[0] - counter[0]
            else:
                user_answers.append(selected_option)
                limit = (len(questions_answers[k])) / 2

                if numbering[0] != limit:
                    numbering[0] = numbering[0] + 1
                    level = k
                    que_val = int(counter[0] + 2)
                    que_no = counter[0] - counter[0]
                    counter[0] = que_val
                    questionShow(level, que_val, que_no)
                else:
                    print("done")
                    calc_score(k)
        else:
            if counter[0] != 1:
                ind = len(user_answers) - 1
                user_answers.pop(ind)
                numbering[0] = numbering[0] - 1
                level = k
                que_val = int(counter[0] - 2)
                que_no = counter[0] - counter[0]
                counter[0] = counter[0] - 2
                questionShow(level, que_val, que_no)
            else:
                numbering.pop(0)
                counter.pop(0)
                getPosition()
#<!----------get question number window End------------->







#<!----------see question windowpython------------->
def questionShow(level, val, no):
    clear(root)
    root.geometry("1300x700")
    root.title("Cyber User Awareness Test")
    root.iconbitmap("images/halo_shield.ico") 
    
    
    sn = str(numbering[0]) + "."
    labelQ2 = Label(
           root,
           text=(sn + str(questions_answers[level][val][no])),
           font=("Bookman Old Style", 24, "bold"),
           background="#ffffff",
           width=500,
           justify="center",
           wraplength=1000,
    )
    labelQ2.pack()

    #create the option buttons
    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)
    options = questions_answers[level][val][no + 1]
    r1 = Radiobutton(
        root,
        text= options[0],
        font = ("Bookman Old STyle", 20),
        value = 0,
        wraplength = 1000,
        variable = radiovar,
        background="#ffffff",
    )
    r1.pack()


    r2 = Radiobutton(
        root,
        text=options[1],
        font=("Bookman Old Style", 20),
        value=1,
        variable=radiovar,
        wraplength = 1200,
        background="#ffffff",
    )
    r2.pack()


    r3 = Radiobutton(
        root,
        text=options[2],
        font=("Bookman Old Style", 20),
        value=2,
        variable=radiovar,
        wraplength = 1000,
        background="#ffffff",

    )
    r3.pack()

    imgexit4 = PhotoImage(file='images/exitbutton.png')
    btnexit = Button(
        root,
        image=imgexit4,
        relief=FLAT,
        border=0,
        command=functools.partial(exit, root),
    )
    btnexit.image = imgexit4
    btnexit.place(x=50, y=540)


    img4 = PhotoImage(file='images/backbutton.png')
    btnback = Button(
        image=img4,
        relief=FLAT,
        border=0,
        command=functools.partial(selected, level, "back"),
    )
    btnback.image = img4
    btnback.place(x=500, y=540)


    img5 = PhotoImage(file='images/nextbutton.png')
    btnnext = Button(
        image=img5,
        relief=FLAT,
        border=0,
        command=functools.partial(selected, level, "next"),
    )
    btnnext.image = img5
    btnnext.place(x=900, y=540)
#<!----------see question window End------------->







#<!----------calculate score function------------->
def calc_score(level):
    
    x = 0
    score = 0
    limit = len(questions_answers[level])
    print(user_answers)
    for i in range(int(limit)):
        if(i % 2 != 0):
            if user_answers[x] == questions_answers[level][i][2]:
                score = score + 10
                x += 1
            else:
                issues.append(questions_answers[level][i - 1])
    
    showresult(level, score)
#<!----------calculate score function End------------->





#<!----------show Result function------------->
def showresult(cat, score):
    global v
    num_que = len(questions_answers[cat])/2
    tot = int(num_que) * 10
    if score != 0:
        percentage = round((score/tot) * 100)
    else:
        percentage = 0

    

    defaults =collections.Counter(issues)
    print(defaults)
    
    new_entry = user_responses
    if len(user_responses) == 0:
        floor = 0
        user_details = {"id": 1, "occupation" : v.get()}
        new_entry.append(user_details)
        for v in range(len(user_answers)):
            key = "Q" + str(v + 1)
            new_entry[floor][key] = user_answers[v]

        new_entry[floor]["score"] = score
        new_entry[floor]["percentage"] = percentage
        new_entry[floor]["defaults"] = defaults
        with open("db/user_responses.json", "w") as e:
                json.dump(new_entry, e)
    else:
        floor = len(new_entry)
        prev_id = floor - 1
        user_id = user_responses[prev_id]['id'] + 1
        user_details = {"id": user_id, "occupation" : v.get()}
        new_entry.append(user_details)
        for v in range(len(user_answers)):
            key = "Q" + str(v + 1)
            new_entry[floor][key] = user_answers[v]

        new_entry[floor]["score"] = score
        new_entry[floor]["percentage"] = percentage
        new_entry[floor]["defaults"] = defaults
        with open("db/user_responses.json", "w") as e:
            json.dump(new_entry, e)     
    
    showResultWindow(score, percentage, defaults)
#<!----------show Result function End------------->






#<!----------show Result function------------->
def showResultWindow(score, percentage, defaults):
    clear(root)
    root.geometry("1300x600")
    root.title("Cyber User Awareness Test")
    root.iconbitmap("images/halo_shield.ico")

    img6 = PhotoImage(file='images/leveler.png')
    labelimage1 = Label(
        root,
        image=img6,
        background="#ffffff",
        height=200
    )
    labelimage1.image = img6
    labelimage1.pack(pady=(10, 0))


    labeltext = Label(
        root,
        text="Thank you for taking your time to participate in this test, Do have a lovely Day",
        font=("Comic sans MS", 24, "bold"),
        background="#ffffff",
    )
    labeltext.pack(pady=(0, 50))

    labeltext = Label(
        root,
        text="Score: " + str(score) + " Percentage: " + str(percentage) + "%",
        font=("Comic sans MS", 24, "bold"),
        background="#ffffff",
    )
    labeltext.pack(pady=(0, 50))

    btnrecommend = Button(
        root,
        text="Get Recommendation",
        font=("CBookman Old Style", 24, "bold"),
        command=functools.partial(showRecommendation, defaults),

    )
    btnrecommend.place(x=190, y=400)

    btnexit = Button(
        root,
        text="Exit",
        font=("Bookman Old Style", 24, "bold"),
        command=root.destroy

    )
    btnexit.place(x=900, y=400)

    root.mainloop()

    #recommendation window
def showRecommendation(defs):
    # global name
    root_rec = Tk()
    root_rec.geometry("1000x800")
    root_rec.title("Cyber User Awareness Test")
    root_rec.iconbitmap("images/halo_shield.ico")
    root_rec.config(background="#ffffff")


    # recommend = ""

    # if(percentage <= 50):
    #     if(name.get() == "IT Professional" and percentage <= 50):
    #         recommend = "Please you need to go for a User Level Training"
    #     if(percentage <= 40):
    #         recommend = "Please you need to go for a User Level Training, your score shows you have a very low understanding of cyber security"

    # elif(percentage > 40 and percentage <= 60):
    #     recommend = "Please embark on the new comer foundation (Awareness Level) course provided by GHCQ"
    # else:
    #     recommend = "You did great.  We recommend for you to take higher level (Application level) courses provided by the GHCQ"

    if len(defs) != 0:
        labelh = Label(
            root_rec,
            text="Based on your answers from the survey we noticed you failed",
            font=("Comic sans MS", 24, "bold"),
            background="#ffffff",
            wraplength="800"
        )
        labelh.pack(pady=(0, 30))


        for i in defs:
            sef = i.split()
            show = sef[0]
            details = str(defs[i]) + " questions in " + str(show) + " Security"
            maxFail = defs.most_common(1)
            labelg = Label(
                root_rec,
                text=details,
                font=("Comic sans MS", 24, "bold"),
                background="#ffffff",
                wraplength="1000"
            )
            labelg.pack(pady=(0, 30))


        sec_name = maxFail[0][0].split()
        sec = sec_name[0]
        recommend = "We recommend you work more on " + str(sec) + " Security"
        labeli = Label(
            root_rec,
            text=recommend,
            font=("Comic sans MS", 24, "bold"),
            background="#ffffff",
            wraplength="1000"
        )
        labeli.pack(pady=(0, 30))

        
    else:
        labelh = Label(
            root_rec,
            text="Based on your answers from the survey we noticed you have a very high level of cyber security awareness, please keep up the Good work!",
            font=("Comic sans MS", 24, "bold"),
            background="#ffffff",
            wraplength="800"
        )
        labelh.pack(pady=(0, 30))

    # imgexit3 = PhotoImage(file='images/exitbutton.png')
    # btnexit = Button(
    #     root_rec,
    #     image=imgexit3,
    #     relief=FLAT,
    #     border=0,
    #     command=functools.partial(exit, root),

    # )
    # btnexit.image = imgexit3
    # btnexit.pack()
    btnexit = Button(
        root_rec,
        text="Exit",
        font=("Bookman Old Style", 24, "bold"),
        command=root_rec.destroy

    )
    btnexit.place(x=500, y=700)

    root_rec.mainloop()
#<!----------show Result window End------------->












    










#<------Program start Here ---------->
root = Tk()
root.title("Cyber User Awareness Test")
root.iconbitmap("images/halo_shield.ico")
root.geometry("1500x800")
root.config(background="#ffffff")
# root.iconbitmap('c:/New Folder/halo_shield.ico')
root.resizable(0,0)
labeltext = Label(
      root,
      text = "Welcome!, Thank you for offering to participate in this test. Click start to begin.",
      font = ("Bookman Old Style", 24, "bold"),
      background = "#ffffff",
)

labeltext.pack(pady=(0,50))


img1 = PhotoImage(file='images/user_awareness1.png')
labelimage1 = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage1.image = img1
labelimage1.pack(pady=(10,0))


img2 = PhotoImage(file='images/start.png')
btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = getPosition,

)
btnStart.image = img2
btnStart.pack()

image3 = PhotoImage(file='images/adminbutton.png')
btnAdmin = Button(
    root,
    image=image3,
    relief=FLAT,
    border=0,
    command=adminOpen,

)
btnAdmin.image = image3
btnAdmin.place(x=1100, y=200)


imgexit4 = PhotoImage(file='images/exitbutton.png')
btnexit = Button(
    root,
    image=imgexit4,
    relief=FLAT,
    border=0,
    command=functools.partial(exit, root),

)
btnexit.image = imgexit4
btnexit.place(x=100, y=200)

root.mainloop()