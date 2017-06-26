#!/usr/bin/env python
# coding: utf-8

import lcba.globalVar as glo
import lcba.util as util
import os

#定义一些全局的关键字
KEY_WORK_PATH="_work_path"
KEY_FINE_PATH= "_fineresources_path"
KEY_GRADLEW_PATH="_gradle_path"
KEY_REASON="_reason"

#############for step lint
#常量: 生成lint报告的文件
LINT_RESULT_PATH = "build/reports/lint-results.xml"
#常量: 生成lint 报告的命令
TASK_LINT = "lint"
#常量: 忽略无用的布局文件
IGNORE_LAYOUTS_FILE = False
#常量: 忽略布局文件里面的内容，不要该成False！！！
IGNORE_LAYOUTS_VALUE = True
#常量: 解决布局文件中被删除的文件中含有@+id，被其他文件@id引用的情况
LAYOUT_IDS_PATH = "src/main/res/values/lint_ids.xml"
#常量: manifest的路径
ANDROID_MANIFEST_FILE = "src/main/AndroidManifest.xml"

###############for step compress
#常量:账号列表
ACCOUNT_KEY_LIST = [
    "sXzp30KfRZaf0NlWaQP0U3qEwQwoCl7s",#use feiy1@jumei.com register
    "l1og95PkmrPVMpf2NMSjnEmtwIL6urf1",#use xiaomom@jumei.com register
    "QfjLJJNOSShBxWtE1-tUC9Bfjg6U9Om3",#use xiaojiangk@jumei.com register
]

MODULES_NAME = [
    'app',
    'jmwebsocketsdk',
    #'baselib',#lint 的时候有依赖baselib，但是它在模块内未使用
]

#########for step andResGuard
#常量: 生成apk的编译命令
BUILD_APK_TASK = "assembleRelease"
#常量: 生成apk的路径
BUILD_APK_PATH = "build/outputs/apk/app-release.apk"

def initModules():
    workPath = findWorkingPath()
    if not workPath:
        print "initModules()...not find work path!!!"
        util.safeQuit(None, None)
    pass

    os.chdir(workPath)
    glo.set_value(KEY_WORK_PATH,workPath)
    fineDirPath=os.path.join(workPath,"fine_resources")
    if os.path.exists(fineDirPath):
        glo.set_value(KEY_FINE_PATH, fineDirPath)
    pass
    gradlewPath=os.path.join(workPath,"gradlew")
    if os.path.exists(gradlewPath):
        glo.set_value(KEY_GRADLEW_PATH,gradlewPath)
    pass
    ##方案一，从目录的settings.gradle 中读取有多少个模块，缺点,在lint的时候被依赖的模块资源会被删除
    # with open(workPath+"settings.gradle") as f:
    #     for line in f.readlines():
    #         if line.startswith('//') or '#' in line:
    #             continue
    #         pass
    #         pattern = re.compile('\':\\b[^\']+')
    #         match_result=re.findall(pattern,line)
    #         if match_result:
    #             for item in match_result:
    #                 bits=item.rsplit(':',2)
    #                 #print bits[1]
    #                 moduleFile=curPath+"/"+bits[1]
    #                 if not os.path.exists(moduleFile):
    #                     os.makedirs(r'%s'%moduleFile)
    #                     print "create module dir:%s"%moduleFile
    #                 pass
    #                 modules_name.append(bits[1])
    #             pass
    #         pass
    #     pass
    # pass

    ##方案二自己添加
    # modules_name.append('app')
    # modules_name.append('jmwebsocketsdk')

pass

def findSettingsGradle(dirPath,count):
    print "findSettingsGradle()...dirPath:%s"%dirPath
    settingsPath = os.path.join(dirPath,"settings.gradle")
    if os.path.exists(settingsPath) and os.path.isfile(settingsPath):
        print "settings.gradle in project:%s"%settingsPath
        return dirPath
    else:
        if count <=0:
            return None
        count -= 1;
        dirPath = os.path.abspath(os.path.join(dirPath,"../"))
        return findSettingsGradle(dirPath,count)
    pass
pass

def findWorkingPath():
    dirPath = os.path.dirname(os.path.realpath(__file__))
    workPath = findSettingsGradle(dirPath,3)
    print "findWorkingPath()...%s"%workPath
    return workPath
pass