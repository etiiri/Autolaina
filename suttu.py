# Testiympäristö
# ==============

import json

settingsFile = open('settings.txt', 'rt')
fileContent = settingsFile.read()
print(fileContent)

#settingsFile = open('settings.txt', 'rt')
#settingsFile.write("tesxt")
#settingsFile.close()



asetuksetDict = {
    'server': 'autolaina@raseko.fi',
    'port': 5432,
    'database': 'autolainaus',
    'userName': 'pertti24',
    'password': 'asdfghjk'
}

# Kirjoitetaan asetukset tiedostoon ja luodaan se tarvittaessa
with open('asetukset.json','wt') as settingsFile:
    settingsFile.write(asetuksetJson)
    print("Asetukset tallennettu")
...
# Luetaan asetukset tiedostosta Python-sanakirjaan
asetuksetDict = {}
with open('asetukset.json','rt') as settingsFile:
    rawSettings = settingsFile.read()
    asetuksetDict = json.loads(rawSettings)
    
# Avataan tiedost settings.txt kirjoitusta varten
settingFile2 = open('settings.txt', 'wt')
uudetAsetukset = 'Asetukset\nPalvelin: 10.66.0.3\n'
settingFile2.write("Tyhjät asetukset:") # Kirjoitetaan uudet tiedot
settingFile2.close() # Suljettava kirjoituksen jälkeen


cipherKey = fernet.Fernet.generate_key()
cipher = fernet.Fernet(chiperKey)

plainPassword = 'asdfghjk'

encryptedPassword = cipherKey.e