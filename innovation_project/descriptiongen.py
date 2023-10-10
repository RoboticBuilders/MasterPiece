'''
IMPORTANT: HOW TO USE
  GENERATING API KEY
    Go to bard.google.com
    Open Chrome DevTools/Application
    Go to Storage/Cookies/https://bard.google.com
    Find Secure-1PSID
    Copy the Value and paste it into the token parameter for the Bard() function
  REGENERATING API KEY
    Clear cookies & cache
    Follow the instructions above
  NOTE: The API key is different for every account
If the API key doesn't work, then follow the instructions for regenerating API keys
'''

from bardapi import Bard

bard = Bard(token='bwgbJ96RXWr-M4Br88NjDzAC8JmgN9UBLRW4EVc3xISOr2VQWsOQ-kmxeRe_-hIFyZ9v8A.') # get the bard api key
image = open('image.png', 'rb').read() # get the image locally
bard_answer = bard.ask_about_image('What is in the image?', image) # send the prompt to bard
print(bard_answer['content']) # print the answer
