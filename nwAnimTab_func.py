'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
================================================================================
================================================================================
Author: Nic Wiederhold
Script: nwAnimTab_func.py
Collection: ghOst_SwissArmyKnife
Website: NA
Date Created: 8/29/14
Last Updated: 8/10/2015
================================================================================
================================================================================
					FUNCTIONS:
nwCreateghOstCam
nwAEcameraSetup













================================================================================
					HOW TO RUN:
import nwAnimTab_func
================================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#=======================#
#	  MAIN IMPORTS	#
#=======================#
# import maya commands
import maya.cmds as cmds 
# import maya mel commands
import maya.mel as mel
#=======================#
#   IMPORT FUNCTIONS	#
#=======================#
import nmGUI_func
# source ghOstCam.mel
#ghOstCam = mel.eval(source "dirname";
#                    dirname( "/Volumes/Macintosh HD/Users/Nic/Documents/maya/nixProjects/MEL/nic/ghOstCam.mel" );
#                    source "./ghOstCam.mel";
 #                   )
#=======================#
#	  FUNCTION	#
#=======================#
# Generate a ghOst camera setup
#def nwCreateghOstCam():
#	mel.eval(
## World Space Tool
# capture transforms/pivot coordinates
def captureManipPiv():
	mmc = cmds.manipMoveContext()
	cmds.setToolTo(mmc)
	manipLoc = cmds.manipMoveContext(mmc, q=True, p=True)
	rotObj = cmds.xform(q=True, ws=True, ro=True)
	posCopy = cmds.xform(q=True, ws=True, t=True)
	scaleCopy = cmds.xform(q=True, r=True, s=True)
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
		cmds.floatFieldGrp('nwSAK_manipPivotAni',e=True,v1=manipPos[0],v2=manipPos[1],v3=manipPos[2])
		cmds.floatFieldGrp('nwSAK_transPivotsAni',e=True,v1=transObj[0],v2=transObj[1],v3=transObj[2])
		cmds.floatFieldGrp('nwSAK_rotPivotsAni',e=True,v1=rotObj[0],v2=rotObj[1],v3=rotObj[2])
		cmds.floatFieldGrp('nwSAK_scalePivotsAni',e=True,v1=scaleObj[0],v2=scaleObj[1],v3=scaleObj[2])
	# line
	else:
		nmGUI_func.nmGUI_runCheck('error','No pivot object(s) selected')
