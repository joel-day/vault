import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from fpdf import FPDF
import os
import random
import sys
import numpy as np

def temp_path(filename):
   # via pyinstaller -- a temp folder is created and stored in _MEIPASSXXXX everytime .exe is opened -- where XXXX is 4 random int
   # this function adds the path to this folder to any file name or path
    try:
        # find path to _MEIPASSXXXX
        temp_path = sys._MEIPASS
    except Exception:
        # "." ponts to the current working directory in case the pseky _MEIPASS isnt found
        temp_path = os.path.abspath(".")

    return os.path.join(temp_path, filename)

def strip(x):
    #removes all the formatting so I can search against a "clean" list
    x = x.str.replace(' ','', regex=True).str.replace('.','', regex=True).str.replace(',','', regex=True).str.replace("'",'', regex=True).str.replace('-',"", regex=True).str.replace("(",'', regex=True).str.replace(')',"", regex=True).str.replace('/',"", regex=True).str.replace('â„¢',"", regex=True).str.replace('â‚¬',"", regex=True).str.replace('Ã¢',"", regex=True).str.replace('&',"", regex=True).str.lower().str.replace('-',"", regex=True).str.replace('&',"", regex=True)
    return x

def allcontract():
    global contract
    contractfile = contract.get()
    global contractdf
    global contractlist
    global slice

    contractdf = pd.read_excel(contractfile, usecols=['Vendor Last/Business Name', 'Department', 'Procurement Desc', 'Vendor First Name', 'Bid Date', 'Contract Execution Date'])
    
    contractdf['Procurement Desc'] = contractdf['Procurement Desc'].fillna('      ').astype(str)
    contractdf['Bid Date'] = contractdf['Bid Date'].fillna('      ').astype(str)
    contractdf['Contract Execution Date'] = contractdf['Contract Execution Date'].fillna('      ').astype(str)
    contractdf['Department'] = contractdf['Department'].fillna('      ').astype(str)
    contractdf['Vendor Last/Business Name'] = contractdf['Vendor Last/Business Name'].fillna('      ').astype(str)
    contractdf['Vendor First Name'] = contractdf['Vendor First Name'].fillna('      ').astype(str)

    contractdf['Procurement Desc'] = contractdf['Procurement Desc'].str.encode("ascii", "ignore").str.decode("ascii")
    contractdf['Bid Date'] = contractdf['Bid Date'].str.encode("ascii", "ignore").str.decode("ascii")
    contractdf['Contract Execution Date'] = contractdf['Contract Execution Date'].str.encode("ascii", "ignore").str.decode("ascii")
    contractdf['Department'] = contractdf['Department'].str.encode("ascii", "ignore").str.decode("ascii")
    contractdf['Vendor Last/Business Name'] = contractdf['Vendor Last/Business Name'].str.encode("ascii", "ignore").str.decode("ascii")
    contractdf['Vendor First Name'] = contractdf['Vendor First Name'].str.encode("ascii", "ignore").str.decode("ascii")






    contractdf['Vendor Last/Business Name']= contractdf['Vendor Last/Business Name'].str.title().str.slice(0,33)
    contractdf['Department']= contractdf['Department'].str.title().str.slice(0,slice)
    contractdf['Procurement Desc']= contractdf['Procurement Desc'].str.title().str.slice(0,slice)
    
    contractdf['Bid Date']=pd.to_datetime(contractdf['Bid Date'], errors='coerce')
    contractdf['Bid Date']=contractdf['Bid Date'].dt.strftime('%m/%d/%Y')
    contractdf['Contract Execution Date']=pd.to_datetime(contractdf['Contract Execution Date'], errors='coerce')
    contractdf['Contract Execution Date']=contractdf['Contract Execution Date'].dt.strftime('%m/%d/%Y')
    
    
    
    contractdf['striplist'] = strip(contractdf['Vendor Last/Business Name'])
    allcontract = contractdf['striplist'].to_list()
    contractlist.append(allcontract)

    return alllobby()

