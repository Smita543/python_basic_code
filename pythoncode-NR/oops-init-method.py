class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("the config of computer is ",self.cpu,self.ram)


comp1 = computer("500 ssd" ,"16gb")
comp1.config()
 # ============ ============================   ================================= #
class computer:
    def __init__(self):
        self.cpu = "500ssd"
        self.ram = "16gb"


comp1 = computer()
print(comp1.cpu)
