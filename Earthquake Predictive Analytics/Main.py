# NEXT STEPS
# TODO: Create an infographic and host it on a web page.
# TODO: Gather live data from news articles (Can try using NLTK & urllib).
# TODO: Use Natural Language Processing to automate some of the data cleaning/integration.

#############################################################################################################
# USEFUL LEARNING RESOURCES                                                                                 #
#                                                                                                           #
# DATA SETS: https://www.hackmageddon.com/2017-master-table/                                                #
# PANDAS DOC: https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html                       #
#                                                                                                           #
# Run a Cleanup Program Once before starting the Analysis:                                                  #
#       - Put all the data together(in one file/database).                                                  #
#       - Remove unneeded data, example data for a sales company from over 10 years ago;                    #
#       - Eliminate repetition of data;                                                                     #
#       - Extract the data in a set format. To do that generic column tags can be created for the user.     #
#       Example: the column breach_start can be tagged with date-time tag. The script can then be           #
#       trained to check then be trained to check if there are any of these symbols '.', '/', '\'           #
#       and split the data on those symbols as long as it is day, month, year it will format correctly.     #
#       More importantly it should have a way to figure out the order of the date, i.e. if the data is      #
#       year, month, day instead of the set format of the database which can be for example day, month,     #
#       year. If all the data used for the analysis is in the same format it can be set to match that       #
#       format.                                                                                             #
#                                                                                                           #
#############################################################################################################

"""
CASE: Analyse the data for most common breaches - most common types of organisations targeted;
      Most common zones attacked; Most common location breached; Most common cause for a breach;
      How long it took the attacker to obtain the sensitive information;
"""

import csv
import os
from pymongo import MongoClient

# region DEFINE SCHEMA
db_name = "CyberBreaches"
collections_schema = {
    "Cases": ["CaseID", "TargetID", "DurationID", "BreachMethodID", "SeverityID", "TargetedData", "BreachSource", "ExploitedVulnerability"],
    "Duration": ["DurationID", "StartDate", "EndDate", "StartTime", "EndTime"],
    "Target": ["TargetID", "TargetName", "Industry", "Location"],
    "BreachSeverity": ["SeverityID", "MonetaryDMGs", "RecordsBreached"],
    "BreachMethods": ["BreachMethodID", "Description", "CommunicationChannels", "Type", "Vulnerabilities"]}
# endregion

# region LOAD DATA
# This structure is a list containing a dictionary with details about a data set for each new data set loaded.
# The reason why the top-level container is a list is because I want to handle the data in order of loading,
# and the dictionary does not contain ordered data.
data_details = []


# Returns None if the data set fails to load.
# @param ds_name - the file name of the given data set.
# @param num_attrib - the number of attributes or columns of the data set that is being loaded.
# @param num_entries - the number of entries in the data set (not counting the first row as it contains column names).
def load_data_set(file_ext, ds_name, num_attrib, num_entries):
    # On load gather data information to help with integration
    new_ds_details = {"Name": ds_name, "NumAttrib": num_attrib, "NumEntries": num_entries}
    data_details.append(new_ds_details)

    file_path = os.getcwd() + "\Data Sets\."    # The . is at the end of the string so that it does noy create a break.
    file_path = file_path[:len(file_path)-1] + ds_name + "." + file_ext

    # If the file fails to load display the current working directory.
    try:
        file_object = open(file_path, "r")
        reader = csv.reader(file_object, delimiter=",")
    except FileNotFoundError:
        print("\n"+117*"-"+"\n"
              "\tNO SUCH FILE OR DIRECTORY: Current Working Directory  - ", os.getcwd(), " \n"
              "\tPlease make sure your data set is stored within the 'Data Sets' directory"
              " in your current working directory!"
              "\n"+117*"-"+"\n")
        return None

    ds_list = list(reader)
    return ds_list


"""
TESTS

test_data_set = load_data_set("txt", "test", 11, 951)
print("Data after loading: ", test_data_set)
"""

data_set1 = load_data_set("csv", "Breach Cases 2017", 11, 951)
print("Data after loading: ", data_set1)
# endregion


# TODO: SHOW I CAN IMPORT FROM AN EXCEL FILE WITH MULTIPLE SPREADSHEETS
# region CLEAN DATA - Make it conform relatively to the set schema.
# print("Clean Data: ", ds1_list)


# Formats the loaded data before storing it into MongoDB.
# @params data_set: a 2D list containing a loaded data set.
def format_data_set(data_set, ds_details):

    # Get all column names and replace them with the appropriate ones.
    column_names = data_set[0]

    print("EDIT: ", column_names[0], " Replaced with ", collections_schema["Cases"][0])
    column_names[0] = collections_schema["Cases"][0]

    # Remove the white spaces (if any) at the end of each column
    data_set = data_set[:ds_details["NumEntries"]+1]    # +1 is there to take into account the column names
    print(len(data_set))

    for count in range(len(data_set)):

            # Remove the white spaces (if any) at the end of each row
            data_set[count] = data_set[count][:ds_details["NumAttrib"]]
            print("Current row: ", data_set[count])


# TODO: Create a main function
# TODO: For each data set run this code
if data_set1 is not None:
    format_data_set(data_set1, data_details[0])

# endregion

# region MONGODB
# CONNECT TO MONGODB
client = MongoClient("mongodb://localhost:27017/")
# endregion
# region VISUALISATION
# TODO: Visualise by Month, by Year, cases in last 2, 3, 4, 5 years
# TODO: Create a pie chart on motivations behind attacks.
# TODO: Create a pie chart of distribution of targets

# endregion