def alllobby():
    global lobby
    lobbyfile = lobby.get()
    global lobbydf
    global lobbylist
    global firmlist
    global slice
    global slice2

    lobbydf = pd.read_excel(lobbyfile, usecols=['Reg Type', 'Lobbying Entity First Name', 'Lobbying Entity Last/Business Name', 'Firm/Employer Name', 'Project Name', 'Auth To Date', 'Agencies Authorized to Lobby'])
    lobbydf[['Lobbying Entity Last/Business Name']] = lobbydf[['Lobbying Entity Last/Business Name']].fillna('meaninglessvalue').astype(str)
    lobbydf[['Firm/Employer Name']] = lobbydf[['Firm/Employer Name']].fillna('meaninglessvalue').astype(str)
    lobbydf[['Lobbying Entity First Name']] = lobbydf[['Lobbying Entity First Name']].fillna('      ').astype(str)
    lobbydf[['Project Name']] = lobbydf[['Project Name']].fillna('      ').astype(str)
    lobbydf['striplist'] = strip(lobbydf['Lobbying Entity Last/Business Name'])
    lobbydf['striplistfirm'] = strip(lobbydf['Firm/Employer Name'])
    alllobby = lobbydf['striplist'].to_list()
    allfirm = lobbydf['striplistfirm'].to_list()
    lobbylist.append(alllobby)
    firmlist.append(allfirm)

    lobbydf['Auth To Date']=pd.to_datetime(lobbydf['Auth To Date'], errors='coerce')
    lobbydf['Auth To Date']=lobbydf['Auth To Date'].dt.strftime('%m/%d/%Y')

    lobbydf['Firm/Employer Name']= lobbydf['Firm/Employer Name'].str.title().str.slice(0,slice2)
    lobbydf['Reg Type']= lobbydf['Reg Type'].str.title().str.slice(0,8)
    lobbydf['Lobbying Entity First Name']= lobbydf['Lobbying Entity First Name'].str.title().str.slice(0,slice2)
    lobbydf['Lobbying Entity Last/Business Name']= lobbydf['Lobbying Entity Last/Business Name'].str.title().str.slice(0,29)
    lobbydf['Project Name']= lobbydf['Project Name'].str.title().str.slice(0,slice2)
    lobbydf['Agencies Authorized to Lobby']= lobbydf['Agencies Authorized to Lobby'].str.title().str.slice(0,slice2)

    lobbydf['Firm/Employer Name'] = lobbydf['Firm/Employer Name'].str.encode("ascii", "ignore").str.decode("ascii")
    lobbydf['Reg Type'] = lobbydf['Reg Type'].str.encode("ascii", "ignore").str.decode("ascii")
    lobbydf['Lobbying Entity First Name'] = lobbydf['Lobbying Entity First Name'].str.encode("ascii", "ignore").str.decode("ascii")
    lobbydf['Lobbying Entity Last/Business Name'] = lobbydf['Lobbying Entity Last/Business Name'].str.encode("ascii", "ignore").str.decode("ascii")
    lobbydf['Project Name'] = lobbydf['Project Name'].str.encode("ascii", "ignore").str.decode("ascii")
    lobbydf['Auth To Date'] = lobbydf['Auth To Date'].str.encode("ascii", "ignore").str.decode("ascii")
    lobbydf['Agencies Authorized to Lobby'] = lobbydf['Agencies Authorized to Lobby'].str.encode("ascii", "ignore").str.decode("ascii")

    return alldeveloper()

def alldeveloper():
    global developer
    developerfile = developer.get()
    global developerdf
    global developerlist
    global slice
    global slice2

    developerdf = pd.read_excel(developerfile, usecols=['Date of Application', 'Organization Name', 'Role', 'Case Number', 'Project Address'])
    developerdf[['Date of Application']] = developerdf[['Date of Application']].fillna('      ').astype(str)
    developerdf[['Organization Name']] = developerdf[['Organization Name']].fillna('      ').astype(str)
    developerdf[['Role']] = developerdf[['Role']].fillna('      ').astype(str)
    developerdf[['Case Number']] = developerdf[['Case Number']].fillna('      ').astype(str)
    developerdf[['Project Address']] = developerdf[['Project Address']].fillna('      ').astype(str)
    developerdf['striplist'] = strip(developerdf['Organization Name'])
    alldeveloper = developerdf['striplist'].to_list()
    developerlist.append(alldeveloper)

    developerdf['Date of Application']=pd.to_datetime(developerdf['Date of Application'], errors='coerce')
    developerdf['Date of Application']=developerdf['Date of Application'].dt.strftime('%m/%d/%Y')

    developerdf['Organization Name'] = developerdf['Organization Name'].str.title().str.slice(0,slice2)
    developerdf['Role'] = developerdf['Role'].str.title().str.slice(0,slice2)
    developerdf['Case Number'] = developerdf['Case Number'].str.title().str.slice(0,slice2)
    developerdf['Project Address'] = developerdf['Project Address'].str.title().str.slice(0,slice2)

    developerdf['Date of Application'] = developerdf['Date of Application'].str.encode("ascii", "ignore").str.decode("ascii")
    developerdf['Organization Name'] = developerdf['Organization Name'].str.encode("ascii", "ignore").str.decode("ascii")
    developerdf['Role'] = developerdf['Role'].str.encode("ascii", "ignore").str.decode("ascii")
    developerdf['Case Number'] = developerdf['Case Number'].str.encode("ascii", "ignore").str.decode("ascii")
    developerdf['Project Address'] = developerdf['Project Address'].str.encode("ascii", "ignore").str.decode("ascii")

    return allvetting()