# set transforms/pivot to captured coordinates
def setPivotToManip_apply():
	# get trans
	transX = cmds.checkBox('nwSAK_modWorldSpaceAniTransXCB',q=True,v=True)
	transY = cmds.checkBox('nwSAK_modWorldSpaceAniTransYCB',q=True,v=True)
	transZ = cmds.checkBox('nwSAK_modWorldSpaceAniTransZCB',q=True,v=True)
	# get rotate
	rotateX = cmds.checkBox('nwSAK_modWorldSpaceAniRotateXCB',q=True,v=True)
	rotateY = cmds.checkBox('nwSAK_modWorldSpaceAniRotateYCB',q=True,v=True)
	rotateZ = cmds.checkBox('nwSAK_modWorldSpaceAniRotateZCB',q=True,v=True)
	# get scale
	scaleX = cmds.checkBox('nwSAK_modWorldSpaceAniScaleXCB',q=True,v=True)
	scaleY = cmds.checkBox('nwSAK_modWorldSpaceAniScaleYCB',q=True,v=True)
	scaleZ = cmds.checkBox('nwSAK_modWorldSpaceAniScaleZCB',q=True,v=True)
	# get selected
	sel = cmds.ls(sl=True, type='transform')
	manipPos = cmds.floatFieldGrp('nwSAK_manipPivotAni',q=True,v=True)
	targetTrans = cmds.floatFieldGrp('nwSAK_transPivotsAni',q=True,v=True)
	targetRot = cmds.floatFieldGrp('nwSAK_rotPivotsAni',q=True,v=True)
	targetScale = cmds.floatFieldGrp('nwSAK_scalePivotsAni',q=True,v=True)
	types = cmds.radioButtonGrp('nwSAK_animovTypeSelect',q=True,sl=True)
	if sel:
		if manipPos:
			if (types==1):
				# cycle
				for stuff in sel:
					# get select trans
					selTrans = cmds.xform(stuff,q=True,ws=True,t=True)
					selRot = cmds.xform(stuff,q=True,ws=True,ro=True)
					selScale = cmds.xform(stuff,q=True,r=True,s=True)
					# set/reset array
					trans = []
					rotate = []
					scale = []
					### check for trans
					if (transX == 1):
						trans.append(targetTrans[0])
					else:
						trans.append(selTrans[0])
					if (transY == 1):
						trans.append(targetTrans[1])
					else:
						trans.append(selTrans[1])
					if (transZ == 1):
						trans.append(targetTrans[2])
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
						scale.append(targetScale[0])
					else:
						scale.append(selScale[0])
					if (scaleY == 1):
						scale.append(targetScale[1])
					else:
						scale.append(selScale[1])
					if (scaleZ == 1):
						scale.append(targetScale[2])
					else:
						scale.append(selScale[2])
					cmds.xform(stuff,ws=True,t=trans,ro=rotate)
					cmds.xform(stuff,r=True,s=scale)
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
	all = cmds.checkBox('nwSAK_modWorldSpaceAniTransAllCB',q=True,v=True)
	### check all
	if (all == 1):
		cmds.checkBox('nwSAK_modWorldSpaceAniTransXCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceAniTransYCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceAniTransZCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceAniTransXCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceAniTransYCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceAniTransZCB',e=True,v=0)
# lock rot all
def setPivotToManip_rotAll():
	'''
	this function sets the rotate axis boxes to checked or unchecked
	'''
	# get all
	all = cmds.checkBox('nwSAK_modWorldSpaceAniRotateAllCB',q=True,v=True)
	### check all
	if (all == 1):
		cmds.checkBox('nwSAK_modWorldSpaceAniRotateXCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceAniRotateYCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceAniRotateZCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceAniRotateXCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceAniRotateYCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceAniRotateZCB',e=True,v=0)
# lock scale all
def setPivotToManip_scaleAll():
	'''
	this function sets the scale axis boxes to checked or unchecked
	'''
	# get all
	all = cmds.checkBox('nwSAK_modWorldSpaceAniScaleAllCB',q=True,v=True)
	### check all
	if (all == 1):
		cmds.checkBox('nwSAK_modWorldSpaceAniScaleXCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceAniScaleYCB',e=True,v=1)
		cmds.checkBox('nwSAK_modWorldSpaceAniScaleZCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceAniScaleXCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceAniScaleYCB',e=True,v=0)
		cmds.checkBox('nwSAK_modWorldSpaceAniScaleZCB',e=True,v=0)
# toggle smooth mesh preview
def smoothPreviewToggle():
	# list all objects
	allObjects = cmds.ls(shapes=True)
	allMesh = []
	smoothed = []
	# get meshes
	for obj in allObjects:
	   if cmds.nodeType(obj) == 'mesh':
	     allMesh.append(obj)
	# get smoothed
	for node in allMesh:
		# check for notes
		list = cmds.attributeQuery('notes', node=node, ex=True)
		# notes dont exist
		if not list:
			cmds.select(node)
			disSm = cmds.displaySmoothness(query=True, polygonObject=1)
			# get smoothed
			if disSm == [3L]:
				print node
				smoothed.append(node)
				cmds.addAttr(node, ln='notes', sn='nts', dt='string')
				cmds.setAttr(node+'.notes', 'smoothed', type='string')
				cmds.select(cl=True)
			else:
				cmds.select(cl=True)
		# notes do exist
		else:
			# get notes
			note = cmds.getAttr(node+'.notes')
			# get smoothed
			if note == 'smoothed':
				smoothed.append(node)
	# toggle smooth mesh preview
	for shapes in smoothed:
		cmds.select(shapes)
		disSm = cmds.displaySmoothness(query=True, polygonObject=1)
		if disSm == [3L]:
			cmds.displaySmoothness(polygonObject=1)
		else:
			cmds.displaySmoothness(polygonObject=3)
