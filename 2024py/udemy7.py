class User:
    def __init__ (self,user_id,user_name):
        self.id = user_id
        self.name = user_name

user1 = User("121","ali")
print(user1.name)


list = [330,300,270,240,210,180,150,120,90,60]
for i in list:
    print(i)