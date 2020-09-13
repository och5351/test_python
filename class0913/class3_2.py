from class0913 import class3

class MoreFourCal(class3.FourCal):
    def add(self):
        result = (self.first * 2) + (self.second * 2)
        return result

    def pow(self):
        result = self.first ** self.second
        return result

def p():
    print('나는 작동할까요?')

x = '나는 작동할까요?2'