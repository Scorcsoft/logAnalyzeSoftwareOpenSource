from random import choice
import os.path
import xlrd
import xlwt
import time
import json


logo = '''
        [               Analyze software of IDS attack log   v1.9             ]
        [                                                                     ]
        [                  Scorcsoft for PICC in 2019-06-04                   ]
        [   This programming by Scorcsoft team of geniuses of cyber security  ]


'''
logo1 = '''
                                                                       $$$$$$\    $$\     
                                                                      $$  __$$\   $$ |    
 $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$$\  $$$$$$$\  $$$$$$\  $$ /  \__|$$$$$$\   
$$  _____|$$  _____|$$  __$$\ $$  __$$\ $$  _____|$$  _____|$$  __$$\ $$$$\     \_$$  _|  
\$$$$$$\  $$ /      $$ /  $$ |$$ |  \__|$$ /      \$$$$$$\  $$ /  $$ |$$  _|      $$ |    
 \____$$\ $$ |      $$ |  $$ |$$ |      $$ |       \____$$\ $$ |  $$ |$$ |        $$ |$$\ 
$$$$$$$  |\$$$$$$$\ \$$$$$$  |$$ |      \$$$$$$$\ $$$$$$$  |\$$$$$$  |$$ |        \$$$$  |
\_______/  \_______| \______/ \__|       \_______|\_______/  \______/ \__|         \____/ 


                                                                                          '''
logo2 = '''
                                                       __ _   
                                                      / _| |  
                     ___  ___ ___  _ __ ___ ___  ___ | |_| |_ 
                    / __|/ __/ _ \| '__/ __/ __|/ _ \|  _| __|
                    \__ \ (_| (_) | | | (__\__ \ (_) | | | |_ 
                    |___/\___\___/|_|  \___|___/\___/|_|  \__|

                                          '''
logo3 = '''
     _______  _______  _______  _______  _______  _______  _______  _______ _________
    (  ____ \(  ____ \(  ___  )(  ____ )(  ____ \(  ____ \(  ___  )(  ____ \\\\__   __/
    | (    \/| (    \/| (   ) || (    )|| (    \/| (    \/| (   ) || (    \/   ) (   
    | (_____ | |      | |   | || (____)|| |      | (_____ | |   | || (__       | |   
    (_____  )| |      | |   | ||     __)| |      (_____  )| |   | ||  __)      | |   
          ) || |      | |   | || (\ (   | |            ) || |   | || (         | |   
    /\____) || (____/\| (___) || ) \ \__| (____/\/\____) || (___) || )         | |   
    \_______)(_______/(_______)|/   \__/(_______/\_______)(_______)|/          )_(   
                                                                                 '''
logo4 = '''
                     ____   ___  __  ____   ___  ____   __  ____  ____ 
                    / ___) / __)/  \(  _ \ / __)/ ___) /  \(  __)(_  _)
                    \___ \( (__(  O ))   /( (__ \___ \(  O )) _)   )(  
                    (____/ \___)\__/(__\_) \___)(____/ \__/(__)   (__) '''

logo5 = '''
                                                             ______ 
                       ______________  ___________________  / __/ /_
                      / ___/ ___/ __ \/ ___/ ___/ ___/ __ \/ /_/ __/
                     (__  ) /__/ /_/ / /  / /__(__  ) /_/ / __/ /_  
                    /____/\___/\____/_/   \___/____/\____/_/  \__/  
                                                        '''

logo6 = '''
                                                     __ _   
                          ___ __ ___ _ _ __ ___ ___ / _| |_ 
                         (_-</ _/ _ \ '_/ _(_-</ _ \  _|  _|
                         /__/\__\___/_| \__/__/\___/_|  \__|
                                                    '''

logo7 = '''

                                                            ,---.  ,--.   
             ,---.  ,---. ,---. ,--.--. ,---. ,---.  ,---. /  .-',-'  '-. 
            (  .-' | .--'| .-. ||  .--'| .--'(  .-' | .-. ||  `-,'-.  .-' 
            .-'  `)\ `--.' '-' '|  |   \ `--..-'  `)' '-' '|  .-'  |  |   
            `----'  `---' `---' `--'    `---'`----'  `---' `--'    `--'   
                                                                  '''
logos = [logo1, logo2, logo3, logo4, logo5, logo6, logo7]

