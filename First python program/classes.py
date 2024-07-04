#  we have two types of programming
# i) Functional/Procedural Programming
# ii) Object Oriented Programming (OOP)

# class Human:
#     def __init__(self,human_name,human_age,human_address): # constructor
#         self.name=human_name
#         self.age=human_age
#         self.address=human_address
    
#     def greet(self):
#         print('Hello! My Name is',self.name,'I am ',self.age,'years old.','I live in ',self.address)

#     def getName(self):
#         return self.name
    
#     def getAge(self):
#         return self.age
    
#     def getAddress(self):
#         return self.address

# noor = Human('Noor',28,'Peshawar') # instanciation



class Vehical:
    def __init__(self,vehical_make,vehical_model,vehical_year):
        self.__make=vehical_make
        self.__model=vehical_model
        self.__year=vehical_year
        

    def getMake(self):
        return self.__make
    
    def getModel(self):
        return self.__model
    
    def getYear(self):
        return self.__year

    def setMake(self,make):
        self.__make=make

    def setModel(self,model):
        self.__model=model

    def setModel(self,year):
        self.__year=year

class Bike(Vehical):
    def __init__(self,make, model, year,bike_color,is_self_start):
        super().__init__(make,model,year)
        self.__color=bike_color
        self.__is_self_start=is_self_start

    def getcolor(self):
        return self.__color
    
    def setcolor(self,color):
        self.__color=color

    def getIsSelfStart(self):
        return self.__is_self_start
    
    def setIsSelfStart(self,is_self_start):
        self.__is_self_start=is_self_start

class Car(Vehical):
    def __init__(self, make, model, year, num_of_doors,is_automatic):
        super().__init__(make, model, year)
        self.__doors=num_of_doors
        self.__is_automatic=is_automatic

    def getNumOfDoors(self):
        return self.__doors
    
    def getIsAutomatic(self):
        return self.__is_automatic
    
    def setNumOfDoors(self,doors):
        self.__doors=doors

    def setIsAutomatic(self,is_automatic):
        self.__is_automatic=is_automatic


# class Car(Vehical):
#     def __init__(self, make, model, year, num_of_doors,is_automatic):
#         super().__init__(make, model, year)
#         self.__doors=num_of_doors
#         self.__is_automatic=is_automatic

#     def getNumOfDoors(self):
#         return self.__doors
    
#     def getIsAutomatic(self):
#         return self.__is_automatic
    
#     def setNumOfDoors(self,doors):
#         self.__doors=doors

#     def setIsAutomatic(self,is_automatic):
#         self.__is_automatic=is_automatic

        

# class Car(Vehical):
#     def __init__(self, make, model, year, num_of_doors,is_automatic):
#         super().__init__(make, model, year)
#         self.__doors=num_of_doors
#         self.__is_automatic=is_automatic

#     def getNumOfDoors(self):
#         return self.__doors
    
#     def getIsAutomatic(self):
#         return self.__is_automatic
    
#     def setNumOfDoors(self,doors):
#         self.__doors=doors

#     def setIsAutomatic(self,is_automatic):
#         self.__is_automatic=is_automatic


civic = Car('Honda','civic',2020,4,True)

honda70= Bike('Honda','70CD',2010,'red',False)
print(honda70.getMake())
print(honda70.getcolor())


# class House:
#     def __init__(self,house_area,house_location,house_price):
#        self.area=house_area
#        self.location=house_location
#        self.price=house_price

#     def getArea(self):
#        return self.area

#     def getLocation(self):
#        return self.location

#     def getprice(self):
#        return self.price
    
#     def setArea(self,area):
#         self.area=area

#     def setLocation(self,location):
#         self.location=location

#     def setprice(self,price):
#         self.price=price
      

# home1 = House("20 Marla","Islamabad",66000000)
# home2 = House("38 Marla","Peshawar",400000)
# home3 = House("20 Marla","Lahore",5500000)

# print(home1.getArea())
# print(home2.getLocation())
# print(home3.getprice())




