


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs): #unlimited number of transactions
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass = SingletonMeta):
    def some_business_logic(self):
        """
        Any singleton should define some bussiness logic.
        """
        #...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance. ")
    else:
        print("Singleton failed, variables contain different instance. ")

