import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401
import time

cmdResults = demisto.executeCommand("getList", {"listName":"Job_Utility_Bulk_Alert_Closer_ID_List"})

results = cmdResults[0]["Contents"]
uri = "/public_api/v1/alerts/update_alerts"
currList = "["
itNum = 1
maxNum = 99


totalAlerts = results.split('\n')

for item in totalAlerts:
    if itNum < maxNum:
        currList = currList + str(item) + ","
        itNum = itNum + 1
    if itNum == maxNum:
        currList = currList + str(item) + "]"
        body = '{"request_data":{"alert_id_list":' + str(currList) + ',"update_data":{"severity":"low","status":"resolved_other","comment":"Emergency Alert Closer"}}}'
        print(body)
        cmdResults = demisto.executeCommand("core-api-post", {"uri": uri, "body": body, "execution-timeout": "5"})
        print(cmdResults)
        currList = "["
        itNum = 1


