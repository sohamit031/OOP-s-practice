class dog:
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
    def introduce(self):
        print(f"Hi, I am {self.name} and I have a  {self.colour} tail.")

dog1 = dog('dean','brown')

print(dog1.name)

dog1.introduce()
    