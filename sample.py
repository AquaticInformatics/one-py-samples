from datetime import datetime, timedelta, timezone
from one_py_sdk.clientsdk import ClientSdk
from one_py_sdk.shared.constants import Environment 

userName =""
password =""
plantId=""

startDate =datetime(2022,7,1,20,13,1,0,timezone.utc)
endDate =datetime(2022,7,16,20,13,1,0,timezone.utc)
updatedAfter =datetime(2022,7,12,20,13,1,0,timezone.utc)

#client =ClientSdk(Environment.get('feature')) #Use for feature environment
#client =ClientSdk(Environment.get('integration')) #Use for integration environment
#client =ClientSdk(Environment.get('stage')) #Use for stage environment

client =ClientSdk() #Use for production environment
if (client.Authentication.GetToken(userName, password)):  # Supply username and password here
    print("Authenticated successfully")
else:
    print("Authentication failed")
print(client.Authentication.UserName)
print(client.Authentication.Token)

client.Exporter.ExportColumnDetails("ColumnInfoAll.csv", plantId)
print(f"Completed export of column information for all worksheet types for plant {plantId}")

client.Exporter.ExportColumnDetails("ColumnInfoDaily.csv", plantId, 4) #providing a worksheet type will only export column info for that type of worksheet
print(f"Completed export of column information for daily worksheets for plant {plantId}")

client.Exporter.ExportColumnDetails("ColumnInfoDaily.csv", plantId, 3) 
print(f"Completed export of column information for four hour worksheets for plant {plantId}")

client.Exporter.ExportColumnDetails("ColumnInfoDaily.csv", plantId, 2) 
print(f"Completed export of column information for hourly worksheets for plant {plantId}")

client.Exporter.ExportColumnDetails("ColumnInfoDaily.csv", plantId, 1) 
print(f"Completed export of column information for fifteen minute worksheets for plant {plantId}")

client.Exporter.ExportWorksheet("ExportWSData.csv", plantId, startDate, endDate)
print(f"Completed export of all worksheet data from {startDate.date()} to {endDate.date()}")

client.Exporter.ExportWorksheet("ExportWSData.csv", plantId, startDate, endDate, updatedAfter)

client.Exporter.ExportWorksheet("ExportFourHour.csv", plantId, startDate, endDate, None, 4) #providing a worksheet type will only export row info for that type of worksheet
print(f"Completed export of daily worksheet data from {startDate.date()} to {endDate.date()}")

client.Exporter.ExportWorksheet("ExportFourHour.csv", plantId, startDate, endDate, None, 3)
print(f"Completed export of four hour worksheet data from {startDate.date()} to {endDate.date()}")

client.Exporter.ExportWorksheet("ExportHourly.csv", plantId, startDate, endDate, None, 2)
print(f"Completed export of hourly worksheet data from {startDate.date()} to {endDate.date()}")

client.Exporter.ExportWorksheet("ExportFifteenMinute.csv", plantId, startDate, endDate, None, 1)
print(f"Completed export of fifteen minute worksheet data from {startDate.date()} to {endDate.date()}")