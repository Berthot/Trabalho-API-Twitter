from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

save = open('salvando_dados.txt', 'w')
contador = open('contador.txt', 'w')





class AssinanteTwitter(StreamListener):

    def __init__(self):
        super().__init__()
        self.lol = 0
        self.mine = 0
        self.pubg = 0
        self.dota = 0
        self.csgo = 0
        self.freefire = 0

    def search(self, lista):
        i = lista.lower()

        if i.find('league of legends') != -1:
            self.lol += 1
        if i.find('minecraft') != -1:
            self.mine += 1
        if i.find('pubg') != -1:
            self.pubg += 1
        if i.find('dota') != -1:
            self.dota += 1
        if i.find('csgo') != -1:
            self.csgo += 1
        if i.find('ff') != -1:
            self.freefire += 1

    def salva(self):
        contador.write(f"|LOL - {self.lol} |MINE - {self.mine} |PUBG - {self.pubg} |DOTA - {self.dota} |CSGO - {self.csgo} |FF - {self.freefire} \n \n")

    def on_data(self, data):
        conteudoJSON = json.loads(data)
        dados = conteudoJSON["text"]
        print(dados)
        save.write(dados + '\n')
        self.search(dados)
        self.salva()
        return True

    # Essa função será invocada automaticamente toda vez que ocorrer um erro
    def on_error(self, status):
        print(status)

print("Inicio do programa")
consumer_key="NLaisEh7x2RXCLsMd1H5c7EQe"
consumer_secret="Zej68qEjbbNsgkN5w8VY1LlZRhHnGbBcWFUIXDeV6x5yfLeuJf"


access_token="1163572452615708674-27nY8JFuviOPTkLLuXHXNUp1wDeUBz"
access_token_secret="bnQ97UZdy7B6IhOtvPvtXu6swonCTFw6MIMsaOb9CZvsV"

assinante = AssinanteTwitter()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, assinante)
stream.filter(track=['league of legends', 'dota', 'minecraft', 'csgo', 'freefire', 'pubg'], languages=["pt"])

