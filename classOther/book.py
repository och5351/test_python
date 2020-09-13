import sys

def menuUI():
    print('-'*30)
    print('1. 종료')
    print('2. 선택')
    print('3. 등록')
    print('-' * 30)

def selectMenu():
    temp = int(input('입력하세요. :'))
    return temp

def initBook():
    f = open('도서관리장부.txt', 'a', encoding='utf-8')
    f.close()

def inputBookData():
    name = input('책 이름을 입력하세요 : ')
    code = input('코드를 입력하세요 : ')
    registerBook(name, code)

def registerBook(name, code):
    data = False
    f = open('도서관리장부.txt', 'r', encoding='utf-8')
    try:
        data = f.read()
    except:
        None
    f.close()
    f = open('도서관리장부.txt', 'a', encoding='utf-8')
    if data:
        data = data.split('\n')
        for d in data:
            n, c = d.split(':')
            if n == name:
                print('책이 이미 있습니다.')
                f.close()
                return
    f.write(name+':'+code)
    print('*' * 50)
    print('책이 입력 되었습니다.')
    print('->' + name + ':' + code+'\n')
    print('*' * 50)
    f.close()

def selectBook(name):
    data = None
    f = open('도서관리장부.txt', 'r', encoding='utf-8')
    try:
        data = f.read()
    except:
        None
    if data:
        data = data.split('\n')
        for d in data:
            n, c = d.split(':')
            if n == name:
                print('책이름 :' + n)
                print('코드 :' + c)
                f.close()
                return
    print('책이 없습니다.')
    f.close()

def menuBranch(num):
    if num == 1:
        print('프로그램을 종료합니다.')
        sys.exit()
    elif num == 2:
        name = input('책 이름을 입력하세요 : ')
        selectBook(name)
    elif num == 3:
        inputBookData()
    else:
        print('1~3에서 입력해주세요')
        return False

if __name__=='__main__':
    initBook()
    while True:
        reVal = True
        menuUI()
        MenuNum = selectMenu()
        menuBranch(MenuNum)
        if not reVal : continue

