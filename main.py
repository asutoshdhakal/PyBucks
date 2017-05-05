import geoplotlib
from geoplotlib.utils import read_csv
import pandas as pd




df = pd.read_csv('directory.csv')
lat = df.lat
lon = df.lon

geoplotlib.dot(lat[0], lon[0])
geoplotlib.show()


print lat[0]
print lon[0]
