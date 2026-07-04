import pandas as pd

df = pd.read_csv("Retail-Store-Sales-Analysis\\Local_Retail_Store_Dataset_550_Rows.csv")
# print(df.head())

lowest_footfall_day = df['Transaction_ID'].groupby(df['Day']).count().idxmin()
highest_footfall_day = df['Transaction_ID'].groupby(df['Day']).count().idxmax()

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
def print_suggestions():
    print("Suggestions:")
    for i in suggestions:
        print(f"- {i}")

while True:
    print("\n------ Choices ------")
    print("1. Day and Time wise suggestions")
    print("2. All suggestions")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 3:
        print("Exiting the program.")
        break
    
    match choice:
        case 1:
            suggestions.clear()  # Clear previous suggestions
            user_input = input("Enter the day of the week to get suggestions (e.g., Monday, Tuesday, etc.): ").strip().capitalize()
            user_time = input("Enter the time of the day (e.g., Morning, Afternoon, Evening): ").strip().capitalize()

            if user_input in df['Day'].values:
                if user_input == lowest_footfall_day: #monday
                    suggestions.append(f"Consider closing the store on {lowest_footfall_day} to save costs and also to give employees a break because the store operations are lower than the revenue it brings.")
                
                elif user_input == highest_footfall_day: #sunday
                    suggestions.append(f"Consider increasing the discount on {highest_footfall_day} to attract more customers and increase sales.")
                    suggestions.append(f"Consider filling the inventory with more products on {highest_footfall_day} to meet the demand and increase sales.")
                    # suggestions.append(f"")
           
                else: #tuesday to friday + saturday
                    if user_time == peak_hours:
                        suggestions.append(f"Consider having Limited Time offers during peak hours ({peak_hours}) to attract more customers and increase sales.")
                    else:
                        suggestions.append(f"Consider adding Happy hours or special promotions like Buy 1 Get 1 Free, Combo Deals, Family Packs discounts during non peak hours ({user_time}) to attract more customers and increase sales.")
                        suggestions.append(f"Consider starting Home Delivery services during non peak hours ({user_time}) to attract more customers, Have free delivery for orders over 300/- to increase sales.")
            print_suggestions()

        case 2:
            suggestions.clear()  # Clear previous suggestions
            suggestions.append(f"1. Consider closing the store on {lowest_footfall_day} to save costs and also to give employees a break because the store operations are lower than the revenue it brings.")
            suggestions.append(f"2. Consider increasing the discount on {highest_footfall_day} to attract more customers and increase sales.")
            suggestions.append(f"3. Consider having Limited Time offers during peak hours ({peak_hours}) to attract more customers and increase sales.")
            suggestions.append("4. Consider adding Happy hours or special promotions like Buy 1 Get 1 Free, Combo Deals, Family Packs discounts during non peak hours (Morning, Evening) to attract more customers and increase sales.")
            suggestions.append(f"5. Consider filling the inventory with more products on {highest_footfall_day} to meet the demand and increase sales.")
            suggestions.append("6. Consider starting Home Delivery services during non peak hours (Morning, Evening) to attract more customers, Have free delivery for orders over 300/- to increase sales.")
            print_suggestions()
            
            
        case _:
            print("Enter a valid choice (1-3).")