# Create ghOst Camera
def nwCreateghOstCam():
	makeCam = cmds.camera(name='ghostCam')
	mel.eval('cameraMakeNode 2 "";')
	cmds.select(makeCam[0])
	# set new pivots for realistic panning.
	cmds.xform(rp=[0,-.4,0.3],sp=[0,-.4,0.3])
	cmds.select(makeCam[0]+'_aim')
	cmds.xform(rp=[0,-.4,0],sp=[0,-.4,0])
	# make ctrl and connect attributes.
	cmds.setAttr(makeCam[0]+'_group'+'.worldUpType', 4)
	camCtrl = cmds.circle(n=("'"+makeCam[0]+"'"+'Ctrl'), c=(0,0,0), nr=(0,1,0), sw=360, r=8)
	cmds.setAttr(camCtrl[0]+'.rx', l=True, k=False)
	cmds.setAttr(camCtrl[0]+'.ry', k=False)
	cmds.setAttr(camCtrl[0]+'.rz', k=False)
	cmds.setAttr(camCtrl[0]+'.sx', l=True, k=False)
	cmds.setAttr(camCtrl[0]+'.sy', l=True, k=False)
	cmds.setAttr(camCtrl[0]+'.sz', l=True, k=False)
	cmds.setAttr(camCtrl[0]+'.visibility', l=True, k=False)
	# add new ctrl attributes
	cmds.addAttr(ln='cameraScale', k=True)
	cmds.setAttr(camCtrl[0]+'.cameraScale', 1)
	cmds.addAttr(ln='cameraTruck', at="enum", en="Rotation")
	cmds.setAttr(camCtrl[0]+'.cameraTruck', channelBox=1)
	cmds.addAttr(ln='orbitY', k=True, at='doubleAngle')
	cmds.addAttr(ln='orbitX', k=True, at='doubleAngle')
	cmds.addAttr(ln='orbitZ', k=True, at='doubleAngle')
	cmds.addAttr(ln='sideTracking', at="enum", en="and Zoom")
	cmds.setAttr(camCtrl[0]+'.sideTracking', channelBox=1)
	cmds.addAttr(ln='trackZoom', k=True)
	cmds.addAttr(ln='trackY', k=True)
	cmds.addAttr(ln='trackX', k=True)
	cmds.setAttr(camCtrl[0]+'.trackZoom', 8)
	cmds.addAttr(ln='cameraLens', at="enum", en="Pan/Tilt")
	cmds.setAttr(camCtrl[0]+'.cameraLens', channelBox=1)
	cmds.addAttr(ln='panY', k=True, at='doubleAngle')
	cmds.addAttr(ln='panX', k=True, at='doubleAngle')
	cmds.addAttr(ln='tilt', k=True, at='doubleAngle')
	cmds.addAttr(ln='lens', at="enum", en="Settings")
	cmds.setAttr(camCtrl[0]+'.lens', channelBox=1)
	cmds.addAttr(ln='lensZoom', k=True)
	cmds.setAttr(camCtrl[0]+'.lensZoom', 35)
	cmds.parent(makeCam[0]+'_group', camCtrl[0])
	# connect new ctrl attributes
	cmds.connectAttr(camCtrl[0]+'.cameraScale', makeCam[0]+'.sx')
	cmds.connectAttr(camCtrl[0]+'.cameraScale', makeCam[0]+'.sy')
	cmds.connectAttr(camCtrl[0]+'.cameraScale', makeCam[0]+'.sz')
	cmds.connectAttr(camCtrl[0]+'.trackZoom', makeCam[0]+'.tz')
	cmds.connectAttr(camCtrl[0]+'.trackX', makeCam[0]+'_group'+'.tx')
	cmds.connectAttr(camCtrl[0]+'.trackY', makeCam[0]+'_group'+'.ty')
	cmds.setAttr(makeCam[0]+'_aim.tz', 0)
	cmds.connectAttr(camCtrl[0]+'.orbitY', makeCam[0]+'_group'+'.rx')
	cmds.connectAttr(camCtrl[0]+'.orbitX', camCtrl[0]+'.ry')
	cmds.connectAttr(camCtrl[0]+'.orbitZ', camCtrl[0]+'.rz')
	cmds.connectAttr(camCtrl[0]+'.panY', makeCam[0]+'_group'+'.offsetX')
	cmds.connectAttr(camCtrl[0]+'.panX', makeCam[0]+'_group'+'.offsetY')
	cmds.connectAttr(camCtrl[0]+'.tilt', makeCam[0]+'_group'+'.offsetZ')
	cmds.connectAttr(camCtrl[0]+'.lensZoom', makeCam[1]+'.focalLength')
	# lock the aim
	cmds.setAttr(makeCam[0]+'_aim.t', l=True)
	cmds.setAttr(makeCam[0]+'_aim.s', l=True)
	cmds.setAttr(makeCam[0]+'_aim.r', l=True)
	cmds.setAttr(makeCam[0]+'_aim.visibility',0, l=True)
	# create and connect new aim for visual feedback.
	aimLoc=cmds.spaceLocator(n=makeCam[0]+"_aimLoc")
	cmds.parent(aimLoc, makeCam[0]+'_group')
	cmds.setAttr(aimLoc[0]+'.displayRotatePivot', 1)
	cmds.setAttr(aimLoc[0]+'Shape.visibility', 0)
	cmds.setAttr(aimLoc[0]+'.visibility', l=True, k=False)
	cmds.setAttr(aimLoc[0]+'.tx', l=True, k=False)
	cmds.setAttr(aimLoc[0]+'.ty', l=True, k=False)
	cmds.setAttr(aimLoc[0]+'.tz', l=True, k=False)
	cmds.setAttr(aimLoc[0]+'.sx', l=True, k=False)
	cmds.setAttr(aimLoc[0]+'.sy', l=True, k=False)
	cmds.setAttr(aimLoc[0]+'.sz', l=True, k=False)
	cmds.setAttr(aimLoc[0]+'.rx', l=True, k=False)
	cmds.setAttr(aimLoc[0]+'.ry', l=True, k=False)
	cmds.setAttr(aimLoc[0]+'.rz', l=True, k=False)
	cmds.select(camCtrl)
