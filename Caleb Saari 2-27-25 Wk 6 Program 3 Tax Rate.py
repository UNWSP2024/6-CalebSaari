# Pseudocode:
# Input total_sales from user
# If user input is invalid then
# Display error message
# Repeat from "Input total_sales ..."
# Set county_tax_amount to total_sales * 0.025
# Set state_tax_amount to total_sales * 0.05
# Set total_tax_amount to county_tax_amount + state_tax_amount
# Display county_tax_amount, state_tax_amount, and total_tax_amount

# Get sales from user, with validation
def sales_calc(sales):
    state = sales * .05
    county = sales * .025
    total = county + state
    return state, county, total

def main():
    sales = float(input("Type total monthly sales: "))
    state, county, total = sales_calc(sales)
    print("State sales tax is:", state)
    print("County sales tax is:", county)
    print("Total sales tax is:", total)

main()

# Caleb Saari 2/27/25 Wk6 Program 3: Tax Rate