# Header Section
# ---------------------------------------------------
# Name: Vijaya Sharma
# Date: 11/12/2024
# Purpose: Write a Python function that takes a customer's age and total purchase amount as input. Apply discounts based on the following conditions:
# If the customer is a senior citizen (age 60 or above), apply a 15% discount.
# If the purchase amount is above £100 and the customer is not a senior citizen, apply a 10% discount.
# If both conditions apply, only apply the higher discount.
# ---------------------------------------------------
#function to implement Calculate discount 
def calculate_discount(age, purchase_amount):
    # Initialize discount percentage
    discount = 0

    # if customer is a senior citizen
    if age >= 60:
        discount = 15
    # if purchase amount is above £100 for non-senior citizens
    elif purchase_amount > 100:
        discount = 10
    
    # Calculate the final amount after applying the discount
    final_amount = purchase_amount * (1 - discount / 100)
    
    return final_amount, discount


age = int(input("Enter the customer's age: "))
purchase_amount = float(input("Enter the total purchase amount: £"))
final_price, applied_discount = calculate_discount(age, purchase_amount)

print(f"Applied discount: {applied_discount}%")
print(f"Final price after discount: £{final_price:.2f}")
