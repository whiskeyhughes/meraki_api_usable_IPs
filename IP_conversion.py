import pandas as pd
import ipcalc

def global_Variables_To_Call ():
    global  meraki_ip_import
    meraki_ip_import = pd.read_csv('meraki_ip_list.csv', header=None).set_index(0).to_dict('index')
    global meraki_mask_import 
    meraki_mask_import = pd.read_csv('meraki_mask_list.csv', header=None).set_index(0).to_dict('index')
    global meraki_ip_list
    meraki_ip_list = []
    global meraki_mask_list
    meraki_mask_list = []
    global list_network_with_cidr
    list_network_with_cidr = [] 
    global full_ip_list
    full_ip_list = []

def create_Master_Ip_List_With_Network_Ip_And_Cidr ():
    for idx,value in meraki_ip_import.items():
        for idx_nested,ip_address in value.items():
            if str(ip_address) != "nan" and str(ip_address) != 'staticIp':
                meraki_ip_list.append(ip_address)

    for idx,value in meraki_mask_import.items():
        for idx_nested,subnet_mask in value.items():
            if str(subnet_mask) != "nan" and str(subnet_mask) != 'staticSubnetMask':
                meraki_mask_list.append(subnet_mask)

    for idx in range(len(meraki_ip_list)):
        addr = ipcalc.IP(meraki_ip_list[idx], mask=meraki_mask_list[idx])
        network_with_cidr = str(addr.guess_network())
        list_network_with_cidr.append(network_with_cidr)

def convert_Network_Cidr_Addresses_To_Usable_Ips ():
    for idx in range(len(list_network_with_cidr)):
        ip = ipcalc.Network(list_network_with_cidr[idx])
        for addr in ip:
            full_ip_list.append(addr)
    print(full_ip_list)
    master_cidr = pd.DataFrame.from_dict(list_network_with_cidr)
    master_usable = pd.DataFrame.from_dict(full_ip_list)
    master_cidr.to_csv('meraki_ip_list_cidr.csv')
    master_usable.to_csv('meraki_ip_list_usable.csv')

global_Variables_To_Call ()
create_Master_Ip_List_With_Network_Ip_And_Cidr ()
convert_Network_Cidr_Addresses_To_Usable_Ips ()