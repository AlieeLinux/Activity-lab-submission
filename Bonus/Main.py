"""The Shipping Cost Calculator with Rules
Write a program that calculates shipping costs based on the following complex rules:

- The base shipping cost is $10.
- If the order total weight is over 20 pounds, add $5.
- If the shipping destination is "international", double the total cost.
- However, if the customer is a "premium" member, they get a 20% discount on the final cost and are exempt from the international surcharge.

Instructions:

1. Create variables for weight, destination ("domestic" or "international"), and membership ("standard" or "premium").
2. Use arithmetic operators to calculate the costs.
3. Use logical operators (and, or, not) to check the conditions for the premium member exemption and other rules.
4. Print a detailed breakdown of the final shipping cost.

Example Output:

Weight (lbs): 25
Destination (domestic/international): international
Final Shipping Cost: $12.00
(Details: Base $10 + Overweight $5, Premium 20% discount applied, International fee waived.)
"""

Destination="international"
membership="premium"
base_shipping=10
weight=29
FinalPrice=base_shipping
IsOverweight=False
discount="20% Premium Discount: "


if weight > 20:
    FinalPrice+=5
    IsOverweight = True

if not membership=="premium" and Destination == "international":
    FinalPrice*=2

if not membership=="premium":
    discount=discount+"No"
elif membership=="premium":
    FinalPrice*= 0.8
    discount=discount+"Yes"

print("Weight (lbs):", weight)
print("Destination (domestic/international):", Destination)
print(f"Final Shipping Cost: ${FinalPrice}")


if not IsOverweight and (not membership=="premium" and Destination == "international"):
    print(f"\nDetails: Base: {base_shipping}, {discount}, International fee applied")

elif IsOverweight and (not membership=="premium" and Destination == "international"):
    print(f"\nDetails: Base: {base_shipping} + overweight 5$, {discount}, International fee applied")

elif IsOverweight and (membership=="premium" or Destination == "international"):
    print(f"\nDetails: Base: {base_shipping} + overweight 5$, {discount}, International fee waived")

elif not IsOverweight and (membership=="premium" or Destination == "international"):
    print(f"\nDetails: Base: {base_shipping}, {discount}, International fee waived")