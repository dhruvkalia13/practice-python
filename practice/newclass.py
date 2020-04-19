class MyNewClass:
    """
    every method sbould have self as first arg
    """
    def __init__(self):
        self.a = 5
        self.b = 6

    def __str__(self):
        return "something"

    def mMethod(self):
        print("I am method")

    def createNewObject(self):
        pass

# object create
newClassObject = None
print(newClassObject)
print(newClassObject.a)
print(newClassObject.b)
print(newClassObject.mMethod())



