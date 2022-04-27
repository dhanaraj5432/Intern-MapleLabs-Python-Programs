def phoneDecorator(fn):
    def wrapperFunction(phoneList):
        fn(['+91 ' + num[-10:-5] + ' ' + num[-5:] for num in phoneList])
    return wrapperFunction

@phoneDecorator
def phoneDisplay(phoneList):
    print(*sorted(phoneList), sep='\n')

n = 3
phoneList = ["07895462130", "919875641230", "9195969878"]
phoneDisplay(phoneList) 