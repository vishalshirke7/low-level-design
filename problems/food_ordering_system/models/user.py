class User(object): 

    def __init__(self, name, gender, mobile, pincode):
        self.name = name
        self.gender = gender
        self.mobile = mobile
        self.pincode = pincode
        self.orders = list()


    def __str__(self):
        return f'{self.name}'