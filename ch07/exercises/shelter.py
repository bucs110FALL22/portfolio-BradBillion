import time

univCount = 1


class Pet:

    def __init__(self, n, t):
        self.name = n
        self.type = t
        self.id = f"{univCount}{n}{t}"
        self.arrDate = time.strftime("%d/%m/%Y")
        self.adpDate = "n/a"

    univCount += 1

    def setAdopted(self):
        self.adpDate = time.strftime("%d/%m/%Y")


def main():
    fido = Pet("fido", "cat")
    print(fido.name, fido.type, fido.id, fido.arrDate)
    fido.setAdopted()
    print(fido.adpDate)


main()
