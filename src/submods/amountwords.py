#import math


def numbers_to_words(num):  #This fn is just an interpretter
    under_20 = ['Zero','One','Two','Three', 'Four','Five','Six','Seven', 'Eight','Nine','Ten','Eleven', 'Twelve','Thirteen', 'Fourteen','Fifteen','Sixteen', 'Seventeen','Eighteen','Nineteen']
    tens = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
    above_100 = {100: 'Hundred',1000:'Thousand', 100000:'Lakhs', 10000000:'Crores'}

    if num < 20:
         return under_20[(int)(num)]

    if num < 100:
        return tens[(int)(num/10)-2] + ('' if num%10==0 else ' ' + under_20[(int)(num%10)])

    # find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
    pivot = max([key for key in above_100.keys() if key <= num])

    return numbers_to_words((int)(num/pivot)) + ' ' + above_100[pivot] + ('' if num%pivot==0 else ' ' + numbers_to_words(num%pivot))


def rupee_paisa_splitter(numbr): #make sure point or . present before calling this function
    number=str(numbr)
    #print(number)
    #print("Above is input")
    if '.' in number: #check if . is present
        before_decimal_num=int(number.split(".")[0])
        #after_decimal_num=int(number.split(".")[1]) #Do not temper this line
        after_decimal_numstr_raw=(number.split(".")[1]) 
        if len(after_decimal_numstr_raw)>2: # reduce digits to two
            after_decimal_twonum=int(after_decimal_numstr_raw[0:2])
        elif len(after_decimal_numstr_raw)==2: # keep as it is     
            after_decimal_twonum=int(after_decimal_numstr_raw)
        elif len(after_decimal_numstr_raw)==1: # add one 0 to it
            after_decimal_twonum=int(after_decimal_numstr_raw + "0")  
        else:
            pass        
    
    return before_decimal_num, after_decimal_twonum 


def amount_indian_currency(numbr): # Try to do rounding to two places before feeding
    if '.' not in str(numbr):  #if no point or dot present
        #print ('dot not present')
        before_decimal_num=int(numbr) 
        after_decimal_twonum=0 
        rupees=numbers_to_words(before_decimal_num)        
        am_words='Rupees ' + rupees +  ' Only' 
        
    if  '.' in str(numbr):
        #print('Dot present')
        before_decimal_num, after_decimal_twonum=rupee_paisa_splitter(numbr)      
        rupees=numbers_to_words(before_decimal_num)
        paise=numbers_to_words(after_decimal_twonum)
        am_words='Rupees ' + rupees + ' and ' + paise + ' Paisa' + ' Only' 
    #print(am_words)
    return am_words
  
        
#amount_indian_currency("325.2")


