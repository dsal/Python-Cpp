class Device:
    count = 0
    def __init__(self, IP, Mac, Name, status=False):
        self.IP = IP
        self.Mac_address = Mac
        self.Name = Name
        Device.count += 1

        if status:
            self.status = 'Active'
        else:
            self.status = 'Unknown'
    
    def get_status(self):
        return f"{self.Name} ({self.IP}) is {self.status}"

class TV(Device):
    def turn_on(self):
        self.status = "Active"
        return f"{self.Name} turned ON"
    
    def turn_off(self):
        self.status = "Inactive"
        return f"{self.Name} turned OFF"

class Thermo(Device):
    def __init__(self, IP, Mac, Name, degree=20, status=False):
        super().__init__(IP, Mac, Name, status)
        self.degree = degree

    def get_degree(self):
        return f"{self.Name} reports {self.degree} °C"

class SmartTV(TV):
    def turn_on(self):
        self.status = "Active"
        return f"{self.Name} SmartTV booted with Internet features enabled."



# TESTING
tv1 = SmartTV("192.168.0.10", "AA:BB:CC:11:22", "Living Room TV", status=True)
thermo1 = Thermo("192.168.0.20", "AA:BB:CC:33:44", "Hall Thermostat", degree=22)

print(tv1.get_status())
print(tv1.turn_off())
print(thermo1.get_status())
print(thermo1.get_degree())
print("Total Devices:", Device.count)



"""
This code defines a simple object-oriented model of IoT devices,
using Python classes to represent different types of devices in a networked environment.

The base class, Device, serves as a general blueprint for all devices,
encapsulating shared attributes such as IP, Mac_address, Name, and status.
It also keeps track of the total number of devices created through the class attribute count.

The method get_status() provides a standardized way to report the current operational state of any device,
reflecting whether it is active or unknown. This encapsulation ensures that each object maintains its own state
while exposing only the necessary interface for interaction.

The subclasses demonstrate inheritance, specialization, and polymorphism.
TV inherits from Device and adds specific behaviors, such as turn_on() and turn_off(),
which modify the device’s status and provide human-readable feedback.

Thermo extends Device by adding a temperature-specific attribute degree and a method get_degree() to retrieve this value,
illustrating how subclasses can extend the functionality of the parent class while reusing its initialization logic via super().__init__().

SmartTV further overrides the turn_on() method from TV, showing polymorphism: the same method name behaves differently depending on the class.
The testing section demonstrates the creation and interaction of these objects, printing their statuses, controlling their power state, and accessing temperature readings,
while the Device.count variable confirms the total number of instantiated devices.
This structure mirrors real-world IoT networks, where multiple device types share common characteristics, but also exhibit specialized behaviors.
"""