def allvetting():
    global vetting
    global vettingdf
    global savename

    vettingfile = vetting.get()
    savename = vettingfile[:-5]
    vettingdf = pd.read_excel(vettingfile, usecols=['First name', 'Last name', 'Occupation', 'Employer'])

    vettingdf['First name']= vettingdf['First name'].str.title().str.slice(0,10)
    vettingdf['First name'] = vettingdf['First name'].str.encode("ascii", "ignore").str.decode("ascii")
    vettingdf['Last name']= vettingdf['Last name'].str.title().str.slice(0,15)
    vettingdf['Last name'] = vettingdf['Last name'].str.encode("ascii", "ignore").str.decode("ascii")
    vettingdf['Occupation']= vettingdf['Occupation'].str.title().str.slice(0,24)
    vettingdf['Occupation'] = vettingdf['Occupation'].str.encode("ascii", "ignore").str.decode("ascii")
    vettingdf['Employer']= vettingdf['Employer'].str.title().str.slice(0,24)
    vettingdf['Employer'] = vettingdf['Employer'].str.encode("ascii", "ignore").str.decode("ascii")
    vettingdf['Striplast'] = strip(vettingdf['Last name'])
    vettingdf['Stripemp'] = strip(vettingdf['Employer'])
    
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'retired', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'notemployed', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'selfemployed', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'not', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'homemaker', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'notemployd', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'self', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'home', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'student', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'selfemp', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'notapplicable', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'none', 'emptyvalue', vettingdf['Stripemp'])
    vettingdf['Stripemp'] = np.where(vettingdf['Stripemp'] == 'unemployed', 'emptyvalue', vettingdf['Stripemp'])

    vettingdf['Contractmatch'] = 'ogn'
    vettingdf['#Contractmatches'] = 'ogn'
    vettingdf['Lobbymatch'] = 'ogn'
    vettingdf['#Lobbymatches'] = 'ogn'
    vettingdf['Developermatch'] = 'ogn'
    vettingdf['#Developermatches'] = 'ogn'

    return report()

