class car:
    wheel = 4
    def __init__(self):
        self.mil = 10
        self.company = "BMW"
        self.speed = "100km/hr"


c1 = car()
c2 = car()
c1.wheel = 5
car.wheel = 6
c1.mil = 20

print(c1.mil)
print(c1.company)
print(c1.speed)
print(c1.wheel)
print(c2.wheel)