import hashlib
import random
import string


#TODO  DONE
class IdCounter:
    def __init__(self):
        self.counter = 0

    def get_id(self):
        counter = self.counter
        self.counter += 1
        return self.counter
    ...

#TODO  похоже работает, но над атрибутами подумать
class Password:

    def __init__(self):
        self._password_hash = None

    def get(self, password: str):
        if len(password) < 8:
            raise ValueError("Пароль должен быть не менее 8 символов")
        # TODO проверить на буквы/цифры

        self._password_hash = self.get_hash(password)
        return

    def check(self, password_to_verify: str):
        if self.get_hash(password_to_verify) == self._password_hash:
            return True

    @staticmethod
    def get_hash(password_str):
        return hashlib.sha256(password_str.encode()).hexdigest()

    ...

#TODO
class Product:
    product_counter = IdCounter()

    def __init__(self, name: str, price: float, rating: float):
        self.__id = self.product_counter.get_id()

        if not isinstance(name, str):
            raise TypeError("Product name should be str")
        self.__name = name

        # checking price
        if not isinstance(price, (int, float)):
            raise TypeError("Product price should be int or float")
        if not price > 0:
            raise ValueError("Product price should be > 0")
        self.price = price

        # checking rating
        if not isinstance(rating, (int, float)):
            raise TypeError("Product rating should be int or float")
        if rating < 0:
            raise ValueError("Product rating should not be < 0")
        self.rating = rating


        # реализуйте __str__ и __repr__ методы. В __str__ вывести строку вида {id}_{name}
    def __str__(self):
        return f"{self.__id}_{self.__name}"

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.__id}, name=\'{self.__name}\', price={self.price}, rating={self.rating})"

class Cart:
    def __init__(self):
        self.goods_list = []

    def add(self, product: Product):
        self.goods_list.append(product)

    def delete(self, product: Product):
        self.goods_list.remove(product)

    def __str__(self):
        return f"В корзине {self.goods_list}"


class User:
    user_counter = IdCounter()

    def __init__(self, user_name, password):
        self.id = self.user_counter.get_id()
        if not isinstance(user_name, str):
            raise TypeError("User name should be str")
        if not len(user_name) > 0:
            raise ValueError("User name should not be empty string")
        self._username = user_name
        self._cart = Cart()
        self._password = Password.get_hash(password)

    @property
    def cart(self):
        return self._cart

    @property
    def username(self):
        return self._username

    def cart_append(self, product: Product):
        self._cart.add(product)

    def __str__(self):
        return f"{self.__class__.__name__}({self._username}, password1)"

    def __repr__(self):
        return f"{self.__class__.__name__}(user_name={self._username}, password=password1)"

class Generator():
    user_list = ["Rajesh", "Priya", "Sangita", "Sanjeev", "Rajiv", "Vanya"]
    product_list = ["cucmber", "beetroot", "banana", "passion fruit", "melon", "grapes"]


    def gen_user(self):
        name = self.user_list[random.randint(0, len(self.user_list)-1)]
        letters = string.ascii_letters
        password = ''.join(random.choice(letters) for i in range(8))
        print(f"Generated password is {password}")
        user = User(name, password)
        return user

    def gen_product(self):
        name = self.product_list[random.randint(0, len(self.user_list)-1)]
        price = round(random.uniform(10.0, 1000.0), 2)
        rating = round(random.uniform(1, 5), 1)
        product = Product(name, price, rating)
        return product


class Store:

    def __init__(self):
        name = input("Pleas input your name: ")
        password = input("Please enter password: ")
        self.user = User(name, password)

    def add_to_cart(self):
        self.user._cart.add(Generator().gen_product())

    def veiw_cart(self):
        print(self.user.cart)


    ...

if __name__ == '__main__':
    prod = Product("dalkjhf", 12, 2)
    print(prod.__repr__())
    print(prod.__str__())

    user = User("galya", "valenok")
    print(user.__repr__())
    print(user.__str__())

    gen = Generator()
    print(gen.gen_user())
    print(gen.gen_product())
    print(gen.gen_user())
    print(gen.gen_user())
    print(gen.gen_product())
    print(gen.gen_product())
    print(gen.gen_product())

    store = Store()

    store.add_to_cart()
    store.add_to_cart()
    store.add_to_cart()
    store.add_to_cart()
    store.veiw_cart()