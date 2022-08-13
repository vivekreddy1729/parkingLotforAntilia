class ParkingLotForAntilia:

    slotNumbers = []
    number_of_slots = 0


    #
    def slotsInitialised(self):
        return(self.number_of_slots != 0)

    # A function to initialise the Parking Lot size in Antilia
    def setSlotNumber(self, number):
        self.number_of_slots = number
        if(len(self.slotNumbers) == 0):
            for i in range(0, number):
                self.slotNumbers.append(0)
            print("Created a parking of "+ str(number) +" slots")
        else:
            print("Sorry!! This Antilia is already in progress, to start from scratch reinitiate the program")





    # A fuction to park a car in parking lot        
    def parkCar(self, carDetails):
        counter = 0
        for slot in range(0, self.number_of_slots):
            if(self.slotNumbers[slot]==0):
                self.slotNumbers[slot] = carDetails
                print("Car with vehicle registration number \"" + carDetails[0] +"\" has been parked at slot number "+str(slot+1))
                break
            counter += 1
        if(counter>=self.number_of_slots):
            print("Parking lot is full")





    #A function to get all the slot numbers of Specific Driver Age        
    def getSlotNumberOfDriverAge(self, age):
        ageArray = []
        for slot in range(0, self.number_of_slots):
            if(self.slotNumbers[slot]!=0):
                if(self.slotNumbers[slot][1]==age):
                    ageArray.append(str(slot+1))
        if(len(ageArray)==0):
            print("There are no drivers with age " + str(age))
        else:
            print(", ".join(ageArray))






    #A function to get Parking Lot number of Specific Car Number
    def getSlotNumberOfCar(self, carNumber):
        for slot in range(0, self.number_of_slots):
            if(self.slotNumbers[slot] != 0):
                if(self.slotNumbers[slot][0] == carNumber):
                    print(slot+1)
                    break
        else:
            print("There is no car parked with that Car Number")


    #A function to vacate the Parking Lot        
    def vacateSlot(self, slot):
        if(slot>0 and slot<=len(self.slotNumbers)):
            if(self.slotNumbers[slot-1] != 0):
                carNumber = self.slotNumbers[slot-1][0]
                driverAge = self.slotNumbers[slot-1][1]
                self.slotNumbers[slot-1] = 0
                print("Slot number " + str(slot) + " vacated, the car with vehicle registration number \""+carNumber+"\" left the space, the driver of the car was of age "+str(driverAge))
            else:
                print("Slot is already Vacant")
        else:
            print("There is no such slot number in the parking lot")





    # A function to get Car Numbers with specific Driver Age
    def getCarNumbersWithDriverAge(self, age):
        carArray = []
        for slot in range(0, self.number_of_slots):
            if(self.slotNumbers[slot]!=0):
                if(self.slotNumbers[slot][1]==age):
                    carArray.append(self.slotNumbers[slot][0])
        if(len(carArray)==0):
            print("There are no cars with Driver Age " + str(age))
        else:
            print(", ".join(carArray))



    def isDriverAgeValid(self, age):
        return(age<18)
        
        


print("####### All Commands #########")
print("All the Commands and data are Case Sensitive")
print("Create_parking_lot  to create Parking Lots")
print("Park XX-00-YY-0000 driver_age Z  to park car with car number XX-00-YY-0000 of Driver age Z")
print("Slot_numbers_for_driver_of_age  to get all the slot numbers of certain driver age")
print("Slot_number_for_car_with_number  to get slot number with specific car number")
print("Leave  is to leave the parking lot")
print("Vehicle_registration_number_for_driver_of_age  is to get the vehicle registration numbers of certain driver age")
print("####### You can now start using the Parking Lot Application#######")


antilia = ParkingLotForAntilia()
while(True):
    command = list(input("$$$").split())
    if(command[0] != "Create_parking_lot"):
        print("First you need to initialise the slots in Parking Lot so, try using correct Command")
    elif(int(command[1]) <= 0):
        print("Number of Slots in Parking Lot should be more than 0")
    else:
        antilia.setSlotNumber(int(command[1]))
        break

    
while(True):
    x = list(input("$$$").split())
    if(x[0] == "Park"):
        if(len(x) != 4):
            print("Expecting 4 inputs")
        elif(antilia.isDriverAgeValid(int(x[3]))):
            print("Driver Age should be more than 18... You are doing a Crime Buddy")
        else:
            details = []
            details.append(x[1])
            details.append(int(x[3]))
            antilia.parkCar(details)
            
    elif(x[0] == "Slot_numbers_for_driver_of_age"):
        if(len(x) != 2):
            print("Expecting 2 inputs")
        elif(antilia.isDriverAgeValid(int(x[1]))):
            print("We allow drivers with age more than 18 So, we dont have drivers with that age")
        else:
            antilia.getSlotNumberOfDriverAge(int(x[1]))
            
    elif(x[0] == "Slot_number_for_car_with_number"):
        if(len(x) != 2):
            print("Expecting 2 inputs")
        else:
            antilia.getSlotNumberOfCar(x[1])
            
    elif(x[0] == "Leave"):
        if(len(x) != 2):
            print("Expecting 2 inputs")
        else:
            antilia.vacateSlot(int(x[1]))
            
    elif(x[0] == "Vehicle_registration_number_for_driver_of_age"):
        if(len(x) != 2):
            print("Expecting 2 inputs")
        else:
            antilia.getCarNumbersWithDriverAge(int(x[1]))
    else:
        print("We dont have such commands, we ae still working on to improve it")
    
