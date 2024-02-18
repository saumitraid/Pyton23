class Encap:
    def __init__(self, name, email, mobile):
        self.name=name
        self._email=email
        self.__mobile=mobile

obj=Encap('Rohit','rohit@gmail.com', '9876543211')
print(obj.name)
print(obj._email)
print(obj.__mobile)