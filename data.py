import pandas as pd
import numpy as np
import json
import os

# Data paths
data_path = os.path.join(os.getcwd(), 'data')
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
    data = pd.read_csv(path_raw_tree_data)

    # Remove entries that do not have a geolocation
    data = data.dropna(subset=['geom'])

    # Extract the lat and long as numerical rows
    geom = data['geom'].apply(json.loads)
    data['lon'] = geom.apply(lambda x: x['coordinates'][0])
    data['lat'] = geom.apply(lambda x: x['coordinates'][1])

    # Drop erroneous lon values
    data = data[data['lon'] < 0]

    # Convert lat lon to x and y using a simple conversion
    data['x'] = data['lon'] * np.cos(data['lat'][0] * np.pi / 180)
    data['y'] = data['lat']

    # Save the processed data
    data.to_csv(path_clean_tree_data, index=False)


if __name__ == '__main__':
    # download_tree_data()
    clean_tree_data()
