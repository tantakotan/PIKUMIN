version 15.2
no service pad
service tcp-keepalives-in
service tcp-keepalives-out
service timestamps debug datetime msec localtime show-timezone year
service timestamps log datetime msec localtime show-timezone year
service password-encryption
service sequence-numbers
no service dhcp
!
hostname {{hostname}}
!
boot-start-marker
boot-end-marker
!
logging buffered 4096000 informational
enable secret hogehogehoge
!
username hoge secret hogehogehoge
no aaa new-model
clock timezone jst 9 0
system mtu routing 1500
vtp mode transparent
!
!
!
!
!
no ip source-route
ip arp proxy disable
!
!
no ip domain-lookup
login on-failure log
login on-success log
!
mls qos
!
!
!
spanning-tree mode rapid-pvst
spanning-tree portfast default
spanning-tree portfast bpduguard default
spanning-tree extend system-id
!
vlan internal allocation policy ascending
!
{% if vlan_id_1 %}
vlan {{vlan_id_1}}
 name {{vlan_name_1}}
{% endif %}
!
{% if vlan_id_2 %}
vlan {{vlan_id_2}}
 name {{vlan_name_2}}
{% endif %}
!
{% if vlan_id_3 %}
vlan {{vlan_id_3}}
 name {{vlan_name_3}}
{% endif %}
!
{% if vlan_id_4 %}
vlan {{vlan_id_4}}
 name {{vlan_name_4}}
{% endif %}
!
{% if vlan_id_5 %}
vlan {{vlan_id_5}}
 name {{vlan_name_5}}
{% endif %}
!
{% if vlan_id_6 %}
vlan {{vlan_id_6}}
 name {{vlan_name_6}}
{% endif %}
!
{% if vlan_id_7 %}
vlan {{vlan_id_7}}
 name {{vlan_name_7}}
{% endif %}
!
{% if vlan_id_8 %}
vlan {{vlan_id_8}}
 name {{vlan_name_8}}
{% endif %}
!
{% if vlan_id_9 %}
vlan {{vlan_id_9}}
 name {{vlan_name_9}}
{% endif %}
!
{% if vlan_id_10 %}
vlan {{vlan_id_10}}
 name {{vlan_name_10}}
{% endif %}
!
!
class-map match-all Class_hugahuga
 match access-group name hugahuga
class-map match-all Class_ef
 match ip dscp ef 
class-map match-all Class_cs5
 match ip dscp cs5 
!
policy-map Marking
 class Class_hugahuga
  set dscp cs5
 class Class_ef
  set dscp cs5
 class Class_cs5
  set dscp cs5
 class class-default
  set dscp default
