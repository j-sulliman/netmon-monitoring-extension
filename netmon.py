#!/usr/bin/env python3
from net_functions import get_host_response_time

hosts = {
    "dns": ["8.8.8.8", "208.67.222.222", "208.67.220.220"],
    "gateway": ["192.168.201.1"],
    "ntp": ["nz.pool.ntp.org"],
    "cloud": ["quicksight.ap-southeast-2.amazonaws.com", "management.azure.com"],
    "saas": ["salesforce.com", "workday.com", "www.office.com"]
}

for dns in hosts["dns"]:
    print(dns)
    pingResult=get_host_response_time(dns)
    print("name=Custom Metrics|Latency|dns|{}, value={}".format(dns,pingResult))
for gateway in hosts["gateway"]:
    pingResult=get_host_response_time(gateway)
    print("name=Custom Metrics|Latency|gateway|{}, value={}".format(gateway,pingResult))
for ntp in hosts["ntp"]:
    pingResult=get_host_response_time(ntp)
    print("name=Custom Metrics|Latency|ntp|{}, value={}".format(ntp, pingResult))
for cloud in hosts["cloud"]:
    pingResult=get_host_response_time(cloud)
    print("name=Custom Metrics|Latency|cloud|{}, value={}".format(cloud, pingResult))
for saas in saas:
    pingResult=get_host_response_time(saas)
    print("name=Custom Metrics|Latency|SaaS|{}, value={}".format(saas, pingResult))