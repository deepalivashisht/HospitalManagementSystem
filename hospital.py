from cProfile import label
from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1480x800+0+0")


        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Numberoftablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        lbltitle=Label(self.root,bd=7,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #***************Dataframe************
        Dataframe=Frame(self.root,bd=7,relief=RIDGE)
        Dataframe.place(x=0,y=100,width=1365,height=370)

        DataframeLeft=LabelFrame(Dataframe,bd=7,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=900,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=7,relief=RIDGE,padx=10,font=("times new roman",12,"bold"),text="Prescription")
        DataframeRight.place(x=910,y=5,width=430,height=350)

        #************Buttons frame*************
        Buttonframe=Frame(self.root,bd=7,relief=RIDGE)
        Buttonframe.place(x=0,y=470,width=1365,height=40)

        #************Details frame*************
        Detailsframe=Frame(self.root,bd=7,relief=RIDGE)
        Detailsframe.place(x=0,y=510,width=1365,height=200)

        #**************Dataframe left***************
        lblNameTablet=Label(DataframeLeft,text="Names of Tablet",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=("arial",12,"bold"),width=28)
        comNametablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=30)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=30)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No of Tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Numberoftablets,width=30)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=30)
        txtLot.grid(row=4,column=1)

        lblIssuedate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssuedate.grid(row=5,column=0,sticky=W)
        txtIssuedate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=30)
        txtIssuedate.grid(row=5,column=1)

        lblExpdate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpdate.grid(row=6,column=0,sticky=W)
        txtExpdate=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ExpDate,width=30)
        txtExpdate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=30)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sideEfect,width=30)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherInfo=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=30)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=30)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=30)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.HowToUseMedication,width=30)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtpatientId=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientId,width=30)
        txtpatientId.grid(row=4,column=3)

        lblNhsNo=Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=6)
        lblNhsNo.grid(row=5,column=2,sticky=W)
        txtNhsNo=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.nhsNumber,width=30)
        txtNhsNo.grid(row=5,column=3)

        lblPatientName=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtpatientName=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=30)
        txtpatientName.grid(row=6,column=3)

        lblDOB=Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=6)
        lblDOB.grid(row=7,column=2,sticky=W)
        txtDOB=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=30)
        txtDOB.grid(row=7,column=3)

        lblPatientAdd=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAdd.grid(row=8,column=2,sticky=W)
        txtpatientAdd=Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientAddress,width=30)
        txtpatientAdd.grid(row=8,column=3)

        #****************Dataframe Right************
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=41,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #**************************Buttons*************
        btnPrescription=Button(Buttonframe,command=self.iPrescription,text="Prescription",bg="green",fg="white",
        font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptiondata=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="green",
        fg="white",font=("arial",12,"bold"),width=22,padx=2,pady=6)
        btnPrescriptiondata.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="green",fg="white",
        font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnUpdate=Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",
        font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnUpdate.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",
        font=("arial",12,"bold"),width=21,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.iExit,text="Exit",bg="green",fg="white",
        font=("arial",12,"bold"),width=22,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

        #***************Table*********8
        #***************Scrollbar*********8
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftablets","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftablets",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)

        #*************functionality decalaration**************
    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Admin@123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.Numberoftablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatientName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Admin@123",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("Update hospital set Nameoftablets=%s, Reference_No=%s, dose=%s,"
                            "Numberoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, "
                            "storage=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s where Reference_No=%s,"
                            (
                                self.Nameoftablets.get(),
                                self.ref.get(),
                                self.Dose.get(),
                                self.Numberoftablets.get(),
                                self.Lot.get(),
                                self.Issuedate.get(),
                                self.ExpDate.get(),
                                self.DailyDose.get(),
                                self.StorageAdvice.get(),
                                self.nhsNumber.get(),
                                self.PatientName.get(),
                                self.DateOfBirth.get(),
                                self.PatientAddress.get()
                            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Record has been updated successfully")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Admin@123",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.Numberoftablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Tablets: \t\t\t" + self.Nameoftablets.get() + "\n")
        self.txtPrescription.insert(END, "Reference No: \t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose: \t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number of Tablets: \t\t\t" + self.Numberoftablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot: \t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date: \t\t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Exp Date: \t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose: \t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effects: \t\t\t" + self.sideEfect.get() + "\n")
        self.txtPrescription.insert(END, "StorageAdvice: \t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "DrivingUsingMachine: \t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END, "PatientId: \t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END, "Nhs Number: \t\t\t" + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name: \t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Date of Birth: \t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address: \t\t\t" + self.PatientAddress.get() + "\n")

    def idelete(self):
        conn = mysql.connector.connect(host="localhost",user="root",password="Admin@123",database="mydata")
        my_cursor = conn.cursor()
        query = "delete from hospital where Reference_No = %s"
        value = (self.ref.get(),)
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Record has been deleted successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.Numberoftablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEfect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital management system", "Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return

root = Tk()
ob=Hospital(root)
root.mainloop()