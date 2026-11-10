import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

print("---excersise 1---")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}. ")

print("---excersise 2---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("---excersise 3---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

print("---excersise 4---")
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

print("---excersise 5---")

rows_read = 0
high_value = []

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "price", "quantity", "total"])
    writer.writerows(high_value)

    

print("---excersise 6---")

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price} = ${total:.2f}")

print(f"Total revenue: ${dict_total:.2f}")

print("---excersise 7---")
summary = {}

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print("---excersise 8---")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")   

entries = 0 
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())

print(f"Log entries so far: {entries}")

# Reflection 1: this compares to doing the same task in excel because it can quickly and easily process large amounts of data, automate calculations, and generate reports without manual intervention. It also allows for more complex data manipulation and analysis that may not be as straightforward in Excel. Although, in Excel it is easier to visualize data and get a more intuitive undedrstanding of the data through charts and graphs.
# Reflection 2: A real business process that would benifit from an append mode log file is a entry system for a university. this tool would allow for students to enter  buildings during the day and the log file would keep track of all entries and exits. This would allow for better security and monitoring of who is in the building at any given time.