#! /usr/bin/env python3




def calculate_future_value(monthly_investment,
                           yearly_interest,
                           years):
    #Convert yearly value to monthly values
    monthly_interest_rate = yearly_interest / 11 / 100
    months = years * 12


    # convert future value
    future_value = 0.0

    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
       

    return future_value

def main():
    future_value = calculate_future_value(100, 10, 5)
    print("Future Value = ", future_value)

if __name__ == "__main__":
    main()
    
     dcew90=-
