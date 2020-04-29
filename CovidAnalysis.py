import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
# %matplotlib inline


from datetime import datetime

def changeDateFormat(dd):
    date_object = datetime.strptime(dd, "%m/%d/%y")
    d = date_object.strftime('%B%d')
    return d

'''
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0

# @hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. It includes your credentials.
# You might want to remove those credentials before you share the notebook.
client_8202d6b0650a4df78d4909399b1384e9 = ibm_boto3.client(service_name='s3',
    ibm_api_key_id='P1j-yI2tbdIiTNxUF593KC6eyh6FUaNWo6IwFByyx_OO',
    ibm_auth_endpoint="https://iam.ng.bluemix.net/oidc/token",
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3-api.us-geo.objectstorage.service.networklayer.com')

body = client_8202d6b0650a4df78d4909399b1384e9.get_object(Bucket='covid19analysis-donotdelete-pr-gqyyvsjf4yposf',Key='time_series_covid_19_deaths_US.csv')['Body']
# add missing __iter__ method, so pandas accepts body as file-like object
if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )
df = pd.read_csv(body)
'''

df = pd.read_csv("C:\Personal\Imp\Coursera\\novel-corona-virus-2019-dataset/time_series_covid_19_deaths_US.csv")



cdf = df[
    ['Combined_Key', '1/22/20', '1/23/20', '1/24/20', '1/25/20', '1/26/20', '1/27/20', '1/28/20', '1/29/20', '1/30/20',
     '1/31/20', '2/1/20', '2/2/20', '2/3/20', '2/4/20', '2/5/20', '2/6/20', '2/7/20', '2/8/20', '2/9/20', '2/10/20',
     '2/11/20', '2/12/20', '2/13/20', '2/14/20', '2/15/20', '2/16/20', '2/17/20', '2/18/20', '2/19/20', '2/20/20',
     '2/21/20', '2/22/20', '2/23/20', '2/24/20', '2/25/20', '2/26/20', '2/27/20', '2/28/20', '2/29/20', '3/1/20',
     '3/2/20', '3/3/20', '3/4/20', '3/5/20', '3/6/20', '3/7/20', '3/8/20', '3/9/20', '3/10/20', '3/11/20', '3/12/20',
     '3/13/20', '3/14/20', '3/15/20', '3/16/20', '3/17/20', '3/18/20', '3/19/20', '3/20/20', '3/21/20', '3/22/20',
     '3/23/20', '3/24/20', '3/25/20', '3/26/20', '3/27/20', '3/28/20', '3/29/20', '3/30/20', '3/31/20', '4/1/20',
     '4/2/20', '4/3/20', '4/4/20', '4/5/20', '4/6/20', '4/7/20', '4/8/20', '4/9/20', '4/10/20', '4/11/20', '4/12/20',
     '4/13/20', '4/14/20']]
dates = ['January22', 'January23', 'January24', 'January25', 'January26', 'January27', 'January28', 'January29',
         'January30', 'January31', 'February01', 'February02', 'February03', 'February04', 'February05', 'February06',
         'February07', 'February08', 'February09', 'February10', 'February11', 'February12', 'February13', 'February14',
         'February15', 'February16', 'February17', 'February18', 'February19', 'February20', 'February21', 'February22',
         'February23', 'February24', 'February25', 'February26', 'February27', 'February28', 'February29', 'March01',
         'March02', 'March03', 'March04', 'March05', 'March06', 'March07', 'March08', 'March09', 'March10', 'March11',
         'March12', 'March13', 'March14', 'March15', 'March16', 'March17', 'March18', 'March19', 'March20', 'March21',
         'March22', 'March23', 'March24', 'March25', 'March26', 'March27', 'March28', 'March29', 'March30', 'March31',
         'April01', 'April02', 'April03', 'April04', 'April05', 'April06', 'April07', 'April08', 'April09', 'April10',
         'April11', 'April12', 'April13', 'April14']
