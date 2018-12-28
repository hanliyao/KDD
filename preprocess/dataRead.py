import pandas as pd
import os

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

from preprocess import __config__

file_path = "C:\\Users\\hly\\Documents\\GitHub\\cache"
names = __config__.names
names_label = __config__.names_label


def test_data_unlabel_10():
    """
    test data unlabled 10 percent
    :return: 
    """
    path = os.path.join(file_path, "kddcup.testdata.unlabeled_10_percent")
    return pd.read_csv(path,header=None, names=names)

def test_data_unlabel():
    """
    test unlabeled data
    :return: 
    """
    path = os.path.join(file_path, "kddcup.testdata.unlabeled")
    return pd.read_csv(path,header=None,names=names)

def newtestdata_10_percent_unlabeled():
    """
    new test data 10 percents (unlabeled)
    :return: 
    """
    path = os.path.join(file_path, "kddcup.newtestdata_10_percent_unlabeled")
    return pd.read_csv(path,header=None,names=names)


def corrected():
    """
    test data with corrected labels
    :return: 
    """
    path = os.path.join(file_path,"corrected")
    return pd.read_csv(path,header=None,names=names_label)


def data_10_percent_corrected():
    """
    data 10 percent
    :return: 
    """
    path = os.path.join(file_path, "kddcup.data_10_percent_corrected")
    return pd.read_csv(path,header=None,names=names_label)

def full_data():
    """
    
    :return: 
    """
    path = os.path.join(file_path, "kddcup.data.corrected")
    return pd.read_csv(path,header=None,names=names_label)

if __name__ == "__main__":
    print(full_data())
