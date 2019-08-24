from Twitter import AssinanteTwitter
from tweepy import OAuthHandler
from tweepy import Stream


"""
Análogo ao método main do java, só tem como propósito chamar as funções com os parametros
"""

if __name__ == '__main__':
    print("Inicio do programa")

    consumer_key = "NLaisEh7x2RXCLsMd1H5c7EQe"
    consumer_secret = "Zej68qEjbbNsgkN5w8VY1LlZRhHnGbBcWFUIXDeV6x5yfLeuJf"

    access_token = "1163572452615708674-27nY8JFuviOPTkLLuXHXNUp1wDeUBz"
    access_token_secret = "bnQ97UZdy7B6IhOtvPvtXu6swonCTFw6MIMsaOb9CZvsV"

    assinante = AssinanteTwitter(tempo=40)  # Definir tempo aqui
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, assinante)
    stream.filter(track=['league of legends', 'dota', 'minecraft', 'csgo', 'free fire', 'free fire', 'pubg'],
                  languages=["pt"])