def writeRow(fpObj,line,style,findDate,findTime,department,sourceIP,attackSource,attackSourceFrom,disName,disIpPort,disType,note):
    fpObj.write(line,0,findDate,style)
    fpObj.write(line,1,findTime,style)
    fpObj.write(line,2,department,style)
    fpObj.write(line,3,sourceIP,style)
    fpObj.write(line,4,attackSource,style)
    fpObj.write(line,5,attackSourceFrom,style)
    fpObj.write(line,6,disName,style)
    fpObj.write(line,7,disIpPort,style)
    fpObj.write(line,8,disType,style)
    fpObj.write(line,9,note,style)

    return line + 1

def ipType(ip):
    return "Scorcsoft仿生算法已删除\n\n感谢使用Scorcsoft开源代码"

def getAttackFrom(attackIP):

    return "Scorcsoft仿生算法已删除\n\n感谢使用Scorcsoft开源代码"


print(choice(logos))
print(logo)

try:
    configFp = open("data/config.ini",'r')
    string = configFp.read()
    configFp.close()
    config = json.loads(string)
except:
    input("[*] You need run this software in attackReport.exe root path.")

    os.exit()

logFile = input("[*] The log file path: ")
try:
    fp = open(logFile,'r')
    fp.close()
except:
    print("[*] Can not to open the log file: %s."%(logFile))
    os.exit()

ipWhiteList = []
ruleWhiteList = []
global piccTerminal
global subCompanyA
global subCompanyB
global piccHost
global outLink
global IPSource

piccTerminal = []
piccHost = []


subCompanyA = {
    "PICC网络架构":"已删除"
}
subCompanyB = {
    "PICC网络架构":"已删除"
}

outLink = [
"PICC网络架构已删除"
]



start = time.perf_counter()
try:
    for i in open("whiteIP.txt"):
        i = i.strip("\n")
        i = i.strip("\r\n")
        ipWhiteList.append(i)
    print("[*] White list of IP: %d"%(len(ipWhiteList)))
except:
    print("[*] No White list of IP")

try:
    for i in open("whiteRule.txt"):
        i = i.strip("\n")
        i = i.strip("\r\n")
        tmp = i.split("#",1)
        i = tmp[0]
        i = i.strip(" ")
        ruleWhiteList.append(i)
    print("[*] White list of rule: %d"%(len(ruleWhiteList)))
except:
    print("[*] No White list of rule")

IPSource = []
try:
    for i in open("IPSource.txt"):
        i = i.strip("\n")
        i = i.strip("\r\n")
        tmp = i.split(",",1)
        if len(tmp) == 2:
            IPSource.append((tmp[0],tmp[1]))
    print("[*] Append IP source: %d"%(len(IPSource)))
except:
    print("[*] No append IP source")

importantEvent = []
try:
    for i in open("importantEvent.txt"):
        i = i.strip("\n")
        i = i.strip("\r\n")
        importantEvent.append(i)
    print("[*] Important event: %d"%(len(importantEvent)))
except:
    print("[*] No important event")

attackData = {}
try:
    rfp = xlrd.open_workbook(logFile)
except:
    print("[*] Can not to open the log file. If \" %s \" is the 天融信 IDS log, You need open it with Excel and save as a \".xls\" or \".xlsx\" file.\n"%(logFile))
    input("Press [enter] or close current dos window to exit.")
    os.exit()
