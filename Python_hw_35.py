class Transport:

    def __init__(self, campaign, country, path):
        self.campaign = campaign
        self.country = country
        self.path = path

    def transport_method(self):
        print("Transport name:             %s" % self.campaign)
        print("Driver's name:              %s" % (self.country))
        print('Path:                       %s' % (self.path))


class Train(Transport):

    def __init__(self, num_of_carriages):
        super().__init__(Transport, self.campaign, self.country, self.path)
        self.num_of_carriages = num_of_carriages

    def train_method(self):
        print('Name of transport:          Train')
        super().transport_method(Train)
        print('Namber of train carriages:  %s' % (self.num_of_carriages))


class Plane(Transport):

    def __init__(self, num_of_turbines):
        super().__init__(Transport, self.campaign, self.country, self.path)
        self.num_of_turbines = num_of_turbines

    def train_method(self):
        print('Name of transport:          Plane')
        super().transport_method(Plane)
        print('Number of plane turbines:   %s' % (self.num_of_turbines))

# (main.py)
#from Python_hw_35 import Transport
#from Python_hw_35 import Train
#from Python_hw_35 import Plane

#Transport.__init__(Transport, 'Alpha transport', 'Ukraine', 'Odessa-Kiev')
#Transport.transport_method(Transport)

#print('========')

#Train.__init__(Train, 20)
#Train.train_method(Train)

#print('========')

#Plane.__init__(Plane, 4)
#Plane.train_method(Plane)
