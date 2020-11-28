class Car:

    isOn = False
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        if self.isOn is True:
            print("{} {} is already On".format(self.brand, self.model))
        else:
            self.isOn = True
            print("{} {} has started".format(self.brand, self.model))
    
    def stop(self):
        if self.isOn is False:
            print("{} {} is already stopped".format(self.brand, self.model))
        else:
            self.isOn = False
            print("{} {} has stopped".format(self.brand, self.model))