cdf.rename(columns={'2/1/20': changeDateFormat('2/1/20'), '2/2/20': changeDateFormat('2/2/20'),
                    '2/3/20': changeDateFormat('2/3/20'), '2/4/20': changeDateFormat('2/4/20'),
                    '2/5/20': changeDateFormat('2/5/20'), '2/6/20': changeDateFormat('2/6/20'),
                    '2/7/20': changeDateFormat('2/7/20'), '2/8/20': changeDateFormat('2/8/20'),
                    '2/9/20': changeDateFormat('2/9/20'), '3/1/20': changeDateFormat('3/1/20'),
                    '3/2/20': changeDateFormat('3/2/20'), '3/3/20': changeDateFormat('3/3/20'),
                    '3/4/20': changeDateFormat('3/4/20'), '3/5/20': changeDateFormat('3/5/20'),
                    '3/6/20': changeDateFormat('3/6/20'), '3/7/20': changeDateFormat('3/7/20'),
                    '3/8/20': changeDateFormat('3/8/20'), '3/9/20': changeDateFormat('3/9/20'),
                    '4/1/20': changeDateFormat('4/1/20'), '4/2/20': changeDateFormat('4/2/20'),
                    '4/3/20': changeDateFormat('4/3/20'), '4/4/20': changeDateFormat('4/4/20'),
                    '4/5/20': changeDateFormat('4/5/20'), '4/6/20': changeDateFormat('4/6/20'),
                    '4/7/20': changeDateFormat('4/7/20'), '4/8/20': changeDateFormat('4/8/20'),
                    '4/9/20': changeDateFormat('4/9/20'), '1/22/20': changeDateFormat('1/22/20'),
                    '1/23/20': changeDateFormat('1/23/20'), '1/24/20': changeDateFormat('1/24/20'),
                    '1/25/20': changeDateFormat('1/25/20'), '1/26/20': changeDateFormat('1/26/20'),
                    '1/27/20': changeDateFormat('1/27/20'), '1/28/20': changeDateFormat('1/28/20'),
                    '1/29/20': changeDateFormat('1/29/20'), '1/30/20': changeDateFormat('1/30/20'),
                    '1/31/20': changeDateFormat('1/31/20'), '2/10/20': changeDateFormat('2/10/20'),
                    '2/11/20': changeDateFormat('2/11/20'), '2/12/20': changeDateFormat('2/12/20'),
                    '2/13/20': changeDateFormat('2/13/20'), '2/14/20': changeDateFormat('2/14/20'),
                    '2/15/20': changeDateFormat('2/15/20'), '2/16/20': changeDateFormat('2/16/20'),
                    '2/17/20': changeDateFormat('2/17/20'), '2/18/20': changeDateFormat('2/18/20'),
                    '2/19/20': changeDateFormat('2/19/20'), '2/20/20': changeDateFormat('2/20/20'),
                    '2/21/20': changeDateFormat('2/21/20'), '2/22/20': changeDateFormat('2/22/20'),
                    '2/23/20': changeDateFormat('2/23/20'), '2/24/20': changeDateFormat('2/24/20'),
                    '2/25/20': changeDateFormat('2/25/20'), '2/26/20': changeDateFormat('2/26/20'),
                    '2/27/20': changeDateFormat('2/27/20'), '2/28/20': changeDateFormat('2/28/20'),
                    '2/29/20': changeDateFormat('2/29/20'), '3/10/20': changeDateFormat('3/10/20'),
                    '3/11/20': changeDateFormat('3/11/20'), '3/12/20': changeDateFormat('3/12/20'),
                    '3/13/20': changeDateFormat('3/13/20'), '3/14/20': changeDateFormat('3/14/20'),
                    '3/15/20': changeDateFormat('3/15/20'), '3/16/20': changeDateFormat('3/16/20'),
                    '3/17/20': changeDateFormat('3/17/20'), '3/18/20': changeDateFormat('3/18/20'),
                    '3/19/20': changeDateFormat('3/19/20'), '3/20/20': changeDateFormat('3/20/20'),
                    '3/21/20': changeDateFormat('3/21/20'), '3/22/20': changeDateFormat('3/22/20'),
                    '3/23/20': changeDateFormat('3/23/20'), '3/24/20': changeDateFormat('3/24/20'),
                    '3/25/20': changeDateFormat('3/25/20'), '3/26/20': changeDateFormat('3/26/20'),
                    '3/27/20': changeDateFormat('3/27/20'), '3/28/20': changeDateFormat('3/28/20'),
                    '3/29/20': changeDateFormat('3/29/20'), '3/30/20': changeDateFormat('3/30/20'),
                    '3/31/20': changeDateFormat('3/31/20'), '4/10/20': changeDateFormat('4/10/20'),
                    '4/11/20': changeDateFormat('4/11/20'), '4/12/20': changeDateFormat('4/12/20'),
                    '4/13/20': changeDateFormat('4/13/20'), '4/14/20': changeDateFormat('4/14/20')}, inplace=True)
