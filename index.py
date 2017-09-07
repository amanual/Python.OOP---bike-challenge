class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
        self.logged = True

    def displayinfo(self):            
        print "\nPrice: {} \nMax Speed: {} \nMiles: {}".format(self.price, self.max_speed, self.miles)
        # return self
    def ride(self):
        print "Riding..."
        self.miles += 10        
        return self    

    def reverse(self):
        print "Reversing..."        
        #prevent negative miles  
        if self.miles >= 5:
            self.miles -= 5  
            return self

#instance of the class
bike1 = Bike("$200", "250 mph", 30)
bike2 = Bike("$300", "300 mph", 40)
bike3 = Bike("$100", "250 mph", 100)

bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()

#To prevent from instance having negative value, we can reate an if-statement that will help it stop from going below 0
#To ride,reverse and displayinfo can have rerurn self, but for displayinfo is not necessery
