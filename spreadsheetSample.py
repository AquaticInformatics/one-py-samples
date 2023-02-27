from datetime import datetime,  timezone
from one_py_sdk.clientsdk import ClientSdk
# imports all methods from datetimehelper class
from one_py_sdk.shared.helpers.datetimehelper import *
from one_py_sdk.shared.constants import Environment as env
from one_py_sdk.shared.models.datapoint import DataPoint

# Use for Production environment with 50 second in memory cache
client = ClientSdk(cacheTimeout=50)
# Supply username and password here
client.Authentication.GetToken("userName", "Password")
startDate = datetime(2023, 2, 22, 20, 13, 1, 0, timezone.utc)
endDate = datetime(2023, 7, 16, 20, 13, 1, 0, timezone.utc)
plantId = ""  # defining the plantId to be passed into the functions
client.LoadCurrentUser()
client.Authentication.User.id
auditUserId = client.Authentication.User.id

# retrieve all rows for specified worksheet type from start to end date
rows = client.Spreadsheet.GetRowsForTimeRange(plantId, 4, startDate, endDate)
# worksheet type values are 1= Fifteen minute, 2=Hourly, 3=FourHour, 4=Daily
# retrieve worksheet definition for specified worksheet type
wsDef = client.Spreadsheet.GetWorksheetDefinition(plantId, 4)
# returns just column ids for a worksheet of the specified type
colIds = client.Spreadsheet.GetWorksheetColumnIds(plantId, 4)
colIdsFourHour = client.Spreadsheet.GetWorksheetColumnIds(plantId, 3)
colIdsHour = client.Spreadsheet.GetWorksheetColumnIds(plantId, 2)
colIdsFifteenMin = client.Spreadsheet.GetWorksheetColumnIds(plantId, 1)

# Loading data to Rio
# Save 150 rows for Fifteen minute, hourly, four hour, and daily data

dates15m = [startDate + timedelta(minutes=15*i) for i in range(150)]
dates1h = [startDate + timedelta(hours=1*i) for i in range(150)]
dates4h = [startDate + timedelta(hours=4*i) for i in range(150)]
dates1d = [startDate + timedelta(days=1*i) for i in range(151)]
data15m = [DataPoint(
    "877", colId, f"noted {colId}", auditUserId, isLocked=True) for colId in colIdsFifteenMin]
data1h = [
    DataPoint("111", colId, f"noted {colId}", auditUserId) for colId in colIdsHour]
data4h = [DataPoint(
    "444", colId, f"noted {colId}", auditUserId) for colId in colIdsFourHour]
data1d = [
    DataPoint("1", colId, f"noted {colId}", auditUserId) for colId in colIds]
fifteenMinuteDictionary = {}
oneHourDict = {}
fourHourDict = {}
dailyDict = {}
for date in dates15m:
    fifteenMinuteDictionary[date] = data15m
for date in dates1h:
    oneHourDict[date] = data1h
for date in dates1d:
    dailyDict[date] = data1d
for date in dates4h:
    fourHourDict[date] = data4h

client.Spreadsheet.ImportDictionary(plantId, fifteenMinuteDictionary, 1)
client.Spreadsheet.ImportDictionary(plantId, oneHourDict, 2)
client.Spreadsheet.ImportDictionary(plantId, fourHourDict, 3)
client.Spreadsheet.ImportDictionary(plantId, dailyDict, 4)

# returns just column numbers for a worksheet of the specified type
colNumbers = client.Spreadsheet.GetWorksheetColumnNumbers(plantId, 3)
# Gets columns for specified day (daily worksheets not supported)
colsForStart = [client.Spreadsheet.GetColumnByDay(
    plantId, 3, col, startDate) for col in colNumbers]
# datetimehelper class has functions for converting rownumbers to datetimes or datetimes to row numbers
startRowDaily = GetRowNumber(startDate, 4)
endRowDaily = GetRowNumber(endDate, 4)  # converts datetime to row number
endDateFromRowNumber = GetDateFromRowNumber(
    endRowDaily, 4)  # converts row number to datetime
# gets rows from start row to end row.
sameRows = client.Spreadsheet.GetRows(plantId, 4, endRowDaily, startRowDaily)
# gets spreadsheet definition which mainly contains timezone info
spreadSheetDef = client.Spreadsheet.GetSpreadsheetDefinition(plantId)
# gets column measurement info for the month of the datetime passed in
columnForStartMonth = client.Spreadsheet.GetColumnByMonth(
    plantId, 3, colNumbers[0], startDate)
# gets column measurement info for the year of the datetime passed in
columnForStartYear = client.Spreadsheet.GetColumnByYear(
    plantId, 3, colNumbers[0], startDate)
# gets rows by day optional parameters are viewId or a list of column numbers with up to 30 columns
rowsForStartDay = client.Spreadsheet.GetRowsByDay(plantId, 4, startDate)
# gets rows for the month of datetime passed in optional parameters are viewId or a list of column numbers with up to 30 columns
rowsForStartMonth = client.Spreadsheet.GetRowsByMonth(plantId, 4, startDate)
