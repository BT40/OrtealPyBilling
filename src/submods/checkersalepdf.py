import sys
import operator
#from submods import functions


def calc_letters_accomodation(invoicedata, whichitem, allsmallcapability):
    itemname= invoicedata[73][whichitem]
    itemname_relevant=itemname[0:allsmallcapability] #necessary, because if caps are in rear end of string, say beyond row capability, it doesnot affect current line capability
    #print(itemname)    
    count = 0
    for character in itemname_relevant:
        if character.isupper():
            count += 1    
    #print(count)
    capitalscount=count
    reductioncapability=0.4*(min(capitalscount, 32)) #min bcoz one row can only contain 32 caps, if calculated with 48 all in case of whole line caps, extra space is left 
    currentcapability=int(allsmallcapability-reductioncapability)
    #print(currentcapability)
    return currentcapability

 
def item_lines_reqd(invoicedata, whichitem):
       
    allsmallcapability=42 #accomodation with all small mix letters
    currentcapability=calc_letters_accomodation(invoicedata, whichitem, allsmallcapability)
    itemnames= invoicedata[73]
    itemquantities=invoicedata[74]
    itemunits=invoicedata[80]
    
    iqty_display=str(itemquantities[whichitem])+str(itemunits[whichitem])
            
            
    tv=0.5
    if len(str(itemnames[whichitem]))>currentcapability:
        tv=tv+1
        
    if len(iqty_display)>8:
        tv=tv+10
        
    #if len(str(itemrates[whichitem]))>10:
    #    tv=tv+1
               
    #if len(str(itemamounts[whichitem]))>9:
    #    tv=tv+1            
        
    if tv>1:
        if tv>11: #both are long
            return 4, currentcapability           
        elif tv>10: #only qty is long
            return 3, currentcapability     
        else: #only name is long
            return 2, currentcapability
    else:
        return 1, currentcapability    
    

def calc_letters_accomodation_myname(companyname, allsmallcapability): #title or my company name
    
    cname_relevant=companyname[0:allsmallcapability] #necessary, because if caps are in rear end of string, say beyond row capability, it doesnot affect current line capability  
    count = 0
    for character in cname_relevant:
        if character.isupper():
            count += 1    
    capitalscount=count
    reductioncapability=0.4*(min(capitalscount, 24)) #min bcoz one row can only contain 24 caps, if calculated with 48 all in case of whole line caps, extra space is left 
    widecount=0
    chars_set_wide=['M', 'W']
    for eachchar in chars_set_wide:
        for eachcharacter in cname_relevant:
            if eachcharacter==eachchar:
                widecount += 1  
    
    additionalred_wide=0.5*widecount #for ultra wide chars like w, m,
    currentcapability=int(allsmallcapability-reductioncapability-additionalred_wide)
    #print(currentcapability)
    return currentcapability    
      
