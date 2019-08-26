import json, os
from tkinter import *
import functools


#global variables
#Open needed Files
getList = []
statinfo = os.stat("db/questions_answers.json")
fileSize = statinfo.st_size
with open('db/questions_answers.json', 'r+') as file:
        if(fileSize == 0):
            getList.append("no entry yet")
            json.dump(getList, file)
with open('db/questions_answers.json', 'r+') as file:
            questions_answers_list = json.load(file)


#<!------------------------Program Functions------------------------------->
#<!--------Program Helper Functions----------------->
def clear(event):
    "'Window cleaning'"
    for element in root.winfo_children():
        element.destroy()
#<!--------Program Helper Functions End------------->

#<!--------Program Main Functions------------------->
#<!------------Error window------------------------->
def error_show(error):
    root_error = Tk()
    root_error.title('Error')
    root_error.geometry('300x150')
    root_error.iconbitmap("images/halo_shield.ico")
    root_error['bg'] = "#ffffff"

    error = Label(
        root_error, 
        text= "Error: \n" + error, 
        font = ('Bookman Old Style', 14, 'bold'),
        fg='red',
         bg = '#ffffff',
        wraplength=300, 
    )
    error.pack()
    
    root_error.mainloop()
#<!------Error window End------------->

#<!------Success window--------------->
def success_show(success):
    root_success = Tk()
    root_success.title('Success')
    root_success.geometry('300x150')
    root_success.iconbitmap("images/halo_shield.ico")
    root_success['bg'] = "#ffffff"

    success = Label(
        root_success, 
        text= "UPDATE SUCCESS: \n" + success, 
        font = ('Bookman Old Style', 14, 'bold'),
        fg='blue',
        bg = '#ffffff',
        wraplength=300, 
    )
    success.pack()

    OK_button = Button(
        root_success, 
        bg='light yellow', 
        activebackground='light yellow', 
        text='OK', 
        command=root_success.destroy
    )
    OK_button.pack()
    
    root_success.mainloop()
#<!------Success window End------------->
#<!------admin authentication window------------->
def Authentication():   
    root_input = Tk()
    root_input.title('Admin Authentication')
    root_input.geometry('600x100')
    root_input.iconbitmap("images/halo_shield.ico")
    root_input['bg'] = '#ffffff'
    global password_entry

    password_Label = Label(
        root_input, 
        text='Enter Password:', 
        bg='#ffffff'
    )
    password_Label.pack()

    password = StringVar()
    password_entry = Entry(
        root_input, 
        textvariable= password, 
        font = ('Bookman Old Styles', 12),
        show="*",
        width=50
    )
    password_entry.pack()
    

    login_button = Button(
        root_input, 
        bg='light yellow', 
        activebackground='light yellow', 
        text='Login', 
        command=functools.partial(checkAuthentication, root_input)
    )
    login_button.pack()

    password_entry.focus_force()
    root_input.mainloop()

#<!------handle authenication------------->
def checkAuthentication(window):
    correctpass = "password4"
    input = password_entry.get()

    if(input == correctpass):
        window.destroy()
        success = "Login Successful, User Authorized"
        categorySelection()
        success_show(success) 
        
        
    else:
        error = "You are not authorized to view this page"
        error_show(error)
#<!------login window End------------->
#<!------Level selection window------------->
def categorySelection():
    clear(root)
    root.geometry("400x200")
    root.title("User Category Selection")
    root.iconbitmap("images/halo_shield.ico")
    global category_listbox

    category_listbox = Listbox(
        root,
        width=58, 
        height=5, 
        bg='light yellow', 
        selectbackground='SkyBlue4'
    )
    category_listbox.place(x=28, y=10)

    for f in range(len(questions_answers_list)):
        if f % 2 == 0 :
            category = f
            category_listbox.insert(1, questions_answers_list[category])

    btnCategoryCreation = Button(
        root,
        text='Create New Category', 
        background='light yellow', 
        activebackground='light yellow', 
        command=functools.partial(categoryBox, "create")
    )

    btnCategoryCreation.place(x=29, y=110)

    btnCategorySelection = Button(
        root,
        text='Next', 
        background='light yellow', 
        activebackground='light yellow', 
       command=functools.partial(categoryBox, "next")
    )
    btnCategorySelection.place(x=170, y=160)

    btncategoryEdit = Button(
        root,
        text='Edit Category', 
        background='light yellow', 
        activebackground='light yellow', 
        command=functools.partial(categoryBox, "edit")
    )
    btncategoryEdit.place(x=170, y=110)

    btncategoryDelete = Button(
        root,
        text='Delete Category', 
        background='light yellow', 
        activebackground='light yellow', 
        command=functools.partial(categoryBox, "delete")
    )
    btncategoryDelete.place(x=270, y=110)    

