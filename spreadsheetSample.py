from datetime import datetime,  timezone
from one_py_sdk.clientsdk import ClientSdk
from one_py_sdk.shared.helpers.datetimehelper import * #imports all methods from datetimehelper class

client =ClientSdk(cacheTimeout=50) #Use for Production environment with 50 second in memory cache
client.Authentication.GetToken("userName", "password") # Supply username and password here
startDate =datetime(2022,7,1,20,13,1,0,timezone.utc)
endDate =datetime(2022,7,16,20,13,1,0,timezone.utc)
plantId ="" #defining the plantId to be passed into the functions 

rows =client.Spreadsheet.GetRowsForTimeRange(plantId, 4, startDate, endDate) #retrieve all rows for specified worksheet type from start to end date
# worksheet type values are 1= Fifteen minute, 2=Hourly, 3=FourHour, 4=Daily
wsDef = client.Spreadsheet.GetWorksheetDefinition(plantId, 4) #retrieve worksheet definition for specified worksheet type 
colIds =client.Spreadsheet.GetWorksheetColumnIds(plantId, 4) # returns just column ids for a worksheet of the specified type
colNumbers = client.Spreadsheet.GetWorksheetColumnNumbers(plantId, 3) # returns just column numbers for a worksheet of the specified type
colsForStart =[client.Spreadsheet.GetColumnByDay(plantId, 3, col, startDate) for col in colNumbers] #Gets columns for specified day (daily worksheets not supported)
startRowDaily =GetRowNumber(startDate, 4) #datetimehelper class has functions for converting rownumbers to datetimes or datetimes to row numbers 
endRowDaily =GetRowNumber(endDate, 4)# converts datetime to row number
endDateFromRowNumber =GetDateFromRowNumber(endRowDaily,4) #converts row number to datetime
sameRows= client.Spreadsheet.GetRows(plantId, 4, endRowDaily, startRowDaily) #gets rows from start row to end row. 
spreadSheetDef=client.Spreadsheet.GetSpreadsheetDefinition(plantId) #gets spreadsheet definition which mainly contains timezone info
columnForStartMonth=client.Spreadsheet.GetColumnByMonth(plantId, 3, colNumbers[0], startDate) #gets column measurement info for the month of the datetime passed in
columnForStartYear =client.Spreadsheet.GetColumnByYear(plantId, 3, colNumbers[0], startDate) #gets column measurement info for the year of the datetime passed in
rowsForStartDay=client.Spreadsheet.GetRowsByDay(plantId, 4, startDate) #gets rows by day optional parameters are viewId or a list of column numbers with up to 30 columns 
rowsForStartMonth = client.Spreadsheet.GetRowsByMonth(plantId, 4, startDate) #gets rows for the month of datetime passed in optional parameters are viewId or a list of column numbers with up to 30 columns 
