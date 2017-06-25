#!/usr/bin/env python             
# coding: utf-8
import os
import lcba.util as util
import config
import lcba.globalVar as glo
import lcba.andres_guard as andres

def andResGuard():
	print "###############################"
	print "Now andResGuard"
	print "###############################"
	workPath = glo.getValue(config.KEY_WORK_PATH)
	lcbaPath = glo.getValue(config.KEY_LCBA_PATH)
	modules_name = config.MODULES_NAME
	if None == workPath or None == modules_name or None == lcbaPath:
		print "andResGuard()...work path is empty!!!"
		util.safeQuit(None, None)
	pass

	# apkPath = os.path.join(workPath,const.BUILD_APK_PATH)
	# useAndResGuard(apkPath,os.path.join(outDirPath,const.AND_RES_GUARD_OUT))
	#apk 应该只有一个
	for module_name in modules_name:
		modulePath = os.path.join(workPath,module_name)
		apkPath = os.path.join(modulePath,config.BUILD_APK_PATH)
		outDirPath = os.path.join(lcbaPath, module_name)
		# andres.useAndResGuard(apkPath,os.path.join(outDirPath,"JumeiOut"))
		configPath = os.path.join('/Users/tory/working/Codes/JUMEI/android/lcba/','AndResGuard_config.xml')
		andres.useAndResGuard(apkPath,os.path.join(outDirPath,"JumeiOut"),configPath)
	pass
pass

################################################
#主函数
###############################################
def main():
	config.initModules()
	andResGuard()
pass

if __name__ == '__main__':
	main()