#----imports start----#
import urllib.request
import json
#----imports end----#
ip = "172.25.0.1"

def set_ip(x):
    global ip
    ip = x
    
def getAPIVersions():
     url = "http://" + ip + "/getAPIVersions.psp"
     req = urllib.request.urlopen(url)
     data = req.read().decode('utf-8')
     return json.loads(data)
     
def getDataRates():
    url = "http://" + ip + "/getDataRates.psp"
    req = urllib.request.urlopen(url)
    data = req.read().decode('utf-8')
    return json.loads(data)
    
def getHDDStat():
    url = "http://" + ip + "/getHDDStat.psp"
    req = urllib.request.urlopen(url)
    data = req.read().decode('utf-8')
    return json.loads(data)
    
def getscannednetworks():
    url = "http://" + ip + "/get-scanned-networks.psp"
    req = urllib.request.urlopen(url)
    data = req.read().decode('utf-8')
    return json.loads(data)
    
def getMaxClient():
    url = "http://" + ip + "/getMaxClient.psp"
    req = urllib.request.urlopen(url)
    data = req.read().decode('utf-8')
    return json.loads(data)

def getLogs():
    url = "http://" + ip + "/getLogs.psp"
    req = urllib.request.urlopen(url)
    data = req.read().decode('utf-8')
    return json.loads(data)

def getTime():
    url = "http://" + ip + "/getTime.psp"
    req = urllib.request.urlopen(url)
    data = req.read().decode('utf-8')
    return json.loads(data)

def batteryStatus():
    url = "http://" + ip + "/batteryStatus.psp"
    req = urllib.request.urlopen(url)
    data = req.read().decode('utf-8')
    return json.loads(data)