def report():
    global contractlist
    global lobbylist
    global firmlist
    global developerlist
    global vettingdf
    global contractdf
    global lobbydf
    global developerdf
    global savename
    global coverpage

    n = (vettingdf.shape[0])-1
    while n > -1:
        last = vettingdf['Striplast'].values[n]
        emp2 = vettingdf['Stripemp'].values[n]
        emp = str(emp2)
        length = len(emp)
        fn = vettingdf['First name'].values[n]
        ln = vettingdf['Last name'].values[n]
        oc = vettingdf['Occupation'].values[n]
        em = vettingdf['Employer'].values[n]
        temporarycontract = contractdf.copy()
        temporarylobby = lobbydf.copy()
        temporarydeveloper = developerdf.copy()

        # Create Dataframes with only the rows forn Contracts and Lobysist that match the names in each row of vettingdf
        temporarycontract['striplist'] = np.where(temporarycontract['striplist'] == last, 'True', temporarycontract['striplist'])
        temporarycontract['striplist'] = np.where(temporarycontract['striplist'] == emp, 'True', temporarycontract['striplist'])
        if length > 2:
            temporarycontract['striplist'] = np.where(temporarycontract['striplist'].str.contains(emp), 'Partial', temporarycontract['striplist'])
        exactcontract = temporarycontract[temporarycontract['striplist'] == 'True']
        partialcontract = temporarycontract[temporarycontract['striplist'] == 'Partial']
        frames1 = [partialcontract, exactcontract]
        contractmatchesdf = pd.concat(frames1)               # IMPORTANT TABLE
        #Fill in excel report with new info
        c = (contractmatchesdf.shape[0])-1
        if c > -1:
            vettingdf.at[n, 'Contractmatch'] = 'TRUE'
            vettingdf.at[n, '#Contractmatches'] = c + 1
        else:
            vettingdf.at[n, 'Contractmatch'] = 'FALSE'
            vettingdf.at[n, '#Contractmatches'] = 'FALSE'

        #Do the same for the lobby list
        temporarylobby['striplist'] = np.where(temporarylobby['striplist'] == last, 'True', temporarylobby['striplist'])
        temporarylobby['striplist'] = np.where(temporarylobby['striplist'] == emp, 'True', temporarylobby['striplist'])
        if length > 2:
            temporarylobby['striplist'] = np.where(temporarylobby['striplist'].str.contains(emp), 'Partial', temporarylobby['striplist'])
        exactlobby = temporarylobby[temporarylobby['striplist'] == 'True']
        partiallobby = temporarylobby[temporarylobby['striplist'] == 'Partial']
        #Added a search through the firm column
        temporarylobby['striplistfirm'] = np.where(temporarylobby['striplistfirm'] == last, 'True', temporarylobby['striplistfirm'])
        temporarylobby['striplistfirm'] = np.where(temporarylobby['striplistfirm'] == emp, 'True', temporarylobby['striplistfirm'])
        if length > 2:
            temporarylobby['striplistfirm'] = np.where(temporarylobby['striplistfirm'].str.contains(emp), 'Partial', temporarylobby['striplistfirm'])        
        exactfirm = temporarylobby[temporarylobby['striplistfirm'] == 'True']
        partialfirm = temporarylobby[temporarylobby['striplistfirm'] == 'Partial']
        #Combine all matches into one dataframe
        frames2 = [partiallobby, partialfirm, exactfirm, exactlobby]
        lobbymatchesdf = pd.concat(frames2)          # IMPORTANT TABLE
        #Fill in excel report with new info
        l = (lobbymatchesdf.shape[0])-1
        if l > -1:
            vettingdf.at[n,'Lobbymatch'] = 'TRUE'
            vettingdf.at[n, '#Lobbymatches'] = l + 1
        else:
            vettingdf.at[n,'Lobbymatch'] = 'FALSE'
            vettingdf.at[n, '#Lobbymatches'] = 'FALSE'



        # Repeat again for Devleopers
        temporarydeveloper['striplist'] = np.where(temporarydeveloper['striplist'] == last, 'True', temporarydeveloper['striplist'])
        temporarydeveloper['striplist'] = np.where(temporarydeveloper['striplist'] == emp, 'True', temporarydeveloper['striplist'])
        if length > 2:
            temporarydeveloper['striplist'] = np.where(temporarydeveloper['striplist'].str.contains(emp), 'Partial', temporarydeveloper['striplist'])
        exactdeveloper = temporarydeveloper[temporarydeveloper['striplist'] == 'True']
        partialdeveloper = temporarydeveloper[temporarydeveloper['striplist'] == 'Partial']
        frames3 = [partialdeveloper, exactdeveloper]
        developermatchesdf = pd.concat(frames3)               # IMPORTANT TABLE
        #Fill in excel report with new info
        d = (developermatchesdf.shape[0])-1
        if d > -1:
            vettingdf.at[n, 'Developermatch'] = 'TRUE'
            vettingdf.at[n, '#Developermatches'] = d + 1
        else:
            vettingdf.at[n, 'Developermatch'] = 'FALSE'
            vettingdf.at[n, '#Developermatches'] = 'FALSE'




        #Formatting Variable for PDF
        epw = pdf.w - pdf.l_margin
        col_width_c = epw/5.82
        col_width_l = epw/6.78
        col_width_d = epw/5.13
        #Create PDF Report for each indivdual with matches
        if c > -1 or l > -1 or d > -1:

            #Create Page Header
            pdf.add_page()
            fn = vettingdf['First name'].values[n]
            ln = vettingdf['Last name'].values[n]
            oc = str(vettingdf['Occupation'].values[n])
            em = str(vettingdf['Employer'].values[n])
            outname = "Name: " + fn + " " + ln
            occ = "Occupation: " + oc + "        Employer: " + em
            ccc = str(c + 1)
            lll = str(l + 1)
            ddd = str(d + 1)
            outcome = "Matches: Contract = " + ccc + "      Lobbyist = " + lll + "      Developer = " + ddd
            pdf.set_font("Arial", 'B', size = 14)                                 # Font for Names INFO
            pdf.cell(epw,10,outname,0,1,'L',0)
            pdf.set_font("Arial", size = 12)                                 # Font for Names INFO
            pdf.cell(epw,10,occ,0,1,'L',0)
            pdf.cell(epw,10,outcome,0,1,'L',0)

            if c > -1:
                #Table Title
                pdf.set_font("Arial", 'B', size = 14)                                 #Font for Table Totle                   
                pdf.cell(epw,10, "Contract Matches" ,0,1,'L',0)
                pdf.set_font("Arial", size = 10)                             # Fnt for Table Headers
                pdf.cell(col_width_c*1.7,5,'Vendor Name',1,0,'C',0)
                pdf.cell(col_width_c/1.8,5,'First Name',1,0,'C',0)
                pdf.cell(col_width_c,5,'Department',1,0,'C',0)
                pdf.cell(col_width_c/1.5,5,'Bid Date',1,0,'C',0)
                pdf.cell(col_width_c/1.5,5,'Contr Exec',1,0,'C',0)
                pdf.cell(col_width_c*1.1,5,'Proc. Desc',1,1,'C',0)
       
                aa = (contractmatchesdf.shape[0])-1
                while aa > -1:
                    VendorName = contractmatchesdf.loc[:,'Vendor Last/Business Name'].astype(str)    
                    Q = VendorName.values[aa]
                    Firstname = contractmatchesdf.loc[:,'Vendor First Name'].astype(str)
                    R = Firstname.values[aa]
                    Dep = contractmatchesdf.loc[:,'Department'].astype(str)
                    S = Dep.values[aa]
                    Proc = contractmatchesdf.loc[:,'Procurement Desc'].astype(str)
                    T = Proc.values[aa]
                    Bid = contractmatchesdf.loc[:,'Bid Date'].astype(str)
                    U = Bid.values[aa]
                    CED = contractmatchesdf.loc[:,'Contract Execution Date'].astype(str)
                    V = CED.values[aa]

                    pdf.set_font("Arial", size = 10)
                    pdf.cell(col_width_c*1.7,5,Q,1,0,'C',0)
                    pdf.cell(col_width_c/1.8,5,R,1,0,'C',0)
                    pdf.cell(col_width_c,5,S,1,0,'C',0)
                    pdf.cell(col_width_c/1.5,5,U,1,0,'C',0)
                    pdf.cell(col_width_c/1.5,5,V,1,0,'C',0)
                    pdf.cell(col_width_c*1.1,5,T,1,1,'C',0)

                    aa = aa - 1

            if l > -1:
                #Table Title
                pdf.set_font("Arial", 'B', size = 14)                                 #Font for Table Title                   
                pdf.cell(epw,10, "Lobbyist Matches" ,0,1,'L',0)
                pdf.set_font("Arial", size = 10)                             # Fnt for Table Headers
                pdf.cell(col_width_l*1.73,5,'Lobbyist Name',1,0,'C',0)
                pdf.cell(col_width_l/1.5,5,'First Name',1,0,'C',0)
                pdf.cell(col_width_l,5,'Firm Name',1,0,'C',0)
                pdf.cell(col_width_l/1.8,5,'Reg Type',1,0,'C',0)
                pdf.cell(col_width_l,5,'Project Name',1,0,'C',0)
                pdf.cell(col_width_l/1.5,5,'Auth Until',1,0,'C',0)
                pdf.cell(col_width_l,5,'Auth Agencies',1,1,'C',0)

                bb = (lobbymatchesdf.shape[0])-1
                while bb > -1:
                    LobbyName = lobbymatchesdf.loc[:,'Lobbying Entity Last/Business Name'].astype(str)
                    F = LobbyName.values[bb]        
                    Firstname2 = lobbymatchesdf.loc[:,'Lobbying Entity First Name'].astype(str)
                    G = Firstname2.values[bb]
                    Firm = lobbymatchesdf.loc[:,'Firm/Employer Name'].astype(str)
                    H = Firm.values[bb] 
                    Regtype = lobbymatchesdf.loc[:,'Reg Type'].astype(str)
                    I = Regtype.values[bb]
                    Pro = lobbymatchesdf.loc[:,'Project Name'].astype(str)
                    J = Pro.values[bb]        
                    Agen = lobbymatchesdf.loc[:,'Agencies Authorized to Lobby'].astype(str)
                    K = Agen.values[bb]
                    ATD = lobbymatchesdf.loc[:,'Auth To Date'].astype(str)
                    L = ATD.values[bb]

                    pdf.set_font("Arial", size = 10)
                    pdf.cell(col_width_l*1.73,5,F,1,0,'C',0)
                    pdf.cell(col_width_l/1.5,5,G,1,0,'C',0)
                    pdf.cell(col_width_l,5,H,1,0,'C',0)
                    pdf.cell(col_width_l/1.8,5,I,1,0,'C',0)
                    pdf.cell(col_width_l,5,J,1,0,'C',0)
                    pdf.cell(col_width_l/1.5,5,L,1,0,'C',0)
                    pdf.cell(col_width_l,5,K,1,1,'C',0)
                        
                    bb = bb -1
    
            if d > -1:
                #Table Title
                pdf.set_font("Arial", 'B', size = 14)                                 #Font for Table Title                   
                pdf.cell(epw,10, "Developer Matches" ,0,1,'L',0)
                pdf.set_font("Arial", size = 10)                             # Fnt for Table Headers


                pdf.cell(col_width_d,5,'Date of Application',1,0,'C',0)
                pdf.cell(col_width_d,5,'Organization Name',1,0,'C',0)
                pdf.cell(col_width_d,5,'Role',1,0,'C',0)
                pdf.cell(col_width_d,5,'Case Number',1,0,'C',0)
                pdf.cell(col_width_d,5,'Project Address',1,1,'C',0)

                cc = (developermatchesdf.shape[0])-1
                while cc > -1:
                    DOA = developermatchesdf.loc[:,'Date of Application'].astype(str)
                    one = DOA.values[cc] 
                    ON = developermatchesdf.loc[:,'Organization Name'].astype(str)
                    two = ON.values[cc]  
                    role = developermatchesdf.loc[:,'Role'].astype(str)
                    three = role.values[cc] 
                    case = developermatchesdf.loc[:,'Case Number'].astype(str)
                    four = case.values[cc]
                    add = developermatchesdf.loc[:,'Project Address'].astype(str)
                    five = add.values[cc] 
                 

                    pdf.set_font("Arial", size = 10)
                    pdf.cell(col_width_d,5,one,1,0,'C',0)
                    pdf.cell(col_width_d,5,two,1,0,'C',0)
                    pdf.cell(col_width_d,5,three,1,0,'C',0)
                    pdf.cell(col_width_d,5,four,1,0,'C',0)
                    pdf.cell(col_width_d,5,five,1,1,'C',0)
                        
                    cc = cc -1
        n = n - 1

    vetdf = vettingdf.sort_values(['Contractmatch', 'Lobbymatch', 'Developermatch'], ascending = [True, True, True])
    finalvettingdf = vetdf.drop(columns=['Striplast', 'Stripemp','Contractmatch', 'Lobbymatch', 'Developermatch'])
    #Create Cover Page
    coverpage.add_page()
    coverpage.set_font("Arial", 'B', size = 18)                                 #Font for Table Title                   
    coverpage.cell(epw,10, "Vetting Summary",0,1,'L',0)
    coverpage.set_font("Arial", size = 10)                             # Font for Table Headers
    coverpage.cell(col_width_l/2,5,'CON',1,0,'C',0)
    coverpage.cell(col_width_l/2,5,'LOB',1,0,'C',0)
    coverpage.cell(col_width_l/2,5,'DEV',1,0,'C',0)
    coverpage.cell(col_width_l*.7,5,'First Name',1,0,'C',0)
    coverpage.cell(col_width_l,5,'Last Name',1,0,'C',0)
    coverpage.cell(col_width_l*1.7,5,'Occuaption',1,0,'C',0)
    coverpage.cell(col_width_l*1.7,5,'Employer',1,1,'C',0)

    ww = (finalvettingdf.shape[0])-1
    while ww > -1:
        vfn= finalvettingdf.loc[:,'First name'].astype(str)
        L = vfn.values[ww]  
        vln = finalvettingdf.loc[:,'Last name'].astype(str)
        M = vln.values[ww]
        vocc = finalvettingdf.loc[:,'Occupation'].astype(str)
        N = vocc.values[ww][:30]
        vemp = finalvettingdf.loc[:,'Employer'].astype(str)
        O = vemp.values[ww][:35]
        vcm = finalvettingdf.loc[:,'#Contractmatches'].astype(str)
        P = vcm.values[ww]        
        vlm = finalvettingdf.loc[:,'#Lobbymatches'].astype(str)
        PP = vlm.values[ww]
        vdm = finalvettingdf.loc[:,'#Developermatches'].astype(str)
        PPP = vdm.values[ww]

        coverpage.set_font("Arial", size = 10)
        coverpage.cell(col_width_l/2,5,P,1,0,'C',0)
        coverpage.cell(col_width_l/2,5,PP,1,0,'C',0)
        coverpage.cell(col_width_l/2,5,PPP,1,0,'C',0)
        coverpage.cell(col_width_l*.7,5,L,1,0,'C',0)
        coverpage.cell(col_width_l,5,M,1,0,'C',0)
        coverpage.cell(col_width_l*1.7,5,N,1,0,'C',0)
        coverpage.cell(col_width_l*1.7,5,O,1,1,'C',0)
                    
        ww = ww -1
    
    rn = random.randint(100, 999)
    rnn = str(rn)
    coverpage.output('Summary_' + savename + '_' + rnn +  '.pdf', 'F')
    pdf.output('Vetting Report_' + savename + '_' + rnn +  '.pdf', 'F')

    return reset()

