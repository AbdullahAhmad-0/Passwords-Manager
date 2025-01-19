# Actual Code Written On 2019 When I'm 15
import sqlite3, pandas, csv
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox,filedialog

class PassMngClass:
    def __init__(self,root) -> None:
        self.root=root
        self.root.geometry("1110x500+220+140")
        self.root.title("Password Manager - Abdullah Ahmad")
        self.root.resizable(0,0)
        self.root.config(bg='white')
        self.root.focus_force()
        self.root.iconbitmap('ico.ico')
        try:
            self.con = sqlite3.connect('password.icd')
            self.cur = self.con.cursor()
            self.cur.execute('''
                CREATE TABLE IF NOT EXISTS pwd (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    pas TEXT,
                    det TEXT,
                    o TEXT,
                    t TEXT
                )
            ''')
            self.con.commit()
        except Exception as e:
            print(e)

        try:
            f = open('set.icd','r')
            f = f.read()
            o,t = f.split('-+|ICD|+-') 
        except:
            o = ''
            t = ''

        # all variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_pass=StringVar()
        self.var_detail=StringVar()
        self.var_1=StringVar()
        self.var_2=StringVar()

        #database connection
        
        try:
            self.cur.execute("select id from pwd")
            self.con.commit()
            row=self.cur.fetchall()
            for i in row:
                for i in i:
                    print(i)
            self.var_id.set(i+1)
        except:
            self.var_id.set(1)
        
        #==== search ====#
        lbl_search=Label(self.root,bg='white',text='Search By Name',font=('goudy old style',15))
        lbl_search.place(x=420,y=80)

        txt_search = Entry(self.root,textvariable=self.var_searchtxt,bg='lightyellow',font=('goudy old style',15))
        txt_search.place(x=600,y=80,height=30,width=450)
        txt_search.bind('<KeyRelease>', self.search)

        # -==== title =====- #
        title = Label(self.root,text='Password Manager',font=('goudy old style',20,'bold'),bg='#0f4d7d',fg='white').place(x=50,y=10,width=1000,height=40)

        # ==== content ==== #
        # ==== row 1 ==== #
        lbl_supplier_invoice = Label(self.root,text='Password ID',font=('goudy old style',15),bg='white').place(x=50,y=80)
        txt_supplier_invoice = Entry(self.root,textvariable=self.var_id,state=DISABLED,font=('goudy old style',15),bd=0,disabledbackground='white',disabledforeground='black').place(x=180,y=80,width=40)

        # ==== row 2 ==== #
        lbl_name = Label(self.root,text='User Name',font=('goudy old style',15),bg='white').place(x=50,y=120)
        txt_name = Entry(self.root,textvariable=self.var_name,font=('goudy old style',15),bg='lightyellow').place(x=180,y=120,width=230)
        
        # ==== row 3 ==== #
        lbl_contact = Label(self.root,text='Password',font=('goudy old style',15),bg='white').place(x=50,y=160)
        txt_contact = Entry(self.root,textvariable=self.var_pass,font=('goudy old style',15),bg='lightyellow').place(x=180,y=160,width=230)
        
        # ==== row 4 ==== #
        lbl_contact = Label(self.root,text='Details',font=('goudy old style',15),bg='white').place(x=50,y=200)
        txt_contact = Entry(self.root,textvariable=self.var_detail,font=('goudy old style',15),bg='lightyellow').place(x=180,y=200,width=230)
        
        # ==== row 5 ==== #
        lbl_desc = Label(self.root,text=o,font=('goudy old style',15),bg='white').place(x=50,y=240)
        txt_desc= Entry(self.root,textvariable=self.var_1,font=('goudy old style',15),bg='lightyellow').place(x=180,y=240,width=230)
        
        # ==== row 6 ==== #
        lbl_desc = Label(self.root,text=t,font=('goudy old style',15),bg='white').place(x=50,y=280)
        txt_desc= Entry(self.root,textvariable=self.var_2,font=('goudy old style',15),bg='lightyellow').place(x=180,y=280,width=230)

        # buttons
        btn_add = Button(self.root,text='Save',bg='#2196f3',fg='white',command=self.add,font=('goudy old style',15),activebackground='#2196f3',cursor='hand2').place(x=180,y=370,width=110,height=35)
        btn_update = Button(self.root,text='Update',bg='#4caf50',fg='white',command=self.update,font=('goudy old style',15),activebackground='#4caf50',cursor='hand2').place(x=300,y=370,width=110,height=35)
        btn_delete = Button(self.root,text='Delete',bg='#f44336',fg='white',command=self.delete,font=('goudy old style',15),activebackground='#f44336',cursor='hand2').place(x=180,y=410,width=110,height=35)
        btn_clear = Button(self.root,text='Clear',bg='#607d8b',fg='white',command=self.clear,font=('goudy old style',15),activebackground='#607d8b',cursor='hand2').place(x=300,y=410,width=110,height=35)

        # tree view emp details

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=420,y=120,width=630,height=350)

        scrooly=Scrollbar(emp_frame,orient=VERTICAL)
        scroolx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.SupplierTable=ttk.Treeview(emp_frame,columns=('1','2','3','4','5','6'),yscrollcommand=scrooly.set,xscrollcommand=scroolx.set)
        scrooly.pack(side=RIGHT,fill=Y)
        scroolx.pack(side=BOTTOM,fill=X)
        scrooly.config(command=self.SupplierTable.yview)
        scroolx.config(command=self.SupplierTable.xview)
        self.SupplierTable.heading('1',text='ID')
        self.SupplierTable.heading('2',text='User')
        self.SupplierTable.heading('3',text='Password')
        self.SupplierTable.heading('4',text='Details')
        self.SupplierTable.heading('5',text=o)
        self.SupplierTable.heading('6',text=t)
        self.SupplierTable["show"]="headings"
        self.SupplierTable.column('1',width=20)
        self.SupplierTable.column('2',width=100)
        self.SupplierTable.column('3',width=100)
        self.SupplierTable.column('4',width=200)
        self.SupplierTable.column('5',width=80)
        self.SupplierTable.column('6',width=80)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        fileMenu = Menu(menubar)

        fileMenu = Menu(fileMenu)
        fileMenu.add_command(label="Save To PDF")
        fileMenu.add_command(label="Save To Excel(CSV)", command=self.exportcsv)
        fileMenu.add_command(label="Save To Excel(XLSX)", command=self.exportexcel)
        fileMenu.add_command(label="Save To HTML", command=self.exporthtml)
        fileMenu.add_command(label="Save To TXT", command=self.exporttxt)
        fileMenu.add_command(label="Copy To Clipboard", command=self.exportclip)
        fileMenu.add_separator()
        fileMenu.add_command(label="Import From CSV", command=self.importcsv)
        fileMenu.add_command(label="Import From Chrome DB")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=0, command=exit)
        menubar.add_cascade(label="File", underline=0, menu=fileMenu)
        menubar.add_cascade(label="Setting", underline=0, command=PassMngClass.setting)

