import factAPI
import emojiAPI


def newFact():  #fetches a random fact
    fApi = factAPI.FactAPI()
    fact = fApi.get()
    if fact != None:
        return fact
    else:
        newFact()


def getEmoji(keyword):  #finds an emoji given a keyword
    eApi = emojiAPI.EmojiAPI()
    emojis = eApi.get(keyword)
    if emojis != None:
        return emojis
    else:
        return None
