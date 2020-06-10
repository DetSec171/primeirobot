import requests
from bs4 import BeautifulSoup
import telepot

def reinit():
    pg = requests.get('https://www.worldometers.info/coronavirus/country/brazil/')
    soup = BeautifulSoup(pg.text, 'html.parser')
    box = soup.findAll("div", {"class": "maincounter-number"})
    bot = telepot.Bot("1011356085:AAHz_f9ITilXVppXUO_KwzwYg3nhH1ikl20")
	
    infectados = box[0].text.strip()
    mortos = box[1].text.strip()
    recuperadoss = box[2].text.strip()
	
    up = bot.getUpdates()
	
    id = up[-1]['message']['from']['id']
	
    nome = up[-1]['message']['chat']['first_name']
	
    msguser = up[-1]['message']['text']
	
    br = ("Olá, " + nome + ", esses são os casos de COVID NO BRASIL 🇧🇷 \n\n\n"+ \
	     "😷 CASOS CONFIRMADOS 😷: " + infectados + "\n\n" + \
	       "💀 MORTOS 💀: " + mortos + "\n\n" + \
	     "❤️ RECUPERADOS ❤️: " + recuperados + "\n\n")	
    bot.sendMessage(id, "apos receber as informacoes, digite /stop para nao bugar o bot")
    if msguser == '/covidbrinfo':
        bot.sendMessage(id, br)
    elif msguser == '/stop':
        exit()
    else:
        bot.sendMessage(id, "Para usar, digite: /covidbrinfo ou /stop para parar o bot")
        reinit()
reinit()