# =================================================================================================================
    def exportcsv(self):
        ff = filedialog.asksaveasfilename()
        gg = self.SupplierTable.get_children()
        try:
            f = open('set.icd','r')
            f = f.read()
            o1,t1 = f.split('-+|ICD|+-') 
        except:
            o1=''
            t1=''
        id,name,pas,det,o,t=[],[],[],[],[],[]
        for i in gg:
            content = self.SupplierTable.item(i)
            pp = content['values']
            id.append(pp[0]),name.append(pp[1]),pas.append(pp[2]),det.append(pp[3]),o.append(pp[4]),t.append(pp[5])
        dd = ['Id','Name','Password','Details',o1,t1]
        df = pandas.DataFrame(list(zip(id,name,pas,det,o,t)),columns=dd)
        paths = r'{}.csv'.format(ff)
        df.to_csv(paths,index=False)
        messagebox.showinfo('Notifications', 'Password Saved Successfully\n{}'.format(paths))

    def exporthtml(self):
        ff = filedialog.asksaveasfilename()
        gg = self.SupplierTable.get_children()
        try:
            f = open('set.icd','r')
            f = f.read()
            o1,t1 = f.split('-+|ICD|+-') 
        except:
            o1=''
            t1=''
        id,name,pas,det,o,t=[],[],[],[],[],[]
        for i in gg:
            content = self.SupplierTable.item(i)
            pp = content['values']
            id.append(pp[0]),name.append(pp[1]),pas.append(pp[2]),det.append(pp[3]),o.append(pp[4]),t.append(pp[5])
        dd = ['Id','Name','Password','Details',o1,t1]
        df = pandas.DataFrame(list(zip(id,name,pas,det,o,t)),columns=dd)
        paths = r'{}.html'.format(ff)
        df.to_html(paths,index=False)
        messagebox.showinfo('Notifications', 'Password Saved Successfully\n{}'.format(paths))

    def exportexcel(self):
        ff = filedialog.asksaveasfilename()
        gg = self.SupplierTable.get_children()
        try:
            f = open('set.icd','r')
            f = f.read()
            o1,t1 = f.split('-+|ICD|+-') 
        except:
            o1=''
            t1=''
        id,name,pas,det,o,t=[],[],[],[],[],[]
        for i in gg:
            content = self.SupplierTable.item(i)
            pp = content['values']
            id.append(pp[0]),name.append(pp[1]),pas.append(pp[2]),det.append(pp[3]),o.append(pp[4]),t.append(pp[5])
        dd = ['Id','Name','Password','Details',o1,t1]
        df = pandas.DataFrame(list(zip(id,name,pas,det,o,t)),columns=dd)
        paths = r'{}.xlsx'.format(ff)
        df.to_excel(paths,index=False)
        messagebox.showinfo('Notifications', 'Password Saved Successfully\n{}'.format(paths))

    def exporttxt(self):
        ff = filedialog.asksaveasfilename()
        gg = self.SupplierTable.get_children()
        try:
            f = open('set.icd','r')
            f = f.read()
            o1,t1 = f.split('-+|ICD|+-') 
        except:
            o1=''
            t1=''
        id,name,pas,det,o,t=[],[],[],[],[],[]
        for i in gg:
            content = self.SupplierTable.item(i)
            pp = content['values']
            id.append(pp[0]),name.append(pp[1]),pas.append(pp[2]),det.append(pp[3]),o.append(pp[4]),t.append(pp[5])
        dd = ['Id','Name','Password','Details',o1,t1]
        df = pandas.DataFrame(list(zip(id,name,pas,det,o,t)),columns=dd)
        a = df.to_string(index=False)
        paths = r'{}.txt'.format(ff)
        f = open(paths,'w')
        f.write(a)
        f.close()
        messagebox.showinfo('Notifications', 'Password Saved Successfully\n{}'.format(paths))

    def exportclip(self):
        gg = self.SupplierTable.get_children()
        try:
            f = open('set.icd','r')
            f = f.read()
            o1,t1 = f.split('-+|ICD|+-') 
        except:
            o1=''
            t1=''
        id,name,pas,det,o,t=[],[],[],[],[],[]
        for i in gg:
            content = self.SupplierTable.item(i)
            pp = content['values']
            id.append(pp[0]),name.append(pp[1]),pas.append(pp[2]),det.append(pp[3]),o.append(pp[4]),t.append(pp[5])
        dd = ['Id','Name','Password','Details',o1,t1]
        df = pandas.DataFrame(list(zip(id,name,pas,det,o,t)),columns=dd)
        df.to_clipboard(index=False)
        messagebox.showinfo('Notifications', 'Password Copy To Clipboard Successfully')

    def importcsv(self):
        try:
            f = open('set.icd','r')
            f = f.read()
            o,t = f.split('-+|ICD|+-') 
        except:
            o=''
            t=''
        msg = messagebox.askyesno('Are You Sure',"Are You Sure You Want To Import CSV File\nDon't Worry It's Not Delete Your Previous Passwords",parent=self.root)
        if msg == True:
            messagebox.showinfo('Read Me',"Make Sure Your First Row (Header) Is Empty Or With Column Names\nMake Sure Your First Column Is A Sr No Or Empty\nThe Program Not Copy First Row And First Column\nMake Sure Your Column Are Sorted According To\n\tID\tName\tPassword\tDetails\t"+o+'\t'+t,parent=self.root)
            ff = filedialog.askopenfilename(title='Open CSV File',filetypes=(('CSV File','*.csv'),('All Files','*.*')))
            a_file = open(ff)
            rows = csv.reader(a_file)
            next(rows, None)
            rows = list(rows)
            row = list()
            for i in rows:
                a = i[1],i[2],i[3],i[4],i[5]
                row.append(list(a))
            self.cur.executemany("INSERT INTO pwd (name,pas,det,o,t) VALUES (?, ?, ?, ?, ?)", row)
            self.con.commit()
            self.show()

    def add(self):
        try:
            if self.var_id.get()=='':
                messagebox.showerror('Error','ID IS REQUIRED',parent=self.root)
            elif self.var_name.get()=='':
                messagebox.showerror('Error','USER NAME IS REQUIRED',parent=self.root)
            elif self.var_pass.get()=='':
                messagebox.showerror('Error','PASSWORD IS REQUIRED',parent=self.root)
            elif self.var_detail.get()=='':
                messagebox.showerror('Error','DETAILS IS REQUIRED',parent=self.root)
            else:
                self.cur.execute("select * from pwd where id='"+self.var_id.get()+"'")
                row=self.cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error','This Id is Already Assigned, try New One',parent=self.root)
                else:
                    self.cur.execute("insert into pwd (id,name,pas,det,o,t) values('"+self.var_id.get()+"','"+self.var_name.get()+"','"+self.var_pass.get()+"','"+self.var_detail.get()+"','"+self.var_1.get()+"','"+self.var_2.get()+"')")
                    self.cur.execute("select id from pwd")
                    row=self.cur.fetchall()
                    for i in row:
                        for i in i:
                            print(i)
                    self.var_id.set(i+1)
                    self.con.commit()
                    r = messagebox.askyesno('Success','Password Added Successfully\nAre You Want To Clear Field',parent=self.root)
                    if r==TRUE:
                        self.var_name.set('')
                        self.var_pass.set('')
                        self.var_detail.set("")
                        self.var_1.set("")
                        self.var_2.set("")
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',ex,parent=self.root)

    def show(self):
        try:
            self.cur.execute('select id,name,pas,det,o,t from pwd')
            rows=self.cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror('Error',ex,parent=self.root)

    def get_data(self,ev):
        try:
            f=self.SupplierTable.focus()
            content=(self.SupplierTable.item(f))
            row=content['values']
            self.var_id.set(row[0])
            self.var_name.set(row[1])
            self.var_pass.set(row[2])
            self.var_detail.set(row[3])
            self.var_1.set(row[4])
            self.var_2.set(row[5])
        except:
            pass
    
    def update(self):
        try:
            if self.var_id.get()=='':
                messagebox.showerror('Error','First Select The Password From Treeview',parent=self.root)
            else:
                self.cur.execute("select * from pwd where id='"+self.var_id.get()+"'")
                row=self.cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Select The Correct Password, Invalid Password ID',parent=self.root)
                else:
                    self.cur.execute("update pwd set name='"+self.var_name.get()+"',pas='"+self.var_pass.get()+"',det='"+self.var_detail.get()+"',o='"+self.var_1.get()+"',t='"+self.var_2.get()+"' where id='"+self.var_id.get()+"'")
                    self.cur.execute("select id from pwd")
                    row=self.cur.fetchall()
                    for i in row:
                        for i in i:
                            print(i)
                    messagebox.showinfo('Success','Password {} Updated Successfully'.format(self.var_id.get()),parent=self.root)
                    self.var_id.set(i+1)
                    self.con.commit()
                    self.var_name.set('')
                    self.var_pass.set('')
                    self.var_1.set("")
                    self.var_detail.set("")
                    self.var_2.set("")
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',ex,parent=self.root)

    def delete(self):
        try:
            if self.var_id.get()=='':
                messagebox.showerror('Error','First Select The Password From Treeview',parent=self.root)
            else:
                self.cur.execute("select * from pwd where id='"+self.var_id.get()+"'")
                row=self.cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Select The Correct Password, Invalid Password ID',parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm','Do you really want to delete Password '+self.var_id.get(),parent=self.root)
                    if op == True:
                        self.cur.execute("delete from pwd where id='"+self.var_id.get()+"'")
                        self.con.commit()
                        self.cur.execute("select id from pwd")
                        row=self.cur.fetchall()
                        for i in row:
                            for i in i:
                                print(i)
                        messagebox.showinfo('Deleted','Password {} Deleted Successfully'.format(self.var_id.get()),parent=self.root)
                        try:
                            self.var_id.set(i+1)
                        except:
                            self.var_id.set(1)
                        self.con.commit()
                        self.var_name.set('')
                        self.var_pass.set('')
                        self.var_1.set("")
                        self.var_detail.set("")
                        self.var_2.set("")
                        self.show()
        except Exception as ex:
            messagebox.showerror('Error',ex,parent=self.root)

    def clear(self):
        self.cur.execute("select id from pwd")
        row=self.cur.fetchall()
        for i in row:
            for i in i:
                print(i)
        self.var_id.set(i+1)
        self.con.commit()
        self.var_name.set('')
        self.var_pass.set('')
        self.var_1.set("")
        self.var_2.set("")
        self.var_detail.set("")
        self.var_searchtxt.set('')
        self.show()

    def search(self,event):
        try:
            self.cur.execute("select id,name,pas,det,o,t from pwd where name LIKE '%"+self.var_searchtxt.get()+"%'")
            rows=self.cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror('Error',ex,parent=self.root)

    def setting():
        tp = Toplevel()
        tp.geometry("420x250+220+140")
        tp.title("Password Manager - IC Developer")
        tp.resizable(0,0)
        tp.config(bg='white')
        tp.focus_force()
        tp.iconbitmap('ico.ico')

        o=StringVar()
        t=StringVar()

        try:
            f = open('set.icd','r')
            f = f.read()
            o1,t1 = f.split('-+|ICD|+-') 
            o.set(o1)
            t.set(t1)
        except:
            pass

        # -==== title =====- #
        title = Label(tp,text='Setting',font=('goudy old style',20,'bold'),bg='#0f4d7d',fg='white').place(x=10,y=10,width=400,height=40)

        # ==== content ==== #
        # ==== row 1 ==== #
        lbl_o = Label(tp,text='2nd Last Field',font=('goudy old style',15),bg='white').place(x=50,y=80)
        txt_o = Entry(tp,textvariable=o,font=('goudy old style',15),bg='lightyellow').place(x=180,y=80,width=230)

        # ==== row 2 ==== #
        lbl_o = Label(tp,text='Last Field',font=('goudy old style',15),bg='white').place(x=50,y=120)
        txt_t = Entry(tp,textvariable=t,font=('goudy old style',15),bg='lightyellow').place(x=180,y=120,width=230)
        
        # ==== row 3 ==== #
        def save():
            f = open('set.icd','w')
            f.write(o.get()+'-+|ICD|+-'+t.get())
            messagebox.showinfo('Success','Restart For Apply Setting',parent=tp)

        btn_update = Button(tp,text='Save',bg='#4caf50',fg='white',command=save,font=('goudy old style',15),activebackground='#4caf50',cursor='hand2').place(x=300,y=160,width=110,height=35)

if __name__=="__main__":
    root = Tk()
    obj = PassMngClass(root)
    root.mainloop()