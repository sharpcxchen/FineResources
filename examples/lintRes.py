#!/usr/bin/env python             
# coding: utf-8
import os
import lcba.lint_cleanup as clean_app
import config
import lcba.globalVar as glo
import lcba.util as util

################################################
#进行lint资源压缩@param just_chek 是否只做检查，if True 不删除lint 多余文件，只报警，一般用于服务器打包测试
###############################################
def lintResource(just_check=False):
	print "###############################"
	print "Now lint Resource "
	print "###############################"
	workPath = glo.getValue(config.KEY_WORK_PATH)
	moduleNames = config.MODULES_NAME
	gradlewPath = glo.getValue(config.KEY_GRADLEW_PATH)
	if None == moduleNames or None == workPath or None == gradlewPath:
		print "lintResource()...not find value"
		util.safeQuit(None, None)

	os.chdir(r'%s'%workPath)
	#方案一，如果有lint 报告文件,就用已有的报告文件
	#缺点:报告是由可能是旧的
	for moduleName in moduleNames:
		modulePath = os.path.join(workPath, moduleName)
		reportsXml = os.path.join(modulePath , config.LINT_RESULT_PATH)
		print "report xml is:%s"%reportsXml
		if os.path.exists(reportsXml):
			print "###############################"
			print "Now delete unUsed file"
			print "###############################"
			manifest_path = os.path.abspath(os.path.join(modulePath, config.ANDROID_MANIFEST_FILE))
			out_ids_path = os.path.abspath(os.path.join(modulePath, config.LAYOUT_IDS_PATH))
			clean_app.deleteRes(modulePath,reportsXml,manifest_path,out_ids_path,
								just_check,config.IGNORE_LAYOUTS_FILE,config.IGNORE_LAYOUTS_VALUE)
		else:
			if util.haveGradleTask(workPath,gradlewPath,config.TASK_LINT):
				print "we will build lint reports with command: %s %s --info --stacktrace"%(gradlewPath,
																							config.TASK_LINT)
				os.system('%s %s --info --stacktrace'%(gradlewPath, config.TASK_LINT))
				if os.path.exists(reportsXml):
					print "###############################"
					print "Now delete unUsed file"
					print "###############################"
					manifest_path = os.path.abspath(os.path.join(modulePath, config.ANDROID_MANIFEST_FILE))
					out_ids_path = os.path.abspath(os.path.join(modulePath, config.LAYOUT_IDS_PATH))
					clean_app.deleteRes(modulePath,reportsXml,manifest_path,out_ids_path,just_check,
										config.IGNORE_LAYOUTS_FILE,config.IGNORE_LAYOUTS_VALUE)
				else:
					print "not find lint reports!!!!"
					#fixme 这里使用sdk lint 命令来替代
					util.safeQuit(None, None)
				pass
			else:
				print "not find task:%s"%config.TASK_LINT
		pass
	pass
pass

#使用方案二： 简单版
def lintResource_2(just_check):
	print "###############################"
	print "Now lint Resource "
	print "###############################"
	workPath = glo.getValue(config.KEY_WORK_PATH)
	moduleNames = config.MODULES_NAME
	gradlewPath = glo.getValue(config.KEY_GRADLEW_PATH)
	if None == moduleNames or None == workPath or None == gradlewPath:
		print "lintResource()...not find value"
		util.safeQuit(None, None)
	for moduleName in moduleNames:
		modulePath = os.path.join(workPath, moduleName)
		clean_app.deleteRes(app_dir=modulePath)
	pass
pass

################################################
#主函数
###############################################
def main():
	config.initModules()
	# lintResource(False)
	lintResource_2(False)

pass

if __name__ == '__main__':
	main()