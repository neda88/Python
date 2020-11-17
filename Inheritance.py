class Property():
    def __init__(self ,Sq='' , beds='', baths='' ):
        self.square_feet=Sq
        self.beds=beds
        self.baths=baths


    def display(self):
        print("Property details:")
        print("=====================")
        print("square footage: {}".format(self.square_feet))
        print("No. of bedrooms:{}".format(self.beds))
        print("No. of bathrooms:",self.baths)


class Apartment(Property):
    def __init__(self,Sq,beds,baths, balacony ,laundary ):
        super().__init__(Sq,beds,baths)
        self.balacony=balacony
        self.laundary=laundary

    def display(self):
        super().display()
        print("Apartment details:")
        print("=====================")
        print("Balacony: ",self.balacony )
        print("laundary type:", self.laundary)
        

class House(Property):
    def __init__(self, Sq, beds,baths, garage, fence):
        super(). __init__(Sq, beds, baths)
        self.garage=garage
        self.fence=fence

    def display(self):
        super().display()
        print("House details:")
        print("=====================")
        print("garage: ",self.garage )
        print("fence: ", self.fence)

    def updateGarage(self, garagetype):
        self.garage=garagetype

            
            








    
if __name__ == '__main__':
    prop1=Property(1000, 2, 2.5)
    prop1.display()
    print()
    apt1=Apartment (2000, 3, 3.5, "yes", "coin")
    apt1.display()
    print()
    house1=House(3000, 4, 4.5, "no", "electric_fence")
    house1.display()
    print()
    house1.updateGarage("two Door")
    house1.display()
    print()
