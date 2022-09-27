import meraki
import pandas as pd

def global_Variables_To_Call ():
    global api_key
    api_key = "INSERT YOUR MERAKI API KEY"
    global meraki_dashboard
    meraki_dashboard = meraki.DashboardAPI(api_key)
    global meraki_orgs
    meraki_orgs = meraki_dashboard.organizations.getOrganizations()
    global big_dict_energy
    big_dict_energy = []
   


def pull_Meraki_Ip_Addresses_Through_Api ():

    for org in meraki_orgs:
        if org["name"] == "INSERT ORG YOU WANT TO SKIP IF APPLICABLE":
            pass
        else:
            gather_device_info = meraki_dashboard.appliance.getOrganizationApplianceUplinkStatuses(org['id'])
            for device in gather_device_info:
                device_mgmt_stats = meraki_dashboard.devices.getDeviceManagementInterface(device['serial'])
                for key, value in device_mgmt_stats.items():
                    big_dict_energy.append(value)

def convert_Meraki_Dict_To_Csv ():
    master_df = pd.DataFrame.from_dict(big_dict_energy)
    master_csv_mask = master_df.drop(columns=['wanEnabled', 'usingStaticIp', 'staticIp', 'staticGatewayIp', 'staticDns', 'vlan', 'activeDdnsHostname', 'ddnsHostnameWan1', 'ddnsHostnameWan2'])
    master_csv_mask = master_csv_mask.replace(['255.255.255.0', '255.255.254.0', '255.255.252.0', '255.255.248.0', '255.255.240.0', '255.255.224.0'], '255.255.255.255')
    master_csv_ip = master_df.drop(columns=['wanEnabled', 'usingStaticIp', 'staticSubnetMask', 'staticGatewayIp', 'staticDns', 'vlan', 'activeDdnsHostname', 'ddnsHostnameWan1', 'ddnsHostnameWan2'])
    master_csv_mask.to_csv('meraki_mask_list.csv')
    master_csv_ip.to_csv('meraki_ip_list.csv')

global_Variables_To_Call()
pull_Meraki_Ip_Addresses_Through_Api()
convert_Meraki_Dict_To_Csv()
