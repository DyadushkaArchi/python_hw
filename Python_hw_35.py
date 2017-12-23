class Transport:

    def __init__(self, transport, driver, path):
        self.transport_name = transport
        self.driver_name = driver
        self.path = path

    def transport_method(self):
        print("Transport name:           %s" % self.transport_name)
        print("Driver's name:            %s" % (self.driver_name))
        print('Path:                     %s' % (self.path))


class Train(Transport):

    def __init__(self, num_of_carriages):
        super().__init__()
        self.num_of_carriages = num_of_carriages

    def train_method(self):
        super().transport_method()
        print('Number of train carriages:%s' % (self.num_of_carriages))


class Plane(Transport):

    def __init__(self, num_of_turbines):
        super().__init__()
        self.num_of_turbines = num_of_turbines

    def train_method(self):
        super().transport_method()
        print('Number of turbines:      %s' % (self.num_of_turbines))
