from gtts import gTTS
import os

textFilePath = "Image_Descriptions/Labor_Day.txt"

fileName = os.path.basename(textFilePath).split('/')[-1].split('.')[-2]

with open(textFilePath, "r") as file:
    text_prompt = file.read()

# Language in which you want to convert. Full list here: https://gtts.readthedocs.io/en/latest/module.html#localized-accents
language = 'en'
accent = 'us'
  
myobj = gTTS(text=text_prompt, lang=language, tld=accent, slow=False)
  
myobj.save('Audio/' + fileName + '.mp3')