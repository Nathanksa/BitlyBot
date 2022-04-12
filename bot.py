#@THANK YOU 
#@THANKSS FLAC
from pyrogram import Client, filters
import requests 
import json 
import os

TOKEN = os.environ.get("TOKEN", "")
API_ID = int(os.environ.get("API_ID",12345))
API_HASH = os.environ.get("API_HASH","")
ONCEHELP_TOKEN = os.environ.get("ONCEHELP_TOKEN","")

headers = {
    'Authorization': ONCEHELP_TOKEN,
    'Content-Type': 'application/json',
}


app = Client("oncehelpbot" ,bot_token = TOKEN ,api_id = API_ID ,api_hash = API_HASH )

@app.on_message(filters.private & filters.command(['start']))
async def start(client,message):
  await message.reply_text(f"Hello {message .from_user.first_name}\nhello i am oncehelp short link genrator\n made  ", reply_to_message_id = message.message_id)
  
@app.on_message(filters.private & filters.regex("http|https"))
async def Bitly(client,message):
  URL = message.text
  DOMAIN = "oncehelp.com"
  value  = {'long_url': URL , 'domain': DOMAIN}
  data = json.dumps(value)
  try:
    r = requests.post('https://api-ssl.oncehelp.com/v4/shorten', headers=headers,data = data )
    result = r.json()
    link = result["link"]
    await message.reply_text(f"```{link}```", reply_to_message_id= message.message_id)
  except Exception as e :
    await message.reply_text(e)
    
app.run()
    
