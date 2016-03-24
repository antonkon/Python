import json

class Letter:
    sign = ""
    number = 0

    def __init__(self,s,n):
        self.sign = s
        self.number = n

    def __str__(self):
        return "{0} - {1}".format(self.number,self.sign)

    def set_sign(self):
        pass

    def set_number(self):
        pass

    def get_sign(self):
        return  self.sign

    def get_number(self):
        return self.number

class Phrase:
    letters = []
    text = ""

    def __init__(self,l):
        self.letters = sorted(l,key=lambda letter: letter.number)

    def __str__(self):
        return self.text

    def set_leters(self):
        pass

    def get_leters(self):
        pass

    def make(self):
        for let in self.letters:
            self.text += let.get_sign()
        return self.text

if __name__ == '__main__':

    with open('task_data.json') as file1:
        data = json.load(file1)
    print(data)

    letter1 = []

    for item in data:
        letter1.append(Letter(item["sign"],item["number"]))

    phras = Phrase(letter1)
    phras.make()
    print(phras)