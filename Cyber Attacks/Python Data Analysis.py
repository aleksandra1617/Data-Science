#############################################################################################################
# USEFUL LEARNING RESOURCES                                                                                 #
#                                                                                                           #
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
