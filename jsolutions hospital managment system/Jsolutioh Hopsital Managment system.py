# hospital managment system using tkinter pyhton 

from tkinter import*
from tkinter import ttk
import random
import time
import datetime
import tkinter.messagebox

    #create class hospital 
class Hospital:
    #constructor
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Managment System by JSolutions")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')


        cmbNameTablets = StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberTablets = StringVar()
        Lot = StringVar()
        IssueDate = StringVar()
        ExpDate = StringVar()
        DailyDose = StringVar()
        PossibleSideEffects = StringVar()
        FurtherInformation = StringVar()
        StorageAdvice = StringVar()
        DrivingUsingMachines = StringVar()
        HowtoUseMedication = StringVar()
        PatientID = StringVar()
        PatientNHSNo = StringVar()
        PatientName = StringVar()
        DateofBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        #==============================Funtion declaration============================================
        def iExit():
            iExit=tkinter.messagebox.askyesno("Hospital Managment System","Confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return
        def iPrescription():

            self.txtPrescription.insert(END,'Name Of Tablets:\t\t\t' + cmbNameTablets.get()+ "\n")
            self.txtPrescription.insert(END,'Reference No:\t\t\t' + Ref.get()+ "\n")
            self.txtPrescription.insert(END,'Dose:\t\t\t' + Dose.get()+ "\n")
            self.txtPrescription.insert(END,'Lot:\t\t\t' + Lot.get()+ "\n")
            self.txtPrescription.insert(END,'Issued Date:\t\t\t' + IssueDate.get()+ "\n")
            self.txtPrescription.insert(END,'Exp.Date:\t\t\t' + ExpDate.get()+ "\n")
            self.txtPrescription.insert(END,'Daily Dose:\t\t\t' + DailyDose.get()+ "\n")
            self.txtPrescription.insert(END,'Possible Side Effects:\t\t\t' + PossibleSideEffects.get()+ "\n")
            self.txtPrescription.insert(END,'Further Information:\t\t\t' + FurtherInformation.get()+ "\n")
            self.txtPrescription.insert(END,'Storage Advice:\t\t\t' + StorageAdvice.get()+ "\n")
            self.txtPrescription.insert(END,'Driving or Using Machines:\t\t\t' + DrivingUsingMachines.get()+ "\n")
            self.txtPrescription.insert(END,'Patient ID:\t\t\t' + PatientID.get()+ "\n")
            self.txtPrescription.insert(END,'NHS Number:\t\t\t' + PatientNHSNo.get()+ "\n")
            self.txtPrescription.insert(END,'Patient Name:\t\t\t' + PatientName.get()+ "\n")
            self.txtPrescription.insert(END,'Date Of Birth:\t\t\t' + DateofBirth.get()+ "\n")
            self.txtPrescription.insert(END,'Patient Address:\t\t\t' + PatientAddress.get()+ "\n")
            return

        def iReciept():
            

            self.txtFrameDetail.insert(END, cmbNameTablets.get()+"\t\t" + Ref.get()+"\t"+Dose.get()+"\t"+ NumberTablets.get()+"\t"+Lot.get()+"\t"+IssueDate.get()+"\t"+ExpDate.get()+"\t"+DailyDose.get()+"\t\t"+ StorageAdvice.get()+"\t"+ PatientNHSNo.get() + "\t\t" + PatientName.get()+ "\t" + PatientAddress.get()+ "\n")
            return 

        def iDelete():

            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("") 
            PatientID.set("")
            PatientNHSNo.set("") 
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)
            return 

        def iReset():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssueDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("") 
            PatientID.set("")
            PatientNHSNo.set("") 
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            #self.txtFrameDetail.delete("1.0",END)
            return    










       #==================Main frame====================================================
        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame (MainFrame,bd=20, width=1350,padx=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame,font=('arial',40,'bold'),text="HOSPITAL MANAGMENT SYSTEM",padx=2)
        self.lblTitle.grid()
        #====================MainFrame ===============
        FrameDetail=Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=20,width=1350,height=400,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame,bd=10,width=800,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Patient Information:")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=LabelFrame(DataFrame,bd=10,width=450,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text="Prescription")
        DataFrameRIGHT.pack(side=RIGHT)
        #========================Data Frame Left=================================================
        self.lblNameTablet =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Name of Tablet",padx=2,pady=2)
        self.lblNameTablet.grid(row =0, column=0, sticky=W)

        self.cboNameTablet=ttk.Combobox(DataFrameLEFT,textvariable=cmbNameTablets, state ='readonly',font=('arial',12,'bold'),width=20)
        self.cboNameTablet['value']=('','coronavaccine','Paracetamol','Amlodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0,column=1)

        self.lblFurtherInfo =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Further Information",padx=2,pady=2)
        self.lblFurtherInfo.grid(row =0, column=2, sticky=W)
        self.txtFurtherInfo =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=FurtherInformation,width=25)
        self.txtFurtherInfo.grid(row =0, column=3)

        self.lblRef =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Refrene No:",padx=2,pady=2)
        self.lblRef.grid(row =1, column=0, sticky=W)
        self.txtRef =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Ref,width=25)
        self.txtRef.grid(row =1, column=1)

        self.lblStorage =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Storage Advice:",padx=2,pady=2)
        self.lblStorage.grid(row =1, column=2, sticky=W)
        self.txtStorage =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=StorageAdvice,width=25)
        self.txtStorage.grid(row =1, column=3)

        self.lblDose =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Dose:",padx=2,pady=2)
        self.lblDose.grid(row =2, column=0, sticky=W)
        self.txtDose=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Dose, width=25)
        self.txtDose.grid(row =2, column=1)

        self.lblUseMachine =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Driving Machines:",padx=2,pady=2)
        self.lblUseMachine .grid(row =2, column=2, sticky=W)
        self.txtUseMachine =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=DrivingUsingMachines, width=25)
        self.txtUseMachine .grid(row =2, column=3)
        
        self.lblNoOfTablets =Label(DataFrameLEFT,font=('arial',12,'bold'),text="No Of Tablets:",padx=2,pady=2)
        self.lblNoOfTablets .grid(row =3, column=0, sticky=W)
        self.txtNoOfTablets =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=NumberTablets, width=25)
        self.txtNoOfTablets .grid(row =3, column=1)

        self.lblUseMedication =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Use Of Medication:",padx=2,pady=2)
        self.lblUseMedication .grid(row =3, column=2, sticky=W)
        self.txtUseMedication =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=HowtoUseMedication, width=25)
        self.txtUseMedication.grid(row =3, column=3)
        
        self.lblLot =Label(DataFrameLEFT,font=('arial',12,'bold'),text="LOT:",padx=2,pady=2)
        self.lblLot .grid(row =4, column=0, sticky=W)
        self.txtLot =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=Lot, width=25)
        self.txtLot.grid(row =4, column=1)

        self.lblPatientID =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Patient ID:",padx=2,pady=2)
        self.lblPatientID .grid(row =4, column=2, sticky=W)
        self.txtPatientID =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=PatientID, width=25)
        self.txtPatientID.grid(row =4, column=3)

        self.lblIssueDate =Label(DataFrameLEFT,font=('arial',12,'bold'),text="Issued Date:",padx=2,pady=2)
        self.lblIssueDate .grid(row =5, column=0, sticky=W)
        self.txtIssueDate =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable=IssueDate, width=25)
        self.txtIssueDate.grid(row =5, column=1)
        
        self.lblNHSNumber =Label(DataFrameLEFT,font=('arial',12,'bold'),text="NHS Number:",padx=2,pady=2)
        self.lblNHSNumber.grid(row =5, column=2, sticky=W)
        self.txtNHSNumber =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PatientNHSNo, width=25)
        self.txtNHSNumber.grid(row =5, column=3)
        
        self.lblExpDate =Label(DataFrameLEFT,font=('arial',12,'bold'),text="ExpDate:",padx=2,pady=2)
        self.lblExpDate.grid(row =6, column=0, sticky=W)
        self.txtExpDate =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= ExpDate, width=25)
        self.txtExpDate.grid(row =6, column=1)

        self.lblPatientName =Label(DataFrameLEFT,font=('arial',12,'bold'),text="PatientName:",padx=2,pady=2)
        self.lblPatientName.grid(row =6, column=2, sticky=W)
        self.txtPatientName =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PatientName, width=25)
        self.txtPatientName.grid(row =6, column=3)

        self.lblDailyDose =Label(DataFrameLEFT,font=('arial',12,'bold'),text="DailyDose:",padx=2,pady=2)
        self.lblDailyDose.grid(row =7, column=0, sticky=W)
        self.txtDailyDose =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= DailyDose, width=25)
        self.txtDailyDose.grid(row =7, column=1)

        self.lblDateofBirth=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Date of Birth:",padx=2,pady=2)
        self.lblDateofBirth.grid(row =7, column=2, sticky=W)
        self.txtDateofBirth =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= DateofBirth, width=25)
        self.txtDateofBirth.grid(row =7, column=3)

        self.lblSideEffects=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Side Effects:",padx=2,pady=2)
        self.lblSideEffects.grid(row =8, column=0, sticky=W)
        self.txtSideEffects =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PossibleSideEffects, width=25)
        self.txtSideEffects.grid(row =8, column=1)

        self.lblPatientAddress=Label(DataFrameLEFT,font=('arial',12,'bold'),text="Patient Address:",padx=2,pady=2)
        self.lblPatientAddress.grid(row =8, column=2, sticky=W)
        self.txtPatientAddress =Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable= PatientAddress, width=25)
        self.txtPatientAddress.grid(row =8, column=3)
        
        #=======================DataFrameRight=============================================
        
        self.txtPrescription=Text(DataFrameRIGHT,font=('arial',12,'bold'),width=43,height=11,padx=2,pady=6)
        self.txtPrescription.grid(row =0, column=0)


        #=======================ButtonFrame=============================================
        self.btnPrescription=Button(ButtonFrame, text='Prescription',font=('arial',12,'bold'),width=24,bd=4,bg="light blue",command =iPrescription)
        self.btnPrescription.grid(row=0,column=0) 

        self.btnReciept=Button(ButtonFrame, text='Receipt',font=('arial',12,'bold'),width=24,bd=4,bg="light blue",command= iReciept)
        self.btnReciept.grid(row=0,column=1) 
       
        self.btnDelete=Button(ButtonFrame, text='Delete',font=('arial',12,'bold'),width=24,bd=4,bg="light blue", command= iDelete)
        self.btnDelete.grid(row=0,column=2) 
        
        self.btnReset=Button(ButtonFrame, text='Reset',font=('arial',12,'bold'),width=24,bd=4,bg="light blue",command= iReset)
        self.btnReset.grid(row=0,column=3) 

        self.btnExit=Button(ButtonFrame, text='Exit',font=('arial',12,'bold'),width=24,bd=4,bg="light blue",command=iExit)
        self.btnExit.grid(row=0,column=4) 
       
       
       
       
       
       
       
        #=======================FrameDetail=============================================
        
        self.lblLabel =Label(FrameDetail,font=('arial',10,'bold'),text="Name Of Tablets\t Refrence No.\t Dosage\t No of Tablets\t Lot \t Issued Date\t Exp. Date\t Daily Dose\t Storage adv.\t NHS Number\t Patient Name.\t DOB\t PatientAddress",pady=8)
        self.lblLabel.grid(row=0,column=0)

        self.txtFrameDetail=Text(FrameDetail,font=('arial',12,'bold'),width=141,height=7,padx=2,pady=4)
        self.txtFrameDetail.grid(row =1, column=0)
         





        



if __name__ == '__main__':
  root=Tk()
  application=Hospital(root)
  root.mainloop()




        

