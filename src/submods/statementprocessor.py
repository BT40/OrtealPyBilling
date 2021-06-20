import sys
import gi
#import functions
from submods import dbmani
from submods import guicommon

#gi.require_version('Gtk', '3.0')
#from gi.repository import Gio
#from gi.repository import Gtk
#from gi.repository import Gdk

#sort priority range 11 to 20
#11 is first choice, #20 is last
# 12 for sale-debit, 13 for purchase-credit, 14 for amount-credit, 15 for amount debit 


def create_statement_entry(inputdata, triggerfrom):
#triger from to detect whether signal is from new invoice or bank entry etc
    edate=inputdata[3]
    vnumber=inputdata[2]
    debitamount=inputdata[71]
    creditamount=0
    if triggerfrom=='newsale':
        typetransaction='Sale'
    else:
        typetransaction='Not available'
    partyname=inputdata[18]
    emonth=edate[5:7]
    eyear=edate[0:4]
    sortpriority=12
    comments=''
    misc=["", "", ""]
    sentrydata=[partyname, edate, vnumber, debitamount, creditamount, typetransaction, emonth, eyear, sortpriority, comments, misc]
    try: #if company present
        rowfulldata=guicommon.statementstableins.readrow(partyname)
        #print(rowfulldata)
        #print('Above is old, below is new data')
        #print(sentrydata)
        rowfulldata.append(sentrydata)
        #print(rowfulldata)
        #print('Above after append')
        guicommon.statementstableins.editrow_without_namechange(partyname, rowfulldata)
        #print('try block of create statement entry fn completed')
    except: #if company not present
        rowfulldata=[sentrydata]
        guicommon.statementstableins.createrow(partyname, rowfulldata)    
        #print('except block of create statement entry fn completed')
    guicommon.loadguicommon()
    

def create_in_statement_entry(inputdata, triggerfrom):
    partyname=inputdata[0]
    edate=inputdata[1]
    vnumber=inputdata[2]
    debitamount=0
    creditamount=inputdata[3]
    comments=inputdata[5]
    sortpriority=14
    
    if inputdata[4]=='Material purchased':
        typetransaction='Purchase'
    elif inputdata[4]=='Payment received':
        typetransaction='Payment in'
    elif inputdata[4]=='Credit note in':
        typetransaction='Credit Note in'
    else:
        typetransaction='Not available'    

    datacol=[partyname, edate, vnumber, debitamount, creditamount, typetransaction, sortpriority, comments]
    process_statement_entry(datacol)
    #print('successfully created statement entry, reporting from statement processor')
    

def process_statement_entry(inputdata):
#triger from to detect whether signal is from new invoice or bank entry etc
    partyname=inputdata[0]
    edate=inputdata[1]
    vnumber=inputdata[2]
    debitamount=inputdata[3]
    creditamount=inputdata[4]
    typetransaction=inputdata[5]    
    emonth=edate[5:7]
    eyear=edate[0:4]
    sortpriority=inputdata[6]
    comments=inputdata[7]
    misc=["", "", ""]
    sentrydata=[partyname, edate, vnumber, debitamount, creditamount, typetransaction, emonth, eyear, sortpriority, comments, misc]
    try: #if company present
        rowfulldata=guicommon.statementstableins.readrow(partyname)
        #print(rowfulldata)
        #print('Above is old, below is new data')
        #print(sentrydata)
        rowfulldata.append(sentrydata)
        #print(rowfulldata)
        #print('Above after append')
        guicommon.statementstableins.editrow_without_namechange(partyname, rowfulldata)
        #print('try block of create statement entry fn completed')
    except: #if company not present
        rowfulldata=[sentrydata]
        guicommon.statementstableins.createrow(partyname, rowfulldata)    
        #print('except block of create statement entry fn completed')
    guicommon.loadguicommon()
    
    
    
    
    
def delete_statement_entry(partyname, edate, vnumber): 
    
        try: #if company present
            rowfulldata=guicommon.statementstableins.readrow(partyname)
            
            #print(rowfulldata)
            #print('Above is old, below is new data')
            #print(sentrydata)
            search_date=edate
            search_vnum=vnumber 
            sl_counter=0
           
            for sublist in rowfulldata:
                if sublist[1] == search_date and sublist[2]==search_vnum:
                    rowfulldata.remove(sublist)
            print(rowfulldata)
            print('Above after del')
            guicommon.statementstableins.editrow_without_namechange(partyname, rowfulldata)
            #print('try block of create statement entry fn completed')
        except: #if company not present
             
            print('except block of del statement entry fn completed')
        guicommon.loadguicommon()
    
    
    
    

    

