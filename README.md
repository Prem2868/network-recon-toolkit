# Network Reconnaissance Toolkit

## About
This repository hosts a professional network reconnaissance toolkit designed for ethical security testing and in-depth network analysis. It provides a suite of tools and scripts to discover network assets, identify open ports, enumerate services, and gather crucial information for security assessments and penetration testing.

## Features
- **Host Discovery**: Efficiently identify active hosts within a specified network range.
- **Port Scanning**: Conduct comprehensive scans to detect open ports and associated services.
- **Service Version Detection**: Accurately determine the versions of running services for vulnerability assessment.
- **OS Fingerprinting**: Attempt to identify the operating system of target hosts.
- **Modular Design**: Easily extendable architecture to integrate new reconnaissance modules.
- **Reporting**: Generate structured output for further analysis and documentation.

## Installation

```bash
git clone https://github.com/Prem2868/network-recon-toolkit.git
cd network-recon-toolkit
pip install -r requirements.txt
```

## Usage

```bash
python main.py --help
python main.py --target 192.168.1.0/24 --ports 1-1024
```

## Tech Stack
- Python 3.x
- Scapy
- Nmap (via python-nmap library)
- Click (for CLI)

## License
This project is licensed under the MIT License - see the LICENSE file for details.
