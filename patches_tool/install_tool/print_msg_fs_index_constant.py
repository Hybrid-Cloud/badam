#!/usr/bin/env python
#-*-coding:utf-8-*-
import logging

class fsLanguageIndexConstant(object):

    LANGUAGE_CN = "CN"
    LANGUAGE_EN = "EN"

    languageMap = \
    {"1000000":{LANGUAGE_EN : "-------------------------------------------------------------------------------------",
                 LANGUAGE_CN : "-------------------------------------------------------------------------------------"},
     "1000001":{LANGUAGE_EN: "Please input your choice %s", LANGUAGE_CN :"请输入您的选择 %s"},
     "1000002":{LANGUAGE_EN: "Please input correct info !", LANGUAGE_CN :"请输入正确的信息！"},
     "1000003":{LANGUAGE_EN: "-------------------System and services logical volume configuration-------------------",
                 LANGUAGE_CN: "-------------------系统与服务逻辑卷空间配置项-------------------------------------------"},
     "1000004":{LANGUAGE_EN : "Please set store size for software repository, GB is the unit [%s] :",
                 LANGUAGE_CN : "请设置软件仓库的大小，以GB为单位 [%s] : "},
     "1000005":{LANGUAGE_EN : "Please set correct number,only support int!",
                 LANGUAGE_CN : "请输入正确的数值，当前只支持int型！"},
     "1000006":{LANGUAGE_EN : "-------------Disk configuration begin -----------------------------------------------",
                 LANGUAGE_CN : "-------------开始配置磁盘信息 --------------------------------------------------------"},
     "1000007":{LANGUAGE_EN : "[s] Save&quit ",
                 LANGUAGE_CN : "[s] 保存并退出 "},
     "1000008":{LANGUAGE_EN : "[1] Set services needed logical volume ",
                 LANGUAGE_CN : "[1] 设置服务的逻辑卷大小 "},
     "1000009":{LANGUAGE_EN : "[2] Extend more disk for services ",
                 LANGUAGE_CN : "[2] 扩展磁盘信息 "},
     "1000010":{LANGUAGE_EN : "-------------Disk configuration end -------------------------------------------------",
                 LANGUAGE_CN : "-------------磁盘配置结束 ------------------------------------------------------------"},
     "1000011":{LANGUAGE_EN : "Please set cache size for nova compute to store local image, GB is the unit [%s] : ",
                 LANGUAGE_CN : "请设置nova compute 的image逻辑卷大小，用于存放虚拟机镜像，以GB为单位 [%s] : "},
     "1000012":{LANGUAGE_EN : "Please set logic volume size for ceilometer mongo db, GB is the unit [%s] : ",
                 LANGUAGE_CN : "请设置 mongo db的逻辑卷大小，以GB为单位 [%s] : "},
     "1000013":{LANGUAGE_EN : "Please set store size for glance to store image file, GB is the unit [%s] : ",
                 LANGUAGE_CN : "请设置 glance 的逻辑卷的大小，以GB为单位 [%s] : "},
     "1000014":{LANGUAGE_EN : "Please set default backend store for glance [file|swift|uds+https][%s] : ",
                 LANGUAGE_CN : "请设置 glance 的后端存储方式 [file|swift|uds+https][%s] : "},
     "1000015":{LANGUAGE_EN : "Still not support swift backend store.",
                 LANGUAGE_CN : "当前暂未支持 swift的后端存储。"},
     "1000016":{LANGUAGE_EN : "Please input correct character,only support file or swift or uds+https!",
                 LANGUAGE_CN : "请输入正确的存储方式。"},
     "1000017":{LANGUAGE_EN : "-------------------System  logical volume configuration end.-------------------------",
                 LANGUAGE_CN : "-------------------逻辑卷相关设置结束。-----------------------------------------------"},
     "1000018":{LANGUAGE_EN : "Please input which hostcfg you want to extend. Input 'enter' for ending. [hostcfg]:",
                 LANGUAGE_CN : "请输入想要扩展的组，如果输入为'',将结束配置 [hostcfg]:"},
     "1000019":{LANGUAGE_EN : "Begin to extend '%s' hostcfg disk.",
                 LANGUAGE_CN : "开始扩展‘%s’的磁盘信息。"},
     "1000020":{LANGUAGE_EN : "Now old '%s' hostcfg infomation is : ",
                 LANGUAGE_CN : "当前老的‘%s’配置信息是 ："},
     "1000021":{LANGUAGE_EN : "Do you want to add '%s' to '%s'?",
                 LANGUAGE_CN : u"是否将磁盘 '%s' 加入 '%s' 组中？"},
     "1000022":{LANGUAGE_EN : "Now new '%s' hostcfg information is : ",
                 LANGUAGE_CN : "当前新的‘%s’的配置信息是 ： "},
     "1000023":{LANGUAGE_EN : "-------------------Extend disk configuration-----------------------------------------",
                 LANGUAGE_CN : "-------------------扩展磁盘配置信息---------------------------------------------------"},
     "1000024":{LANGUAGE_EN : "Do you want to extend disk for 'control' host or 'compute' host?",
                 LANGUAGE_CN : "是否对部署‘control’或者 'compute' 角色的主机扩展磁盘?"},
     "1000025":{LANGUAGE_EN : "Configuration 'control' hostcfgs start-------------------------------------------------",
                 LANGUAGE_CN : "开始配置部署'control' 角色的主机磁盘信息-----------------------------------------------"},
     "1000026":{LANGUAGE_EN : "'control' hostcfgs are :",
                 LANGUAGE_CN : "'control' 组包含以下配置信息："},
     "1000027":{LANGUAGE_EN : "Configuration 'control' hostcfgs end---------------------------------------------------",
                 LANGUAGE_CN : "配置部署'control'角色组的磁盘配置信息结束。--------------------------------------------"},
     "1000028":{LANGUAGE_EN : "Configuration 'compute' hostcfgs start-------------------------------------------------",
                 LANGUAGE_CN : "开始配置'compute' 角色的主机磁盘信息---------------------------------------------------"},
     "1000029":{LANGUAGE_EN : "'compute' hostcfgs are :",
                 LANGUAGE_CN : "'compute' 配置包含以下信息："},
     "1000030":{LANGUAGE_EN : "Configuration 'compute' hostcfgs end---------------------------------------------------",
                 LANGUAGE_CN : "配置部署'compute'角色组的磁盘配置信息结束。--------------------------------------------"},
     "1000031":{LANGUAGE_EN : "-------------------Remove disk configuration-----------------------------------------",
                 LANGUAGE_CN : "-------------------删除磁盘的配置项---------------------------------------------------"},
     "1000032":{LANGUAGE_EN : "Do you want to remove disk for 'control' host or 'compute' host?",
                 LANGUAGE_CN : "是否对部署‘control’或者 'compute' 角色的主机减少部署的磁盘？"},
     "1000033":{LANGUAGE_EN : "Begin to romove '%s' hostcfg disk.",
                 LANGUAGE_CN : "开始减少 '%s' 组部署的磁盘配置信息。"},
     "1000034":{LANGUAGE_EN : "Please input which hostcfgname you want to remove. Input 'enter' for ending.[hostcfg]:",
                 LANGUAGE_CN : "请输入想要减少的配置名，如果输入为'',将结束配置。 [hostcfg]:"},
     "1000035":{LANGUAGE_EN : "Do you want to remove '%s' from '%s'?",
                 LANGUAGE_CN : u"是否将 '%s' 从 '%s'组中删除？"},
     "1000036":{LANGUAGE_EN : "Default file not exist.",
                 LANGUAGE_CN : "默认文件不存在。"},
     "1000037":{LANGUAGE_EN : "--------------Start extend or remove disk from host ---------------------------------",
                 LANGUAGE_CN : "--------------开始扩展或者删除磁盘的配置-----------------------------------------------"},
     "1000038":{LANGUAGE_EN : "Do you want to extend or remove disk from host?",
                 LANGUAGE_CN : "是否想要扩展或者删除磁盘配置？"},
     "1000039":{LANGUAGE_EN : "--------------Extend or remove disk from host end -----------------------------------",
                 LANGUAGE_CN : "--------------扩展或者删除磁盘配置信息结束 --------------------------------------------"},
     "1000040":{LANGUAGE_EN : "Please input your choice [y|n][n]:",
                 LANGUAGE_CN : "请输入你的选择 [y|n][n]:"},
     "1000041":{LANGUAGE_EN : "------Start to check commit result.%s",
                 LANGUAGE_CN : "------开始检查磁盘生效信息。%s"},
     "1000042":{LANGUAGE_EN : "Check commit result,but get host detailed info failed,host = %s.",
                 LANGUAGE_CN : ""},
     "1000043":{LANGUAGE_EN : "Host : %s still in progress !",
                 LANGUAGE_CN : u"主机 ：%s 还在执行中！"},
     "1000044":{LANGUAGE_EN : "Host : %s is commit ok!",
                 LANGUAGE_CN : u"主机 ：%s 已经执行成功！"},
     "1000045":{LANGUAGE_EN : "------All hosts commit for hostcfg are ok.",
                 LANGUAGE_CN : "------所有的数据提交成功。"},
     "1000046":{LANGUAGE_EN : "Do you want to cancel checking disk infomation?",
                 LANGUAGE_CN : "是否取消继续检查磁盘配置信息？"},
     "1000047":{LANGUAGE_EN : "[s] Save&quit",
                 LANGUAGE_CN : "[s] 保存并退出"},
     "1000048":{LANGUAGE_EN : "[1] Extend",
                 LANGUAGE_CN : "[1] 扩展"},
     "1000049":{LANGUAGE_EN : "[2] Remove",
                 LANGUAGE_CN : "[2] 删除"},
     "1000050":{LANGUAGE_EN : "Please choose section to config:",
                 LANGUAGE_CN : "请选择需要配置的选项:"},
     "1000051":{LANGUAGE_EN : "[2] Disk config",
                 LANGUAGE_CN : "[2] 磁盘配置"},
     "1000052":{LANGUAGE_EN : "[3] Stroage config",
                 LANGUAGE_CN : "[3] 存储配置"},
     "1000053":{LANGUAGE_EN : "Please set cache size for nova compute to store local image for control host, GB is the unit [%s] : ",
                 LANGUAGE_CN : "请设置nova compute控制节点image逻辑卷大小，用于存放虚拟机镜像，以GB为单位 [%s] : "},
     "1000054":{LANGUAGE_EN : "Please set cache size for nova compute to store local image for compute host, GB is the unit [%s] : ",
                 LANGUAGE_CN : "请设置nova compute计算节点image逻辑卷大小，用于存放虚拟机镜像，以GB为单位 [%s] : "},
     "1000055":{LANGUAGE_EN : "",
                 LANGUAGE_CN : ""},
     "1000056":{LANGUAGE_EN: "Please set cache size for backup service to store backup packages for control host, GB is the unit [%s] : ",
                LANGUAGE_CN: "请设置backup service控制节点backup逻辑卷大小，用于存放备份包，以GB为单位 [%s] : "},


     "1000101":{LANGUAGE_EN : "--------------Set storage configuration begin ---------------------------------------",
                 LANGUAGE_CN : "--------------开始设置存储相关配置项 -------------------------------------------------"},
     "1000102":{LANGUAGE_EN : "Please set default backend store for cinder [file|fusionstorage|ipsan|other][%s] : ",
                 LANGUAGE_CN : "请为 cinder 配置后台存储对接方式 [file|fusionstorage|ipsan|other][%s] : "},
     "1000103":{LANGUAGE_EN : "Please input OceanStor T series storage iSCSI default ip ,format as 'ip' or 'ip1,ip2..' [%s] :",
                 LANGUAGE_CN : "请设置华为OceanStor T系列存储iSCSI默认目标的ip，格式为'ip' [%s]: "},
     "1000104":{LANGUAGE_EN : "Please input OceanStor T series storage controller ip, format as 'ip1,ip2' [%s] :",
                 LANGUAGE_CN : "请设置华为OceanStor T系列存储控制节点ip, 格式为 'ip1,ip2' [%s] : "},
     "1000105":{LANGUAGE_EN : "Please input OceanStor T series storage password %s:",
                 LANGUAGE_CN : "请设置华为OceanStor T系列存储密码 [%s] :"},
     "1000106":{LANGUAGE_EN : "Please input OceanStor T series storage pool names for cinder,format as 'poolname1,poolname2' [%s] : ",
                 LANGUAGE_CN : "请设置华为OceanStor T系列存储池名字，格式为 [poolname1,poolname2] [%s] : "},
     "1000107":{LANGUAGE_EN : "Please input OceanStor T series storage user name for cinder [%s] : ",
                 LANGUAGE_CN : "请设置华为OceanStor T系列存储用户名字 [%s] : "},
     "1000108":{LANGUAGE_EN : "Host num little than 3 ,can not deploy dsware!",
                 LANGUAGE_CN : "节点个数不满足3个及以上，不能部署dsware！"},
     "1000109":{LANGUAGE_EN : "Please input correct character,only support file or fusionstorage or ipsan!",
                 LANGUAGE_CN : "请输入正确的选项，当前只支持 file,fusionstorage 与 ipsan！"},
     "1000110":{LANGUAGE_EN : "--------------Set storage configuration end -----------------------------------------",
                 LANGUAGE_CN : "--------------设置存储相关配置项结束 -------------------------------------------------"},
     "1000111":{LANGUAGE_EN : "Please input correct ip information.",
                 LANGUAGE_CN : "请输入正确的ip信息。"},
     "1000113":{LANGUAGE_EN : "",
                 LANGUAGE_CN : ""},
     "1000114":{LANGUAGE_EN : "",
                 LANGUAGE_CN : ""},

     "1000201":{LANGUAGE_EN : "Welcome to Dns config",
                 LANGUAGE_CN : "dns配置"},
     "1000202":{LANGUAGE_EN : "If you only have one az dc ,you need not config Dns (just press enter to pass)",
                 LANGUAGE_CN : "如果您只部署了一个az dc，您可以选择跳过，按回车键即可"},
     "1000203":{LANGUAGE_EN : "Do you want to config dns [y|n][n] : ",
                 LANGUAGE_CN : "请问是否需要修改dns配置 [y|n][n]"},
     "1000204":{LANGUAGE_EN : "Please input correct character,only support \'y\',\'n\',\'\'!",
                 LANGUAGE_CN : "请输入正确的字符，只支持 \'y\',\'n\',\'\'!"},
     "1000205":{LANGUAGE_EN : '''Please set dns address such as "/domain1/ip1, /domain2/ip2, ..."[%s] : ''',
                 LANGUAGE_CN : '''请输入dns的地址，格式为"域名1/IP地址1，域名2/IP地址2..."[%s] '''},
     "1000206":{LANGUAGE_EN : '''Set error please input dns address such as "/domain1/ip1, /domain2/ip2, ...''',
                 LANGUAGE_CN : '''请输入正确的地址 格式为"域名1/IP地址1，域名2/IP地址2..."'''},
     "1000207":{LANGUAGE_EN : '''Illegal dns address''',
                 LANGUAGE_CN : '''非法地址'''},
     "1000208":{LANGUAGE_EN : "Please input correct ip address!",
                 LANGUAGE_CN : "请输入正确的dns地址"},
     "1000209":{LANGUAGE_EN : '''Please set dns server such as "/domain1/ip1(#port)(@dev),/domain2/ip2(#port)(@dev),..."[%s] ''',
                 LANGUAGE_CN : '''请输入dns server 格式为"域名1/IP地址1(#端口)(@设备名)，域名2/IP地址2(#端口)(@设备名)..."[%s]'''},
     "1000210":{LANGUAGE_EN : '''Set error please input dns server such as "/domain1/ip1(#port)(@dev),/domain2/ip2(#port)(@dev), ...''',
                 LANGUAGE_CN : '''请输入正确的dns server 格式为"域名1/IP地址1(#端口)(@设备名)，域名2/IP地址2(#端口)(@设备名)..."'''},
     "1000211":{LANGUAGE_EN : '''Please set dns network [%s] ''',
                 LANGUAGE_CN : '''请输入dns network [%s]'''},
     "1000212":{LANGUAGE_EN : "Please set correct dns network ",
                 LANGUAGE_CN : "请输入正确的dns network "},
     "1000213":{LANGUAGE_EN : "Please set correct dns ip",
                 LANGUAGE_CN : "请输入正确的dns ip"},
     "1000214":{LANGUAGE_EN : "Please set dns ip [%s]",
                 LANGUAGE_CN : "请输入dns ip [%s]"},
     "1000215":{LANGUAGE_EN : "",
                 LANGUAGE_CN : ""},
     "1000216":{LANGUAGE_EN : "",
                 LANGUAGE_CN : ""},
     "1000217":{LANGUAGE_EN : "",
                 LANGUAGE_CN : ""},


     "1000301":{LANGUAGE_EN : 'You have been deployed success',
                 LANGUAGE_CN : "您的环境已经部署成功，无需再次部署"},
     "1000302":{LANGUAGE_EN : "HELP! I am in  trouble.please see fsinstall.log or connect HUAWEI FSP support staff!",
                 LANGUAGE_CN : "哎呀，一键部署配置脚本挂掉了，请尝试查看日志fsinstall.log或者联系华为 FSP支持人员处理"},
     "1000303":{LANGUAGE_EN : "You has been deployed once ",
                 LANGUAGE_CN : "以下是您曾经部署过的信息"},
     "1000304":{LANGUAGE_EN : "You has been deployed once ",
                 LANGUAGE_CN : "您曾经部署过:"},
     "1000305":{LANGUAGE_EN : "You choose %s",
                 LANGUAGE_CN : "您选择了 %s"},
     "1000306":{LANGUAGE_EN : "Your control host list is %s",
                 LANGUAGE_CN : "您选择的控制节点列表是%s"},
     "1000307":{LANGUAGE_EN : "Glance will deploy on %s",
                 LANGUAGE_CN : "Glance 会部署到 %s"},
     "1000308":{LANGUAGE_EN : "Keystone will deploy on %s",
                 LANGUAGE_CN : "Keystone 会部署到 %s"},
     "1000309":{LANGUAGE_EN : "Do you want to continue [y|n][y]",
                 LANGUAGE_CN : "请问是否确认[y|n][y] : "},
     "1000310":{LANGUAGE_EN : "Please input correct character,only support \'y\',\'n\',\'\'!",
                 LANGUAGE_CN : "请输入正确的字符，只支持 \'y\',\'n\',\'\'!"},
     "1000311":{LANGUAGE_EN : "------------------------------Host discovery & configuration--------------------------------------------------",
                 LANGUAGE_CN : "----------------------------------------------节点列表--------------------------------------------------"},
     "1000312":{LANGUAGE_EN : "Host discovery failed,host = %s.",
                 LANGUAGE_CN : "获取节点信息失败,节点为 %s."},
     "1000313":{LANGUAGE_EN : "Please set deploy mode [1|2][%s] : ",
                 LANGUAGE_CN : "请选择部署模式 [1|2][%s] : "},
     "1000314":{LANGUAGE_EN : "There is only %s host(s) you can't choose %s",
                 LANGUAGE_CN : "现在只有%s个节点,你不能选择 %s"},
     "1000315":{LANGUAGE_EN : "Please input correct character,only support \'1\', \'2\'!",
                 LANGUAGE_CN : "请输入正确的选择，正确的模式有 \'1\', \'2\' !"},
     "1000316":{LANGUAGE_EN : "You choose %s mode, all the control roles will be install on the current host.",
                 LANGUAGE_CN : "您选择了%s模式，所有的角色都会部署在当前节点。"},
     "1000317":{LANGUAGE_EN : "You choose %s mode, all the control roles will be installed on 3 hosts.",
                 LANGUAGE_CN : "您选择了%s模式，所有的管理角色都会部署在3个控制节点"},
     "1000318":{LANGUAGE_EN : "Please set 3 hostid formatted as \'host1,host2,host3\' .(press enter for auto choose) [%s]: ",
                 LANGUAGE_CN : "请输入3个节点的id号，以逗号分隔，\'host1,host2,host3\'.(press enter for auto choose) [%s]: "},
     "1000319":{LANGUAGE_EN : "Manager host must be 3, formatted as \'host1,host2,host3\' or you can input \'b\' or \'back\' to reselect mode.",
                 LANGUAGE_CN : "输入的管理节点个数应该是3个，以逗号分隔，或者输入\'b\' 或者 \'back\'返回上一级选择模式"},
     "1000320":{LANGUAGE_EN : "Host id not exist,please input right host id.the error host id is %s.",
                 LANGUAGE_CN : "输入的节点id不存在，错误的节点id列表为 %s."},
     "1000321":{LANGUAGE_EN : "There is same hostid in your input",
                 LANGUAGE_CN : "您的输入中存在相同的hostid"},
     "1000322":{LANGUAGE_EN : "First host id must in 3controllers. first host id is %s",
                 LANGUAGE_CN : "当前节点必须在输入的3个节点内，当前节点的id为 %s"},
     "1000323":{LANGUAGE_EN : "number of controllers must be 3, formatted as \'host1,host2,host3\' or you can input \'b\' or \'back\' to reselect mode .",
                 LANGUAGE_CN : "输入的管理节点个数应该是3个，以逗号分隔，或者输入\'b\' 或者 \'back\'返回上一级选择模式"},
     "1000324":{LANGUAGE_EN : "If you deploy success this time, you can't change your deploy mode except PXE reinstall",
                 LANGUAGE_CN : "您配置成功后，将无法修改当前配置，除非重新PXE安装"},
     "1000325":{LANGUAGE_EN : "You choose %s",
                 LANGUAGE_CN : "您选择了 %s"},
     "1000326":{LANGUAGE_EN : "Please choose hosts which will be used to deploy router role,formatted as \'host1,host2,host3\' [%s]:",
                 LANGUAGE_CN : "请选择用来部署router角色的节点"},
     "1000327":{LANGUAGE_EN : "Please choose hosts which will be used to deploy loadbalancer role,formatted as \'host1,host2,host3\' [%s]:",
                 LANGUAGE_CN : "请选择用来部署loadbalancer角色的节点"},
     "1000328":{LANGUAGE_EN : "Please choose hosts which will be used to deploy blockstorage-driver role,formatted as \'host1,host2,host3\' [%s]:",
                 LANGUAGE_CN : "请选择用来部署blockstorage-driver角色的节点"},
     "1000329":{LANGUAGE_EN : "Please set backend storage type[file|fusionstorage|ipsan][%s]",
                 LANGUAGE_CN : "请设置后端存储类型[file|fusionstorage|ipsan][%s]"},
     "1000330":{LANGUAGE_EN : "Router will deploy on %s",
                 LANGUAGE_CN : "Router角色会被部署在 %s"},
     "1000331":{LANGUAGE_EN : "Loadbalancer will deploy on %s",
                 LANGUAGE_CN : "Loadbalancer角色会被部署在 %s"},
     "1000332":{LANGUAGE_EN : "Blockstorage-driver will deploy on %s",
                 LANGUAGE_CN : "Blockstorage-driver角色会被部署在 %s"},
     "1000333":{LANGUAGE_EN : "Backup storage type is %s",
                 LANGUAGE_CN : "后端存储类型是 %s"},
     "1000334":{LANGUAGE_EN : "Please choose router mode,formatted as[legacy|dvr][%s]",
                 LANGUAGE_CN : "请选择router角色的模式，格式为[legacy|dvr][%s]"},
     "1000335":{LANGUAGE_EN : "Please input correct router mode,formatted as[legacy|dvr],the error mode is [%s]",
                 LANGUAGE_CN : "请输入正确的router角色的模式，格式为[legacy|dvr][%s]"},
     "1000336":{LANGUAGE_EN : "Router mode will be %s",
                 LANGUAGE_CN : "Router 的模式是 %s"}
     }

