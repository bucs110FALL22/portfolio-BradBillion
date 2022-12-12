import requests

bannedWords = "the of to and a in is it you that he was for on are with as I his they be at one have this from or had by not word but what some we can out other were all there when up use your how said an each she which do their time if will way about many then them write would like so these her long make thing see him two has look more day could go come did number sound no most my over know than who may down side been now"
# words to ban from the emoji search bc they are meaningless
# top 100 most used english words bc im lazy


class EmojiAPI:

    def __init__(self):
        self.url = "https://emojihub.yurace.pro/api/all"

    def get(self, word):  #finds an emoji that contains a given keyword
        if word not in bannedWords:  #makes sure its not in the banned words
            r = requests.get(self.url)
            response = r.json()  #list of EVERY SINGLE EMOJI in the API
            desiredEmoji = None
            for i in response:  # for every emoji in the list
                if word in i['name']:  # if the keyword is in it
                    name = i['name']
                    if len(name) != len(word):
                        if f" {word}" in name or f"{word} " in name:
                            # and its not a case like "apple" being in "pineapple"
                            desiredEmoji = i
                            break
                    else:
                        desiredEmoji = i
                        break
            return desiredEmoji
        else:
            return None
