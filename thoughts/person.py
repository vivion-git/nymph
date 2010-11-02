class person:
    def __init__(self,name,age,pay=0,job=None):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job
    def lastname(self):
        return self.name.split()[-1]
    def giveraise(self,percent):
        self.pay*=(1.0+percent)
if __name__ == '__main__':
    bob=person('bob smith',42,30000,'sweng')
    sue=person('sue jones',45,40000,'music')
    print bob.name,sue.pay
    print bob.lastname()
    sue.giveraise(.10)
    print sue.pay

