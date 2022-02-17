
#import abc modules
from abc import ABC, abstractmethod


#create parent class with abstract method
class Gift(ABC):
    def giftCard(self, amount):
        print("Your gift card total is: ", amount)
    @abstractmethod
    def total(self, amount):
        pass

#create children class to inherit from parent class
class GiftCardMin(Gift):
    def total(self,amount):
        print("You need a min of $50 to purchase a gift card. Your {} total does not qualify!".format(amount))

#call and print function

gift = GiftCardMin()
gift.giftCard("$25")
gift.total("$25")
