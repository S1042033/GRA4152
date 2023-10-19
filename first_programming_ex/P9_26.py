
## Defines a Customer class to handle a customer loyalty marketing campaign
#  A customer receiver a $10 discount on their next purchase when they have 
#  made accumulated purchases of at least $100.
#
class Customer:
    ## Constructs a costumer with accumulated purchases of zero and no earned discount
    #
    def __init__(self):
        self._accumPurchases = 0
        self._discountOnNextPurchase = False

    ## Makes a purchase
    #  @param amount the initial purchase amount
    #
    def makePurchase(self, amount):
        # If the customer has earned a discount he/she will use it on this purchase
        # and the accumulated purchases will only increase with the maximum of amount - 10 and 0
        if self._discountOnNextPurchase: 
            effPurchaseAmount = max(amount - 10, 0)
            self._discountOnNextPurchase = False
            print(f"You made a purchase of ${amount} but with a $10 discount you only paid ${effPurchaseAmount}!")
        # Otherwise, the self.accumPurchases will increase with the full amount
        else: 
            effPurchaseAmount = amount
            print(f"Thank you for making a purchase of ${amount}.")
        
        self._accumPurchases += effPurchaseAmount

        # If accumulated purchases is $100 or above, set _discountOnNextPurchase to true and reset accumulated purchases
        if self._accumPurchases >= 100:
            self._discountOnNextPurchase = True
            self._accumPurchases = 0
    
    ## Check if customer is eligible for a discount on the next purchase
    #  @return the boolean value of whether the customer will receive discount on the next purchase
    #
    def discountReached(self):
        return self._discountOnNextPurchase
        


## Test program, only executed if this file is executed directly
#
if __name__ == "__main__":
    testCustomer = Customer()
    print("A discount should not be used:")
    testCustomer.makePurchase(50)
    print("A discount should not be used:")
    testCustomer.makePurchase(60)
    print("A discount should be available on the next purchase:")
    print("Discount on next purchase: ", testCustomer.discountReached())
    print("Discount should be used:")
    testCustomer.makePurchase(50)
    print("A discount should not be used:")
    testCustomer.makePurchase(45)
    print("A discount should not be used:")
    testCustomer.makePurchase(30)
    print("A second discount should have been obtained:")
    print("Discount on next purchase: ", testCustomer.discountReached())
    