import pandas as pd

df = pd.read_csv("Retail-Store-Sales-Analysis\\Local_Retail_Store_Dataset_550_Rows.csv")

suggestions = []


# ---------- BASIC ANALYSIS ----------

def footfall_analysis():

    transactions = df.groupby('Day')['Transaction_ID'].count()

    lowest_day = transactions.idxmin()
    highest_day = transactions.idxmax()

    print("\n------ FOOTFALL ANALYSIS ------")
    print("Lowest Footfall Day:", lowest_day)
    print("Highest Footfall Day:", highest_day)

    print("\nTransactions Per Day:")
    print(transactions)

    return lowest_day, highest_day



def revenue_analysis():

    revenue = df.groupby('Day')['Bill_Amount'].sum()

    lowest_revenue = revenue.idxmin()
    highest_revenue = revenue.idxmax()

    print("\n------ REVENUE ANALYSIS ------")
    print("Lowest Revenue Day:", lowest_revenue)
    print("Highest Revenue Day:", highest_revenue)

    return lowest_revenue, highest_revenue



def time_analysis():

    hours = pd.to_datetime(df['Time'], format='%H:%M').dt.hour

    df['Time_Block'] = pd.cut(
        hours,
        bins=[8,14,17,21],
        labels=[
            "Morning (8 AM - 2 PM)",
            "Afternoon (2 PM - 5 PM)",
            "Evening (5 PM - 9 PM)"
        ]
    )

    time_count = df.groupby(
        'Time_Block',
        observed=True
    )['Transaction_ID'].count()

    peak_time = time_count.idxmax()
    lowest_time = time_count.idxmin()


    print("\n------ TIME ANALYSIS ------")
    print(time_count)

    print("Peak Time:", peak_time)
    print("Lowest Traffic Time:", lowest_time)

    return peak_time, lowest_time



def product_analysis():

    products = df.groupby('Product')['Quantity'].sum()

    best_product = products.idxmax()
    low_product = products.idxmin()


    print("\n------ PRODUCT ANALYSIS ------")

    print("Best Selling Product:", best_product)
    print("Lowest Selling Product:", low_product)


    return best_product, low_product



# ---------- SUGGESTION SYSTEM ----------

def generate_suggestions(
        lowest_day,
        highest_day,
        peak_time,
        low_time,
        best_product,
        low_product):


    


    # Monday issue

    if lowest_day == "Monday":

        suggestions.append(
            "Monday has the lowest sales. "
            "Store can remain closed on Monday "
            "to reduce operating cost and provide employee weekly off."
        )


    # Sunday

    if highest_day == "Sunday":

        suggestions.append(
            "Sunday has maximum customers. "
            "Introduce loyalty points and combo offers "
            "to improve customer retention."
        )



    # Timing issue

    if peak_time == "Afternoon (2 PM - 5 PM)":

        suggestions.append(
            "Most customers visit between 2 PM and 5 PM. "
            "Keep enough stock available during this time."
        )


    suggestions.append(
        f"Low traffic detected during {low_time}. "
        "Start home delivery service and provide free delivery "
        "on orders above ₹300."
    )



    # Product suggestion

    suggestions.append(
        f"{best_product} sells the most. "
        "Keep this product properly stocked."
    )


    suggestions.append(
        f"{low_product} has low demand. "
        "Create combo offers with popular products."
    )



    print("\n========== STORE IMPROVEMENT SUGGESTIONS ==========")

    for i in suggestions:
        print("-", i)


# ----------- OWNER DETAILS & GOALS -----------

def owner_details():
    emp_count= int(input("Enter the number of employees in the store: "))
    home_delivery = input("Does the store provide home delivery? (yes/no): ").strip().lower()
    target_revenue = float(input("Enter the target revenue for the store: "))

    return emp_count, home_delivery, target_revenue

def emp_suggestions(employees, lowest_day):
    if employees <= 2 and lowest_day.lower() == "monday":
        suggestions.append("Consider closing the store on Monday to save costs and also to give employees a break because the store operations are lower than the revenue it brings.")
    
    else:
        suggestions.append("Consider employee shift management to optimize operations and reduce costs on low footfall days.")

    return suggestions

def delivery_suggestions(home_delivery, lowest_hours):
    if home_delivery == "no":
        suggestions.append("Consider starting home delivery service during low footfall hours to increase sales and customer convenience.")
    
    else:
        suggestions.append("Maintain current home delivery services and optimize delivery times based on customer demand.")

    return suggestions

#calculate current revenue
current_revenue = df['Bill_Amount'].sum()

def revenue_suggestions(target_revenue, current_revenue):

    if target_revenue > current_revenue:
        difference = target_revenue - current_revenue
        suggestions.append(f"Target revenue is ₹{difference:.2f} more than current revenue. Implement strategies to bridge this gap.")

    else:
        suggestions.append("Current revenue meets or exceeds the target. Continue current strategies and explore new growth opportunities.")

    return suggestions






# ---------- MAIN PROGRAM ----------


lowest_day, highest_day = footfall_analysis()

lowest_revenue, highest_revenue = revenue_analysis()

peak_time, low_time = time_analysis()

best_product, low_product = product_analysis()


employees, delivery, target = owner_details()


current_revenue = df['Bill_Amount'].sum()


emp_suggestions(
employees,
lowest_day
)


delivery_suggestions(
delivery,
low_time
)


revenue_suggestions(
target,
current_revenue
)


generate_suggestions(
lowest_day,
highest_day,
peak_time,
low_time,
best_product,
low_product
)