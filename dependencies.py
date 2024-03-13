# Importing required libraries
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Creating a function to preprocess data
def preprocess(df):

    # Creating a standardiation object
    scaler = StandardScaler()

    # Standardizing the dataframe
    scaled_data = scaler.fit_transform(df)

    # Creating a dimensionality reduction object to reduce to 2 dimensions
    pca = PCA(n_components=2)

    # Reducing the dimensions of the data
    reduced_data = pca.fit_transform(scaled_data)

    # Returning the reduced data
    return reduced_data