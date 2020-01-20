import os
#import matplotlib

os.getcwd()
print(os.getcwd())

# Load data
file_object = open(os.getcwd() + "\Data\groceries.csv", "r")
dataset = [line.strip().split(',') for line in file_object.readlines()]

data_sample = dataset[:10]
print("Loaded Data Sample: ", data_sample)

# This is a dictionary which will contain a dictionary for each data item with the item name as the key
# and tags for the item details of interest.
item_analysis_data = {}

# The index in this list is equivalent to the row number in the dataset.
num_items_per_purchase = []


def main():

    # Main loop
    for purchase in dataset:
        print("\n\nPurchase Recite: ", purchase)
        for item in purchase:

            # Update the item_analysis_data dictionary to store all unique items
            if item not in item_analysis_data.keys():
                print("\tNew item found: ", item)
                print("\t\tAppending << ", item, " >> item to dictionary. ")
                print("\t\tList of items in dictionary: ", list(item_analysis_data.keys()))

                item_details = {item: {"Frequency": 1}}
                item_analysis_data.update(item_details)

            else:
                print("No new items found! \n\n Increasing Frequency: ")
                item_analysis_data[item]["Frequency"] += 1


    print("\n\n Dictionary after analysis: ", item_analysis_data)


main()
