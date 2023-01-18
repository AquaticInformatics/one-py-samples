from datetime import datetime, timedelta, timezone
from one_py_sdk.clientsdk import ClientSdk
from one_py_sdk.shared.constants import Environment
from creds import *
client =ClientSdk() #Use for production environment with no cache
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
reportDefsForPlant = client.Report.GetReportDefinitions(plantId)
reportDef = client.Report.GetReportDefinitionById(nameId[0])
colIdsUsingReportId = client.Report.GetColumnIdsByReportId(nameId[0])
colIdsUsingName = client.Report.GetColumnIdsByReportName(nameId[1], plantId)
colIdsForWholePlant = client.Report.GetColumnIdsByPlant(plantId)
reportDefById = client.Report.GetReportDefinitionById("")
print(f"ReportDefByIdNull {reportDefById}")
print(f"Columns in Report by name: \n {colIdsUsingName}")
print(f"Columns in Report by Id: \n {colIdsUsingReportId}")
print(f"Columns in Reports by plant: \n {colIdsForWholePlant}")
print(f"Reports by plant: \n {reportDefsForPlant}")
print(f"Report retrieved by Id: \n {reportDef}")
