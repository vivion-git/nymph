from person import person
class manager(person):
    def giveraise(self,percent,bonus=0.1):
        self.pay*=(1.0+percent+bonus)
if __name__=='__main__':
    tom =manager(name='tom doe',age=50,pay=50000)
    print tom.lastname()
    tom.giveraise(.20)
    print tom.pay