# Setup AE export cameras
def nwAEcameraSetup():
	#get selected ghOstcam control
	camSel=cmds.listRelatives(ad=1, typ='camera')
	# get/select camera transforms
	if camSel:
		cmds.select(camSel)
		gCam=cmds.listRelatives(p=1)
		cmds.select(gCam)
		# duplicate for AE export cams
		newCam=cmds.duplicate(gCam, name="camera"+"0#")
		for nCam in newCam:
			cmds.setAttr(nCam+'.t', l=False)
			cmds.setAttr(nCam+'.r', l=False)
			cmds.setAttr(nCam+'.s', l=False)
			cmds.setAttr(nCam+'.tx', l=False)
			cmds.setAttr(nCam+'.rx', l=False)
			cmds.setAttr(nCam+'.sx', l=False)
			cmds.setAttr(nCam+'.ty', l=False)
			cmds.setAttr(nCam+'.ry', l=False)
			cmds.setAttr(nCam+'.sy', l=False)
			cmds.setAttr(nCam+'.tz', l=False)
			cmds.setAttr(nCam+'.rz', l=False)
			cmds.setAttr(nCam+'.sz', l=False)
		cmds.parent(newCam, world=True)
		# loop
		i=0
		# parent constrain new duplicate cams to respective ghOstCam
		for cam in newCam:
			cmds.parentConstraint(gCam[i], cam)
			gCamShape=cmds.listRelatives(gCam[i], shapes=True)
			camShape=cmds.listRelatives(cam, shapes=True)
			cmds.connectAttr(gCamShape[0]+'.focalLength', camShape[0]+'.focalLength')
			cmds.connectAttr(gCamShape[0]+'.centerOfInterest', camShape[0]+'.centerOfInterest')
			i+=1
		# get time slider for bake
		minTime=cmds.playbackOptions(query=True, min=True)
		maxTime=cmds.playbackOptions(query=True, max=True)
		timeSlider=[int(minTime), int(maxTime)]
		# bake animation on cams
		cmds.bakeResults(newCam, simulation=True, time=(timeSlider[0], timeSlider[1]), disableImplicitControl=True, preserveOutsideKeys=True, sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False, removeBakedAnimFromLayer=False, bakeOnOverrideLayer=False, minimizeRotation=True, controlPoints=False, shape=True)
		# delete constraints
		constraints = ['pointConstraint','aimConstraint','orientConstraint','scaleConstraint','parentConstraint','geometryConstraint','tangentConstraint','poleVectorConstraint','normalConstraint','pointOnPolyConstraint']
		# cycle
		for stuff in newCam:
			connections = cmds.listRelatives(stuff)
			if (connections):
				for item in connections:
					if (cmds.objExists(item)):
						objType = cmds.objectType(item)
						if objType in constraints:
							cmds.delete(item)
		nmGUI_func.nmGUI_runCheck('complete','Selected ghOstCam(s) duplicated and baked for AE export')
	else:
		nmGUI_func.nmGUI_runCheck('error','Select one or more ghOstCam controls')
