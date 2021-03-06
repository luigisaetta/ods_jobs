import pandas as pd
import ocifs

def read_from_object_storage(prefix, file_name):
    # get access to OSS as an fs
    # config={} assume RESOURCE PRINCIPAL auth
    fs = ocifs.OCIFileSystem(config={})
    
    FILE_PATH = prefix + file_name
    
    # reading data from Object Storage
    with fs.open(FILE_PATH, 'rb') as f:
        df = pd.read_csv(f)
    
    return df

PREFIX = "oci://credit_scoring@emeaseitalyproxima/"
FILE_NAME = "cs-training.csv"



print()
print('Test1 for JOBS: access to Object Storage using OCIFS and RP')
print()
print("Reading csv file")
print()
data_orig = read_from_object_storage(PREFIX, FILE_NAME)
print('DataFrame shape is:', data_orig.shape)
print()