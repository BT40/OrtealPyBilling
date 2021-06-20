# This file contains standard data which will be copied to databases.
# Examples are standard tax rates, countries list.


countrieslist=['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 
    'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and herzegovina', 'botswana', 'brazil', 'brunei', 'bulgaria', 'burkina faso', 'burundi', 
     'Cambodia', 'Cameroon', 'Canada', 'Cape verde', 'Central african republic', 'Chad', 'Chile', 'China', 'Columbia', 'Comoros', 'Congo', 'Costa rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech republic czechia' 'Cote d ivoire', 
    'Denmark', 'Djibouti', 'Dominica', 'Dominician republic', 'Dr congo' 
     'Ecuador', 'Egypt', 'El salvador', 'Equatorial guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 
     'Fiji', 'Finland', 'France', 
     'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-bissau', 'Guyana', 
     'Haiti', 'Holy see (Vatican city)', 'Honduras', 'Hungary', 
     'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory coast (Republic of cote d ivoire)'
     'Jamaica', 'Japan', 'Jordan', 
     'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyztan' 
     'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
     'Madagaskar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 
     'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North korea', 'North macedonia', 'Norway', 
     'Oman', 
     'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua new guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
      'Qatar', 
      'Republic of cabo verde', 'Republic of uzbekistan ', 'Romania', 'Russia', 'Rwanda', 
       
     'Saint kitts & nevis', 'Saint lucia', 'Saint vincent and the grenadines', 'Samoa', 'San marino', 'Sao Tome & principe', 'Saudi arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon islands', 'Somalia', 'South africa', 'South korea', 'South ossetia' 'South sudan', 'Spain', 'Sri lanka', 'St. vincent & grenadines', 'State of palestine', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria',  
     'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-leste', 'Togo', 'Tonga', 'Trinidad and tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 
     'Uganda', 'Ukraine', 'United arab emirates', 'United kingdom', 'United states of america', 'Uruguay', 'Uzbekistan', 
     'Vanuatu', 'Venezuela', 'Vietnam', 
     'Yamen', 'Zambia', 'Zimbabwe' 
     'USA', 'East timor', 'England', 'Kosovo', 'Great britain', 'Swaziland (eswatini)', 'Vatican city (Holy see)', 'Other']



statelist_india_std=['Chandigarh', 'Delhi', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Karnataka', 'Punjab', 'Maharashtra', 'Tamil nadu']

statecodesgst_india_std=['04', '07', '06', '2', '01', '29', '03', '27', '33']

statelist_india_stdGST=['Jammu and Kashmir', 'Himachal Pradesh', 'Punjab', 'Chandigarh', 'Uttrakhand', 'Haryana', 'Delhi', 'Rajasthan', 'Uttar Pradesh', 'Bihar', 'Sikkim', 'Arunachal Pradesh', 'Nagaland', 'Manipur', 'Mizoram', 'Tripura', 'Meghalaya', 'Assam', 'West Bengal', 'Jharkhand', 'Odisha', 'Chhatisgarh', 'Madhya Pradesh', 'Gujarat', 'Dadra Nagar Haveli Daman Diu', 'Maharashtra', 'Andhra Pradesh Before devision', 'Karanataka', 'Goa', 'Lakshadweep', 'Kerala', 'Tamil Nadu', 'Puducherry', 'Andaman Nicobar Islands', 'Telangana', 'Andhra Pradesh', 'Ladakh'] #State codes are index number of states +1



gstslabs_list_std=['GST 0% (SGST+CGST)', 'GST 5% (SGST+CGST)', 'GST 12% (SGST+CGST)', 'GST 18% (SGST+CGST)', 'GST 28% (SGST+CGST)', 'IGST 0%',  'IGST 5%', 'IGST 12%', 'IGST 18%', 'IGST 28%']

gstslabs_data_std=[
['GST 0% (SGST+CGST)', 'y', 'y', 'n', 'SGST', 'CGST', '', '0', '0', '0', '0' ], 
['GST 5% (SGST+CGST)', 'y', 'y', 'n', 'SGST', 'CGST', '', '2.5', '2.5', '0', '5'],
['GST 12% (SGST+CGST)', 'y', 'y', 'n', 'SGST', 'CGST', '', '6', '6', '0', '12'],
['GST 18% (SGST+CGST)', 'y', 'y', 'n', 'SGST', 'CGST', '', '9', '9', '0', '18'],
['GST 28% (SGST+CGST)', 'y', 'y', 'n', 'SGST', 'CGST', '', '14', '14', '0', '28'],
['IGST 0%', 'y', 'n', 'n', 'IGST', '', '', '0', '0', '0', '0'],
['IGST 5%', 'y', 'n', 'n', 'IGST', '', '', '5', '0', '0', '5'],
['IGST 12%', 'y', 'n', 'n', 'IGST', '', '', '12', '0', '0', '12'],
['IGST 18%', 'y', 'n', 'n', 'IGST', '', '', '18', '0', '0', '18'],
['IGST 28%', 'y', 'n', 'n', 'IGST', '', '', '28', '0', '0', '28']
]


	
taxontax_list_std=['None', 'Demo Cess 1%']

taxontax_data_std=[
['None', 'n', 'n', 'n', '', '', '', '0', '0', '0', '0' ], 
['Demo Cess 1%', 'y', 'n', 'n', 'Cess', '', '', '1', '0', '0', '1' ]
]




        
        

