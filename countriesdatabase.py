allCountries = ['afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'antigua and barbuda', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 
                'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bhutan', 'bolivia', 'bosnia and herzegovina', 'botswana', 
                'brazil', 'brunei', 'bulgaria', 'burkina faso', 'burundi', 'cambodia', 'cameroon', 'canada', 'cape verde', 'central african republic', 'chad', 'chile',
                'china', 'colombia', 'comoros', 'costa rica', 'croatia', 'cuba', 'cyprus', 'czech republic', 'democratic republic of the congo', 'denmark', 'djibouti', 
                'dominica', 'dominican republic', 'east timor', 'ecuador', 'egypt', 'el salvador', 'equatorial guinea', 'eritrea', 'estonia', 'eswatini', 'ethiopia', 
                'federated states of micronesia', 'fiji', 'finland', 'france', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 'guatemala', 
                'guinea', 'guinea-bissau', 'guyana', 'haiti', 'honduras', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 
                'ivory coast', 'jamaica', 'japan', 'jordan', 'kazakhstan', 'kenya', 'kiribati', 'kosovo', 'kuwait', 'kyrgyzstan', 'laos', 'latvia', 'lebanon', 
                'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'madagascar', 'malawi', 'malaysia', 'maldives', 'mali', 'malta', 
                'marshall islands', 'mauritania', 'mauritius', 'mexico', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'myanmar', 
                'namibia', 'nauru', 'nepal', 'netherlands', 'new zealand', 'nicaragua', 'niger', 'nigeria', 'north korea', 'north macedonia', 'norway', 'oman', 
                'pakistan', 'palau', 'palestine', 'panama', 'papua new guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'republic of the congo', 
                'romania', 'russia', 'rwanda', 'saint kitts and nevis', 'saint lucia', 'saint vincent and the grenadines', 'samoa', 'san marino', 'saudi arabia', 'senegal', 
                'serbia', 'seychelles', 'sierra leone', 'singapore', 'slovakia', 'slovenia', 'solomon islands', 'somalia', 'south africa', 'south korea', 'south sudan', 
                'spain', 'sri lanka', 'sudan', 'suriname', 'sweden', 'switzerland', 'syria', 'são tomé and príncipe', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'togo', 
                'tonga', 'trinidad and tobago', 'tunisia', 'turkey', 'turkmenistan', 'tuvalu', 'uganda', 'ukraine', 'united arab emirates', 'united kingdom', 
                'united states of america', 'uruguay', 'uzbekistan', 'vanuatu', 'vatican city', 'venezuela', 'vietnam', 'yemen', 'zambia', 'zimbabwe']





countries = []

removedCountries = []

##########

countriesInAfrica = ['algeria', 'angola', 'benin', 'botswana', 'burkina faso', 'burundi', 'cameroon', 'cape verde', 'central african republic', 'chad', 'comoros',
                    'democratic republic of the congo', 'djibouti', 'egypt', 'equatorial guinea', 'eritrea', 'eswatini', 'ethiopia', 'gabon', 'gambia', 'ghana',
                    'guinea', 'guinea-bissau', 'ivory coast', 'kenya', 'lesotho', 'liberia', 'libya', 'madagascar', 'malawi', 'mali', 'mauritania', 'mauritius',
                    'morocco', 'mozambique', 'namibia', 'niger', 'nigeria', 'republic of the congo', 'rwanda', 'são tomé and príncipe', 'senegal', 'seychelles',
                    'sierra leone', 'somalia', 'south africa', 'south sudan', 'sudan', 'tanzania', 'togo', 'tunisia', 'uganda', 'zambia', 'zimbabwe']

countriesInNorthAmerica = ['antigua and barbuda', 'bahamas', 'barbados', 'belize', 'canada', 'costa rica', 'cuba', 'dominica', 'dominican republic', 'el salvador', 
                           'grenada', 'guatemala', 'haiti', 'honduras', 'jamaica', 'mexico', 'nicaragua', 'panama', 'saint kitts and nevis', 'saint lucia', 
                           'saint vincent and the grenadines', 'trinidad and tobago', 'united states of america']

countriesInSouthAmerica = ['argentina', 'bolivia', 'brazil', 'chile', 'colombia', 'ecuador', 'guyana', 'paraguay', 'peru', 'suriname', 'uruguay', 'venezuela']