analyzeIP = []
print()
sum = 0
for sheetIndex in range(0,len(rfp.sheets())):
    rsheet = rfp.sheet_by_index(sheetIndex)
    indexLine = rsheet.row_values(0)
    attackIpIndex = -1
    disPortIndex = -1
    disIpIndex = -1
    eventIndex = -1
    ruleIdIndex = -1
    timeIndex = -1
    quantityIndex = -1

    for i in range(0,len(indexLine)):
        if indexLine[i] == "源地址" or indexLine[i] == "源IP" or "src" in indexLine[i]:
            attackIpIndex = i
        elif indexLine[i] == "目的地址" or indexLine[i] == "目的IP" or "dst" in indexLine[i]:
            disIpIndex = i
        elif indexLine[i] == "目的端口" or "dport" in indexLine[i]:
            disPortIndex = i
        elif indexLine[i] == "事件名称" or indexLine[i] == "事件" or "msg" in indexLine[i]:
            eventIndex = i
        elif indexLine[i] == "规则编号" or "rule" in indexLine[i]:
            ruleIdIndex = i
        elif indexLine[i] == "时间" or "time" in indexLine[i]:
            timeIndex = i
        elif "次数" in indexLine[i] or "repeat" in indexLine[i]:
            quantityIndex = i
        else:
            pass
    if ruleIdIndex == -1:
        ruleIdIndex = eventIndex #绿盟的IDS规则id和事件写在一起的，下面获取规则id的时候首先判断规则id索引和事件名称索引是否相等，如果相等说明当前的绿盟IDS日志，使用split取出规则id

    if attackIpIndex < 0 or disIpIndex < 0 or disPortIndex < 0 or eventIndex < 0 or timeIndex < 0:
        print("[*] Can not find the key index, Please call the Scorcsoft team.")
        os.exit()

    startLine = 1
    if "time=" in indexLine[0]:
        startLine = 0
    for i in range(startLine,rsheet.nrows): #读入日志 #debug
        value = rsheet.row_values(i)
        sum += 1
        attackIP = value[attackIpIndex]

        if "src=" in attackIP:

            attackIP = attackIP[5:]

        jump = False
        for ipFilter in ipWhiteList:
            if attackIP[:len(ipFilter)] == ipFilter:
                jump = True
                break
        if jump: #如果当前攻击IP在白名单里，就跳过这一行
            continue

        if attackIP not in analyzeIP:
            analyzeIP.append(attackIP)
            print("\r                                            ",end="")
            print("\r[*] analyzing of %s"%(attackIP),end="")


        if ruleIdIndex == eventIndex: #取出规则id和事件名称
            eventString = value[eventIndex]
            tmp = eventString.split(" ",1)
            ruleID = tmp[0]
            if  "rule=" in ruleID:
                ruleID = ruleID[6:]
            eventName = tmp[1]
            if  "msg=" in eventName:
                eventName = eventName[6:-1]
        else:
            ruleID = value[ruleIdIndex]
            if "rule=" in ruleID:
                ruleID = ruleID[6:]
            eventName = value[eventIndex] #取id和事件名称结束
            if "msg=" in eventName:
                eventName = eventName[6:-1]

        jump = False
        for ruleFilter in ruleWhiteList:#判断当前事件是否加白
            if ruleID == ruleFilter:
                jump = True
                break
        if jump:
            continue #如果当前事件在白名单里，就跳过这一行

        dport = value[disPortIndex]
        if "dport=" in dport:
            dport = dport[7:]
        disIP = "%s:%s"%(value[disIpIndex],dport)
        if "dst=" in disIP:
            disIP = disIP[5:]
        if attackIP not in attackData.keys():
            attackData[attackIP] = {}

            attackFrom = getAttackFrom(attackIP)
            attackData[attackIP]["from"] = attackFrom
            attackTime = value[timeIndex]
            if "time=" in attackTime:

                attackTime = attackTime[6:-1]

            timeArray = time.strptime(attackTime, "%Y-%m-%d %H:%M:%S")
            t = int(time.mktime(timeArray))
            attackData[attackIP]["time"] = t
        if disIP not in attackData[attackIP].keys():
            attackData[attackIP][disIP] = {}

        if eventName not in attackData[attackIP][disIP].keys():
            if quantityIndex != -1:
                attackQuantity = value[quantityIndex]
                if "repeat=" in attackQuantity:
                    attackQuantity = attackQuantity[8:]
                attackData[attackIP][disIP][eventName] = int(attackQuantity)
            else:
                attackData[attackIP][disIP][eventName] = 1
        else:
            if quantityIndex != -1:
                attackQuantity = value[quantityIndex]
                if "repeat=" in attackQuantity:
                    attackQuantity = attackQuantity[8:]
                attackData[attackIP][disIP][eventName] += int(attackQuantity)
            else:
                attackData[attackIP][disIP][eventName] += 1
        attackTime = value[timeIndex]
        if "time=" in attackTime:
            attackTime = attackTime[6:-1]
        timeArray = time.strptime(attackTime, "%Y-%m-%d %H:%M:%S")
        t = int(time.mktime(timeArray))
        if attackData[attackIP]["time"] > t: #保证记录当前IP最早的攻击时间
            attackData[attackIP]["time"] = t


