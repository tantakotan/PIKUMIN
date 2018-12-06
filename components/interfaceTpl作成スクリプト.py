


#
#
#
# for x in range(1,49):
#     print(
#         "interface {{FastEthernet0_",x,"}}\n"
#         " description ### To {{if_description1_Fa0_",x,"}} {{if_description2_Fa0_",x,"}} ###\n"
#         " {% if if_vlan_mode_Fa0_",x," == 'access' %}\n"
#         " switchport mode access\n"
#         " switchport access vlan {{if_vlan_access_Fa0_",x,"}}\n"
#         " {% elif if_vlan_mode_Fa0_",x," == 'trunk' %}\n"
#         " swichport mode trunk\n"
#         " switchport trunk native vlan {{if_vlan_native_Fa0_",x,"}}\n"
#         " switchport trunk allowed vlan {{if_vlan_trunk_Fa0_",x,"}}\n"
#         " {% endif %}\n"
#         " switchport nonegotiate\n"
#         " priority-queue out\n"
#         " mls qos trust dscp\n"
#         "!"
#         , sep = ""
#     )
#


for x in range(1,5):
    print(
        "interface {{GigaEthernet0_",x,"}}\n"
        " description ### To {{if_description1_Gi0_",x,"}} {{if_description2_Gi0_",x,"}} ###\n"
        " {% if if_vlan_mode_Gi0_",x," == 'access' %}\n"
        " switchport mode access\n"
        " switchport access vlan {{if_vlan_access_Gi0_",x,"}}\n"
        " {% elif if_vlan_mode_Gi0_",x," == 'trunk' %}\n"
        " swichport mode trunk\n"
        " switchport trunk native vlan {{if_vlan_native_Gi0_",x,"}}\n"
        " switchport trunk allowed vlan {{if_vlan_trunk_Gi0_",x,"}}\n"
        " {% endif %}\n"
        " switchport nonegotiate\n"
        " priority-queue out\n"
        " mls qos trust dscp\n"
        "!"
        , sep = ""
    )



# ifDhGi0_1 -> if_description1_Gi0_
# ifDpGi0_1 -> if_description2_Gi0_
# ifVlmGi0_1 -> if_vlan_mode_Gi0_
# ifVlaGi0_1 -> if_vlan_access_Gi0_
# ifVlnGi0_1 -> if_vlan_native_Gi0_
# ifVltGi0_1 -> if_vlan_trunk_Gi0_

# for x in range(1,49):
#     print(
#         "GigabitEthernet0_",x,"\n"
#         "if_description1_Gi0_",x,"\n"
#         "if_description2_Gi0_",x,"\n"
#         "if_vlan_mode_Gi0_",x,"\n"
#         "if_vlan_access_Gi0_",x,"\n"
#         "if_vlan_native_Gi0_",x,"\n"
#         "if_vlan_trunk_Gi0_",x,"\n"
#         "!", sep = ""
#     )


for x in range(1,11):
    print(
        "{% if vlan_id_",x," %}\n"
        "vlan {{vlan_id_",x,"}}\n"
        " name {{vlan_name_",x,"}}\n"
        "{% endif %}\n"
        "!"
        , sep = ""
    )

