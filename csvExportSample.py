from datetime import datetime, timezone
from one_py_sdk.clientsdk import ClientSdk
import json

#client =ClientSdk() #Use for production environment 
client =ClientSdk(cacheTimeout=30) #Use for production with 30 second in memory cache of requests

plantId="providePlantGuidHere"
    
if (client.Authentication.GetToken("UserName", "Password")):# Supply username and password here
    print("Authenticated successfully")
else:
    print("Authentication failed")
print(client.Authentication.UserName)
print(client.Authentication.Token)



client.Exporter.ExportLimits("Limits.csv", plantId) #Exports limit columns for all worksheet types

client.Exporter.ExportLimits("LimitsForFourHour.csv", plantId, 3)#providing a worksheet type and view will only export limits in worksheets of the specified time interval

startDate =datetime(2022,7,1,20,13,1,0,timezone.utc)
endDate =datetime(2022,11,16,20,13,1,0,timezone.utc)
updatedAfter =datetime(2022,8,16,20,13,1,0,timezone.utc)

client.Exporter.ExportColumnDetails("ColumnInfoJustMyViewAll.csv", plantId, None, "MyView") #Only exports columns in specified view for every worksheet type
print(f"Completed export of column information for all worksheet types for plant {plantId}")

client.Exporter.ExportColumnDetails("ColumnInfoDailyJustMyView.csv", plantId, 4,  "MyView") #providing a worksheet type and view will only export column info in views with that name for that type of worksheet
print(f"Completed export of column information for daily worksheets for plant {plantId}")

client.Exporter.ExportColumnDetails("ColumnInfoDaily.csv", plantId, 4) 
print(f"Completed export of column information for daily worksheets for plant {plantId}")

client.Exporter.ExportLimitColumns("LimitColumnInfoAllLimitsTest.csv", plantId, 4, "", True)  #Only exports columns with regulatory limits unless the final parameter is set to true (it defaults to false) then it will export all columns with limits
print(f"Completed export of column information for all limit columns for daily worksheet for plant {plantId}")

client.Exporter.ExportLimitColumns("LimitColumnInfoRegulatoryLimitsTest.csv", plantId, 4, "")  #Only exports columns with regulatory limits unless the final parameter is set to true (it defaults to false) then it will export all columns with limits
print(f"Completed export of column information for regulatory limit columns for daily worksheet for plant {plantId}")

client.Exporter.ExportColumnDetails("ColumnInfoHourly.csv", plantId, 2) 
print(f"Completed export of column information for hourly worksheets for plant {plantId}")

client.Exporter.ExportWorksheet("ExportWSData.csv", plantId, startDate, endDate)
print(f"Completed export of all worksheet data from {startDate.date()} to {endDate.date()}")

client.Exporter.ExportWorksheet(f"ExportWSDataEnteredSince{str(updatedAfter)[:11]}.csv", plantId, startDate, endDate, updatedAfter) # passing in this third date parameter will only give you data that was updated since that time
print(f"Completed export of daily worksheet data from {startDate.date()} to {endDate.date()} that was entered since")

client.Exporter.ExportWorksheet("ExportDaily.csv", plantId, startDate, endDate, None, 4) #providing a worksheet type will only export row info for that type of worksheet
print(f"Completed export of daily worksheet data from {startDate.date()} to {endDate.date()}")

client.Exporter.ExportWorksheet("ExportFourHour.csv", plantId, startDate, endDate, None, 3)
print(f"Completed export of four hour worksheet data from {startDate.date()} to {endDate.date()}")

client.Exporter.ExportWorksheet("ExportHourly.csv", plantId, startDate, endDate, None, 2)
print(f"Completed export of hourly worksheet data from {startDate.date()} to {endDate.date()}")

client.Exporter.ExportWorksheet("ExportFifteenMinute.csv", plantId, startDate, endDate, None, 1)
print(f"Completed export of fifteen minute worksheet data from {startDate.date()} to {endDate.date()}")

client.Exporter.ExportWorksheetByType("ExportFifteenByType.csv", plantId, startDate, endDate, 1)
# This method will be deprecated as the same functionality is achieved by calling ExportWorksheetByType 
# and passsing in a worksheet type parameter.
print(f"Completed export of fifteen minute worksheet data from {startDate.date()} to {endDate.date()}")
client.Exporter.ExportColumnDetailsByType("ColumnInfo15M.csv", plantId, 1) # This method will be deprecated as the same functionality is achieved by calling export column
#details and passsing in a worksheet type parameter.
print(f"Completed export of column information for fifteen minute worksheets for plant {plantId}")