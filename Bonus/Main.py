"""
Author: AlieeLinux
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