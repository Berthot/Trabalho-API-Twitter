from tweepy.streaming import StreamListener
import json
from time import strftime, localtime, time


save = open('salvando_dados.txt', 'w')


class AssinanteTwitter(StreamListener):

    def __init__(self, tempo=30):
        self.start_time = time()
        self.end_time = tempo

        self.time_stamp = strftime("%d-%m-%Y %H:%M:%S - Curitiba, Brazil", localtime())  # Hora e data real

        self.salva_dados(f"INICIO COLETA DE TWEETS- {self.time_stamp}")

        self.lol = 0
        self.mine = 0
        self.pubg = 0
        self.dota = 0
        self.csgo = 0
        self.freefire = 0
        super().__init__()  # Inicializador da classe pai

    def cronometro(self):  # Retorna o tempo decorrido
        return time() - self.start_time

    def search(self, tweet):
        tweet = tweet.lower()

        if 'league of legends' in tweet:
            self.lol += 1
        if 'minecraft' in tweet:
            self.mine += 1
        if 'pubg' in tweet:
            self.pubg += 1
        if 'dota' in tweet:
            self.dota += 1
        if 'csgo' in tweet:
            self.csgo += 1
        if any(jogo in tweet for jogo in ['free fire', 'free fire']):  # Procura pelos 2 termos
            self.freefire += 1

    def salva_json(self):

        # Lendo o json
        with open('contador.json') as file:
            data = json.load(file)

        # Modificando o json
        data["lol"] = self.lol
        data["mine"] = self.mine
        data["pubg"] = self.pubg
        data["lol"] = self.dota
        data["dota"] = self.csgo
        data["ff"] = self.freefire

        # Salvando o json
        with open('contador.json', "w") as file:
            json.dump(data, file, indent=4)

    def salva_dados(self, conteudo):
        with open('salvando_dados.txt', 'a+') as file:
            head = "-" * 140
            file.write(f"{conteudo}\n{head}\n")

    # Função de loop pelos tweets
    def on_data(self, data):
        if self.cronometro() < self.end_time: # Testa se ainda não passou o tempo limete
            conteudoJSON = json.loads(data)
            dados = conteudoJSON["text"]
            print(dados)
            self.salva_dados(dados)
            self.search(dados)
            self.salva_json()
            return True
        else:
            self.salva_json()
            return False

    # Essa função será invocada automaticamente toda vez que ocorrer um erro
    def on_error(self, status):
        print(status)

