from datetime import datetime, timedelta, timezone
from one_py_sdk.clientsdk import ClientSdk
from one_py_sdk.shared.constants import Environment
userName = "userName"
password = "password"
plantId = "plantId"
client = ClientSdk()  # Use for production environment with no cache
# Use for feature environment with 50 second in memory cache of API requests
# client = ClientSdk(Environment.get('feature'), 50)
# client =ClientSdk(Environment.get('integration')) #Use for integration environment no cache
# client =ClientSdk(Environment.get('stage')) #Use for stage environment no cache
# client =ClientSdk(cacheTimeout=30) Use for production with 30 second in memory cache of requests

if (client.Authentication.GetToken(userName, password)):  # Supply username and password here
    print("Authenticated successfully")
else:
    print("Authentication failed")
reportDefs = client.Report.GetReportDefinitions(plantId)

reportNamesAndIds = [[report.id, report.name.value] for report in reportDefs]

nameId = reportNamesAndIds[0]
# Returns all report definitions associated with a plant if a valid plant Id is passed in
reportDefsForPlant = client.Report.GetReportDefinitions(plantId)
# or all report definitions available to the user if no plant id is passed in
# Returns a specific report definition based on the report id that is passed in
reportDef = client.Report.GetReportDefinitionById(nameId[0])
# Returns column ids associated with a specific report definition based on the report id that is passed in
colIdsUsingReportId = client.Report.GetColumnIdsByReportId(nameId[0])
# Returns column ids associated with reports with the name that is passed in for the plant Id that is passed in
colIdsUsingName = client.Report.GetColumnIdsByReportName(nameId[1], plantId)
# if no plant id is passed in this will return column ids associated with reports that have the name that is passed in for all available plants
# Returns column ids associated with all reports in a specific plant based on the plant id that is passed in
colIdsForWholePlant = client.Report.GetColumnIdsByPlant(plantId)


print(f"Columns in Report by name: \n {colIdsUsingName}")
print(f"Columns in Report by Id: \n {colIdsUsingReportId}")
print(f"Columns in Reports by plant: \n {colIdsForWholePlant}")
print(f"Reports by plant: \n {reportDefsForPlant}")
print(f"Report retrieved by Id: \n {reportDef}")
