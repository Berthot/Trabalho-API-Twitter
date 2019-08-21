from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


class AssinanteTwitter(StreamListener):
    #Essa função será invocada automaticamente toda vez que um twitter for identificado
    def on_data(self, data):
        conteudoJSON = json.loads(data)
        print(conteudoJSON["text"])
        return True

    # Essa função será invocada automaticamente toda vez que ocorrer um erro
    def on_error(self, status):
        print(status)

# Para executar esse exemplo é preciso possuir uma conta no twitter, caso não possua crie uma.
# Entre no site http://apps.twitter.com e crie uma nova applicação preenchendo as informações
# Será gerado o consumer key e o consumer secret, que são a identificação de sua aplicação no twitter.
print("Inicio do programa")
consumer_key=""
consumer_secret=""

#Você será redirecionado para outra página, clique na aba 'Keys and Access Tokens'
#Crie um token de acesso novo, ele será utilizado no lugar de suas credenciais
access_token=""
access_token_secret=""

assinante = AssinanteTwitter()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, assinante)
stream.filter(track=['league of legends', 'dota', 'minecraft', 'pubg'], languages=["pt"])

#Se o programa apresentar o erro 401, significa que as credenciais são inválidas
#Verifique se não há espaçamentos nas credenciais
#Se o programa apresentar o erro 420, significa que estrapolou o limite de requisições gratuitas
#Se o programa estiver apresentando erros de caracteres, apague todos comentários



