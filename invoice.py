#! usr/bin/env python3
from datetime import datetime, timedelta


# Retrieve the invoice date
def get_invoice_date():
    invoice_date_str = input("Enter the invoice date (MM/DD/YY): ")
    invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%y")
    return invoice_date
def main():
    print("The Invoice Due Date program")
    print()

    while True:
        date_format = "%B %d, %Y"
        invoice_date = get_invoice_date()

        # calculate due date and days over due
        due_date = invoice_date + timedelta(days=30)
        current_date = datetime.now()
        days_overdue = (current_date - due_date).days

        # display results
        print("Invoice Date: " + invoice_date.strftime(date_format))
        print("Due Date: " + due_date.strftime(date_format))
        print("Current Dat: " + current_date.strftime(date_format))
        print()

        if days_overdue > 0:
            print("This invoice is", days_overdue, "day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print("This invoice is due in", days_due, "day(s).")
        print()

        # asj if user wants to continue
        result = input("Continue (y/n): ")
        if result.lower() != "y":
            print("Exit")
            break
if __name__ == "__main__":
    main()
