allCountries = ['afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'antigua & deps', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 'bahamas', 'bahrain', 
                'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bhutan', 'bolivia', 'bosnia herzegovina', 'botswana', 'brazil', 'brunei', 'bulgaria', 
                'burkina', 'burundi', 'cambodia', 'cameroon', 'canada', 'cape verde', 'central african rep', 'chad', 'chile', 'china', 'colombia', 'comoros', 'congo', 'costa rica', 
                'croatia', 'cuba', 'cyprus', 'czech republic', 'denmark', 'djibouti', 'dominica', 'dominican republic', 'east timor', 'ecuador', 'egypt', 'el salvador', 
                'equatorial guinea', 'eritrea', 'estonia', 'ethiopia', 'fiji', 'finland', 'france', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 
                'guatemala', 'guinea', 'guinea-bissau', 'guyana', 'haiti', 'honduras', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 
                'ivory coast', 'jamaica', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kiribati', 'north korea', 'south korea', 'kosovo', 'kuwait', 'kyrgyzstan', 'laos', 'latvia', 
                'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'macedonia', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 
                'marshall islands', 'mauritania', 'mauritius', 'mexico', 'micronesia', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'myanmar', 'namibia', 
                'nauru', 'nepal', 'netherlands', 'new zealand', 'nicaragua', 'niger', 'nigeria', 'norway', 'oman', 'pakistan', 'palau', 'panama', 'papua new guinea', 'paraguay', 
                'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russian federation', 'rwanda', 'st kitts & nevis', 'st lucia', 'saint vincent & the grenadines', 
                'samoa', 'san marino', 'sao tome & principe', 'saudi arabia', 'senegal', 'serbia', 'seychelles', 'sierra leone', 'singapore', 'slovakia', 'slovenia', 
                'solomon islands', 'somalia', 'south africa', 'south sudan', 'spain', 'sri lanka', 'sudan', 'suriname', 'swaziland', 'sweden', 'switzerland', 'syria', 'taiwan', 
                'tajikistan', 'tanzania', 'thailand', 'togo', 'tonga', 'trinidad & tobago', 'tunisia', 'turkey', 'turkmenistan', 'tuvalu', 'uganda', 'ukraine', 
                'united arab emirates', 'united kingdom', 'united states', 'uruguay', 'uzbekistan', 'vanuatu', 'vatican', 'venezuela', 'vietnam', 'yemen', 'zambia', 'zimbabwe']


countries = []

removedCountries = []

##########

countriesInAfrica = []

countriesInNorthAmerica = ["canada", "united states", ]

countriesInLatinAmerica = ['antiqua&barbuda', 'bahamas', 'barbados', 'cuba', 'dominica', 'dominican republic', 'grenada', 'haiti', 'jamaica', 'puerto rico', 'saint barthélemy', 
                           'st kitts&nevis', 'st lucia', 'st. vincent and the grenadines', 'trinidad&tobago', 'belize', 'costa rica', 'el salvador', 'guatemalahonduras', 'mexico', 
                           'nicaragua', 'panama', 'argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador', 'french guiana', 'guyana', 'paraguay', 'peru', 'suriname', 
                           'uruguay', 'venezuela']

countriesInAsia = []

countriesInAntartica = ["", "antartica"]

countriesInEurope = ['russia', 'germany', 'united kingdom', 'france', 'italy', 'spain', 'poland', 'ukraine', 'romania', 'netherlands', 'belgium', 'sweden', 'czech republic', 
                     'greece', 'portugal', 'hungary', 'belarus', 'austria', 'switzerland', 'serbia', 'bulgaria', 'denmark', 'slovakia', 'finland', 'norway', 'ireland', 'croatia', 
                     'moldova', 'bosnia and herzegovina', 'albania', 'lithuania', 'slovenia', 'north macedonia', 'latvia', 'estonia', 'luxembourg', 'montenegro', 'malta', 'iceland', 
                     'andorra', 'liechtenstein', 'monaco', 'san marino', 'holy see']

countriesInOceania = ["australia", "papua new guinea", "new zealand", "fiji", "solomon islands", "micronesia", "vanuatu",
                      "samoa", "kiribati", "tonga", "marshall islands", "palau", "nauru", "tuvalu"]


class Functions:

    def Restart():
        Functions.ResetCountriesList()
        Functions.ResetRemovedCountriesList()
        Functions.UpdateCountriesList()

    def ResetCountriesList():
        for x in range(0,len(countries)):
            del countries[-1]

    def ResetRemovedCountriesList():
        for x in range(0, len(removedCountries)):
            del removedCountries[-1]
    
    def UpdateCountriesList():
        countries.extend(allCountries)

countriesInEurope = [x.lower() for x in countriesInEurope]
print(countriesInEurope)