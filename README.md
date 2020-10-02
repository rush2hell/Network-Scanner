# Network-Scanner
Basic network scanner with 3 main functionality 
1. Provide list of connected device
2. Changing MAC Address
3. Port Scanning

## Run 
```bash
python3 network.py
```
## Usage
### To check the Device connected 
Specify the IP Address range to perform mapping
```bash
python3 network.py -n ['IP Address Range']
```
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

### To Change the MAC Address
Specify the interface to change MAC
```bash
python3 network.py -i ['interface_name'] -m ['New MAC Address']
```
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

### Port Scanning   
Here you can secify the range of Port to scan 
```bash
python3 network.py -s ['Host_name'] -a ['Start Port'] -z ['End Port']
```
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)
