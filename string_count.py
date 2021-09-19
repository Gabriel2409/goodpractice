#%%
import pandas as pd
import numpy as np
from collections import Counter

def count_a_in_string(mystring):
    return Counter(mystring)["a"]

def convert_df_to_unique_string(df):
    return df.astype(str).sum().sum()


# good practice in your scrip files. Define a main function and use if __name__ == "__main__"
def main():
    mystr = "Good practices for a python repo."
    nb_a = count_a_in_string(mystr)
    print(f"There are {nb_a} 'a' in the string '{mystr}'")

    my_df = pd.DataFrame({"col1":['The lazy', 'airplane'], 'col2':["is in the airport", "of San Francisco"]})
    print("My dataframe")
    print(my_df)
    combined_str = convert_df_to_unique_string(my_df)
    print("Combining into a string =>", combined_str)
    print("Total nb of a in df:", count_a_in_string(combined_str))


if __name__== '__main__'  :
    main()






