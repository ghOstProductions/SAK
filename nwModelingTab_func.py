'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
================================================================================
================================================================================
Author: Nic Wiederhold
Script: nwModelingTab_func.py
Collection: ghOst_SwissArmyKnife
Website: www.ghostproductions.com
Date Created: 8/4/15
Last Updated: 8/10/15
================================================================================
================================================================================
				    FUNCTIONS:
nwPivot_SetToManip
================================================================================
				    HOW TO RUN:
import nwModelingTab_func
================================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#=======================#
#      MAIN IMPORTS	#
#=======================#
# import maya commands
import maya.cmds as cmds 
# import maya mel commands
import maya.mel as mel
#=======================#
#   IMPORT FUNCTIONS	#
#=======================#
import nmGUI_func
#=======================#
#       FUNCTIONS	#
#=======================#
### mr. freeze ###
# freeze
def nmMrFreeze_freeze():
	'''
	this function will freeze transforms on the selected objects
	given the checked options.
	'''
	# get trans
	trans = cmds.checkBoxGrp('nmSAK_modfrzCBG',q=True,v1=True)
	# get rot
	rot = cmds.checkBoxGrp('nmSAK_modfrzCBG',q=True,v2=True)
	# get scl
	scl = cmds.checkBoxGrp('nmSAK_modfrzCBG',q=True,v3=True)
	# sel
	sel = cmds.ls(sl=True)
	### check
	if (trans == 1):
		tr = True
	else:
		tr = False
	if (rot == 1):
		ro = True
	else:
		ro = False
	if (scl == 1):
		sc = True
	else:
		sc = False
	# check
	if (len(sel) > 0):
		for stuff in sel:
			if not((cmds.getAttr(stuff+'.tx',l=True))and(cmds.getAttr(stuff+'.ty',l=True))and(cmds.getAttr(stuff+'.tz',l=True))):
				cmds.makeIdentity(stuff,a=True,t=tr,r=0,s=0,n=0)
			if not((cmds.getAttr(stuff+'.rx',l=True))and(cmds.getAttr(stuff+'.ry',l=True))and(cmds.getAttr(stuff+'.rz',l=True))):
				cmds.makeIdentity(stuff,a=True,t=0,r=ro,s=0,n=0)
			if not((cmds.getAttr(stuff+'.sx',l=True))and(cmds.getAttr(stuff+'.sy',l=True))and(cmds.getAttr(stuff+'.sz',l=True))):
				cmds.makeIdentity(stuff,a=True,t=0,r=0,s=sc,n=0)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Transforms have been frozen.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')
# zero
def nmMrFreeze_zero():
	'''
	this function zeros out the transforms on the selected objects
	given the checked options.
	'''
	# get trans
	trans = cmds.checkBoxGrp('nwSAK_modfrzCBG',q=True,v1=True)
	# get rot
	rot = cmds.checkBoxGrp('nwSAK_modfrzCBG',q=True,v2=True)
	# get scl
	scl = cmds.checkBoxGrp('nwSAK_modfrzCBG',q=True,v3=True)
	# sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel) > 0):
		# cycle
		for stuff in sel:
			### check
			if (trans == 1):
				if (cmds.getAttr(stuff+'.tx',l=True)==0):
					cmds.setAttr(stuff+'.tx',0)
				if (cmds.getAttr(stuff+'.ty',l=True)==0):
					cmds.setAttr(stuff+'.ty',0)
				if (cmds.getAttr(stuff+'.tz',l=True)==0):
					cmds.setAttr(stuff+'.tz',0)
			if (rot == 1):
				if (cmds.getAttr(stuff+'.rx',l=True)==0):
					cmds.setAttr(stuff+'.rx',0)
				if (cmds.getAttr(stuff+'.ry',l=True)==0):
					cmds.setAttr(stuff+'.ry',0)
				if (cmds.getAttr(stuff+'.rz',l=True)==0):
					cmds.setAttr(stuff+'.rz',0)
			if (scl == 1):
				if (cmds.getAttr(stuff+'.sx',l=True)==0):
					cmds.setAttr(stuff+'.sx',1)
				if (cmds.getAttr(stuff+'.sy',l=True)==0):
					cmds.setAttr(stuff+'.sy',1)
				if (cmds.getAttr(stuff+'.sz',l=True)==0):
					cmds.setAttr(stuff+'.sz',1)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Transforms have been zeroed out.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')
		
