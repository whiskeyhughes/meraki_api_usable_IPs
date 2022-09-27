## Name
Meraki Usable IP Address Report! 

## Description
This is a script I created that helps pull WAN IP Addresses and Subnet Masks from the Meraki API, and then converts the results into usable IP Addresses. (For us we wanted to add all of our IP Addresses to Shodan to scan for vulnerabilites, and you couldn't add IP Ranges or Masks) 

## Badges

![Python](https://img.shields.io/badge/Python-%F0%9F%90%8D-brightgreen)
![Pandas](https://img.shields.io/badge/Pandas-%F0%9F%90%BC-brightgreen)


## Instructions
To get Meraki API Key: 

Step 1	
Log into the Meraki dashboard.

Step 2	
In the navigation panel click Organization > Settings.

Step 3	
Under Dashboard API Access, check Enable access to the Cisco Meraki Dashboard API. Without this option, you cannot generate API keys to onboard MX devices to CDO.

Step 4	
Click Save changes.

Step 5	
On the Meraki dashboard, click on your username in the upper right corner of the screen and then click My Profile.

Step 6	
Locate the API access header and click Generate new API key. Copy this API key. We recommend temporarily pasting it into a note until you are ready to use it. If you close the copy source before you paste the API key, you lose the copied API key.

Note
You only need one API key per template. You can re-onboard a template without generating a new key.

Once you have your API Key, add it to the script and then run "Meraki_Import.py". Once this finishes, run "IP_Conversion.py".

You should have the following files created: 
'meraki_ip_list_cidr.csv' & 'meraki_ip_list_usable.csv'

## Contributing
If you can help make this project better, help would be much appreciated! 

## Authors and acknowledgment
Joshua Hughes