#<!------Handle Category Selection------------->
def categoryBox(mode):
    selected = category_listbox.curselection()
    value = ""

    if((mode == "edit" or mode == "delete") and (selected == ())):
        error = "Nothing selecetd please select a level to edit"
        error_show(error)
    else:         
        if mode == "create":
            root_input = Tk()
            root_input.title('create Level')
            root_input.geometry('300x150')
            root_input.iconbitmap("images/halo_shield.ico")
            root_input['bg'] = 'SteelBlue2'

            category_label = Label(
                root_input, 
                text='Enter new Category Name:', 
                bg='SteelBlue2'
            )
            category_label.pack()

            category_value = StringVar()
            category_entry = Entry(
                root_input, 
                textvariable= category_value, 
                font = ('Cosmic Sans', 12),
                width=30
            )
            category_entry.pack()

            save_button = Button(
                root_input, 
                bg='light yellow', 
                activebackground='light yellow', 
                text='Save', 
                command=functools.partial(save_create, category_entry, root_input)
            )
            save_button.pack()

            category_entry.focus_force()
            root_input.mainloop()

        elif mode == "edit":
            root_input = Tk()
            root_input.title('Edit category')
            root_input.geometry('300x150')
            root_input.iconbitmap("images/halo_shield.ico")
            root_input['bg'] = 'SteelBlue2'
            value = category_listbox.get(selected[0])

            category_label = Label(
                root_input, 
                text='Enter new category Name:', 
                bg='SteelBlue2'
            )
            category_label.pack()

            category_value = StringVar()
            category_entry = Entry(
                root_input, 
                textvariable= category_value, 
                font = ('Cosmic Sans', 12),
                width=30
            )
            category_entry.insert(0,value)
            category_entry.pack()

            save_button = Button(
                root_input, 
                bg='light yellow', 
                activebackground='light yellow', 
                text='Save', 
                command=functools.partial(save_edit, value, category_entry, root_input)
            )
            save_button.pack()

            category_entry.focus_force()
            root_input.mainloop()

        elif mode == "next":
            value = category_listbox.get(selected[0])
            global questions_listbox, root_que
            root_que = Tk()
            root_que.title(value + "Questions")
            root_que.geometry('1500x500')
            root_que.iconbitmap("images/halo_shield.ico")
            

            questions_listbox = Listbox(
                root_que, 
                width=200,
                font = ('Cosmic Sans', 10), 
                height=25
            )
            questions_listbox.place(x=50, y=20)

            indexLevel = questions_answers_list.index(value)
            if(len(questions_answers_list[indexLevel + 1]) == 0):
                questions_listbox.insert("end", "No Questions Entered ")
            else:
                questions = questions_answers_list[indexLevel + 1]
                for i in range(len(questions)):
                    ques = typ = ""   
                    if i % 2 != 0:
                        ques = questions[i][0]
                        typ = questions[i - 1]
                        fee = str(ques) + " ---- " + str(typ)
                        questions_listbox.insert("end", fee)

            create_button = Button(
                root_que,
                text='Create New question',
                bg='light yellow',
                activebackground='light yellow',
                command=functools.partial(question_actions, "create", indexLevel)
            )
            create_button.place(x=50, y=460)

            change_button = Button(
                root_que,
                text='Edit question',
                bg='light yellow',
                activebackground='light yellow',
                command=functools.partial(question_actions, "edit", indexLevel)
            )
            change_button.place(x=190, y=460)

            delete_button = Button(
                root_que,
                text='Delete question',
                bg='light yellow',
                activebackground='light yellow',
                command=functools.partial(question_actions, "delete", indexLevel)
            )
            delete_button.place(x=291, y=460)


            exit_button = Button(
                root_que,
                text='Exit',
                bg='light yellow',
                activebackground='light yellow',
                command=root_que.destroy
            )
            exit_button.place(x=1250, y=460)
            root_que.mainloop()
        
        else:
            value = category_listbox.get(selected[0])
            getList = questions_answers_list
            for i in getList:
                index = getList.index(i)
                if i == value: 
                    getList.remove(i)
                    getList.pop(index)

            with open("db/questions_answers.json", "w") as tempF:
                json.dump(getList, tempF)
                success = "Category removed successfully"
            categorySelection()
            success_show(success)


