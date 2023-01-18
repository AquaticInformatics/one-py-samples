from datetime import datetime, timedelta, timezone
from one_py_sdk.clientsdk import ClientSdk
from one_py_sdk.shared.constants import Environment 
from creds import *
#client =ClientSdk() #Use for production environment with no cache
client =ClientSdk(Environment.get('feature'), 50) #Use for feature environment with 50 second in memory cache of API requests
#client =ClientSdk(Environment.get('integration')) #Use for integration environment no cache
#client =ClientSdk(Environment.get('stage')) #Use for stage environment no cache
#client =ClientSdk(cacheTimeout=30) Use for production with 30 second in memory cache of requests

if (client.Authentication.GetToken(userName, password)):  # Supply username and password here
    print("Authenticated successfully")
else:
    print("Authentication failed")

try:
    ############## Null Checks ##################
    # get all report definitions
    reportDefsForPlant = client.Report.GetReportDefinitions("14eeb5ad-d924-439f-b4e5-2c8f5768dc45")    
    print (f"Get Report Definitions: \n {reportDefsForPlant}")

    allReportDefs = client.Report.GetReportDefinitions()    
    print (f"Get Report Definitions: \n {allReportDefs}")

    reportDefById = client.Report.GetReportDefinitionById("")
    print (f"GetReportDefinitionById: \n {reportDefById}")

    columnByReportId = client.Report.GetColumnIdsByReportId("")    
    print (f"GetColumnIdsByReportId: \n {columnByReportId}")

    columnIdsByReportName = client.Report.GetColumnIdsByReportName("")
    print (f"GetColumnIdsByReportName: \n {columnIdsByReportName}")

    columnIdsByPlant = client.Report.GetColumnIdsByPlant("")
    print (f"GetReportColumnIdsByPlant: \n {columnIdsByPlant}")

    # ############# Happy Path ######################
    happyReportDefinitions = client.Report.GetReportDefinitions("746926c1-cada-4d72-a11d-7963977112c3")    
    print (f"Get Report Definitions: \n {happyReportDefinitions}")

    happyReportDefById = client.Report.GetReportDefinitionById("2533826c-1e83-430c-9a8c-1c7a743e0f1d")
    print (f"GetReportDefinitionById: \n {happyReportDefById}")

    happyColumnByReportId = client.Report.GetColumnIdsByReportId("2533826c-1e83-430c-9a8c-1c7a743e0f1d")    
    print (f"GetColumnIdsByReportId: \n {happyColumnByReportId}")

    happyColumnIdsByReportName = client.Report.GetColumnIdsByReportName("JR Tests Python", "bogus name")
    print (f"GetColumnIdsByReportName: \n {happyColumnIdsByReportName}")

    happyColumnIdsByPlant = client.Report.GetColumnIdsByPlant("746926c1-cada-4d72-a11d-7963977112c3")
    print (f"GetReportColumnIdsByPlant: \n {happyColumnIdsByPlant}")

    input("Press Any Key")
except Exception as e:
    print("Ooops", e)
    input("Press Any Key")
