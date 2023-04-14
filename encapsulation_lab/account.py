class Account:
    def __init__(self, account_id: int, balance: float or int, pin: int):
        self.__id = account_id
        self.__pin = pin
        self.balance = balance

    def get_id(self, pin: int):
        if self.__pin == pin:
            return self.__id

        return "Wrong pin"

    def change_pin(self, old_pin: int, new_pin: int):
        if self.__pin == old_pin:
            self.__pin = new_pin

            return "Pin changed"

        return "Wrong pin"
