class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can Work")
class Female(Human):
    def sleep(sleep):
        print(sleep)
    def work(self):
        super().work()
        print("I can code")
Female_1=Female()
Female_1.sleep()
Female_1.work()                       