print(cdf.columns)
no_of_cases = []
for row in cdf.itertuples(index=True, name='Pandas'):
    location = getattr(row, "Combined_Key")
    if location == "Cook, Illinois, US":
        no_of_cases.append(getattr(row, 'January22'))
        no_of_cases.append(getattr(row, 'January23'))
        no_of_cases.append(getattr(row, 'January24'))
        no_of_cases.append(getattr(row, 'January25'))
        no_of_cases.append(getattr(row, 'January26'))
        no_of_cases.append(getattr(row, 'January27'))
        no_of_cases.append(getattr(row, 'January28'))
        no_of_cases.append(getattr(row, 'January29'))
        no_of_cases.append(getattr(row, 'January30'))
        no_of_cases.append(getattr(row, 'January31'))
        no_of_cases.append(getattr(row, 'February01'))
        no_of_cases.append(getattr(row, 'February02'))
        no_of_cases.append(getattr(row, 'February03'))
        no_of_cases.append(getattr(row, 'February04'))
        no_of_cases.append(getattr(row, 'February05'))
        no_of_cases.append(getattr(row, 'February06'))
        no_of_cases.append(getattr(row, 'February07'))
        no_of_cases.append(getattr(row, 'February08'))
        no_of_cases.append(getattr(row, 'February09'))
        no_of_cases.append(getattr(row, 'February10'))
        no_of_cases.append(getattr(row, 'February11'))
        no_of_cases.append(getattr(row, 'February12'))
        no_of_cases.append(getattr(row, 'February13'))
        no_of_cases.append(getattr(row, 'February14'))
        no_of_cases.append(getattr(row, 'February15'))
        no_of_cases.append(getattr(row, 'February16'))
        no_of_cases.append(getattr(row, 'February17'))
        no_of_cases.append(getattr(row, 'February18'))
        no_of_cases.append(getattr(row, 'February19'))
        no_of_cases.append(getattr(row, 'February20'))
        no_of_cases.append(getattr(row, 'February21'))
        no_of_cases.append(getattr(row, 'February22'))
        no_of_cases.append(getattr(row, 'February23'))
        no_of_cases.append(getattr(row, 'February24'))
        no_of_cases.append(getattr(row, 'February25'))
        no_of_cases.append(getattr(row, 'February26'))
        no_of_cases.append(getattr(row, 'February27'))
        no_of_cases.append(getattr(row, 'February28'))
        no_of_cases.append(getattr(row, 'February29'))
        no_of_cases.append(getattr(row, 'March01'))
        no_of_cases.append(getattr(row, 'March02'))
        no_of_cases.append(getattr(row, 'March03'))
        no_of_cases.append(getattr(row, 'March04'))
        no_of_cases.append(getattr(row, 'March05'))
        no_of_cases.append(getattr(row, 'March06'))
        no_of_cases.append(getattr(row, 'March07'))
        no_of_cases.append(getattr(row, 'March08'))
        no_of_cases.append(getattr(row, 'March09'))
        no_of_cases.append(getattr(row, 'March10'))
        no_of_cases.append(getattr(row, 'March11'))
        no_of_cases.append(getattr(row, 'March12'))
        no_of_cases.append(getattr(row, 'March13'))
        no_of_cases.append(getattr(row, 'March14'))
        no_of_cases.append(getattr(row, 'March15'))
        no_of_cases.append(getattr(row, 'March16'))
        no_of_cases.append(getattr(row, 'March17'))
        no_of_cases.append(getattr(row, 'March18'))
        no_of_cases.append(getattr(row, 'March19'))
        no_of_cases.append(getattr(row, 'March20'))
        no_of_cases.append(getattr(row, 'March21'))
        no_of_cases.append(getattr(row, 'March22'))
        no_of_cases.append(getattr(row, 'March23'))
        no_of_cases.append(getattr(row, 'March24'))
        no_of_cases.append(getattr(row, 'March25'))
        no_of_cases.append(getattr(row, 'March26'))
        no_of_cases.append(getattr(row, 'March27'))
        no_of_cases.append(getattr(row, 'March28'))
        no_of_cases.append(getattr(row, 'March29'))
        no_of_cases.append(getattr(row, 'March30'))
        no_of_cases.append(getattr(row, 'March31'))
        no_of_cases.append(getattr(row, 'April01'))
        no_of_cases.append(getattr(row, 'April02'))
        no_of_cases.append(getattr(row, 'April03'))
        no_of_cases.append(getattr(row, 'April04'))
        no_of_cases.append(getattr(row, 'April05'))
        no_of_cases.append(getattr(row, 'April06'))
        no_of_cases.append(getattr(row, 'April07'))
        no_of_cases.append(getattr(row, 'April08'))
        no_of_cases.append(getattr(row, 'April09'))
        no_of_cases.append(getattr(row, 'April10'))
        no_of_cases.append(getattr(row, 'April11'))
        no_of_cases.append(getattr(row, 'April12'))
        no_of_cases.append(getattr(row, 'April13'))
        no_of_cases.append(getattr(row, 'April14'))
        print("Location is %s" % location)
        print(no_of_cases)
        break

plt.scatter(dates, no_of_cases, color='blue')
plt.xlabel("dates")
plt.ylabel("no_of_cases")
plt.show()

index = range(1,93)
days = []
for x in index:
    days.append(x)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures

dates = days
poly = PolynomialFeatures(degree = 4)
X_poly = poly.fit_transform([dates])
poly.fit(X_poly, [no_of_cases])

lin2 = LinearRegression()
lin2.fit([dates],[no_of_cases])