#<!------save category edit------------->
def save_edit(orgvalue, newvalue, window):
    if(newvalue.get() == ""):
        error = "Empty Input Not Accepted, please fill All field(s)"
        error_show(error)
    else:
        getList = questions_answers_list
        if(newvalue.get() not in getList):
            for r in range(len(questions_answers_list)):
                if(getList[r] == orgvalue):
                    getList[r] = newvalue.get()
                    with open("db/questions_answers.json", "w") as tempF:
                        json.dump(getList, tempF)
                        success = "Category Name Changed Successfully"
    window.destroy()
    categorySelection()
    success_show(success)

#<!------see newly created category------------->
def save_create(input, window):
    if(input.get() == ""):
        error = "Empty Input Not Accepted, please fill All field(s)"
        error_show(error)
    else:
        getList = questions_answers_list
        if(getList[0] == "no entry yet"):
            getList = []
            getList.append(input.get())
            getList.append([])
            
            with open("db/questions_answers.json", "w") as tempF:
                json.dump(getList, tempF)
                success="Category Created Successfully"
        else:
            if input.get() not in getList:
                getList.append(input.get())
                getList.append([])

                with open("db/questions_answers.json", "w") as tempF:
                    json.dump(getList, tempF)
                    success = "Category Created Successfully"
            else:
                error = "category already exixt in database"
                error_show(error)
        window.destroy()
        categorySelection()
        success_show(success)
