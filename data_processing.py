import pandas as pd
def clean():
    data_train = pd.read_csv("data/train_data.csv")
    data_train_label =  pd.read_csv("data/train_results.csv")
    data_test =  pd.read_csv("data/test_data.csv")


    data_train.set_index('id', inplace=True)
    data_train_label.set_index('id', inplace=True)
    data_test.set_index('id', inplace=True)
    
    
    return data_train,data_train_label,data_test
