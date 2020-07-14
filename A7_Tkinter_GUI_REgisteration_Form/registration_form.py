from tkinter import *
from re import match as re_match

# Alaa' Omar
# Simple Registration Form using Tkinter


def display_root_screan():
    """ This function display the root screan """
    root = Tk()
    root.geometry('220x200')
    root.title('Simple Registration Form')
    global user_name
    global user_job
    global user_salary
    global register_status

    user_name = StringVar()
    user_job = StringVar()
    user_salary = StringVar()
    register_status = StringVar()

    Label(root, text='Please fill in the information below:').grid(
        row=0, columnspan=2)
    Label(root, text="Name:").grid(row=1, sticky=E)
    Entry(root, textvariable=user_name).grid(row=1, column=1, padx=2, pady=2,
                                             sticky=NSEW)

    Label(root, text="Job:").grid(row=2, sticky=E)
    Entry(root, textvariable=user_job).grid(
        row=2, column=1, padx=2, pady=2, sticky=NSEW)

    Label(root, text="Salary:").grid(row=3, sticky=E)
    Entry(root, textvariable=user_salary).grid(
        row=3, column=1, padx=2, pady=2, sticky=NSEW)

    btn_register = Button(root, text="Register", command=register_user)
    btn_register.grid(
        row=4, column=1, padx=2, pady=2, sticky=NSEW)
    btn_register.configure(relief='raised', cursor='hand2')
    Label(
        root, textvariable=register_status, fg='green', font=("Calibri", 10), wraplength=300, justify="center").grid(row=5, padx=2, pady=2, sticky=NSEW, columnspan=2)
    root.mainloop()


def register_user():
    ''' This function updates the register_status variable with success/fail register message '''
    if is_empty():
        register_status.set(
            'Register Faild,\n make sure all the fileds \nare filled with the\n appropriate values')
    else:
        print('Button clicked')
        print(f'Welcome {user_name.get()}, you have successfully registerd')
        register_status.set(
            f'Welcome {user_name.get()},\n you have successfully registerd\n with job title {user_job.get()}\n and salary ={user_salary.get()}')


def is_empty():
    ''' This function returns a boolean value, True if the registeration fileds are filled with the appropriate values, else it returs fulse '''
    is_entry_empty = len(user_job.get()) == 0 or len(user_name.get()) == 0
    is_salary_empty = user_salary.get() == 0.0 or not is_number_regex(user_salary.get())
    is_wedgit_empty = is_entry_empty or is_salary_empty

    return is_wedgit_empty


def is_number_regex(s):
    """ Returns True is string is a number. """
    if re_match("^\d+?\.\d+?$", s) is None:
        return s.isdigit()
    return True


display_root_screan()