#<!------Level selection window End------------->
#<!------Handle create new and edit old questions------------->
def question_actions(mode, index):
    selected_que = questions_listbox.curselection()

    if((mode == "edit" or mode == "delete") and (selected_que == ())):
        error = "Nothing selecetd please select a question to make changes too"
        error_show(error)
    else:
        if mode == "create" :  
            root_input = Tk()
            root_input.title('create question')
            root_input.geometry('1000x300')
            root_input.iconbitmap("images/halo_shield.ico")
            root_input['bg'] = 'SteelBlue2'

            questionType_label = Label (
                root_input,
                text= "Enter Question Type: ",
                bg='SteelBlue2'
            )
            questionType_label.pack()

            typeVar = StringVar()
            questionType_entry = Entry(
                root_input,
                textvariable=typeVar,
                font=("Cosmic Sans", 12),
                width = 110
            )
            questionType_entry.pack()

            question_label = Label(
                root_input, 
                text='Enter Question:', 
                bg='SteelBlue2'
            )
            question_label.pack()

            question = StringVar()
            question_entry = Entry(
                root_input, 
                textvariable= question, 
                font = ('Cosmic Sans', 12),
                width=110
            )
            question_entry.pack()

            option_1 = Label(
                root_input, 
                text='Enter Option 1:', 
                bg='SteelBlue2'
            )
            option_1.pack()

            option_one = StringVar()
            option_1_entry = Entry(
                root_input, 
                textvariable= option_one, 
                font = ('Cosmic Sans', 12),
                width=110
            )
            option_1_entry.pack()

            option_2 = Label(
                root_input, 
                text='Enter Option 2:', 
                bg='SteelBlue2'
            )
            option_2.pack()

            option_two = StringVar()
            option_2_entry = Entry(
                root_input, 
                textvariable= option_two, 
                font = ('Cosmic Sans', 12),
                width=110
            )
            option_2_entry.pack()

            option_3 = Label(
                root_input, 
                text='Enter Option 3:', 
                bg='SteelBlue2'
            )
            option_3.pack()

            option_three = StringVar()
            option_3_entry = Entry(
                root_input, 
                textvariable= option_three, 
                font = ('Cosmic Sans', 12),
                width=110
            )
            option_3_entry.pack()

            answer_name = Label(
                root_input, 
                text='Enter answer:', 
                bg='SteelBlue2'
            )
            answer_name.pack()


            answer_text = StringVar()
            answer_s_entry = Entry(
                root_input, 
                textvariable= answer_text, 
                font = ('Cosmic Sans', 12),
                width=110
            )
            answer_s_entry.pack()

            save_button = Button(
                root_input, 
                bg='light yellow', 
                activebackground='light yellow', 
                text='Save', 
                command=functools.partial(saveCreateQuestion, index, questionType_entry, question_entry,  option_1_entry, option_2_entry, option_3_entry, answer_s_entry, root_input)
            )
            save_button.pack()

            questionType_entry.focus_force()
            root_input.mainloop()

        elif mode == "edit": 
            value = questions_listbox.get(selected_que[0])
            root_input = Tk()
            root_input.title('create question')
            root_input.geometry('1000x300')
            root_input.iconbitmap("images/halo_shield.ico")
            root_input['bg'] = 'SteelBlue2'

            getList = questions_answers_list
            qt = value.split(" ---- ")
            q = qt[0]
            t = qt[1]
            for g in range(len(getList[index + 1])):
                if g % 2 != 0:
                    if getList[index + 1][g][0] == q:
                        o1 = getList[index + 1][g][1][0]
                        o2 = getList[index + 1][g][1][1]
                        o3 = getList[index + 1][g][1][2]
                        answer = getList[index + 1][g][2]
                        if(getList[index + 1][g][1].index(o1) == answer):
                            ans = o1
                        elif(getList[index + 1][g][1].index(o2) == answer):
                            ans = o2
                        else:
                            ans = o3
            original_value = [t, q, o1, o2, o3, ans]

            questionType_label = Label (
                root_input,
                text= "Enter Question Type: ",
                bg='SteelBlue2'
            )
            questionType_label.pack()

            typeVar = StringVar()
            questionType_entry = Entry(
                root_input,
                textvariable=typeVar,
                font=("Cosmic Sans", 12),
                width = 110
            )
            questionType_entry.insert(0,t)
            questionType_entry.pack()

            question_label = Label(
                root_input, 
                text='Enter Question:', 
                bg='SteelBlue2'
            )
            question_label.pack()

            question = StringVar()
            question_entry = Entry(
                root_input, 
                textvariable= question, 
                font = ('Cosmic Sans', 12),
                width=110
            )
            question_entry.insert(0,q)
            question_entry.pack()

            option_1 = Label(
                root_input, 
                text='Enter Option 1:', 
                bg='SteelBlue2'
            )
            option_1.pack()

            option_one = StringVar()
            option_1_entry = Entry(
                root_input, 
                textvariable= option_one, 
                font = ('Cosmic Sans', 12),
                width=110
            )
            option_1_entry.insert(0,o1)
            option_1_entry.pack()

            option_2 = Label(
                root_input, 
                text='Enter Option 2:', 
                bg='SteelBlue2'
            )
            option_2.pack()

            option_two = StringVar()
            option_2_entry = Entry(
                root_input, 
                textvariable= option_two, 
                font = ('Cosmic Sans', 12),
                width=110
            )
            option_2_entry.insert(0,o2)
            option_2_entry.pack()

            option_3 = Label(
                root_input, 
                text='Enter Option 3:', 
                bg='SteelBlue2'
            )
            option_3.pack()

            option_three = StringVar()
            option_3_entry = Entry(
                root_input, 
                textvariable= option_three, 
                font = ('Cosmic Sans', 12),
                width=110
            )
            option_3_entry.insert(0,o3)
            option_3_entry.pack()

            answer_name = Label(
                root_input, 
                text='Enter answer:', 
                bg='SteelBlue2'
            )
            answer_name.pack()


            answer_text = StringVar()
            answer_s_entry = Entry(
                root_input, 
                textvariable= answer_text, 
                font = ('Cosmic Sans', 12),
                width=110
            )
            answer_s_entry.insert(0,ans)
            answer_s_entry.pack()


            save_button = Button(
                root_input, 
                bg='light yellow', 
                activebackground='light yellow', 
                text='Save', 
                command=functools.partial(saveEditQuestion, index, original_value, questionType_entry, question_entry,  option_1_entry, option_2_entry, option_3_entry, answer_s_entry, root_input)
            )
            save_button.pack()

            questionType_entry.focus_force()
            root_input.mainloop()
        else:
            value = questions_listbox.get(selected_que[0])
            getList = questions_answers_list
            qt = value.split(" ---- ")
            q = qt[0]
            t = qt[1]
            for h in range(len(getList[index + 1])):
                if h % 2 != 0:
                    if getList[index + 1][h][0] == q and getList[index + 1][h -1] == t:
                        getList[index + 1].pop(h)
                        getList[index + 1].pop(h -1)

                        with open("db/questions_answers.json", "w") as tempF:
                            json.dump(getList, tempF)
                            success = "Question removed successfully"
                        root_que.destroy()
                        categorySelection()
                        success_show(success)