!
!
!
!
!
!
interface {{FastEthernet0_1}}
 description ### To {{if_description1_Fa0_1}} {{if_description2_Fa0_1}} ###
 {% if if_vlan_mode_Fa0_1 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_1}}
 {% elif if_vlan_mode_Fa0_1 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_1}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_1}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_2}}
 description ### To {{if_description1_Fa0_2}} {{if_description2_Fa0_2}} ###
 {% if if_vlan_mode_Fa0_2 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_2}}
 {% elif if_vlan_mode_Fa0_2 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_2}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_2}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_3}}
 description ### To {{if_description1_Fa0_3}} {{if_description2_Fa0_3}} ###
 {% if if_vlan_mode_Fa0_3 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_3}}
 {% elif if_vlan_mode_Fa0_3 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_3}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_3}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_4}}
 description ### To {{if_description1_Fa0_4}} {{if_description2_Fa0_4}} ###
 {% if if_vlan_mode_Fa0_4 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_4}}
 {% elif if_vlan_mode_Fa0_4 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_4}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_4}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_5}}
 description ### To {{if_description1_Fa0_5}} {{if_description2_Fa0_5}} ###
 {% if if_vlan_mode_Fa0_5 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_5}}
 {% elif if_vlan_mode_Fa0_5 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_5}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_5}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_6}}
 description ### To {{if_description1_Fa0_6}} {{if_description2_Fa0_6}} ###
 {% if if_vlan_mode_Fa0_6 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_6}}
 {% elif if_vlan_mode_Fa0_6 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_6}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_6}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_7}}
 description ### To {{if_description1_Fa0_7}} {{if_description2_Fa0_7}} ###
 {% if if_vlan_mode_Fa0_7 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_7}}
 {% elif if_vlan_mode_Fa0_7 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_7}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_7}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_8}}
 description ### To {{if_description1_Fa0_8}} {{if_description2_Fa0_8}} ###
 {% if if_vlan_mode_Fa0_8 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_8}}
 {% elif if_vlan_mode_Fa0_8 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_8}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_8}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_9}}
 description ### To {{if_description1_Fa0_9}} {{if_description2_Fa0_9}} ###
 {% if if_vlan_mode_Fa0_9 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_9}}
 {% elif if_vlan_mode_Fa0_9 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_9}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_9}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_10}}
 description ### To {{if_description1_Fa0_10}} {{if_description2_Fa0_10}} ###
 {% if if_vlan_mode_Fa0_10 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_10}}
 {% elif if_vlan_mode_Fa0_10 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_10}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_10}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_11}}
 description ### To {{if_description1_Fa0_11}} {{if_description2_Fa0_11}} ###
 {% if if_vlan_mode_Fa0_11 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_11}}
 {% elif if_vlan_mode_Fa0_11 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_11}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_11}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_12}}
 description ### To {{if_description1_Fa0_12}} {{if_description2_Fa0_12}} ###
 {% if if_vlan_mode_Fa0_12 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_12}}
 {% elif if_vlan_mode_Fa0_12 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_12}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_12}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_13}}
 description ### To {{if_description1_Fa0_13}} {{if_description2_Fa0_13}} ###
 {% if if_vlan_mode_Fa0_13 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_13}}
 {% elif if_vlan_mode_Fa0_13 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_13}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_13}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_14}}
 description ### To {{if_description1_Fa0_14}} {{if_description2_Fa0_14}} ###
 {% if if_vlan_mode_Fa0_14 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_14}}
 {% elif if_vlan_mode_Fa0_14 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_14}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_14}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_15}}
 description ### To {{if_description1_Fa0_15}} {{if_description2_Fa0_15}} ###
 {% if if_vlan_mode_Fa0_15 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_15}}
 {% elif if_vlan_mode_Fa0_15 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_15}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_15}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_16}}
 description ### To {{if_description1_Fa0_16}} {{if_description2_Fa0_16}} ###
 {% if if_vlan_mode_Fa0_16 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_16}}
 {% elif if_vlan_mode_Fa0_16 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_16}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_16}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_17}}
 description ### To {{if_description1_Fa0_17}} {{if_description2_Fa0_17}} ###
 {% if if_vlan_mode_Fa0_17 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_17}}
 {% elif if_vlan_mode_Fa0_17 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_17}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_17}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_18}}
 description ### To {{if_description1_Fa0_18}} {{if_description2_Fa0_18}} ###
 {% if if_vlan_mode_Fa0_18 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_18}}
 {% elif if_vlan_mode_Fa0_18 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_18}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_18}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_19}}
 description ### To {{if_description1_Fa0_19}} {{if_description2_Fa0_19}} ###
 {% if if_vlan_mode_Fa0_19 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_19}}
 {% elif if_vlan_mode_Fa0_19 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_19}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_19}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_20}}
 description ### To {{if_description1_Fa0_20}} {{if_description2_Fa0_20}} ###
 {% if if_vlan_mode_Fa0_20 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_20}}
 {% elif if_vlan_mode_Fa0_20 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_20}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_20}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_21}}
 description ### To {{if_description1_Fa0_21}} {{if_description2_Fa0_21}} ###
 {% if if_vlan_mode_Fa0_21 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_21}}
 {% elif if_vlan_mode_Fa0_21 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_21}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_21}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_22}}
 description ### To {{if_description1_Fa0_22}} {{if_description2_Fa0_22}} ###
 {% if if_vlan_mode_Fa0_22 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_22}}
 {% elif if_vlan_mode_Fa0_22 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_22}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_22}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_23}}
 description ### To {{if_description1_Fa0_23}} {{if_description2_Fa0_23}} ###
 {% if if_vlan_mode_Fa0_23 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_23}}
 {% elif if_vlan_mode_Fa0_23 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_23}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_23}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_24}}
 description ### To {{if_description1_Fa0_24}} {{if_description2_Fa0_24}} ###
 {% if if_vlan_mode_Fa0_24 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_24}}
 {% elif if_vlan_mode_Fa0_24 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_24}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_24}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_25}}
 description ### To {{if_description1_Fa0_25}} {{if_description2_Fa0_25}} ###
 {% if if_vlan_mode_Fa0_25 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_25}}
 {% elif if_vlan_mode_Fa0_25 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_25}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_25}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_26}}
 description ### To {{if_description1_Fa0_26}} {{if_description2_Fa0_26}} ###
 {% if if_vlan_mode_Fa0_26 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_26}}
 {% elif if_vlan_mode_Fa0_26 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_26}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_26}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_27}}
 description ### To {{if_description1_Fa0_27}} {{if_description2_Fa0_27}} ###
 {% if if_vlan_mode_Fa0_27 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_27}}
 {% elif if_vlan_mode_Fa0_27 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_27}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_27}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_28}}
 description ### To {{if_description1_Fa0_28}} {{if_description2_Fa0_28}} ###
 {% if if_vlan_mode_Fa0_28 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_28}}
 {% elif if_vlan_mode_Fa0_28 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_28}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_28}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_29}}
 description ### To {{if_description1_Fa0_29}} {{if_description2_Fa0_29}} ###
 {% if if_vlan_mode_Fa0_29 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_29}}
 {% elif if_vlan_mode_Fa0_29 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_29}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_29}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_30}}
 description ### To {{if_description1_Fa0_30}} {{if_description2_Fa0_30}} ###
 {% if if_vlan_mode_Fa0_30 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_30}}
 {% elif if_vlan_mode_Fa0_30 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_30}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_30}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_31}}
 description ### To {{if_description1_Fa0_31}} {{if_description2_Fa0_31}} ###
 {% if if_vlan_mode_Fa0_31 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_31}}
 {% elif if_vlan_mode_Fa0_31 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_31}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_31}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_32}}
 description ### To {{if_description1_Fa0_32}} {{if_description2_Fa0_32}} ###
 {% if if_vlan_mode_Fa0_32 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_32}}
 {% elif if_vlan_mode_Fa0_32 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_32}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_32}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_33}}
 description ### To {{if_description1_Fa0_33}} {{if_description2_Fa0_33}} ###
 {% if if_vlan_mode_Fa0_33 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_33}}
 {% elif if_vlan_mode_Fa0_33 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_33}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_33}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_34}}
 description ### To {{if_description1_Fa0_34}} {{if_description2_Fa0_34}} ###
 {% if if_vlan_mode_Fa0_34 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_34}}
 {% elif if_vlan_mode_Fa0_34 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_34}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_34}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_35}}
 description ### To {{if_description1_Fa0_35}} {{if_description2_Fa0_35}} ###
 {% if if_vlan_mode_Fa0_35 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_35}}
 {% elif if_vlan_mode_Fa0_35 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_35}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_35}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_36}}
 description ### To {{if_description1_Fa0_36}} {{if_description2_Fa0_36}} ###
 {% if if_vlan_mode_Fa0_36 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_36}}
 {% elif if_vlan_mode_Fa0_36 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_36}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_36}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_37}}
 description ### To {{if_description1_Fa0_37}} {{if_description2_Fa0_37}} ###
 {% if if_vlan_mode_Fa0_37 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_37}}
 {% elif if_vlan_mode_Fa0_37 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_37}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_37}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_38}}
 description ### To {{if_description1_Fa0_38}} {{if_description2_Fa0_38}} ###
 {% if if_vlan_mode_Fa0_38 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_38}}
 {% elif if_vlan_mode_Fa0_38 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_38}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_38}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_39}}
 description ### To {{if_description1_Fa0_39}} {{if_description2_Fa0_39}} ###
 {% if if_vlan_mode_Fa0_39 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_39}}
 {% elif if_vlan_mode_Fa0_39 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_39}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_39}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_40}}
 description ### To {{if_description1_Fa0_40}} {{if_description2_Fa0_40}} ###
 {% if if_vlan_mode_Fa0_40 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_40}}
 {% elif if_vlan_mode_Fa0_40 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_40}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_40}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_41}}
 description ### To {{if_description1_Fa0_41}} {{if_description2_Fa0_41}} ###
 {% if if_vlan_mode_Fa0_41 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_41}}
 {% elif if_vlan_mode_Fa0_41 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_41}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_41}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_42}}
 description ### To {{if_description1_Fa0_42}} {{if_description2_Fa0_42}} ###
 {% if if_vlan_mode_Fa0_42 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_42}}
 {% elif if_vlan_mode_Fa0_42 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_42}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_42}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_43}}
 description ### To {{if_description1_Fa0_43}} {{if_description2_Fa0_43}} ###
 {% if if_vlan_mode_Fa0_43 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_43}}
 {% elif if_vlan_mode_Fa0_43 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_43}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_43}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_44}}
 description ### To {{if_description1_Fa0_44}} {{if_description2_Fa0_44}} ###
 {% if if_vlan_mode_Fa0_44 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_44}}
 {% elif if_vlan_mode_Fa0_44 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_44}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_44}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_45}}
 description ### To {{if_description1_Fa0_45}} {{if_description2_Fa0_45}} ###
 {% if if_vlan_mode_Fa0_45 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_45}}
 {% elif if_vlan_mode_Fa0_45 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_45}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_45}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_46}}
 description ### To {{if_description1_Fa0_46}} {{if_description2_Fa0_46}} ###
 {% if if_vlan_mode_Fa0_46 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_46}}
 {% elif if_vlan_mode_Fa0_46 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_46}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_46}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_47}}
 description ### To {{if_description1_Fa0_47}} {{if_description2_Fa0_47}} ###
 {% if if_vlan_mode_Fa0_47 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_47}}
 {% elif if_vlan_mode_Fa0_47 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_47}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_47}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{FastEthernet0_48}}
 description ### To {{if_description1_Fa0_48}} {{if_description2_Fa0_48}} ###
 {% if if_vlan_mode_Fa0_48 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Fa0_48}}
 {% elif if_vlan_mode_Fa0_48 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Fa0_48}}
 switchport trunk allowed vlan {{if_vlan_trunk_Fa0_48}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{GigaEthernet0_1}}
 description ### To {{if_description1_Gi0_1}} {{if_description2_Gi0_1}} ###
 {% if if_vlan_mode_Gi0_1 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Gi0_1}}
 {% elif if_vlan_mode_Gi0_1 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Gi0_1}}
 switchport trunk allowed vlan {{if_vlan_trunk_Gi0_1}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{GigaEthernet0_2}}
 description ### To {{if_description1_Gi0_2}} {{if_description2_Gi0_2}} ###
 {% if if_vlan_mode_Gi0_2 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Gi0_2}}
 {% elif if_vlan_mode_Gi0_2 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Gi0_2}}
 switchport trunk allowed vlan {{if_vlan_trunk_Gi0_2}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{GigaEthernet0_3}}
 description ### To {{if_description1_Gi0_3}} {{if_description2_Gi0_3}} ###
 {% if if_vlan_mode_Gi0_3 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Gi0_3}}
 {% elif if_vlan_mode_Gi0_3 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Gi0_3}}
 switchport trunk allowed vlan {{if_vlan_trunk_Gi0_3}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
interface {{GigaEthernet0_4}}
 description ### To {{if_description1_Gi0_4}} {{if_description2_Gi0_4}} ###
 {% if if_vlan_mode_Gi0_4 == 'access' %}
 switchport mode access
 switchport access vlan {{if_vlan_access_Gi0_4}}
 {% elif if_vlan_mode_Gi0_4 == 'trunk' %}
 swichport mode trunk
 switchport trunk native vlan {{if_vlan_native_Gi0_4}}
 switchport trunk allowed vlan {{if_vlan_trunk_Gi0_4}}
 {% endif %}
 switchport nonegotiate
 priority-queue out
 mls qos trust dscp
!
{% if Vl1 %}
interface {Vl1}
 {% if if_ipaddr_Vl1 %}
 description ### {{if_description1_Vl1}} {{if_description2_Vl1}} ###
 ip address {{if_ipaddr_Vl1}} {{if_ipmask_Vl1}}
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 {% else %}
 description ### Unused ###
 shutdown
 {% endif %}
{% endif %}
!
{% if Vl2 %}
interface {Vl2}
 {% if if_ipaddr_Vl2 %}
 description ### {{if_description1_Vl2}} {{if_description2_Vl2}} ###
 ip address {{if_ipaddr_Vl2}} {{if_ipmask_Vl2}}
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 {% else %}
 description ### Unused ###
 shutdown
 {% endif %}
{% endif %}
!
{% if Vl3 %}
interface {Vl3}
 {% if if_ipaddr_Vl3 %}
 description ### {{if_description1_Vl3}} {{if_description2_Vl3}} ###
 ip address {{if_ipaddr_Vl3}} {{if_ipmask_Vl3}}
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 {% else %}
 description ### Unused ###
 shutdown
 {% endif %}
{% endif %}
!
ip default-gateway {{default_gateway}}
no ip http server
no ip http secure-server
!
ip access-list standard Remote_Login
 permit any
 permit 172.21.10.0 0.0.0.255
!
ip access-list extended hugahuga
 remark hugahuga_SIP&TLIB
 permit ip any host 10.224.50.187
snmp-server community public RO
snmp-server trap-source Vlan90
snmp-server queue-length 200
snmp-server location UNKO
snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart
snmp-server enable traps transceiver all
snmp-server enable traps call-home message-send-fail server-fail
snmp-server enable traps tty
snmp-server enable traps cluster
snmp-server enable traps entity
snmp-server enable traps cpu threshold
snmp-server enable traps vtp
snmp-server enable traps vlancreate
snmp-server enable traps vlandelete
snmp-server enable traps flash insertion removal
snmp-server enable traps port-security
snmp-server enable traps auth-framework sec-violation
snmp-server enable traps envmon fan shutdown supply temperature status
snmp-server enable traps energywise
snmp-server enable traps power-ethernet group 1
snmp-server enable traps power-ethernet police
snmp-server enable traps fru-ctrl
snmp-server enable traps event-manager
snmp-server enable traps trustsec-sxp conn-srcaddr-err msg-parse-err conn-config-err binding-err conn-up conn-down binding-expn-fail oper-nodeid-change binding-conflict
snmp-server enable traps config-copy
snmp-server enable traps config
snmp-server enable traps config-ctid
snmp-server enable traps vstack
snmp-server enable traps bridge newroot topologychange
snmp-server enable traps stpx inconsistency root-inconsistency loop-inconsistency
snmp-server enable traps syslog
snmp-server enable traps mac-notification change move threshold
snmp-server enable traps vlan-membership
snmp-server enable traps errdisable
snmp-server enable traps bulkstat collection transfer
snmp-server host 172.21.10.253 version 2c msp
snmp ifmib ifindex persist
!
banner exec ^C
*********************************************
**   1. Date      :    2017/9/29           **
**   2. Host Name :    {{hostname}}        **
**   3. Type      :    {{devicename}}    **
**   4. Version   :    15.2(2)E6           **
**   5. Location  :    UNKO                **
*********************************************
^C
!
line con 0
 exec-timeout 15 0
 logging synchronous
 login local
 exec prompt timestamp
line vty 0 4
 access-class Remote_Login in
 exec-timeout 15 0
 logging synchronous
 login local
 exec prompt timestamp
 transport input all
 transport output all
line vty 5 15
 access-class Remote_Login in
 exec-timeout 15 0
 logging synchronous
 login local
 exec prompt timestamp
 transport input all
 transport output all
!
!
monitor session 1 destination interface Fa0/48
ntp source Vlan90
ntp server 10.127.245.1
ntp server 10.127.245.9 prefer
end
