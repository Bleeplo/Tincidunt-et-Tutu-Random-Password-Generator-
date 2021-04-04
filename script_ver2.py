import os, random #imports os & random module
from tkinter import *
from tkinter import ttk
import tkinter
def resource_path(relative_path):   #so when turning script into a exe, allows us to use other files, such as images
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    
#### (Start) Tkinter stuff
### Resources
root = tkinter.Tk()
window_icon = resource_path('icon(ico).ico')#just our resource paths
def button_command():   #our command when the user presses the button
    file_directory_input = file_direct_entry_box.get()
    num_of_characters = int(char_file_direct.get())
    password_name = password_name_entry_box.get()

    ### Directory
    os.chdir(file_directory_input)        # find directery of folder
    save_path = open('passwords.txt', 'a') # creates the txt (if it doesn't exist); opens it up and writes/edits the txt document
    
    ### Generating random password
    for i in range(num_of_characters):
        crypt_letter_characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z', 
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # Equal (50/50) chance to get a capital or lowercase english letter
        crypt_numeric_characters = ['1','2','3','4','5','6','7','8','9','0',]
        crypt_special_characters = ['!','@','#','$','%','^','&','*','(',')']

        # Because there aren't as many number keys as their are letters for the english alphabet. Putting them in categories give it a 1/3 chance of picking a number,special character, or a letter
        crypt_characters = random.choice(crypt_letter_characters), random.choice(crypt_numeric_characters), random.choice(crypt_special_characters)

        ### Saves random generated password
        save_path.write(str(random.choice(crypt_characters)))

        ### Adding onto the txt document
    save_path.write("   | ");save_path.write(password_name)
    save_path.write("\n")
    save_path.close

save_button = Button(root, text="Save", command=button_command) #button

##We have 3 different text_w_entryboxs because each entry box has different function
def text_w_entrybox_file_direct(text_label_sentence, text_row, text_rowspan, text_column, text_columnspan): #file directory
    text_label = Label(root, text=text_label_sentence,
    bg="white",
    fg="black",
    font="none 15").grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan,)
def text_w_entrybox_char_amount(text_label_sentence, text_row, text_rowspan, text_column, text_columnspan):
    text_label = Label(root, text=text_label_sentence,
    bg="white",
    fg="black",
    font="none 15").grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan,)
def text_w_entrybox_password_name(text_label_sentence, text_row, text_rowspan, text_column, text_columnspan):
    text_label = Label(root, text=text_label_sentence,
    bg="white",
    fg="black",
    font="none 15").grid(row=text_row, rowspan=text_rowspan, column=text_column, columnspan=text_columnspan,)

### Window Info
root.geometry('') #width & height of window
root.title('Tincidunt et Tutu') #title of window
root.iconbitmap(window_icon)       #icon of image
root.configure(background='white') #makes background white
root.resizable(0,0)                #makes window unmovable

### What is Displayed/UI
text_w_entrybox_file_direct("File directory:", 1, 1, 1, 1) #File directory
text_w_entrybox_char_amount("Number of Characters:", 2, 1, 1, 1) #Number of Characters
text_w_entrybox_password_name("Name of Password:", 3, 1, 1, 1) #Name of Password
save_button.grid(row=4, column=2, sticky=W) #position of the button
file_direct_entry_box = Entry(root, width=35)                                                               # Entry box for the file directory
file_direct_entry_box.grid(row=1, rowspan=1, column=2, columnspan=1, sticky=W)                              # Entry box for the file directory
char_file_direct = Entry(root, width=35)                                                           # Entry box for the character amount
char_file_direct.grid(row=2, rowspan=1, column=2, columnspan=1, sticky=W)                          # Entry box for the character amount
password_name_entry_box = Entry(root, width=35)                                                           # Entry box for the password name
password_name_entry_box.grid(row=3, rowspan=1, column=2, columnspan=1, sticky=W)                          # Entry box for the password name

### Main loop
root.mainloop() #keeps the window open forever, till closed
#### (End) Tkinter stuff