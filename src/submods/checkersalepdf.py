import sys
import operator
#from submods import functions

 
def item_lines_reqd(invoicedata, whichitem):
       
    
    itemnames= invoicedata[73]
    itemquantities=invoicedata[74]
    itemunits=invoicedata[80]
    
    iqty_display=str(itemquantities[whichitem])+str(itemunits[whichitem])
            
            
    tv=0.5
    if len(str(itemnames[whichitem]))>32:
        tv=tv+1
        
    if len(iqty_display)>8:
        tv=tv+10
        
    #if len(str(itemrates[whichitem]))>10:
    #    tv=tv+1
               
    #if len(str(itemamounts[whichitem]))>9:
    #    tv=tv+1            
        
    if tv>1:
        if tv>11: #both are long
            return 4           
        elif tv>10: #only qty is long
            return 3     
        else: #only name is long
            return 2
    else:
        return 1    
    
    
    
    
    #print('above was guicommon initialisation')    
   
    
      
