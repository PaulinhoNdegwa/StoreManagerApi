
products = []
sales = []
users = []

class Product():
    """This class initialized a sales object. 
    Also it has a save method that saves the sale in a list"""

    def __init__(self, product_name, product_price, quantity, min_quantity):
        """Method to initialize Product objects"""
        self.quantity = quantity
        self.min_quantity = min_quantity
        self.product_name = product_name
        self.product_price = product_price

    def save_product(self):
        """Method to create and save a product dict object"""
        if len(products) == 0:
            product_id= 1
        else:
            product_id = products[-1]["product_id"] + 1
        product = {
            "product_id": product_id,
            "product_name": self.product_name,
            "product_price": self.product_price,
            "quantity": self.quantity,
            "min_quantity": self.min_quantity
        }
        products.append(product)
        return product




class Sale():
    """This class initialized a sales object. 
    Also it has a save method that saves the sale in a list"""

    def __init__(self, product_name, product_price, quantity, total_price, attendant):
        """Method to initialize sales"""
        self.product_name = product_name
        self.product_price = product_price
        self.quantity = quantity
        self.total_price = total_price
        self.attendant =  attendant

    def save_sale(self):
        if len(sales) == 0:
            sale_id = 1
        else:
            sale_id = sales[-1]["sale_id"] + 1
        sale = {
            "sale_id": sale_id,
            "product_name": self.product_name,
            "product_price": self.product_price,
            "quantity": self.quantity,
            "total_price": self.total_price,
            "attendant": self.attendant
        }
        sales.append(sale)
        return sale



class User():
    """This class initialized a user object. 
    Also it has a save method that saves the user in a list"""

    def __init__(self, f_name, s_name, email, password, role="attendant"):
        self.f_name = f_name
        self.s_name = s_name
        self.email = email
        self.password = password
        self.role = role

    def save_user(self):
        if len(users) == 0:
            user_id = 1
        else:
            user_id = users[-1]["user_id"] + 1
        user = {
            "user_id": user_id,
            "f_name": self.f_name,
            "s_name": self.s_name,
            "email": self.email,
            "password": self.password,
            "role":self.role
        }
        users.append(user)
        return user    