def reset():
    global pdf
    global vettingdf
    global coverpage
    global savename
    pdf = FPDF()
    coverpage = FPDF()
    vettingdf = pd.DataFrame()
    savename = 'empty'

#Global Variables
savename = 'empty'
pdf = FPDF()
coverpage = FPDF()
slice = 17
slice2 = 15

developerlist = []
contractlist = []
lobbylist = []
firmlist = []

developerdf = pd.DataFrame()
contractdf = pd.DataFrame()
lobbydf = pd.DataFrame()
vettingdf = pd.DataFrame()

#Change working directory to the users desktop because the user works directly with .xlsx files on desktop. 
username = os.getlogin()
os.chdir('C:\\Users\\'+ username +'\\Desktop')

#Create the Frame the world will interact with 
LA = tk.Tk()
LA.title("Falcon 2")  # to define the title
LA.option_add('*Font', '80')
LA.option_add('*Font', 'Times')
LA.geometry("400x700")

#Add the Beautiful ActBlue Photo -- WoW
pic = str(temp_path("download.png"))
photo = tk.PhotoImage(file = pic)
label1 = Label(LA, image = photo).place(relx=.07, rely=.0, relwidth=1, relheight=.6)

#Adds all the-- .xlsx --excel files on the desktop into a list for dropbox options
files = [f for f in os.listdir('.') if f.endswith('.xlsx')]

#Create the input variables and interactive dropdown menu to selct Contracts and Lobbyist files. Button to process
contract = tk.StringVar(value = "Contract:")
lobby = tk.StringVar(value = "Lobby:")
developer = tk.StringVar(value = "Developer:")
vetting = tk.StringVar(value = "Vetting List:")
optmenu = ttk.Combobox(LA, textvariable=contract, values=files).place(relx=.05, rely=.5, relwidth=.9, relheight=.08)
optmenu2 = ttk.Combobox(LA, textvariable=lobby, values=files).place(relx=.05, rely=.6, relwidth=.9, relheight=.08)
optmenu3 = ttk.Combobox(LA, textvariable=developer, values=files).place(relx=.05, rely=.7, relwidth=.9, relheight=.08)
optmenu4 = ttk.Combobox(LA, textvariable=vetting, values=files).place(relx=.05, rely=.8, relwidth=.9, relheight=.08)
Button1 = tk.Button(LA, text="DOWNLOAD", command=lambda:[allcontract()]).place(relx=.05, rely=.9, relwidth=.9, relheight=.08)

LA.mainloop()