import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

df = pd.read_csv("retail\\Local_Retail_Store_Dataset_550_Rows.csv")
# print(df.head())

lowest_footfall_day = df['Transaction_ID'].groupby(df['Day']).count().idxmin()
highest_footfall_day = df['Transaction_ID'].groupby(df['Day']).count().idxmax()

weekday = df[~df['Day'].isin(['Saturday', 'Sunday'])]
# weekend = ['Saturday', 'Sunday']

time_block = pd.to_datetime(df['Time'], format='%H:%M').dt.hour
df['time_block'] = pd.cut(time_block, bins=[9, 13, 17, 20], labels=['Morning', 'Afternoon', 'Evening'])
peak_hours = df.groupby('time_block')['Transaction_ID'].count().idxmax()
lowest_hours = df.groupby('time_block')['Transaction_ID'].count().idxmin()

print("Lowest footfall on: ", lowest_footfall_day)
print("Highest footfall on: ", highest_footfall_day)
print("Average footfall on weekdays: ", df['Transaction_ID'].groupby(df['Day']).count().mean().round(2))
print("Count of transactions per day: \n", df['Transaction_ID'].groupby(df['Day']).count().sort_values())
print("Peak hours of footfall: ", peak_hours)
print("Lowest hours of footfall: ", lowest_hours)

suggestions = []

user_input = input("Enter the day of the week to get suggestions (e.g., Monday, Tuesday, etc.) or leave blank for weekend suggestions: ").strip().lower().capitalize()
user_time = input("Enter the time of the day (e.g., Morning, Afternoon, Evening): ").strip().lower().capitalize()
# user_time = input("Time: ")
# user_time = pd.to_datetime(user_time, format='%H:%M').hour
# if user_time >13 and user_time < 17:
#     pass

if user_input in weekday['Day'].values:
    if user_input == lowest_footfall_day:
        suggestions.append(f"Consider closing the store on {lowest_footfall_day} to save costs and also to give employees a break because the store operations are lower than the revenue it brings.")
    else:
        if user_time == peak_hours:
            suggestions.append(f"Consider increasing the discount during peak hours ({peak_hours}) to attract more customers and increase sales.")
        else:
            suggestions.append(f"Consider adding Happy hours or special promotions during non peak hours ({user_time}) to attract more customers and increase sales.")
else:
    if highest_footfall_day: #sunday
        suggestions.append(f"Consider increasing the discount on {highest_footfall_day} to attract more customers and increase sales.")
    else:
        pass #saturday


print("Suggestions:")
for i in suggestions:
    print(f"- {i}")

    # price = float(input("Enter price per unit: "))
    # qty = int(input("Enter quantity: "))
    # total_revenue = price * qty
    # discount = total_revenue * 0.10
    # print("Total revenue: ", total_revenue)
    # print("Discount: ", discount)
    # print("Final amount after discount: ", total_revenue - discount)