countriesInAsia = ['afghanistan', 'armenia', 'azerbaijan', 'bahrain', 'bangladesh', 'bhutan', 'brunei', 'cambodia', 'china', 'cyprus', 'east timor', 'georgia', 
                   'india', 'indonesia', 'iran', 'iraq', 'israel', 'japan', 'jordan', 'kazakhstan', 'kuwait', 'kyrgyzstan', 'laos', 'lebanon', 'malaysia', 'maldives', 
                   'mongolia', 'myanmar', 'nepal', 'north korea', 'oman', 'pakistan', 'philippines', 'palestine', 'qatar', 'saudi arabia', 'singapore', 'south korea', 
                   'sri lanka', 'syria', 'taiwan', 'tajikistan', 'thailand', 'turkey', 'turkmenistan', 'united arab emirates', 'uzbekistan', 'vietnam', 'yemen']

countriesInAntartica = ['', 'antartica']

countriesInEurope = ['albania', 'andorra', 'austria', 'belarus', 'belgium', 'bosnia and herzegovina', 'bulgaria', 'croatia', 'czech republic', 'denmark', 'estonia', 
                     'finland', 'france', 'germany', 'greece', 'hungary', 'iceland', 'ireland', 'italy', 'kosovo', 'latvia', 'liechtenstein', 'lithuania', 'luxembourg',
                       'malta', 'moldova', 'monaco', 'montenegro', 'netherlands', 'north macedonia', 'norway', 'poland', 'portugal', 'romania', 'russia', 'san marino', 
                       'serbia', 'slovakia', 'slovenia', 'spain', 'sweden', 'switzerland', 'ukraine', 'united kingdom', 'vatican city']

countriesInOceania = ['australia', 'federated states of micronesia', 'fiji', 'kiribati', 'marshall islands', 'nauru', 'new zealand', 'palau', 'papua new guinea', 'samoa',
                       'solomon islands', 'tonga', 'tuvalu', 'vanuatu']


class Functions:

    def RestartAll():
        Functions.ResetCountriesList()
        Functions.ResetRemovedCountriesList()
        Functions.UpdateCountriesListAllCountries()

    def RestartAfrica():
        Functions.ResetCountriesList()
        Functions.ResetRemovedCountriesList()
        Functions.UpdateCountriesListAfrica()

    def RestartNA():
        Functions.ResetCountriesList()
        Functions.ResetRemovedCountriesList()
        Functions.UpdateCountriesListNA()

    def RestartSA():
        Functions.ResetCountriesList()
        Functions.ResetRemovedCountriesList()
        Functions.UpdateCountriesListSA()

    def RestartAsia():
        Functions.ResetCountriesList()
        Functions.ResetRemovedCountriesList()
        Functions.UpdateCountriesListAsia()

    def RestartAntartica():
        Functions.ResetCountriesList()
        Functions.ResetRemovedCountriesList()
        Functions.UpdateCountriesListAntartica()

    def RestartEurope():
        Functions.ResetCountriesList()
        Functions.ResetRemovedCountriesList()
        Functions.UpdateCountriesListEurope()

    def RestartOceania():
        Functions.ResetCountriesList()
        Functions.ResetRemovedCountriesList()
        Functions.UpdateCountriesListOceania()

    def ResetCountriesList():
        for x in range(0,len(countries)):
            del countries[-1]

    def ResetRemovedCountriesList():
        for x in range(0, len(removedCountries)):
            del removedCountries[-1]
    
    def UpdateCountriesListAllCountries():
        countries.extend(allCountries)

    def UpdateCountriesListAfrica():
        countries.extend(countriesInAfrica)

    def UpdateCountriesListNA():
        countries.extend(countriesInNorthAmerica)

    def UpdateCountriesListSA():
        countries.extend(countriesInSouthAmerica)

    def UpdateCountriesListAsia():
        countries.extend(countriesInAsia)

    def UpdateCountriesListAntartica():
        countries.extend(countriesInAntartica)

    def UpdateCountriesListEurope():
        countries.extend(countriesInEurope)

    def UpdateCountriesListOceania():
        countries.extend(countriesInOceania)

countriesInOceania = [x.lower() for x in countriesInOceania]
print(countriesInOceania)

