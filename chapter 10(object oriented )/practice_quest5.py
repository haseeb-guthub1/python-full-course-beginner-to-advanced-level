"""class train which has a method book a ticket, get status no of seats
 and get fare information of running under indian railway"""
import random
class train :
    def __init__(self, trainno):
        self.trainno = trainno
        pass
    def book(self, fro, to):
        print(f"ticket is booked from in train no : {self.trainno} from {fro} too {to}")
        
    

    def getstatus(self ):
        print(f" status of train no is : {self.trainno}")

    def getfare(self,  fro, to):
        print(f"ticket fair  in train no : {self.trainno} from {fro} too {to} is {random.randint(222,5555)}")

t  = train(1234)
t.book("Rawalpindi", "Skardu")
t.getstatus()
t.getfare("Rawalpindi", "Skardu")
