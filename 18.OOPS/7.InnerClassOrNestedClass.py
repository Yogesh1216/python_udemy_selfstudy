# inner class or nested class

class Customer:
    def __init__(self,Id,name,billingHno,billingStreet,billingCity,billingCountry,billingPin,shippingHno,shippingStreet,shippingCity,shippingCountry,shippingPin):
        self.customerId = Id
        self.name=name
        self.billingAddress = self.Address(billingHno,billingStreet,billingCity,billingCountry,billingPin)
        self.shippingAddress = self.Address(shippingHno,shippingStreet,shippingCity,shippingCountry,shippingPin)

    class Address:
        def __init__(self, Hno, street, city, country, pin):
            self.Hno = Hno
            self.street = street
            self.city = city
            self.country = country
            self.pin = pin

        def display(self):
            print(self.Hno)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)

obj1 = Customer(1,'yogesh',101,'rajiv chowk','gurgaon','India','122018',101,'rajiv chowk','gurgaon','India','122018')
print(obj1.shippingAddress.display())

# if a class is becoming lengthy and some contents are repetating inside , you can use inner class.


