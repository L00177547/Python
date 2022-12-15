"""
Script: main.py
By:Richard Vaughan
Purpose: Test code to call classes and methods from devices.py
Prerequisites: None.
Tested: On python 3.10 on Windows 11.
Revision history:
Alpha Version: 08OCT22
Notes:
"""

from devices import Firewall, Switch, LoadBalancer

# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")
# Create a switch instance
switch1 = Switch("switch1")
# Configure it
switch1.configure_switch()
# Create a switch instance
switch2 = Switch("switch2")
# Verify a CRC
switch2.calculate_crc("dummy data")
# Create a load balancer instance
lb_1 = LoadBalancer("loadbalancer1")
# Configure it
lb_1.configure_loadbalancer()
# Create a switch instance
lb_2 = LoadBalancer("loadbalancer2")
# Verify a CRC
lb_2.calculate_crc("dummy data")