#<!------save new questions ---------->
def saveCreateQuestion(index, Qtype, Que, op1, op2, op3, ans, window):
    questionType = Qtype.get()
    question = Que.get()
    option1 = op1.get()
    option2 = op2.get()
    option3 = op3.get()
    answer = ans.get()
    error = ""
    if(questionType == "" or question == "" or answer == "" ):
        error = "Cannot Create Question, Question type and answer required"
        error_show(error)
    else:
        getList = questions_answers_list
        if(answer == option1):
            san = 0
        elif(answer == option2):
            san = 1
        elif(answer == option3):
            san = 2
        else:
            error = "answer does not match any option"
            error_show(error) 
        questions = questions_answers_list[index + 1]
        for i in range(len(questions)):   
            if i % 2 != 0:
                if questions[i][0] == question:
                    error = "Question already exist in database"
        if(error == ""):
            options = [option1, option2, option3]
            qu_opt_ans = [question, options, san]
            getList[index + 1].append(questionType)
            getList[index + 1].append(qu_opt_ans)
            
            with open("db/questions_answers.json", "w") as tempF:
                json.dump(getList, tempF)
                success = "New Question added to Question List successfully"
            window.destroy()
            root_que.destroy()
            categorySelection()
            success_show(success)
        else:
            error_show(error)

#<!---------save edited Question ---------->
def saveEditQuestion(index, org,  Qtype, Que, op1, op2, op3, ans, window):
    questionType = Qtype.get()
    question = Que.get()
    option1 = op1.get()
    option2 = op2.get()
    option3 = op3.get()
    answer = ans.get()
    error = ""
    if(questionType == "" or question == "" or answer == "" ):
        error = "Cannot Create Question, Question type and answer required"
        error_show(error)
    else:
        getList = questions_answers_list
        if(answer == option1):
            san = 0
        elif(answer == option2):
            san = 1
        elif(answer == option3):
            san = 2
        else:
            error = "answer does not match any option"
            error_show(error) 
        questions = getList[index + 1]
        for i in range(len(questions)):   
            if i % 2 != 0:
                if (questions[i - 1] == org[0] and questions[i][0] == org[1] and questions[i][1][0] == org[2]):
                    getList[index + 1][i-1] = questionType
                    getList[index + 1][i][0] = question
                    getList[index + 1][i][1][0] = option1
                    getList[index + 1][i][1][1] = option2
                    getList[index + 1][i][1][2] = option3
                    getList[index + 1][i][2] = san
                    with open("db/questions_answers.json", "w") as tempF:
                        json.dump(getList, tempF)
                        success = "New Question added to Question List successfully"
                    window.destroy()
                    root_que.destroy()
                    categorySelection()
                    success_show(success)
        

    
   
    



#<!--------Program Main Functions End--------------->

#<!-----------------------Program Functions End---------------------------->








#<!------ Program starts here------->
root = Tk()
root.title("Cyber User Awareness Question Editor")
root.geometry("400x190")
root.config(background="#ffffff")
root.iconbitmap("images/halo_shield.ico")
root.resizable(0,0)

hello_label = Label(
      root,
      text = "This is for admin use,\n to add/delete any questions and options",
      font = ("Comic sans MS", 11, "bold"),
      background = "#ffffff",
)
hello_label.place(x=60, y=45)

btnNext = Button(
    root,
    text = "Next",
    relief = FLAT,
    command = Authentication,

)
btnNext.place(x=170, y=140)


root.mainloop()