### Pivots and Transforms ###
## World Space Tool
# capture transforms/pivot coordinates
def captureManipPiv():
	mmc = cmds.manipMoveContext()
	cmds.setToolTo(mmc)
	manipLoc = cmds.manipMoveContext(mmc, q=True, p=True)
	rotObj = cmds.xform(q=True, ws=True, ro=True)
	posCopy = cmds.xform(q=True, ws=True, t=True)
	scaleCopy = cmds.xform(q=True, ws=True, s=True)
	manipPos = []
	transObj = []
	scaleObj = []
	if manipLoc:
		for num in manipLoc:
		    numFloat = float(num)
		    numRound = round(numFloat,5)
		    manipPos.append(numRound)
		cmds.setToolTo('moveSuperContext')
		cmds.deleteUI(mmc)
		for trans in posCopy:
			posFloat = float(trans)
			posRound = round(posFloat,5)
			transObj.append(posRound)
		for scale in scaleCopy:
			scaleFloat = float(scale)
			scaleRound = round(scaleFloat,5)
			scaleObj.append(scaleRound)
		# insert field values
		cmds.floatFieldGrp('nwSAK_manipPivot',e=True,v1=manipPos[0],v2=manipPos[1],v3=manipPos[2])
		cmds.floatFieldGrp('nwSAK_transPivots',e=True,v1=transObj[0],v2=transObj[1],v3=transObj[2])
		cmds.floatFieldGrp('nwSAK_rotPivots',e=True,v1=rotObj[0],v2=rotObj[1],v3=rotObj[2])
		cmds.floatFieldGrp('nwSAK_scalePivots',e=True,v1=scaleObj[0],v2=scaleObj[1],v3=scaleObj[2])
	# line
	else:
		nmGUI_func.nmGUI_runCheck('error','No pivot object(s) selected')
