#!/usr/bin/env python             
# coding: utf-8
import os
import lcba.util as util
import compressRes
import lintRes
import signal
import config
import lcba.globalVar as glo
import andResGuard

################################################
#主函数
###############################################
def main():
	config.initModules()
	signal.signal(signal.SIGINT, util.safeQuit)
	signal.signal(signal.SIGTERM, util.safeQuit)
	workPath = glo.getValue(config.KEY_WORK_PATH)
	print "workpath:%s"%workPath

	modules_name = config.MODULES_NAME
	if None == workPath or None == modules_name:
		print "main()...work path is empty!!!"
		util.safeQuit(None, None)
	pass
	os.chdir(r'%s'%workPath)
	gradlewPath = glo.getValue(config.KEY_GRADLEW_PATH)
	if os.path.exists(gradlewPath):
		os.system('%s clean'%gradlewPath)
	pass

	#lint 和删除无用资源
	lintRes.lintResource()

	#压缩png
	compressRes.compressPic()

	#编译生成apk
	if util.haveGradleTask(workPath,gradlewPath,config.BUILD_APK_TASK):
		#删除build目录自己编译，因为lint资源删除了一些资源，不删除会提示找不到
		print "###############################"
		print "Now build apk"
		print "###############################"
		# os.system('rm -rf ../build')
		# os.system('rm -rf JuMeiYouPinV1.0.0/build/intermediates/')
		os.chdir(r'%s'%workPath)
		os.system('%s clean'%gradlewPath)
		os.system("%s %s --stacktrace"%(gradlewPath, BUILD_APK_TASK))
	pass

	#资源混淆压缩，请配置AndResGuard_config.xml
	andResGuard.andResGuard()
pass



if __name__ == '__main__':
	main()