end = time.perf_counter()
tmp = time.strftime("%Y,%m,%d,%H,%M,%S",time.localtime())
date = tmp.split(",")

fp = xlwt.Workbook(encoding="utf-8")
style = xlwt.XFStyle()
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
style.alignment = alignment


sheet = fp.add_sheet("监控记录")
sheet.col(0).width = 256 * 12
sheet.col(1).width = 256 * 22
sheet.col(2).width = 256 * 30
sheet.col(3).width = 256 * 22
sheet.col(4).width = 256 * 24
sheet.col(5).width = 256 * 24
sheet.col(6).width = 256 * 15
sheet.col(7).width = 256 * 22
sheet.col(8).width = 256 * 10
sheet.col(9).width = 256 * 52
line = 0
line = writeRow(
    fpObj=sheet,line=line,style=style,
    findDate="发现日期",
    findTime="发现时间",
    department="上报机构及联系人",
    sourceIP="（疑似）攻击源IP",
    attackSource="攻击IP类型",
    disName="目标系统名称",
    attackSourceFrom="攻击来源",
    disIpPort="目标IP地址及端口",
    disType="IP地址类型",
    note="简述"
)

line = writeRow(
    fpObj=sheet,line=line,style=style,
    findDate="感谢",
    findTime="使用",
    department="scorcsoft",
    sourceIP="开源代码",
    attackSource=" ",
    disName="genius",
    attackSourceFrom="Scorcsoft",
    disIpPort="team",
    disType="of",
    note="cyber security"
)
attackMemory = {}
if os.path.isfile("data/memory.db"):
    rfp = open("data/memory.db",'r')
    string = rfp.read()
    rfp.close()
    attackMemory = json.loads(string)


for attackIP in attackData.keys():


    ######################################################################
    #                                                                    #
    #                                                                    #
    #                        Scorcsoft仿生算法已删除                      #
    #                                                                    #
    #                                                                    #
    ######################################################################

    disIPString = ''
    noteString = ''
    flag = False
    for disIP in attackData[attackIP]:
        attackQuantity = 0

        if disIP == "time" or disIP == "from":
            continue
        disIPString += "%s\n" % (disIP)
        for eventName in attackData[attackIP][disIP].keys():
            noteString += "%s(%d次)\n"%(eventName,attackData[attackIP][disIP][eventName])

            #for important in importantEvent:
            #    if important in eventName:
            #        flag = True
            #        break
            #     Scorcsoft仿生算法已删除

    line = writeRow(
        fpObj=sheet, line=line, style=style,
        findDate="%s/%s/%s" % (date[0], date[1], date[2]),
        findTime="%s/%s/%s  %s:%s" % (date[0], date[1], date[2],date[3], date[4]),
        department="报告人信息已删除",
        sourceIP=attackIP,
        attackSource=ipType(attackIP),
        attackSourceFrom=attackData[attackIP]["from"],
        disName="",
        disIpPort=disIPString,
        disType="",
        note=noteString
    )

path = os.path.dirname(logFile)
filename = os.path.join(path,"scorcsoftReport%s_%s%s%s.xls"%(date[2],date[3],date[4],date[5]))
fp.save(filename)
print("\r[*] The report has been save to %s. \n[*] Analyze %d logs in %f seconds\n\n"%(filename,sum,(end - start)))

#print("Night gathers, and now my watch begins. It shall not end until my death. \nI shall take no wife, hold no lands, father no children. \nI shall wear no crowns and win no glory. \nI shall live and die at my post. \nI am the sword in the darkness. I am the watcher on the walls. I am the fire that burns against the cold, the light that wakes the sleepers, the shield that guards the realms of men. \nI pledge my life and honor to the Night's Watch, for this night, and all the nights to come.")
#print("\n长夜将至，我从今开始守望，至死方休。\n我将不娶妻，不封地，不生子。\n我将不戴宝冠，不争荣宠。\n我将尽忠职守，生死于斯。\n我是黑暗中的利剑，长城上的守卫，抵御寒冷的烈焰，破晓时分的光线，唤醒眠者的号角，守护王国的坚盾。\n我将生命与荣耀献给守夜人，今夜如此，夜夜皆然。\n")
input("Press [enter] or close current dos window to exit.")
