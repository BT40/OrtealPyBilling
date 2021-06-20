# Table wrapper over Pickledb. Store data in tabular form utilizing nosql.
# Revision 19 June 2021

import sys
import os
import signal
import pickledb
from datetime import datetime
from pathlib import Path

# notations: suffix f for function variables, suffix c for class variables
# use print statements for debugging
# Future plan: create a log file for debugging by a function if set on by user, create a variable property of object in main class debugmodec

class Tealor():
    def createtable(self, tablename, autosav="yes"):
        self.tablename=tablename
        #print("You gave table name : ") 
        #print(tablename)
        self.autosav=autosav
        #print("Autosave is set to : " )
        #print(autosav)
        #self.copies=2
        self.rowcount=0
        self.rowcollection=[]
        self.rowlist=[]
        self.collist=[]
        self.checkpresence='present'
        
        self.diskname=self.thresher(tablename)+'.db'
        
        home_dir=Path.home()
        user_dir=str(home_dir)+'/ortealbilling_data'     #change this address application wise 
        wd=user_dir + '/tealordb'
        self.pathname= wd + '/' + self.diskname
        #print (self.pathname)
        self.db = pickledb.load(self.pathname, False)
        self.db.set('tablename', self.tablename)
        self.db.set('diskname', self.diskname)
        self.db.set('autosav', self.autosav)
        self.db.set('checkpresence', self.checkpresence) 
        self.db.set('rowcount', self.rowcount) 
        self.db.set('collist', self.collist)
        self.db.set('rowlist', self.rowlist)  
        self.db.set('rowcollection', self.rowcollection)        
        self.autosave()
                

    def loaddata(self, which):
        tempdiskname=which+ '.db'
        
        home_dir=Path.home()
        user_dir=str(home_dir)+'/ortealbilling_data'     #change this address application wise 
        wd=user_dir + '/tealordb'
        self.pathname= wd + '/' + tempdiskname
        #print (self.pathname)   
            
        if not os.path.exists(wd): # check folder exist, if not create
            os.makedirs(wd)
        #print('trying to load database with allocated disk name: ')
        #print(tempdiskname)
        #print('Reporting from tealordb loaddata' )
        self.db = pickledb.load(self.pathname, False) # which has to be string representing tablename or filename (diskname) of database
        self.checkpresence=self.db.get('checkpresence')
        #print (self.checkpresence)
        #print ('above is value of checkpresence, reporting from tealordb loaddata fnction header')     
        
        if self.checkpresence==False:       
            self.tablename=which
            self.diskname=self.thresher(self.tablename)+'.db'
            #print('Database not found on disk, allocating disk name as:')
            #print(self.diskname)
            self.autosav='yes'
            self.checkpresence='present'
            self.rowcount=0
            self.collist=[]
            self.rowlist=[]
            self.rowcollection=[]                        
        
            self.db.set('tablename', self.tablename)
            self.db.set('diskname', self.diskname)
            self.db.set('autosav', self.autosav)
            self.db.set('checkpresence', self.checkpresence)  
            self.db.set('rowcount', self.rowcount) 
            self.db.set('collist', self.collist)
            self.db.set('rowlist', self.rowlist)  
            self.db.set('rowcollection', self.rowcollection)        
            self.autosave()           
            print(str(self.tablename) + "database not found on disk, created new one. Reporting from tealordb initialization")

        elif self.checkpresence=='present':            
            self.tablename=self.db.get('tablename')
            self.diskname=self.db.get('diskname')
            #print('Database found on disk, name is:')
            #print(self.diskname)
            self.autosav=self.db.get('autosav')
            self.checkpresence=self.db.get('checkpresence')
            self.rowcount=self.db.get('rowcount')
            self.collist=self.db.get('collist')
            self.rowlist=self.db.get('rowlist')   
            self.rowcollection=self.db.get('rowcollection')
            #print("Loaded " + self.tablename + " database from disk. Reporting from else block in tealordb initialization")
         
        else:
            print('Something went wrong in loading database' + str(self.tablename))               
        
        # below are tests for initialization    
        #print(type(self.rowlist))
        #print("-------Above is init test----")
        #print(type(self.tablenamec))		

		
    def setcolumnheadings(self, colnames):
        self.collist=colnames
        #argCount = len(colnames)
        #strArgCount=str(argCount)
        #print("Number of columns is " + strArgCount)        
        ##for elem in colnames :
        ##    print(elem)        
        #print("-----------")
        self.db.set('collist', self.collist)
        self.autosave()
		
				
    def createrow(self, rowname, rowdata): #rowdata has to be array
        self.rowlist.append(rowname)
        self.rowcollection.append(rowdata)
        self.rowcount=self.rowcount+1
        self.db.set('rowcount', self.rowcount) 
        self.db.set('rowlist', self.rowlist)  
        self.db.set('rowcollection', self.rowcollection)
        self.autosave()
        #print("createrow called and successfully completed, reporting from tealordb")
        
	           		
    def deleterow(self, rownametodelete):
        #print(self.db.get('rowlist'))
        #print ("database row list original, reporting from deteterow in Tealordb")  
        rowindex=self.rowlist.index(rownametodelete) 
        #rownameref= self.rowlist[rowindex]    # seems redundant and faulty, will mess with argument rowname
        del self.rowlist[rowindex]
        del self.rowcollection[rowindex]
        self.rowcount=self.rowcount-1
        self.db.set('rowcount', self.rowcount)         
        #print(self.db.get('rowlist'))
        #print ("database row list after deletion operation, reporting from deleterow in Tealordb ")  
        #No need to remove from database self.db as it is auto updated due to mutation in lists       
        self.autosave()
        #print ("Successfully deleted the row, reporting from tealordb")

          
    def editrow(self, rownametomodify, rowdata):
        #print ("Finding Index for your requested row... ") 
        rowindex=self.rowlist.index(rownametomodify) 
        #rowname= self.rowlist[rowindex] # seems redundant and faulty, will mess with argument rowname
        self.rowcollection[rowindex]=rowdata 
        self.rowlist[rowindex]=rowdata[0]
        #No need to remove from database self.db as it is auto updated due to mutation in lists      
        self.autosave()
        #print ("Successfully modified row, reporting from editrow in Tealordb ") 
        

    def editrow_without_namechange(self, rownametomodify, rowdata):
        #print ("Finding Index for your requested row... ") 
        rowindex=self.rowlist.index(rownametomodify) 
        #rowname= self.rowlist[rowindex] # seems redundant and faulty, will mess with argument rowname
        self.rowcollection[rowindex]=rowdata 
        #No need to remove from database self.db as it is auto updated due to mutation in lists      
        self.autosave()
        #print ("Successfully modified row, reporting from editrow in Tealordb ")         
    	
   
    def setvalue(self, rowname, columnname, newvalue):
        #print ("Finding Index for your requested row... ") 
        rowindex=self.rowlist.index(rowname) 
        colindex=self.collist.index(columnname)
        rowdata=self.rowcollection[rowindex]
        #print (rowdata)
        #print ("Above is old row, Replacing one value in row now... ") 
        rowdata[colindex]=newvalue
        #print ("Replaced in local variable, global automatically changed,reporting from tealordb initialization, check updated value: ")
        #print(rowdata)        
        #print(self.rowcollection[rowindex])
        self.autosave()
        #print ("Successfully modified row, reporting from editrow in Tealordb ") 
        			

	### READ OPERATIONS
    def readrow(self, rowname):
        #print ("Finding Index for your search... ") 
        try:
            rowindex=self.rowlist.index(rowname) 
            #print ("Matching row for your search is :  ") 
            rowdata=self.rowcollection[rowindex]
            #print(rowdata)
            return rowdata
        
        except:
            #print("Not found, reporting from tealordb readrow")    
            val='not_found_row'
            return val
	

    def getval(self, rowname, columnname):
        try:
            rowindex=self.rowlist.index(rowname) 
            colindex=self.collist.index(columnname)
            rowdata=self.rowcollection[rowindex]
            val=rowdata[colindex]
            #print("Value of required field is : ")
            #print (val)
            return val
        except:
            #print("Not found, reporting from tealordb getval")    
            val='not_found'
            return val
	
		
    def createid(self, rowname):
        now= str(datetime.now())
        spacerem=now.replace(" ", "")
        colonrem=spacerem.replace(":", "")
        dotrem=colonrem.replace(".", "")
        dashrem=dotrem.replace("-", "")
        prefix=str(rowname)
        suffix=str(dashrem)
        rowid=prefix+suffix
        return rowid
		

    def timerecorder(self):
        nowf= str(datetime.now())
        spaceremf=nowf.replace(" ", "")
        colonremf=spaceremf.replace(":", "")
        dotremf=colonremf.replace(".", "")
        dashremf=dotremf.replace("-", "")
        rectime=str(dashremf)
        return rectime	
		
					
    def getrowlist (self):
        #print('getrowlist called')
        #print(self.rowlist)
        return self.rowlist	
        
   
    def getcollist (self):
        #print('getcollist called')
        #print(self.collist)
        return self.collist	    

	
    def printtable (self):
        print(self.rowcollection)
        return self.rowcollection	
	
	
    def thresher(self, tothresh):
        #print (tothresh)
        spacerem=tothresh.replace(" ", "")
        colonrem=spacerem.replace(":", "")
        dotrem=colonrem.replace(".", "")
        dollarrem=dotrem.replace("$", "")
        fslashrem=dollarrem.replace("/", "")
        bslashrem=fslashrem.replace("\\", "")
        threshed=bslashrem
        #print (threshed)
        return threshed
        
        
    def gendiskname(self):
        diskname=self.thresher(self.tablename)+'.db'
        #print (diskname)
        return diskname

            
    def autosave(self):
        if self.autosav==0:
            #print("Autosave disabled, reporting from tealordb autosave function")
            pass
            
        elif self.autosav==1:
            self.db.dump() 
            #print("Autosave enabled, reporting from tealordb autosave function")
            
        elif self.autosav=='y':
            self.db.dump() 
            #print("Autosave enabled, reporting from tealordb autosave function")      
        
        elif self.autosav=='n':
            #print("Autosave disabled, reporting from tealordb autosave function")  
            pass  
        
        elif self.autosav=='yes':
            self.db.dump() 
            #print("Autosave enabled, reporting from tealordb autosave function")      
        
        elif self.autosav=='no':
            #print("Autosave disabled, reporting from tealordb autosave function")  
            pass                  
                
        else:
            print("Autosave not properly configured, reporting from tealordb autosave function")   
            self.db.dump() 
           
		
    def saveitodisk(self):
        #print ("Saving table to disk... ")
        self.db.dump() 
        #print ("Saved successfully... ") 
		


        


        
		
 	
        
