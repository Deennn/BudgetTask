class Budget:
    """
    A simple attempt on creating a budget app with some few attributes like food, clothing
    and entertainment. We set their default value to zero so that we change or make an
    increment with time.
    """

    def __init__(self, name):
        self.name = name
        self.food = 0
        self.clothing = 0
        self.entertainment = 0

    def deposit_fund(self):
        """
        A deposit function that can deposit into any of the attributes possible
        :return:A well formatted statement of how much was deposited and where to
        """
        print("Welcome " + str(self.name.title()))
        deposit = int(input('Where would you like to deposit to?\nEnter(1): for Food\nEnter(2): for Clothing\nEnter('
                            '3): for Entertainment\n'))
        if deposit == 1:
            deposit_amount = int(input("How much would you like to deposit:\n"))
            self.food += deposit_amount
            print("You've successfully deposit {} to your food budget.".format(self.food))
        elif deposit == 2:
            deposit_amount = int(input("How much would you like to deposit:\n"))
            self.clothing += deposit_amount
            print("You've successfully deposit {} to your clothing budget.".format(self.clothing))
        elif deposit == 3:
            deposit_amount = int(input("How much would you like to deposit:\n"))
            self.entertainment += deposit_amount
            print("You've successfully deposit {0} to your entertainment budget.".format(self.entertainment))
        else:
            print("Invalid option,try again")

    def withdraw_fund(self):
        """
        A withdrawal function that withdraw money from any of the attributes
        :return: Return a well structured statement of how much you withdraw and from where. #note you can't
        withdraw what you don't have.
        """
        print("Welcome " + str(self.name.title()))
        withdrawal = int(input("Where would you like to withdraw from?\nEnter(1): for Food\nEnter(2): for "
                               "Clothing\nEnter(3): for Entertainment\n"))
        if withdrawal == 1:
            withdrawal_amount = int(input("How much would you like to withdraw?\n"))
            if withdrawal_amount > self.food:
                print("Insufficient fund,your food budget is {}".format(self.food))
            else:
                self.food -= withdrawal_amount
                print("You've successfully withdraw {} from your food budget".format(withdrawal_amount))
        elif withdrawal == 2:
            withdrawal_amount = int(input("How much would you like to withdraw?\n"))
            if withdrawal_amount > self.clothing:
                print("Insufficient fund,your food budget is {}".format(self.clothing))
            else:
                self.clothing -= withdrawal_amount
                print("You've successfully withdraw {} from your clothing budget".format(withdrawal_amount))
        elif withdrawal == 3:
            withdrawal_amount = int(input("How much would you like to withdraw?\n"))
            if withdrawal_amount > self.entertainment:
                print("Insufficient fund,your food budget is {}".format(self.entertainment))
            else:
                self.entertainment -= withdrawal_amount
                print("You've successfully withdraw {} from your entertainment budget".format(withdrawal_amount))
        else:
            print("Invalid option,try again")

    def transfer_fund(self):
        """
        A transfer function that help transfer fund from any of the attributes into any of the attributes
        :return: Return a well statement of the amount you transfer and from where.
        """
        print("Welcome " + str(self.name.title()))
        transfer = int(input("Where would you like to transfer fund from?\nEnter(1): for Food\nEnter(2): for "
                             "Clothing\nEnter(3): for Entertainment\n"))
        if transfer == 1:
            transfer_destination = int(input("Where would you like to transfer fund to?\nEnter(1): for "
                                             "Clothing\nEnter(2): for Entertainment\n"))
            if transfer_destination == 1:
                transfer_amount = int(input("How much would you like to transfer:\n"))
                if transfer_amount > self.food:
                    print("Insufficient fund,your food budget is {}".format(self.food))
                else:
                    self.food -= transfer_amount
                    self.clothing += transfer_amount
                    print("You've successfully transfer {} to your clothing budget from food budget.".format(
                        self.clothing))
            elif transfer_destination == 2:
                transfer_amount = int(input("How much would you like to transfer:\n"))
                if transfer_amount > self.food:
                    print("Insufficient fund,your food budget is {}".format(self.food))
                else:
                    self.food -= transfer_amount
                    self.entertainment += transfer_amount
                    print("You've successfully transfer {} to your entertainment budget from food budget.".format(
                        self.entertainment))
            else:
                print("invalid option")
        elif transfer == 2:
            transfer_destination = int(input("Where would you like to transfer fund to?\nEnter(1): for "
                                             "food\nEnter(2): for Entertainment\n"))
            if transfer_destination == 1:
                transfer_amount = int(input("How much would you like to transfer:\n"))
                if transfer_amount > self.clothing:
                    print("Insufficient fund,your clothing budget is {}".format(self.clothing))
                else:
                    self.clothing -= transfer_amount
                    self.food += transfer_amount
                    print("You've successfully transfer {} to your food budget from clothing budget.".format(self.food))
            elif transfer_destination == 2:
                transfer_amount = int(input("How much would you like to transfer:\n"))
                if transfer_amount > self.clothing:
                    print("Insufficient fund,your clothing budget is {}".format(self.clothing))
                else:
                    self.clothing -= transfer_amount
                    self.entertainment += transfer_amount
                    print("You've successfully transfer {} to your entertainment budget from clothing budget.".format(
                        self.entertainment))
            else:
                print("invalid option")
        elif transfer == 3:
            transfer_destination = int(input("Where would you like to transfer fund to?\nEnter(1): for "
                                             "food\nEnter(1): for clothing\n"))
            if transfer_destination == 1:
                transfer_amount = int(input("How much would you like to transfer:\n"))
                if transfer_amount > self.entertainment:
                    print("Insufficient fund,your entertainment budget is {}".format(self.entertainment))
                else:
                    self.entertainment -= transfer_amount
                    self.food += transfer_amount
                    print("You've successfully transfer {} to your food budget from entertainment budget.".format(
                        self.food))
            elif transfer_destination == 2:
                transfer_amount = int(input("How much would you like to transfer:\n"))
                if transfer_amount > self.entertainment:
                    print("Insufficient fund,your clothing budget is {}".format(self.entertainment))
                else:
                    self.entertainment -= transfer_amount
                    self.clothing += transfer_amount
                    print("You've successfully transfer {} to your entertainment budget from entertainment budget.".format(
                        self.entertainment))
            else:
                print("invalid option")
        else:
            print("Invalid option,Try again")

    def category_balances(self):
        """
        A function that calculate the balance of each attribute
        :return:Balance of each attribute
        """
        print("Welcome " + str(self.name.title()))
        check_category_balance = int(input(
            'Which balance would you like to check?\nEnter(1): for Food\nEnter(2): for '
            'Clothing\nEnter(3): for Entertainment\n'))
        if check_category_balance == 1:
            print("Your food balance is {}".format(self.food))
        elif check_category_balance == 2:
            print("Your clothing balance is {}".format(self.clothing))
        elif check_category_balance == 3:
            print("Your entertainment balance is {}".format(self.entertainment))
        else:
            print("Invalid option")


x = Budget('ade')
x.food = 0
x.deposit_fund()
x.category_balances()
x.transfer_fund()
x.transfer_fund()
x.withdraw_fund()
x.withdraw_fund()
x.category_balances()
x.category_balances()
x.transfer_fund()
