'''
IMPORTANT: HOW TO USE
  GENERATING API KEY
    Go to bard.google.com
    Open Chrome DevTools/Application
    Go to Storage/Cookies/https://bard.google.com
    Find Secure-1PSID
    Copy the Value and paste it into the API_KEY variable
  REGENERATING API KEY
    Clear cookies & cache
    Follow the instructions above
  NOTE: The API key is different for every account
If the API key doesn't work, then follow the instructions for regenerating API keys
'''

from bardapi import Bard
import os

API_KEY = ""

os.environ['_BARD_API_KEY']=API_KEY

painting_link = str(input("Insert link to painting:"))

request = str("Write a description for this painting: " + painting_link)
print(Bard().get_answer(request)['content'])
