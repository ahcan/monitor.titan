import requests
from config import titan_ip, account
import config
import json
import logging
import logging.config


class Titan:

    def __init__(self, host):
        # Create the Logger
        self.logger = logging.getLogger("Titan")
        #logger.setLevel(logging.WARNING)
        self.host = host
        self.headers = {
            'Authorization': "Basic {0}".format(account[self.host]),
            'Host': "{0}".format(self.host),
        }

    def getCPU(self):
        # get CPU use titan(%)
        #
        url = "http://{0}/api/v1/system/information/cpu".format(self.host)
        try:
            response = requests.request("GET", url, headers=self.headers)
            if response.status_code == requests.codes.ok:
                self.logger.debug("OK")
                return float(json.loads(response.text)['CPULoad'])
            else:
                return 0
        except Exception as e:
            print (e)
            return 0

    def getRAM(self):
        url = "http://{0}/api/v1/system/information/memory".format(self.host)
        response = requests.request("GET",url, headers=self.headers)
        print response.status_code
        print response.headers
        data = json.loads(response.text)
        res = self.percentRAM(total=float(data['MemorySize']), use=float(data['MemoryUsage']))
        return res

    def percentRAM(self,total, use):
        #return float xx,xx
        return round(float(use)/float(total)*100,2)

for item in titan_ip:
    print item
    titan = Titan(item)
    print titan.getCPU()
    titan.getRAM()