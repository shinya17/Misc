# i saw a tweet that said earthquakes don't happen distributed evenly but clustered. i wanted to test that. 
# first i looked at the net, it says because earthquakes trigger smaller earthquakes. let's see that. then let's see if removing triggered earthquakes, what we have

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in CSV file from the data source
#TODO change times
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from geopy.distance import geodesic

# Read in CSV file from the data source
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from geopy.distance import geodesic
from sklearn.cluster import KMeans

# Read in CSV file from the data source
# url = "https://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=2023-03-20%2000:00:00&endtime=2023-04-19%2023:59:59&minmagnitude=4.5&eventtype=earthquake&orderby=time&limit=20000"

url="https://www.emidius.eu/services/europe/wfs?service=wfs&request=GetFeature&typeNames=europe:EPICA_1000_1899&CQL_FILTER=Mw>=3.0%20AND%20Year>=1500&outputFormat=csv"
# this data has something to be aware of, some entries' time is incomplete. it might make sense to group by time availability as well. or just care only about year month day ones. and additionaly year month day hour minute ones maybe
os.system("wget "+url+" -O=earthquakeData.csv")

df = pd.read_csv("earthquakeData.csv", 
usecols=[
"Lat",
"Lon",
"Year",
"Mo",
"Da",
"Ho",
"Mi"])


"""
algorithm is as follows,

first group by area, maybe it'd be the best to group by fault lines but then they're not known well and the data is too big.
then calculate time distance between earthquakes
"""


# coordinates df["Lat"], df["Lon"]
# time df["Year"], df["Mo"], df["Da"], df["Ho"], df["Mi"]  
