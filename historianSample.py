from datetime import datetime, timedelta, timezone
from one_py_sdk.clientsdk import ClientSdk
client =ClientSdk(cacheTimeout=30) # Use for production with 30 second in memory cache of requests

if (client.Authentication.GetToken("userName", "password")):  # Supply username and password here
    print("Authenticated successfully")
else:
    print("Authentication failed")
startDate = datetime(2022,7,1,23,45,0,0, timezone.utc)
endDate = datetime(2022,7,3,20,19,1,0,timezone.utc)
datum = client.Historian.GetHistorianData("twinId", startDate)
data = client.Historian.GetHistorianDataRange("twinId", startDate, endDate)
