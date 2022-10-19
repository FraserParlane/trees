import pandas as pd
import os

# Data paths
data_path = os.path.dirname('data')
path_raw_tree_data = os.path.join(data_path, 'raw_tree_data.csv')
path_clean_tree_data = os.path.join(data_path, 'clean_tree_data.csv')


def download_tree_data():
    """
    Download the tree data from:
    https://opendata.vancouver.ca/explore/dataset/street-trees/
    """

    # Download the raw data
    url = "https://opendata.vancouver.ca/explore/dataset/street-trees/" \
          "download/?format=csv"
    data = pd.read_csv(url, delimiter=';')
    data.to_csv(path_raw_tree_data, index=False)


def clean_tree_data():
    """
    Clean the raw_tree_data.csv
    """

    # Read in raw data
    raw = pd.read_csv(path_raw_tree_data)

    # Save the processed data
    raw.to_csv(path_clean_tree_data)


if __name__ == '__main__':
    download_tree_data()
    clean_tree_data()
