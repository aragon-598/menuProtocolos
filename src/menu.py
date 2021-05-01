from gtts import gTTS

texto = 'Presione 1 para escuchar el espacio libre en el disco duro donde está instalado asterisk. Presione 2 si desea llamar a un agente disponible. Presione 3 para volver a escuchar el menú'

language = 'es'

audio = gTTS(text= texto, lang=language,slow=False)

audio.save('menusintilde.gsm')