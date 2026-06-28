import random

class train:
    


    def __init__(self,trainNo):
        self.trainNo = trainNo


    def book(self,fro,to):
        print(f"Train is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self,fro ,to):
        print(f"Train no: {self.trainNo} is running on time")


t = train("312121M")

t.book("pune" , "delhi")

t.getstatus("pune" , "delhi")

t.getFare("pune" , "delhi")
