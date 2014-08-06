class PersonInfo:
    __filename = "01_e.txt"

    def __init__(self, name, age, redditUser):
        self.name = name
        self.age = age
        self.redditUser = redditUser

        self.__saveAndReturn()

    def __saveAndReturn(self):
        self.__saveInfo()
        self.__printInfo()

    def __saveInfo(self):
        f = open(self.__filename, 'w')
        f.write("your name is %s, you are %i years old, and your username is %s" % (self.name, int(self.age), self.redditUser))
        f.close()

    def __printInfo(self):
        f = open(self.__filename, 'r')
        print(f.read())
        f.close()

name = input("please enter your name: ")
age = input("please enter your age: ")
redditUser = input("please enter you Reddit user name: ")
PersonInfo(name, age, redditUser)
