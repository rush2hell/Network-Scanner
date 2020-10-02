# Network-Scanner
Network Scanner is used for scanning both large corporate networks that have hundred thousands of computers along with small home networks with several computers. These network scanner is developed with: -   

Basic network scanner with 3 main functionality 
1. Provide list of connected device
2. Changing MAC Address
3. Port Scanning

## Technology Used 
[![Generic badge](https://img.shields.io/badge/Python-3.7-<COLOR>.svg)](https://shields.io/) [![Generic badge](https://img.shields.io/badge/Scapy-2.4-<COLOR>.svg)](https://shields.io/)



## Run and Installation
```bash
python3 network.py
```
![git_clone_scanner](https://user-images.githubusercontent.com/47297909/94921486-6ade1480-0486-11eb-82cd-f499cdaf07ad.png)

## Usage
### To check the Device connected 
Specify the IP Address range to perform mapping
```bash
python3 network.py -n ['IP Address Range']
```
![network_scan_1st_feature](https://user-images.githubusercontent.com/47297909/94921527-7af5f400-0486-11eb-999e-5e0db8a0e7a2.png)

### To Change the MAC Address
Specify the interface to change MAC
```bash
python3 network.py -i ['interface_name'] -m ['New MAC Address']
```
![mac_change_2nd_feature](https://user-images.githubusercontent.com/47297909/94921511-73364f80-0486-11eb-8eac-991b68afe0eb.png)

### Port Scanning   
Here you can secify the range of Port to scan 
```bash
python3 network.py -s ['Host_name'] -a ['Start Port'] -z ['End Port']
```
![port_scan_3rd_feature](https://user-images.githubusercontent.com/47297909/94921538-81846b80-0486-11eb-80a5-5ebbacc5b754.png)
