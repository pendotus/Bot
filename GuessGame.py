from random import randrange, choice
import requests
class guessgame:
    SUITS = ["D", "C", "S", "H"]
    CARDS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K"]
    games = {}


    def __init__(self, chat_id):
        self.chat_id = chat_id

        if(chat_id not in self.__class__.games):
            self.__class__.games[chat_id] = {}
            self.__class__.games[chat_id]["first"] = {
                "val": randrange(1, 14),
                "suits": choice(self.__class__.SUITS)
            }
            self.__class__.games[chat_id]["second"] = {
                "val": randrange(1, 14),
                "suits": choice(self.__class__.SUITS)
            }


    @classmethod
    def getResults(cls, bet, chat_id):
        if cls.games[chat_id]["first"].get("val") < cls.games[chat_id]["second"].get("val"):
            if bet == "higher":
                return True
            else:
                return False
        else:
            if bet == "higher":
                return False
            else:
                return True

    @classmethod
    def getCard(cls, cardNumber, chat_id):
        gameObj = cls.games[chat_id]
        card = gameObj.get(cardNumber)
        return f'https://deckofcardsapi.com/static/img/{cls.CARDS[card["val"]-1]}{card["suits"]}.png'
    @classmethod
    def resetGame(cls, chat_id):
        cls.games.pop(chat_id, None)