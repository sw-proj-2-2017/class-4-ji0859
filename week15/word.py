import random

class Word:

    def __init__(self, filename):

        self.words = []
        self.maxlength = 0
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1
            if self.count !=0:
                if len(line) > self.maxlength:
                    self.maxlength = len(line)
                else:
                    self.maxlength = len(line)

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self, minlength):

        r = random.randrange(self.count)
        answer = self.words[r]
        if minlength > self.maxlength:
            minlength = self.maxlength
        while len(answer) <= minlength:
            answer = self.words[random.randrange(self.count)]
        return answer
