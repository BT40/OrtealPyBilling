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


class Company():
    def createcompany(self, namecf, gstcf, addresscf, statecf, contactcf, catcf):
        self.namec=namecf

	



class Items():
    def createitem(self, idata):
        self.name=idata[0]
        self.hsn=idata[1]
        self.group=idata[2]
        self.unit=idata[3]
        self.tax=idata[4]
        self.openstock=idata[5]
        self.critical=idata[6]
        self.listprice=idata[7]
        self.stddisc=idata[8]
        self.sellprice=idata[9]
        self.purprice=idata[10]
        self.comments=idata[11]
        return idata
        
        
    
    def precreateitem(self): #preprocessor for creating item
        pass

    

        
        

