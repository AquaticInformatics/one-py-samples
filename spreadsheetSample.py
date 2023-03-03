from datetime import datetime,  timezone
from one_py_sdk.clientsdk import ClientSdk
# imports all methods from datetimehelper class
from one_py_sdk.shared.helpers.datetimehelper import *
from one_py_sdk.shared.constants import Environment as env
from one_py_sdk.shared.models.datapoint import DataPoint

# Use for Production environment with 50 second in memory cache
client = ClientSdk(env.get("feature"), cacheTimeout=50)
# Supply username and password here
client.Authentication.GetToken("", "")
plantId = "c1ed7bab-f0bb-4fd6-83fc-c7882a0c057b"  # defining the plantId to be passed into the functions
client.LoadCurrentUser()
client.Authentication.User.id
auditUserId = client.Authentication.User.id

try:



    data1d = [
        # Silver
        DataPoint("6", "b79a7405-9a92-4814-b73f-d73c9759e659", "", "3c1474fb-02c3-4fea-a08e-6982effc22eb", datetime(2023, 3, 3, 13, 17, 1, 0), False)
        # DataPoint("2", "b79a7405-9a92-4814-b73f-d73c9759e659", "", "", datetime(2023, 3, 3, 13, 18, 1, 0, timezone.utc)),
        # DataPoint("3", "b79a7405-9a92-4814-b73f-d73c9759e659", "", "", datetime(2023, 3, 3, 13, 19, 1, 0, timezone.utc))
        # Beryllium
        # DataPoint("1", "7952609d-293a-4f52-9feb-e3bc0898ddd9", "", "", datetime(2023, 3, 3, 13, 17, 1, 0, timezone.utc)),
        # DataPoint("2", "7952609d-293a-4f52-9feb-e3bc0898ddd9", "", "", datetime(2023, 3, 3, 13, 18, 1, 0, timezone.utc)),
        # DataPoint("3", "7952609d-293a-4f52-9feb-e3bc0898ddd9", "", "", datetime(2023, 3, 3, 13, 19, 1, 0, timezone.utc))

        ]
    
    print(data1d)

    dailyDict = {}

    firstDate = datetime(2023, 3, 13, 15, 55, 1, 0, timezone.utc)
    # secondDate = datetime(2023, 3, 14, 15, 55, 1, 0, timezone.utc)


    print("about to add to dictionary")

    dailyDict[firstDate] = data1d
    # dailyDict[secondDate] = data1d

    print("about to save")


    client.Spreadsheet.ImportDictionary(plantId, dailyDict, 4)

except Exception as e:
    print("oops", e)

input("done, enter value to close")

