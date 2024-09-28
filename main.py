from tkinter import messagebox
import random
import tkinter
from tkinter import END
import json

def find_pass():
    try:

        ans = websiteentry.get()

        with open("file.json", "r") as df:
            data = json.load(df)

    except:
        messagebox.showerror(title="Error", message="No data found")
    else:
        if ans in data:
            messagebox.showinfo(title=ans,
                                message=f"Username : {data[ans]["email"]} \n Password : {data[ans]["password"]} ")
        else:
            messagebox.showerror(title="Error", message=f"No data found for {ans}")






# --------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():
    passwntry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    list1 = [random.choice(letters) for x in range(nr_numbers)]
    list2 = [random.choice(numbers) for x in range(nr_symbols)]
    list3 = [random.choice(symbols) for x in range(nr_letters)]

    password_list = list1 + list2+ list3

    random.shuffle(password_list)

    password = "".join(password_list)

    passwntry.insert(0, password)





# ---------------------------- SAVE PASSWORD ------------------------------- #
def savefile():
    website_entry = websiteentry.get()
    email_entry = emailentry.get()
    passwntry11 = passwntry.get()
    data_dict = {
        website_entry: {"email" : email_entry,
                        "password": passwntry11
                                 }}


    if len(website_entry) == 0 or len(passwntry11)==0:
        messagebox.showerror(title="ERROR", message="Please do no leave any of the field empty")
    else:

        try:
            with open("file.json", "r") as file:
                main_file = json.load(file)
        except:
            with open("file.json","w") as file:
                json.dump(data_dict, file)
        else:
            main_file.update(data_dict)

            with open("file.json", "w") as file:
                json.dump(main_file, file, indent=4)

        finally:
            websiteentry.delete(0, END)
            emailentry.delete(0,END)
            passwntry.delete(0,END)








# ---------------------------- UI SETUP ------------------------------- #


window =  tkinter.Tk()
window.title("Password Generator")
window.config(pady=50,padx=50)

canvas = tkinter.Canvas(height=200, width=200)
image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image)
canvas.grid(row=0, column=1)

website = tkinter.Label(text="Website:")
website.grid(row=1, column=0)
websiteentry = tkinter.Entry(width=21)
websiteentry.focus()

websiteentry.grid(row=1, column=1, columnspan=1)

email = tkinter.Label(text="Email/Username:")
email.grid(row=2,column=0)
emailentry = tkinter.Entry(width=38)
emailentry.grid(row=2, column=1, columnspan=2)

passw = tkinter.Label(text="Password:")
passw.grid(row=3, column=0)
passwntry = tkinter.Entry(width=21)
passwntry.grid(row=3,column=1)

generate_pass = tkinter.Button(text="Generate Password", command=pass_gen)
generate_pass.grid(row=3, column=2)


add_button = tkinter.Button(text="Add", width=36, command=savefile)
add_button.grid(row=4, column=1, columnspan=2)

search_button = tkinter.Button(text="Search", width=13, command=find_pass)
search_button.grid(row=1, column=2)




window.mainloop()