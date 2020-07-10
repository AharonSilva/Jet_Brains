class CoffeeMachine:

    exit = False
    water_qty = 400
    milk_qty = 540
    beans_qty = 120
    cups_qty = 9
    money = 550

    def coffee_method(self, entry):
        msg = '''\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n> '''

        if entry == 'buy':
            action = input(msg)

            if action == '1':
                if self.water_qty < 250:
                    print('Sorry, not enough water!', '\n')

                elif self.beans_qty < 16:
                    print('Sorry, not enough beans!', '\n')

                elif self.cups_qty < 1:
                    print('Sorry, not enough cups!', '\n')

                else:
                    print('I have enough resources, making you a coffee!', '\n')
                    self.water_qty -= 250
                    self.beans_qty -= 16
                    self.cups_qty -= 1
                    self.money += 4

            elif action == '2':
                if self.water_qty < 350:
                    print('Sorry, not enough water!', '\n')

                elif self.milk_qty < 75:
                    print('Sorry, not enough milk!', '\n')

                elif self.beans_qty < 20:
                    print('Sorry, not enough beans!', '\n')

                elif self.cups_qty < 1:
                    print('Sorry, not enough cups!', '\n')

                else:
                    print('I have enough resources, making you a coffee!', '\n')
                    self.water_qty -= 350
                    self.milk_qty -= 75
                    self.beans_qty -= 20
                    self.cups_qty -= 1
                    self.money += 7

            elif action == '3':
                if self.water_qty < 200:
                    print('Sorry, not enough water!', '\n')

                elif self.milk_qty < 100:
                    print('Sorry, not enough milk!', '\n')

                elif self.beans_qty < 12:
                    print('Sorry, not enough beans!', '\n')

                elif self.cups_qty < 1:
                    print('Sorry, not enough cups!', '\n')

                else:
                    print('I have enough resources, making you a coffee!', '\n')
                    self.water_qty -= 200
                    self.milk_qty -= 100
                    self.beans_qty -= 12
                    self.cups_qty -= 1
                    self.money += 6

            elif action == 'back':
                print('')
                pass

        elif entry == 'fill':
            self.water_qty += int(input('''\nWrite how many ml of water do you want to add: \n> '''))
            self.milk_qty += int(input('''Write how many ml of milk do you want to add: \n> '''))
            self.beans_qty += int(input('''Write how many grams of coffee beans do you want to add: \n> '''))
            self.cups_qty += int(input('''Write how many disposable cups of coffee do you want to add: \n> '''))
            print('')
            pass

        elif entry == 'take':
            print('I gave you {}$'.format(self.money))
            self.money -= self.money
            print('')
            pass

        elif entry == 'remaining':
            print('\nThe coffee machine has: \n',
                  self.water_qty, 'of water\n',
                  self.milk_qty, 'of milk \n',
                  self.beans_qty, 'of coffee beans \n',
                  self.cups_qty, 'of disposable cups \n',
                  '$' + str(self.money), 'of money \n')
            pass

        elif entry == 'exit':
            self.exit = True
            return self.exit


CoffeeMaker = CoffeeMachine()
while not CoffeeMaker.exit:
    CoffeeMaker.coffee_method(input('''Write action (buy, fill, take, remaining, exit):\n> '''))
