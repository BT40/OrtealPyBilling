# This file contains functions which will be called from elsewhere to perform the required operation
# Examples are creating new supplier, creating item, calculating tax

from datetime import datetime

countrieslist=['afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'antigua and barbuda', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 
    'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bhutan', 'bolivia', 'bosnia and herzegovina', 'botswana', 'brazil', 'brunei', 'bulgaria', 'burkina faso', 'burundi', 
     'cambodia', 'cameroon', 'canada', 'cape verde', 'central african republic', 'chad', 'chile', 'china', 'columbia', 'comoros', 'congo', 'costa rica', 'croatia', 'cuba', 'cyprus', 'czech republic czechia' 'cote d ivoire', 
    'denmark', 'djibouti', 'dominica', 'dominician republic', 'dr congo' 
     'ecuador', 'egypt', 'el salvador', 'equatorial guinea', 'eritrea', 'estonia', 'eswatini', 'ethiopia', 
     'fiji', 'finland', 'france', 
     'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 'guatemala', 'guinea', 'guinea-bissau', 'guyana', 
     'haiti', 'holy see (vatican city)', 'honduras', 'hungary', 
     'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 'ivory coast (Republic of cote d ivoire)'
     'jamaica', 'japan', 'jordan', 
     'kazakhstan', 'kenya', 'kiribati', 'kuwait', 'kyrgyztan' 
     'laos', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg',
     'madagaskar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 'marshall islands', 'mauritania', 'mauritius', 'mexico', 'micronesia', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'myanmar', 
     'namibia', 'nauru', 'nepal', 'netherlands', 'new zealand', 'nicaragua', 'niger', 'nigeria', 'niue', 'north korea', 'north macedonia', 'norway', 
     'oman', 
     'pakistan', 'palau', 'palestine', 'panama', 'papua new guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal',
      'qatar', 
      'Republic of cabo verde', 'republic of uzbekistan ', 'romania', 'russia', 'rwanda', 
       
     'saint kitts & nevis', 'saint lucia', 'saint vincent and the grenadines', 'samoa', 'san marino', 'sao tome & principe', 'saudi arabia', 'senegal', 'serbia', 'seychelles', 'sierra leone', 'singapore', 'slovakia', 'slovenia', 'solomon islands', 'somalia', 'south africa', 'south korea', 'south ossetia' 'south sudan', 'spain', 'sri lanka', 'st. vincent & grenadines', 'state of palestine', 'sudan', 'suriname', 'sweden', 'switzerland', 'syria',  
     'taiwan', 'tajikistan', 'tanzania', 'thailand', 'timor-leste', 'togo', 'tonga', 'trinidad and tobago', 'tunisia', 'turkey', 'turkmenistan', 'tuvalu', 
     'uganda', 'ukraine', 'united arab emirates', 'united kingdom', 'united states of america', 'uruguay', 'uzbekistan', 
     'vanuatu', 'venezuela', 'vietnam', 
     'yamen', 'zambia', 'zimbabwe' 
     'usa', 'east timor', 'england', 'kosovo', 'britain', 'swaziland (eswatini)', 'vatican city (holy see)', 'other']


dobj = datetime.now() #object for datetime class accessing
todayobj=dobj.date()
todaysdate_string=str(todayobj) 
current_timeobj=dobj.time()
currenttime_string=str(current_timeobj) 

def check_date_format(date_string):

    try:
        yyyy=int(date_string[0:4])
        mm=int(date_string[5:7])
        dd=int(date_string[8]+date_string[9])    
        #print(yyyy)
        #print(mm)
        #print(dd)
    except:
        #print("Date seems invalid, reporting from except block of check_date_format")
        return 'invalid'   
    #print('currently just above rules')
    rules = [mm<13, dd<32, date_string[4]=='-', date_string[7]=='-', len(date_string)==10]

    if all(rules):
        #print("Date seems valid")
        return 'valid'
        
    else:
        #print('date seems invalid, reporting from else block')    
        return 'invalid' 
