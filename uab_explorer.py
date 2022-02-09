
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot

class UabExplorer():
    def __init__(self, filename):
        self.df = pd.read_excel(filename)
        self.df_cleaned = None

        self.needed_columns = ["Name", "Email Address", "Open-Ended Response"]

    def get_raw_df(self):
        return self.df

    def get_cleaned_df(self):
        return self.df_cleaned

    def get_list_of_columns(self):
        return list(self.df.columns)

    def clean_data(self):
        # Drop unwanted columns
        print("Selecting needed columns: " + ', '.join(needed_columns))
        new_df = self.df[self.needed_columns]

        print("Dropping blank rows")
        new_df = new_df.dropna()

        print("Filtering invalid email rows")
        new_df = delete_junky_responses(new_df)

        # Assign cleaned df to class variable
        self.df_cleaned = new_df

    # Delete rows that don't contain email adresses
    def delete_junky_responses(self, df):
        new_df = df[~df["Email Address"].str.contains("@")]                                          ### don't have @ symbol in it
        print(new_df.head(5))
        return new_df

    def write_cleaned_df_to_xls(self, output_file_name):
        if not self.df_cleaned:
            print("self.df_cleaned has not been assigned. You need to run `clean_data()`")
            return

        print("File is being created: " + output_file_name)
        self.df_cleaned.to_excel(output_file_name)
        return('DataFrame written to Excel File successfully.')

if __name__ == '__main__':
    ## STEP 1 - open dataset and explore
    filename = "UAB_dataset1.xlsx"
    uab_explorer = UabExplorer(filename)

    # Directly print wanted output here
    print(uab_explorer.get_df().columns)

    ## STEP 2 - select needed columns "Name" "Email" "ID" (which is named as "Open-ended response")
    ## STEP 3 - remove irrelevant raws and junky data.
    ### 1) Remove blank rows (NAN) 2) Identify and remove rows that contain not valid emails
    uab_explorer.clean_data()

    ##STEP 4 - create excel file with cleaned data
    output_file_name = 'Userdata_cleaned.xlsx'
    uab_explorer.write_cleaned_df_to_xls(output_file_name)
