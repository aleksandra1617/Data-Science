import pandas as pd

# Bounce Rate - % of people who visit the website and leave immediately.
web_stats = {"Day": [1, 2, 3, 4, 5, 6], "Visitors": [43, 53, 34, 45, 64, 34], "Bounce_Rate": [65, 72, 62, 64, 54, 66],
             "Daily_Revenue": ["£3", "£0", "£7", "£6", "£4", "£1"]}

web_data_frame = pd.DataFrame(web_stats)

# Set Index (how all the data is related) returns a new data frame.
# web_data_frame = web_data_frame.set_index("Day")
web_data_frame.set_index("Day", inplace=True)  # inplace is a cleaner way of writing the above.

# Get First 5 Entries
print(web_data_frame.head())

# Get Last 2 Entries
print(web_data_frame.tail(2))

# Get Specific Column
column = web_data_frame["Visitors"]

# Get Multiple columns
print(web_data_frame[["Bounce_Rate", "Daily_Revenue"]])