# set transforms/pivot to captured coordinates
def setPivotToManip_apply():
	# get trans
	transX = cmds.checkBox('nwSAK_modWorldSpaceTransXCB',q=True,v=True)
	transY = cmds.checkBox('nwSAK_modWorldSpaceTransYCB',q=True,v=True)
	transZ = cmds.checkBox('nwSAK_modWorldSpaceTransZCB',q=True,v=True)
	# get rotate
	rotateX = cmds.checkBox('nwSAK_modWorldSpaceRotateXCB',q=True,v=True)
	rotateY = cmds.checkBox('nwSAK_modWorldSpaceRotateYCB',q=True,v=True)
	rotateZ = cmds.checkBox('nwSAK_modWorldSpaceRotateZCB',q=True,v=True)
	# get scale
	scaleX = cmds.checkBox('nwSAK_modWorldSpaceScaleXCB',q=True,v=True)
	scaleY = cmds.checkBox('nwSAK_modWorldSpaceScaleYCB',q=True,v=True)
	scaleZ = cmds.checkBox('nwSAK_modWorldSpaceScaleZCB',q=True,v=True)
	# get selected
	sel = cmds.ls(sl=True, type='transform')
	manipPos = cmds.floatFieldGrp('nwSAK_manipPivot',q=True,v=True)
	targetTrans = cmds.floatFieldGrp('nwSAK_transPivots',q=True,v=True)
	targetRot = cmds.floatFieldGrp('nwSAK_rotPivots',q=True,v=True)
	targetScale = cmds.floatFieldGrp('nwSAK_scalePivots',q=True,v=True)
	types = cmds.radioButtonGrp('nwSAK_modmovTypeSelect',q=True,sl=True)
	if sel:
		if manipPos:
			if (types==1):
				# cycle
				for stuff in sel:
					# get select trans
					selTrans = cmds.xform(stuff,q=True,ws=True,t=True)
					selRot = cmds.xform(stuff,q=True,ws=True,ro=True)
					relScale = cmds.xform(stuff,q=True,r=True,s=True)
					wsScale = cmds.xform(stuff,q=True,ws=True,s=True)
					selScale = [((relScale[0])/(wsScale[0])),((relScale[1])/(wsScale[1])),((relScale[2])/(wsScale[2]))]
					targetWScale = [((targetScale[0])*(selScale[0])),((targetScale[1])*(selScale[1])),((targetScale[2])*(selScale[2]))]
					# set/reset array
					trans = []
					rotate = []
					scale = []
					### check for trans
					if (transX == 1):
						trans.append(manipPos[0])
					else:
						trans.append(selTrans[0])
					if (transY == 1):
						trans.append(manipPos[1])
					else:
						trans.append(selTrans[1])
					if (transZ == 1):
						trans.append(manipPos[2])
					else:
						trans.append(selTrans[2])
					### check for rot
					if (rotateX == 1):
						rotate.append(targetRot[0])
					else:
						rotate.append(selRot[0])
					if (rotateY == 1):
						rotate.append(targetRot[1])
					else:
						rotate.append(selRot[1])
					if (rotateZ == 1):
						rotate.append(targetRot[2])
					else:
						rotate.append(selRot[2])
					### check for scl
					if (scaleX == 1):
						scale.append(targetWScale[0])
					else:
						scale.append(relScale[0])
					if (scaleY == 1):
						scale.append(targetWScale[1])
					else:
						scale.append(relScale[1])
					if (scaleZ == 1):
						scale.append(targetWScale[2])
					else:
						scale.append(relScale[2])
					cmds.xform(stuff,ws=True,t=trans,ro=rotate)
					cmds.scale(scale[0],scale[1],scale[2],stuff)
				nmGUI_func.nmGUI_runCheck('complete','Selected transforms set to captured')
			else:
				# do pivot
				for obj in sel:
					cmds.xform(worldSpace=True, pivots=manipPos)
				# line
				nmGUI_func.nmGUI_runCheck('complete','Pivot(s) set to captured pivot position')
		# line
		else:
			nmGUI_func.nmGUI_runCheck('error','No captured target transforms/pivot')
	# line
	else:
		nmGUI_func.nmGUI_runCheck('error','Select a target to set transforms/pivot')
#check all
# lock trans all
def setPivotToManip_transAll():
	'''
	this function sets the translate axis boxes to checked or unchecked
	'''
	# get all
	all = cmds.checkBox('nwSAK_modWorldSpaceTransAllCB',q=True,v=True)
	### check all
	if (all == 1):
		cmds.checkBox('nwSAK_modWorldSpaceTransXCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceTransYCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceTransZCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceTransXCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceTransYCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceTransZCB',e=True,v=0)
# lock rot all
def setPivotToManip_rotAll():
	'''
	this function sets the rotate axis boxes to checked or unchecked
	'''
	# get all
	all = cmds.checkBox('nwSAK_modWorldSpaceRotateAllCB',q=True,v=True)
	### check all
	if (all == 1):
		cmds.checkBox('nwSAK_modWorldSpaceRotateXCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceRotateYCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceRotateZCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceRotateXCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceRotateYCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceRotateZCB',e=True,v=0)
# lock scale all
def setPivotToManip_scaleAll():
	'''
	this function sets the scale axis boxes to checked or unchecked
	'''
	# get all
	all = cmds.checkBox('nwSAK_modWorldSpaceScaleAllCB',q=True,v=True)
	### check all
	if (all == 1):
		cmds.checkBox('nwSAK_modWorldSpaceScaleXCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceScaleYCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceScaleZCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceScaleXCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceScaleYCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceScaleZCB',e=True,v=0)