# Xray view utilities
def nwXrayAllToggle():
	# list all objects
	allObjects = cmds.ls(shapes=True)
	allMesh = []
	xRayDisp = []
	# get meshes
	for obj in allObjects:
	   if cmds.nodeType(obj) == 'mesh':
	     allMesh.append(obj)
	# get smoothed
	for shape in allMesh:
		# check for notes
		list = cmds.attributeQuery('notes', node=shape, ex=True)
		# notes dont exist
		if not list:
			cmds.select(shape)
			xRay = cmds.displaySurface(query=True, xRay=True)
			# get mesh with xRay display turned on
			if xRay == [True]:
				xRayDisp.append(shape)
				cmds.addAttr(shape, ln='notes', sn='nts', dt='string')
				cmds.setAttr(shape+'.notes', 'xray', type='string')
				cmds.select(cl=True)
			else:
				cmds.select(cl=True)
		# notes do exist
		else:
			# get notes
			note = cmds.getAttr(shape+'.notes')
			# get xray displayed
			if note == 'xray':
				xRayDisp.append(shape)
	# toggle xray display
	for shapes in xRayDisp:
		cmds.select(shapes)
		xRay = cmds.displaySurface(query=True, xRay=True)
		if xRay == [True]:
			cmds.displaySurface(xRay=False)
		else:
			cmds.displaySurface(xRay=True)
	cmds.select(xRayDisp)
# single xray display toggle
def nwXraySelectedToggle():
	# get selected
	sel=cmds.ls(sl=1)
	xRayDisp = []
	# query xray mode
	if sel:
		for shape in sel:
			cmds.select(shape)
			xRay = cmds.displaySurface(query=True, xRay=True)
			if xRay == [False]:
				cmds.displaySurface(xRay=True)
			else:
				cmds.displaySurface(xRay=False)
	cmds.select(sel)




