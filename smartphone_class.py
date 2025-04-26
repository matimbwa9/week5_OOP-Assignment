# Smartphone class definition
class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    def display_info(self):
        return f"{self.brand} {self.model} - {self.storage}GB - Color: {self.color}"

    def call(self, number):
        return f"Calling {number}... 📞"

    def send_message(self, number, message):
        return f"Sending message to {number}: {message} 📱"

# Creating objects of the Smartphone class
phone1 = Smartphone("Apple", "iPhone 13", 128, "Blue")
phone2 = Smartphone("Samsung", "Galaxy S21", 256, "Black")

# Displaying information about the phones
print(phone1.display_info())
print(phone2.display_info())

# Calling and sending a message using the phones
print(phone1.call("123-456-7890"))
print(phone2.send_message("987-654-3210", "Hello there!"))
