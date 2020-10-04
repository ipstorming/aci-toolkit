# ACI-Toolkit
An interactive python-based menu with the most common ACI actions. Save time using the CLI instead of the GUI.

The menu includes the most common actions on the daily ACI operations such as:

#### 1. Ports with particular VLAN: 
Displays the current encapsulation VLANs for a particular fabric port. 
#### 2. Ports connected to server: 
Identifies to which fabric ports a server is connected to. 
#### 3. EPGs in port: 
Displays the static path assignment for a particular fabric port. 
#### 4. VLANs per server: 
For a concrete endpoint, displays the list of encapsulation vlans allowed. 
#### 5. Fabric ports status per server: 
For a concrete endpoint, lists the status of the fabric ports, including VPC/PC. 
#### 6. Server commissioning: 
Creates the required access policies + EPGs association from an excel file. 
#### 7. Server decommissioning: 
Removes the access policy and EPG static assignment objects for a server. 
#### 8. New tenant: 
Taking an excel as an input, creates a new tenant with a dedicated VRF and dedicated L3Out. An external VRF is also
added on the Cisco Cat6500 using SVIs for the tenant. 

## Laboratory setup

The laboratory encompasses the following devices:
* Physical ACI fabric with 1 x APIC, 1 x Spine and 2 x leafs.
* Physical Cisco Cat6509.
* 4 x HP G7 servers runnning VMware hypervisor.

## Requirements

This project leverages the following technologies:
* "moquery" tool built-in the APIC.
* "Cobra" SDK for APIC version 5.0.2
*  Ansible v2.9.11
*  Jinja2. 
*  NAPALM.

## Installation

### Install the script

1. Clone the Github repository
git clone https://github.com/ipstorming/aci-toolkit

### Add the Cobra SDK 
2. Create an "include" folder and download the SDK from the APIC.

## Using the script
In progress...

 
