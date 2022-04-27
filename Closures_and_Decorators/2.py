def boldDecorator(fn):
    def wrapperFunction():
        return "<b>" + fn() + "</b>"
    return wrapperFunction

def italicDecorator(fn):
    def wrapperFunction():
        return "<i>" + fn() + "</i>"
    return wrapperFunction

def underlineDecorator(fn):
    def wrapperFunction():
        return "<u>" + fn() + "</u>"
    return wrapperFunction


#single decorator
@boldDecorator
def hi():
    return("Hi")
print(hi())

#chain of decorators
@boldDecorator
@italicDecorator
@underlineDecorator
def hello():
    return("Hello World")
print(hello())

