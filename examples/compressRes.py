#!/usr/bin/env python             
# coding: utf-8
import os
import lcba.util as util
import  config
import lcba.globalVar as glo
import lcba.compress as compress

################################################
# 遍历文件夹进行压缩
###############################################
def compressPic(just_check=False):
    # 压缩匹配的文件夹drawable mipmap assert
    print "###############################"
    print "Now compress picture "
    print "###############################"

    workPath = glo.getValue(config.KEY_WORK_PATH)
    lcbaPath = glo.getValue(config.KEY_FINE_PATH)
    print "Current Path is:%s" % (workPath)
    modules_name = config.MODULES_NAME
    if not workPath or not modules_name or not lcbaPath:
        print " ERROR !!! %s %s %s" % (workPath, modules_name,lcbaPath)
        util.safeQuit(None, None)
    os.chdir(workPath)
    for module_name in modules_name:
        modulePath = os.path.join(workPath , module_name)
        print "modulePath:%s"%modulePath
        outDir = os.path.join(lcbaPath,module_name)
        compress.compressModule(modulePath,outDir,config.ACCOUNT_KEY_LIST,just_check)
    pass
pass


################################################
# 主函数
###############################################
def main():
    config.initModules()
    compressPic()
pass

if __name__ == '__main__':
    main()
