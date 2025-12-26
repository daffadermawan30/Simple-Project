import tkinter as tk
import customtkinter as ctk
from PIL import Image
import random
from tkcalendar import DateEntry
import time
from tkinter import messagebox
import sqlite3

#Connect to the database
conn = sqlite3.connect('fintrack.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS account (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT NOT NULL UNIQUE, 
    password TEXT NOT NULL)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS financial_record (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    date DATE NOT NULL,
    description TEXT, 
    amount REAL NOT NULL,
    type TEXT CHECK(type IN ('income', 'expense')) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES account(id) ON DELETE CASCADE)
''')

conn.commit()
conn.close()

class App:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("Demo Aplikasi")
        self.window.geometry("1024x576")
        self.window.configure(bg="#64644e")
        self.window.resizable(False, False)
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")  

        self.quotes = [
            "Save first, spend later. - Unknown",
            "Wealth is the ability to fully experience life. - Thoreau",
            "Time is money. - Benjamin Franklin",
            "Risk comes from ignorance. - Warren Buffett",
            "A penny saved is a penny earned. - Benjamin Franklin",
            "Small steps lead to big gains. - Unknown",
            "Invest in yourself. - Unknown",
            "Plan your work, work your plan. - Napoleon Hill",
            "Less debt, more freedom. - Unknown",
            "The best investment is in yourself. - Warren Buffett",
            "Money grows when managed well. - Unknown",
            "Every expense tells a story. - Unknown",
            "Simplicity is the key to success. - Unknown",
            "Budgeting is the first step to wealth. - Unknown",
            "Opportunity favors the prepared. - Unknown",
            "Earn more, spend less. - Unknown",
            "Patience builds wealth. - Unknown",
            "Control your money, or it controls you. - Unknown",
            "Your habits define your future. - Unknown",
            "A strong foundation builds lasting wealth. - Unknown"]
        

        self.po_image = Image.open("finance.png") 
        self.po = ctk.CTkImage(self.po_image, size=(150,120))  
        
        self.image = Image.open("dashboard.png")  
        self.photo = ctk.CTkImage(self.image, size=(595,66))  

        self.logo_image = Image.open('logo.png')
        self.logo =ctk.CTkImage(self.logo_image, size=(320,576))

        self.hello_image = Image.open('header.png')
        self.hello = ctk.CTkImage(self.hello_image, size=(598,170))

        self.income_image =Image.open('income.png')
        self.income = ctk.CTkImage(self.income_image, size=(296,140))

        self.expense_image =Image.open('expense.png')
        self.expense = ctk.CTkImage(self.expense_image, size=(296,140))

        self.logout_image = Image.open('logout.png')
        self.logout = ctk.CTkImage(self.logout_image,size=(50,50))

        self.font1 = ("arial", 14, 'bold')
        self.font2 = ("arial", 49, 'bold')
        self.font3 = ("arial", 44,"bold")
        self.font4 = ("arial", 28, "bold")

        self.is_signup_mode = False
        self.current_user_id = None
        self.logged_in_username = None

        self.login_page()

    def login_page(self):
        
        def submit_click(event=None):
            conn = sqlite3.connect('fintrack.db')
            cursor = conn.cursor()

            username = entry_username.get()
            password = entry_password.get()

            self.logged_in_username = username

            if not username or not password:
                messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
                return
            
            elif self.is_signup_mode:
                try:
                    cursor.execute("INSERT INTO account (username, password) VALUES (?, ?)", (username, password))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Registration Successful." ,"Account successfully created!")
                    switch_to_login()
                    entry_username.delete(0, 'end')  
                    entry_password.delete(0, 'end')
                    
                except sqlite3.IntegrityError:
                    messagebox.showerror("Error","Username is already taken!")

            else:
                cursor.execute("SELECT id, username FROM account WHERE username = ?", (username,))
                user = cursor.fetchone()

                if user:
                    cursor.execute('''SELECT id, username FROM account WHERE username = ? AND password = ?''', (username, password))
                    user_with_pw=cursor.fetchone()

                    if user_with_pw:
                        self.current_user_id = user_with_pw[0]
                        messagebox.showinfo("Success", "LOGIN SUCCESSFUL!")
                        conn.close
                    
                        for widget in self.window.winfo_children():
                            widget.destroy()
                        self.main_page()
                        
                    else:    
                        messagebox.showerror("Login Failed", "PASSWORD INCORRECT!")
                        conn.close()

                else:
                    messagebox.showerror("Error", "ACCOUNT IS NOT EXIST!!")

        def switch_to_signup():
            self.is_signup_mode = True
            entry_username.focus()
            entry_username.delete(0, 'end')  # Menghapus teks di entry tanggal
            entry_password.delete(0, 'end')
            print(self.is_signup_mode)
            label_header.configure(text="SIGN UP")
            button_submit.configure(text="Sign up", font= self.font1)
            button_createaccount.configure(text="Already have an account",command=switch_to_login, width=190, height=38)

        def switch_to_login():
            self.is_signup_mode = False
            entry_username.focus()
            entry_username.delete(0, 'end')  
            entry_password.delete(0, 'end')
            print(self.is_signup_mode)
            label_header.configure(text="LOGIN")
            button_submit.configure(text="Login", font=self.font1)
            button_createaccount.configure(text="Register account",command=switch_to_signup, width=190, height=38)
        
        def focus_password(event):
            entry_password.focus()


        # Halaman login
        frame1 = tk.Frame(self.window, bg="#8EAC50")
        frame2 = ctk.CTkFrame(frame1, fg_color="#002250", border_width=4, border_color="#002250")

        frame1.place(x=0, y=0, relwidth=1, relheight=1)
        frame2.place(x=15, y=15, relheight=0.95)

        label_logo = ctk.CTkLabel(frame2, text='', image=self.logo)
        label_logo.pack(pady=5)

        label_header = ctk.CTkLabel(frame1, text="LOGIN", font=self.font2, text_color="#ffde59")
        entry_username = ctk.CTkEntry(frame1, width=350, height=45, placeholder_text="Username",fg_color="#E4F1AC",border_color="#002250")
        entry_password = ctk.CTkEntry(frame1, width=350, height=45, placeholder_text="Password", fg_color="#E4F1AC", border_color="#002250",show="*")

        button_submit = ctk.CTkButton(frame1, text='Login', width=190, height=38, command=submit_click,text_color="#E7FBB4", fg_color="#130170")
        label_pembatas = ctk.CTkLabel(frame1, text="-----------------------------", font=("arial", 35, "bold"), text_color="#ffde59")
        button_createaccount = ctk.CTkButton(frame1, text="Don't have an account?", width=190, height=38, text_color="#E7FBB4", cursor='hand2',command=switch_to_signup, fg_color="#130170")

        label_header.place(x=680, y=120, anchor='center')
        entry_username.place(x=680, y=270, anchor=tk.CENTER)
        entry_username.bind("<Return>", focus_password)
        entry_password.place(x=680, y=330, anchor=tk.CENTER)
        entry_password.bind("<Return>", submit_click)
        button_submit.place(x=588, y=380)
        label_pembatas.place(x=678, y=450, anchor='center')
        button_createaccount.place(x=588, y=480)

    def main_page(self):
        def logout():
            self.current_user_id = None
            self.logged_in_username = None
            
            for widget in self.window.winfo_children():
                widget.destroy()
           
            self.login_page()
            messagebox.showinfo("Logout", "You have been logged out!") 

        def search_transactions():
            conn = sqlite3.connect('fintrack.db')
            cursor = conn.cursor()

            date = combobox_CRUD_date.get() 

            if not date:
                messagebox.showerror("Error", "Tanggal tidak boleh kosong.")
                return

            query = '''
                SELECT date, description, amount, type
                FROM financial_record
                WHERE account_id = ? 
                AND date = ?
            '''
            
            try:
                cursor.execute(query, (self.current_user_id, date))
                results = cursor.fetchall()

                print(f"Results: {results}")  

                for item in self.tree.get_children():
                    self.tree.delete(item)

                if results:
                    for row in results:
                        self.tree.insert("", "end", values=row)  
                else:
                    messagebox.showinfo("Info", "Tidak ada hasil yang ditemukan.")

            except Exception as e:
                print(f"Error executing query: {e}")
                messagebox.showerror("Error", "Terjadi kesalahan saat menjalankan pencarian.")

            finally:
                conn.close()

        def update_total_expense():
            try:
                conn = sqlite3.connect('fintrack.db')
                cursor = conn.cursor()
                cursor.execute("SELECT SUM(amount) FROM financial_record WHERE type = 'expense'  AND account_id = ?", (self.current_user_id,))
                result = cursor.fetchone()
                total_expense = result[0] if result[0] else 0 
                conf_label_RP1.configure(text=f"Rp. {total_expense:,}")  
                conn.close()
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")

        def update_total_income():
            try:
                conn = sqlite3.connect('fintrack.db')
                cursor = conn.cursor()

                cursor.execute("SELECT SUM(amount) FROM financial_record WHERE type = 'income' AND account_id = ?", (self.current_user_id,))
                result = cursor.fetchone()
                total_income = result[0] if result[0] else 0  

                conf_label_RP.configure(text=f"Rp. {total_income:,}")  

                conn.close()
            except Exception as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")

        def delete():
            
            selected_item = self.tree.focus()  
            if not selected_item:
                messagebox.showerror("Error", "No item selected to delete!")
                return

            row = self.tree.item(selected_item)['values']  
            confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this record?")
            if not confirm:
                return

            try:
                conn = sqlite3.connect('fintrack.db')
                cursor = conn.cursor()

                cursor.execute("DELETE FROM financial_record WHERE date = ? AND description = ? AND amount = ? AND type = ?", (row[0], row[1], row[2], row[3]))
                conn.commit()
                conn.close()

                self.tree.delete(selected_item)
                clear()
                load_data()
                first_conditional_button()
                messagebox.showinfo("Success", "Record deleted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        def edit():
            

            selected_item = self.tree.focus()  
            if not selected_item:
                messagebox.showerror("Error", "No item selected to edit!")
                return

            row = self.tree.item(selected_item)['values'] 

            date = combobox_CRUD_date.get()
            amount = entry_CRUD_nominal.get()
            description = entry_CRUD_description.get()
            record_type = selected_choice.get()

            if not (date and description and amount and record_type):
                messagebox.showerror("Error", "Please enter all fields!")
                return

            if not amount.isdigit():
                messagebox.showerror("Error", "Amount must be numeric!")
                return

            try:
                conn = sqlite3.connect('fintrack.db')
                cursor = conn.cursor()

                cursor.execute('''UPDATE financial_record 
            SET date = ?, description = ?, amount = ?, type = ? 
            WHERE account_id = ? AND date = ? AND description = ? AND amount = ? AND type = ?''',(date, description, amount, record_type, self.current_user_id, row[0], row[1], row[2], row[3]))
                conn.commit()
                conn.close()

                self.tree.item(selected_item, values=(date, description, amount, record_type))
                clear()
                first_conditional_button()
                load_data()
                messagebox.showinfo("Success", "Record updated successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        def display_data(event=None):
            selected_item = self.tree.focus()
            if selected_item:
                second_conditional_button()
                row = self.tree.item(selected_item)['values']
                clear()
                combobox_CRUD_date.insert(0, row[0])
                entry_CRUD_nominal.insert(0, row[2])
                entry_CRUD_description.insert(0, row[1])
                selected_choice.set(row[3])
            else:
                pass

        def clear(clicked=None):
            if clicked:
                first_conditional_button()
                self.tree.selection_remove(self.tree.focus())
                self.tree.focus('')
            combobox_CRUD_date.delete(0, tk.END)
            entry_CRUD_nominal.delete(0, tk.END)
            entry_CRUD_description.delete(0, tk.END)
            selected_choice.set(None)
            
            
        def load_data():
            conn = sqlite3.connect("fintrack.db")
            cursor = conn.cursor()
            cursor.execute("SELECT date, description, amount, type FROM financial_record WHERE account_id = ?", (self.current_user_id,)) 
            rows = cursor.fetchall()
            conn.close()

            for item in self.tree.get_children():
                self.tree.delete(item)

            for row in rows:
                self.tree.insert("", 0, values=row)

            update_total_income()
            update_total_expense()

        def insert():
            date = combobox_CRUD_date.get()
            amount = entry_CRUD_nominal.get()
            description = entry_CRUD_description.get()
            type = selected_choice.get()
            
            if not (date and description and amount and type):
                messagebox.showerror('Error', 'Please enter all fields!')
                return
            if not amount.isdigit():
                messagebox.showerror('Error', 'Amount must be a numeric value!')
                return
    
            try:
                conn = sqlite3.connect('fintrack.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO financial_record (account_id, date, description, amount, type) VALUES (?, ?, ?, ?, ?)', (self.current_user_id, date, description, amount, type))
                conn.commit()
                clear()
                load_data()
                update_total_income()
                messagebox.showinfo('Success', 'Data has been added!')
                conn.close()
            except Exception as e:
                messagebox.showerror('Database Error', f'An error occurred: {e}')

        def clear_display():
            first_conditional_button()
            combobox_CRUD_date.delete(0, 'end')  
            entry_CRUD_nominal.delete(0, 'end')  
            entry_CRUD_description.delete(0, 'end')  
            selected_choice.set(None)  
            for selected_item in self.tree.selection():
                self.tree.selection_remove(selected_item)
            load_data()

        def update_time():
            current_time = time.strftime("%H:%M:%S") 
            label_clock.configure(text=current_time)  
            label_clock.after(1000, update_time) 

        def second_conditional_button():
            self.button_delete_CRUD.configure(state='normal')
            self.button_edit_CRUD.configure(state='normal')
            self.button_add_CRUD.configure(state='disabled')

        def first_conditional_button():
            self.button_delete_CRUD.configure(state='disabled')
            self.button_edit_CRUD.configure(state='disabled')
            self.button_add_CRUD.configure(state='normal')

        def next_patch_page():
            for widget in self.window.winfo_children():
                widget.destroy()

            self.next_patch()

        # Frame Background
        frame_bg = ctk.CTkFrame(self.window, fg_color='#c1ff72')
        frame_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame widget Sidebar
        frame_sidebar = ctk.CTkFrame(frame_bg,fg_color="#00712d", width=180, border_width=3,border_color="#33372C")
        label_sidebar = ctk.CTkLabel(frame_sidebar,image=self.po, text="", ) 
        button1_sidebar = ctk.CTkButton(frame_sidebar, text='Dashboard', fg_color='#264742', width=120, height=35, corner_radius=0, border_width=0, border_color= '#711DB0', state='disabled')
        button2_sidebar = ctk.CTkButton(frame_sidebar, text='Comingsoon', fg_color='#7ed957',width=120, height=35,corner_radius=0,border_width=0, command= next_patch_page)
        button_logout = ctk.CTkButton(frame_sidebar,text='',image=self.logout,width=40, height=40,bg_color="#00712d",fg_color="#00712d", command=logout)
        
        frame_sidebar.pack(padx=5, pady=10, side="left", fill="y")
        label_sidebar.pack(padx= 2.5, pady=(10,0), side="top", expand=0)
        button1_sidebar.pack(pady=(10,0), side="top", fill='x')
        button2_sidebar.pack(side="top", fill='x')
        button_logout.pack(pady= 5,side='bottom', expand=0)

        # Frame Input
        frame_input = ctk.CTkFrame(frame_bg, fg_color="#c1ff72", width=240)
        frame_title = ctk.CTkFrame(frame_input, width=240, height=245,fg_color='#c1ff72')
        frame_title_clock = ctk.CTkFrame(frame_title,fg_color="#eed1b0",width=240,height=50, corner_radius=5, border_width=3, border_color='#33372C')
        frame_finder = ctk.CTkFrame(frame_title, fg_color="#ffde59", width=240, height=185, corner_radius=5, border_width=3 , border_color='#33372C')
        frame_CRUD= ctk.CTkFrame(frame_input, width=230,height=0, fg_color='#d1c48f', corner_radius=3, border_width=3, border_color='#33372C')

        frame_input.pack(padx=(8,10), pady=(0,10), side="right", fill="y")
        frame_input.pack_propagate(False)
        frame_title.pack(side='top',pady=10)
        frame_title.pack_propagate(False)
        frame_title_clock.pack(side='top')
        frame_title_clock.pack_propagate(False)
        frame_finder.place(x=0, y=60)
        frame_CRUD.pack(pady=(5,0), side='bottom',fill='y', expand=1 )

        label_clock= ctk.CTkLabel(frame_title_clock, text='test', font=('arial', 20, 'bold'), corner_radius=15)
        label_clock.pack(side="top",pady=10)
        update_time()

        label_title_quote= ctk.CTkLabel(frame_title, text="Quote", font=("Arial", 36,'bold'),fg_color='#ffde59')
        label_title_quote.place(relx=0.5, rely=0.35, anchor="center")
        label_quote=ctk.CTkLabel(frame_finder, text=random.choice(self.quotes), font=("Arial", 15, "normal"), wraplength=200 )
        label_quote.place(relx=0.1,rely=0.1, relwidth=0.8,relheight=0.8)

        # CRUD
        frame_CRUD.columnconfigure((0,1,2,3,4,5,6), weight=1)
        frame_CRUD.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight=1)

        selected_choice = tk.StringVar()

        label_data_entry = ctk.CTkLabel(frame_CRUD, text="Data Entry", font=("Arial", 20,'bold'))
        label_CRUD_date= ctk.CTkLabel(frame_CRUD, text="Date", font=("Arial", 15))
        combobox_CRUD_date = DateEntry(frame_CRUD, date_pattern="yyyy-mm-dd", background='darkblue', foreground='yellow', selectbackground="blue", fieldbackground='#d9d9d9')
        label_CRUD_nominal = ctk.CTkLabel(frame_CRUD, text= "Nominal :")
        entry_CRUD_nominal = ctk.CTkEntry(frame_CRUD, width=100)
        label_CRUD_description = ctk.CTkLabel(frame_CRUD, text= "Description:")
        entry_CRUD_description = ctk.CTkEntry(frame_CRUD, width=100)
        label_type = ctk.CTkLabel(frame_CRUD, text="Type")
        radiobutton_CRUD1 = ctk.CTkRadioButton(frame_CRUD,text="Income", value="income",variable=selected_choice)
        radiobutton_CRUD2 = ctk.CTkRadioButton(frame_CRUD, text="Expense", value="expense", variable=selected_choice )
        self.clear_button= ctk.CTkButton(frame_CRUD, text="CLEAR",corner_radius=0,fg_color="red",command=clear_display, text_color="black")
        self.button_add_CRUD = ctk.CTkButton(frame_CRUD, text="Add",command= insert ,corner_radius=0, fg_color="white", text_color='black')
        self.button_edit_CRUD = ctk.CTkButton(frame_CRUD, text="Update", command= edit,corner_radius=0, fg_color="white", text_color='black',)
        self.button_delete_CRUD = ctk.CTkButton(frame_CRUD, text="Delete", command = delete,corner_radius=0, fg_color="white", text_color='black', )
        button_find_CRUD = ctk.CTkButton(frame_CRUD, text="Find", command = search_transactions,corner_radius=0, fg_color="pink", text_color='black')
        
        #layout finder, progressbar, CRUD
        label_data_entry.grid(padx=3,pady=(7,0), row=0, column=0, columnspan=7,rowspan=2, sticky="nsew")
        label_CRUD_date.grid(padx=3,row=2, column=0,columnspan=3, )
        combobox_CRUD_date.grid(padx=3, row=3, column=0,columnspan=3)
        
        label_CRUD_nominal.grid(row=4,column=0, columnspan=3)
        entry_CRUD_nominal.grid(padx=3,row=5,column=0, columnspan=3)
        label_CRUD_description.grid(row=6,column=0,columnspan=3)
        entry_CRUD_description.grid(padx=3,row=7,column=0, columnspan=3)
        label_type.grid(row=3, column=3, columnspan=3, rowspan=2)
        radiobutton_CRUD1.grid(row=4, column=3, columnspan=4, rowspan=2)
        radiobutton_CRUD2.grid(row=5, column=3, columnspan=4,rowspan=2)
        self.clear_button.grid(padx=(0,3),row=8, column=5, columnspan=2)
        self.button_add_CRUD.grid(padx= (3,0),row=9, column=0,columnspan=4)
        self.button_edit_CRUD.grid(padx=(0,3),pady=(0,7),row=10, column=4, columnspan=3)
        self.button_delete_CRUD.grid(padx= (3,0),pady=(0,7),row=10, column=0, columnspan=4, )
        button_find_CRUD.grid(padx=(0,3),row=9, column=4, columnspan=3)

        # Frame Header Bar
        frame_headbar = ctk.CTkFrame(frame_bg, height=60, fg_color="#5DB996", border_width=3, border_color='#33372C')  
        label_dashboard = ctk.CTkLabel(frame_headbar, image=self.photo, text='')
        
        frame_headbar.pack(pady=(10,5), side="top", fill='x')
        frame_headbar.pack_propagate(False)
        label_dashboard.place(relx=0.5,rely=0.5, relheight= 0.90, relwidth=0.96, anchor='center')

        # Frame Content 1
        frame_content = ctk.CTkFrame(frame_bg, width =598 , height=170, fg_color="blue", border_width=3, border_color='#33372C')
        label_hello = ctk.CTkLabel(frame_content, text="", image= self.hello,)
        label_username = ctk.CTkLabel(frame_content, text=self.logged_in_username, font=self.font3, fg_color='#5eaab2')

        frame_content.pack(pady=(0, 5), side='top', fill=None, expand=0)
        frame_content.pack_propagate(False)
        frame_content.pack(pady=(0, 5), side='top', fill=None, expand=0)
        frame_content.pack_propagate(False)
        label_hello.place(relx=0.5,rely=0.4975, relwidth=0.99 ,relheight=0.97, anchor='center')
        label_username.place(x=17, y=85,  )
        
        # frame widget Content 2 (Subframes)
        frame_content1 = ctk.CTkFrame(frame_bg, fg_color="#c1ff72", width=596, height=140)
        frame_a = ctk.CTkFrame(frame_content1, fg_color="purple", width=296, height=140, corner_radius=3)
        label_income= ctk.CTkLabel(frame_a,text='', image=self.income)
        frame_b = ctk.CTkFrame(frame_content1, fg_color="purple", width=296, height=140,)
        label_expense= ctk.CTkLabel(frame_b,text='', image=self.expense)

        # layout frame widget content 2
        frame_content1.pack(pady=(0,5), side='top', expand=0)
        frame_content1.pack_propagate(False)
        frame_a.place(x=0,y=0)
        frame_a.pack_propagate(False)
        label_income.place(x=0,y=0)
        frame_b.place(x=301, y=0)
        frame_b.pack_propagate(False)
        label_expense.place(x=0,y=0)

        # widget content 2 a 
        conf_label_RP = ctk.CTkLabel(frame_a, text='Rp. 0' , font= self.font4, fg_color = '#06d001')
        conf_label_RP.place(x=14,y=61, anchor= 'w')

        # widget content 2 b
        conf_label_RP1 = ctk.CTkLabel(frame_b, text='Rp. 0', font= self.font4, fg_color='#fb4141')
        conf_label_RP1.place(x=14,y=61, anchor= 'w')

        # Frame Content 3
        frame_content2 = ctk.CTkFrame(frame_bg, height=170, fg_color="red")
        frame_content2.pack(pady=(0,5), side='top', fill='x', expand=0)
        frame_content2.pack_propagate(False)

        style= tk.ttk.Style(self.window)
        style.theme_use('clam')
        style.configure('Treeview',font=('arial', 10),foreground='black',background='#ffde59', fieldbackground='#d9d9d9',borderwidth=0)
        
        style.configure('Treeview.Heading', background = '#B1F0F7')
        style.map('Treeview', background=[('selected', '#685752')])

        self.tree = tk.ttk.Treeview(frame_content2, columns=("DATE", "DESCRIPTION", "AMOUNT", "TYPE"), show="headings")

        self.tree.column('DATE', anchor=tk.CENTER, width=80)
        self.tree.column('DESCRIPTION', anchor=tk.CENTER, width=80)
        self.tree.column('AMOUNT', anchor=tk.CENTER, width=80)
        self.tree.column('TYPE', anchor=tk.CENTER, width=80)

        self.tree.heading("DATE", text="Date")
        self.tree.heading("DESCRIPTION", text="Description")
        self.tree.heading("AMOUNT", text="Amount")
        self.tree.heading("TYPE", text="Type")
        self.tree.pack(fill='both', expand=True)
        self.tree.bind('<ButtonRelease>', lambda event : display_data(event))

        load_data()
        first_conditional_button()
        combobox_CRUD_date.delete(0, tk.END)

    def next_patch(self):

        def dashboard_page():
            for widget in self.window.winfo_children():
                widget.destroy()
            
            self.main_page()
        
        # Frame Background
        frame_bg = ctk.CTkFrame(self.window, fg_color='#c1ff72')
        frame_bg.place(x=0, y=0, relwidth=1, relheight=1)

        #label
        label = ctk.CTkLabel(frame_bg, text='Stay Tune...', font= ("arial", 30, 'bold'))
        label.place(relx=0.5, rely=0.5)

        # Frame widget Sidebar
        frame_sidebar = ctk.CTkFrame(frame_bg,fg_color="#00712d", width=180, border_width=3,border_color="#33372C")
        label_sidebar = ctk.CTkLabel(frame_sidebar,image=self.po, text="", ) 
        button1_sidebar = ctk.CTkButton(frame_sidebar, text='Dashboard', fg_color='#7ed957' ,width=120, height=35, corner_radius=0, border_width=0, border_color= '#711DB0', command=dashboard_page)
        button2_sidebar = ctk.CTkButton(frame_sidebar, text='Comingsoon', fg_color='#264742',width=120, height=35,corner_radius=0,border_width=0, state='disabled')
        button_logout = ctk.CTkButton(frame_sidebar,text='',image=self.logout,width=40, height=40,bg_color="#00712d",fg_color="#00712d", command=self.logout)
        
        frame_sidebar.pack(padx=5, pady=10, side="left", fill="y")
        label_sidebar.pack(padx= 2.5, pady=(10,0), side="top", expand=0)
        button1_sidebar.pack(pady=(10,0), side="top", fill='x')
        button2_sidebar.pack(side="top", fill='x')
        button_logout.pack(pady= 5,side='bottom', expand=0)
        
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()