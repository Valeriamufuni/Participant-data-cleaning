
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot

class OpenandExplore():
    def __init__(self):
        pass
    
    def open_file(self, filename):
        print("Running open_file()")

        df = pd.read_excel(filename)
        #list(df.columns)
        #df.head(50)
        #return df.head(50)
        #return list(df.columns)
        #import pdb; pdb.set_trace();

    def dataset_overview(self, filename):

        df = pd.read_excel(filename)
        df.head(50)
        return df.head(50)

    def list_of_columns(self, filename):

        df = pd.read_excel(filename)
        list(df.columns)
        return list(df.columns)


    def close_file(self):
        pass


class SelectNeededColumns():
    def __init__(self):
        pass

    def select_columns(self, filename):
        print("Selecting needed columns")

        df = pd.read_excel(filename)
        # Select columns
        df_cleaned = df[["Name", "Email Address", "Open-Ended Response"]]
        # print(df.head(50))


class CleanAndRemoveJunk():
    def __init__(self):
        pass
        

    def drop_blanks(self, filename):
        print("Dropping blank raws")

        df = pd.read_excel(filename)        
        df_cleaned = df[["Name", "Email Address", "Open-Ended Response"]]
        new_df = df_cleaned.dropna()
        # print(df_cleaned.head(50))

    def delete_junky_responses(self, filename):   ### function will delete raws that don't contain email adresses
        print("Deleting junks")

        df = pd.read_excel(filename)        
        df_cleaned = df[["Name", "Email Address", "Open-Ended Response"]]
        new_df = df_cleaned.dropna()

        if new_df_filtered == new_df[~new_df["Email Address"].str.contains("@")]     ### still working on function that will delete raws with responses that                   
            drop                                                                     ### don't have @ symbol in it
        print(new_df_filtered.head(50))


    # def count_number_of_raws(self, filename):
    # df = pd.read_excel(filename)
    # total_rows = len(df.index)
    # return total_rows


#class createexcelfile():
    # def __init__(self):
    #     pass

    # def create_excel_file(self, filename):
    #     print("File is being created")
    
    #     df = pd.read_excel(filename)
    #     new_df = df.dropna()
    #     file_name = 'Userdata.xlsx'
    #     new_df.to_excel(file_name)
    #     return('DataFrame is written to Excel File successfully.')
    

if __name__ == '__main__':
   

    ## STEP 1 - open dataset and explore
    filename = "UAB_dataset1.xlsx"
    tool_class = OpenandExplore
    tool_object = tool_class()
    tool_object.open_file(filename)
    tool_object.dataset_overview(filename)
    tool_object.list_of_columns(filename)


    ## STEP 2 - select needed columns "Name" "Email" "ID" (which is named as "Open-ended response")
    tool_class = SelectNeededColumns
    tool_object = tool_class()
    tool_object.select_columns(filename)

    ## STEP 3 - remove irrelevant raws and junky data.
    ### 1) Remove blank raws (NAN) 2) Identify and remove raws that contain not valid emails 
    tool_class = CleanAndRemoveJunk
    tool_object = tool_class()
    tool_object.drop_blanks(filename)
    tool_object.delete_junky_responses(filename)
    #tool_object.create_bolean(filename)

    ##STEP 4 - create excel file with cleaned data
    # tool_class = Create_excel_file
    # tool_object = tool_class()
    # tool_object.create_excel_file(filename)




















### Create boolean method did not work
    # def create_bolean(self, filename):   
    #     df = pd.read_excel(filename)        
    #     df_cleaned = df[["Name", "Email Address", "Open-Ended Response"]]
    #     df_cleaned[df_cleaned["Email Address"]=="@"]
    #     print(df_cleaned.head())





    #print(approach_two(filename))
    #print(select_columns(filename))
    #print(drop_blanks(filename))
    #print(count_number_of_raws(filename))
    #print(create_excel_file(filename))
