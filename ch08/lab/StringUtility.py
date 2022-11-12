class StringUtility():

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def vowels(self):
        count = 0
        for c in self.string:
            vowels = ["a", "e", "i", "o", "u"]
            if c in vowels:
                count += 1
        if count < 5:
            return f"{count}"
        else:
            return "many"

    def bothEnds(self):
        length = len(self.string)
        if length > 2:
            return f"{self.string[0]}{self.string[1]}{self.string[length-2]}{self.string[length-1]}"
        else:
            return ""

    def fixStart(self):
        if len(self.string) > 1:
            firstChar = self.string[0]
            newString = ""
            check = False
            for c in self.string:
                if c != firstChar:
                    newString += c
                else:
                    if check == True:
                        newString += "*"
                    else:
                        newString += c
                        check = True
            return newString
        else:
            return self.string

    def asciiSum(self):
        value = 0
        for c in self.string:
            value += ord(c)
        return value

    def cipher(self):
        alpha = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ]
        aLPHA = []
        for a in alpha:
            aLPHA.append(a.upper())
        length = len(self.string)
        newString = ""
        for c in self.string:
            check = False
            if c == " ":
                newString += " "
                continue
            for d in alpha:
                if c == d:
                    check = True
                    num = alpha.index(d)
                    newNum = num + length
                    while newNum > 25:
                        newNum -= 26
                    newString += alpha[newNum]
            if check == False:
                for d in aLPHA:
                    if c == d:
                        check = True
                        num = aLPHA.index(d)
                        newNum = num + length
                        while newNum > 25:
                            newNum -= 26
                        newString += aLPHA[newNum]
        return newString


# def cipher(self):
# return an encoded string by incrementing all letters by the length of the string. You should leave any characters that are not letters unchanged.
# For example, the string "Dog" would be shifted by 3, resulting in "Grj", while "Horse" would become "Mtwxj" because it shifts by 5 characters.
# You must account for wrap around (z=>a). Uppercase always wraps around to upper case, and lowercase always wraps around to lower case.
