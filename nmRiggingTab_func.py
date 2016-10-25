'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
================================================================================
================================================================================
Author: Nole Murphy
Ammended: Nic Wiederhold
Script: nmRiggingTab_func.py
Collection: ghOst_SwissArmyKnife
Website: www.nm3d.net
Date Created: 3/11/2011
Last Updated: 5/24/2016
================================================================================
================================================================================
				    FUNCTIONS:
nmJoints_removeJoint
nmJoints_insertJoint
nmJoints_joint
nmJoints_orientJoint
nmMirrorJoint_mirror
nmLocalJointScale_scale
nmGlobalJointScale_scale
nmBlender_blend


Nix functions:
nwToggleLockNode
nwControls_ball
nwControls_diamond
nwSpecialControls_addOffset
nwAtt_SimpleAdd
nwAtt_Shiftup
nwAtt_ShiftDown
nwSpecialControls_CurveControls
nwSpecialControls_EdgeJointSpline


================================================================================
				    HOW TO RUN:
import nmRiggingTab_func
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
### joints ###
# remove joint
def nmJoints_removeJoint():
	'''
	this function will remove the selected joints.
	'''
	# sel
	sel = cmds.ls(sl=True)
	if sel:
		# remove all selected joints
		for stuff in sel:
			cmds.removeJoint(stuff)
# insert joint
def nmJoints_insertJoint():
	'''
	this function will insert a joint at the given position.
	'''
	cmds.InsertJointTool()
# create joint
def nmJoints_joint():
	'''
	this function will create a joint.
	'''
	# get options
	mel.eval('JointToolOptions;')
# create joint
def nmJoints_orientJoint():
	'''
	this function will bring up the orient joint options.
	'''
	# get options
	mel.eval('OrientJointOptions;')
# mirror joint
def nmMirrorJoint_mirror():
	'''
	this function will mirror all selected joints and utilizes the
	search and replace function as well.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# get axis
	axis = cmds.radioButtonGrp('nmSAK_rigMirrorAxis',q=True,sl=True)
	# get actions
	action = cmds.radioButtonGrp('nmSAK_rigMirrorAction',q=True,sl=True)
	# get search
	search = cmds.textFieldGrp('nmSAK_rigMirrorSearch',q=True,tx=True)
	# get replace
	replace = cmds.textFieldGrp('nmSAK_rigMirrorReplace',q=True,tx=True)	
	# check
	if sel:
		# mirror selected
		for stuff in sel:
			if (cmds.objectType(stuff)=='joint'):
				if ((search == '') or (replace == '')):
					if (action == 1):
						if (axis == 1):
							cmds.mirrorJoint(stuff,mxy=True,myz=False,mxz=False,mb=True)
						elif (axis == 2):
							cmds.mirrorJoint(stuff,mxy=False,myz=True,mxz=False,mb=True)
						elif (axis == 3):
							cmds.mirrorJoint(stuff,mxy=False,myz=False,mxz=True,mb=True)
					elif (action == 2):
						if (axis == 1):
							cmds.mirrorJoint(stuff,mxy=True,myz=False,mxz=False,mb=False)
						elif (axis == 2):
							cmds.mirrorJoint(stuff,mxy=False,myz=True,mxz=False,mb=False)
						elif (axis == 3):
							cmds.mirrorJoint(stuff,mxy=False,myz=False,mxz=True,mb=False)
				else:
					if (action == 1):
						if (axis == 1):
							cmds.mirrorJoint(stuff,mxy=True,myz=False,mxz=False,mb=True,sr=[search,replace])
						elif (axis == 2):
							cmds.mirrorJoint(stuff,mxy=False,myz=True,mxz=False,mb=True,sr=[search,replace])
						elif (axis == 3):
							cmds.mirrorJoint(stuff,mxy=False,myz=False,mxz=True,mb=True,sr=[search,replace])
					elif (action == 2):
						if (axis == 1):
							cmds.mirrorJoint(stuff,mxy=True,myz=False,mxz=False,mb=False,sr=[search,replace])
						elif (axis == 2):
							cmds.mirrorJoint(stuff,mxy=False,myz=True,mxz=False,mb=False,sr=[search,replace])
						elif (axis == 3):
							cmds.mirrorJoint(stuff,mxy=False,myz=False,mxz=True,mb=False,sr=[search,replace])
				# line
				nmGUI_func.nmGUI_runCheck('complete','Selected joints have been mirrored.')
			else:
				# line
				nmGUI_func.nmGUI_runCheck('error','Please select joints only.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more joints.')
# local joint scale
def nmLocalJointScale_scale():
	'''
	this function will set the local joint scale.
	'''
	# get
	select = cmds.radioButtonGrp('nmSAK_rigJntLocalSel',q=True,sl=True)
	radius = cmds.floatSliderGrp('nmSAK_rigJntLocFLG',q=True,v=True)
	# sel
	sel = cmds.ls(sl=True)
	### sel
	if sel:
		### check whole chain
		if (select == 2):
			sels = cmds.ls(sl=True,dag=True)
		else:
			sels = cmds.ls(sl=True)
		# loop for setting joint radius
		for jnt in sels:
			if (cmds.objectType(jnt)=='joint'):
				# set joint size
				cmds.setAttr(jnt+'.radius',radius)
# global joint scale
def nmGlobalJointScale_scale():
	'''
	this function will set the global joint scale.
	'''
	# get
	value = cmds.floatSliderGrp('nmSAK_rigJntGlobScale',q=True,v=True)
	# set
	cmds.jointDisplayScale(value)
# load bind chain
def nmBlender_bind():
	'''
	this function loads the selected bind joint into the chain blender.
	'''
	# Sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel)==1):
		if (cmds.objectType(sel[0])=='joint'):
			cmds.textFieldGrp('nmSAK_rigBlendBndTFG',e=True,tx=sel[0])
			nmGUI_func.nmGUI_runCheck('complete','Bind joint loaded.')
		else:
			nmGUI_func.nmGUI_runCheck('error','Please only load joints.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one bind joint to load.')
# load fk chain
def nmBlender_fk():
	'''
	this function loads the selected fk joint in the the chain blender.
	'''
	# Sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel)==1):
		if (cmds.objectType(sel[0])=='joint'):
			cmds.textFieldGrp('nmSAK_rigBlendFkTFG',e=True,tx=sel[0])
			nmGUI_func.nmGUI_runCheck('complete','FK joint loaded.')
		else:
			nmGUI_func.nmGUI_runCheck('error','Please only load joints.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one FK joint to load.')
# load ik chain
def nmBlender_ik():
	'''
	this function loads the selected ik joint in the chain blender.
	'''
	# Sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel)==1):
		if (cmds.objectType(sel[0])=='joint'):
			cmds.textFieldGrp('nmSAK_rigBlendIkTFG',e=True,tx=sel[0])
			nmGUI_func.nmGUI_runCheck('complete','IK joint loaded.')
		else:
			nmGUI_func.nmGUI_runCheck('error','Please only load joints.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one IK joint to load.')
# blender
def nmBlender_blend():
	'''
	this function blends the bind, ik, fk joints together creating
	an ik/fk switch.
	'''
	# get
	whole = cmds.checkBox('nmSAK_rigBlendWholeChainCB',q=True,v=True)
	bind = cmds.textFieldGrp('nmSAK_rigBlendBndTFG',q=True,tx=True)
	ik = cmds.textFieldGrp('nmSAK_rigBlendIkTFG',q=True,tx=True)
	fk = cmds.textFieldGrp('nmSAK_rigBlendFkTFG',q=True,tx=True)
	# blend
	if not((bind=='')or(ik=='')or(fk=='')):
		if (whole==1):
			# get
			hBind = cmds.ls(bind,dag=True)
			hIk = cmds.ls(ik,dag=True)
			hFk = cmds.ls(fk,dag=True)
			wBind=[]
			wIk=[]
			wFk=[]
			# get joints
			if (len(hBind)>0):
				for stuff in hBind:
					if (cmds.objectType(stuff)=='joint'):
						wBind.append(stuff)
			if (len(hIk)>0):
				for stuff in hIk:
					if (cmds.objectType(stuff)=='joint'):
						wIk.append(stuff)
			if (len(hFk)>0):
				for stuff in hFk:
					if (cmds.objectType(stuff)=='joint'):
						wFk.append(stuff)
			# counter
			i=0
			# cycle
			if ((cmds.objectType(bind)=='joint')and(cmds.objectType(ik)=='joint')and(cmds.objectType(fk)=='joint')):
				while(i < ((len(wBind))and(len(wIk))and(len(wFk)))):
					if not(cmds.objExists(wBind[i]+'_blend')):
						# create blend color
						cmds.shadingNode('blendColors',au=True,n=wBind[i]+'_blend')
						# connect bind,ik,fk
						cmds.connectAttr(wIk[i]+'.rotate',wBind[i]+'_blend.color2',f=True)
						cmds.connectAttr(wFk[i]+'.rotate',wBind[i]+'_blend.color1',f=True)
						cmds.connectAttr(wBind[i]+'_blend.output',wBind[i]+'.rotate',f=True)
						# line
						nmGUI_func.nmGUI_runCheck('complete','Whole joint chain blend complete.')
					else:
						nmGUI_func.nmGUI_runCheck('error','"'+wBind[i]+'_blend" node already exists.')
					# counter
					i+=1
			else:
				nmGUI_func.nmGUI_runCheck('error','Please only load joints.')
		else:
			if ((cmds.objectType(bind)=='joint')and(cmds.objectType(ik)=='joint')and(cmds.objectType(fk)=='joint')):
				if not(cmds.objExists(bind+'_blend')):
					# create blend color
					cmds.shadingNode('blendColors',au=True,n=bind+'_blend')
					# connect bind,ik,fk
					cmds.connectAttr(ik+'.rotate',bind+'_blend.color2',f=True)
					cmds.connectAttr(fk+'.rotate',bind+'_blend.color1',f=True)
					cmds.connectAttr(bind+'_blend.output',bind+'.rotate',f=True)
					# line
					nmGUI_func.nmGUI_runCheck('complete','Joint blend complete.')
				else:
					nmGUI_func.nmGUI_runCheck('error','"'+bind+'_blend" node already exists.')
				
			else:
				nmGUI_func.nmGUI_runCheck('error','Please only load joints.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please load all blend joints.')
		
### controls ###
# point constraint
def nmConstraints_point():
	'''
	this function creates a point constraint between the selected
	objects.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel) > 1):
		# offset
		if (cmds.checkBox('nmSAK_rigConOffSetCB',q=True,v=True)==1):
			cmds.pointConstraint(mo=True)
		else:
			cmds.pointConstraint(mo=False)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Point constraint created.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select two or more objects.')
# orient constraint
def nmConstraints_orient():
	'''
	this function creates an orient constraint between the selected
	objects.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel) > 1):
		# offset
		if (cmds.checkBox('nmSAK_rigConOffSetCB',q=True,v=True)==1):
			cmds.orientConstraint(mo=True)
		else:
			cmds.orientConstraint(mo=False)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Orient constraint created.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select two or more objects.')
# scale constraint
def nmConstraints_scale():
	'''
	the function creates a scale constraint between the selected
	objects.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel) > 1):
		# offset
		if (cmds.checkBox('nmSAK_rigConOffSetCB',q=True,v=True)==1):
			cmds.scaleConstraint(mo=True)
		else:
			cmds.scaleConstraint(mo=False)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Scale constraint created.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select two or more objects.')
# parent constraint
def nmConstraints_parent():
	'''
	this function creates a parent constraint between the selected
	objects.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel) > 1):
		# offset
		if (cmds.checkBox('nmSAK_rigConOffSetCB',q=True,v=True)==1):
			cmds.parentConstraint(mo=True)
		else:
			cmds.parentConstraint(mo=False)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Parent constraint created.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select two or more objects.')
# pole vector constraint
def nmConstraints_poleVector():
	'''
	this functions creates a pole vector constraint between the selected
	objects.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel) > 1):
		# create
		cmds.poleVectorConstraint()
		# line
		nmGUI_func.nmGUI_runCheck('complete','Pole vector constraint created.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select two or more objects.')
# aim options
def nmConstraints_aimOptions():
	'''
	this function brings up the aim constraint options.
	'''
	mel.eval('AimConstraintOptions;')
# delete constraint
def nmConstraints_deleteConstraints():
	'''
	this function will delete all constraints to the selected
	objects and will preserve empty groups.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# constraint list
	constraints = ['pointConstraint','aimConstraint','orientConstraint','scaleConstraint','parentConstraint','geometryConstraint','tangentConstraint','poleVectorConstraint','normalConstraint','pointOnPolyConstraint']
	# cycle
	if sel:
		for stuff in sel:
		    connections = cmds.listConnections(stuff,s=True,d=False)
		    if (connections):
			    for item in connections:
				    if (cmds.objExists(item)):
					    objType = cmds.objectType(item)
					    if objType in constraints:
						    cmds.delete(item)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Constraints deleted.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')
# cluster
def nmEasyCluster_cluster():
	'''
	this function will cluster the selected objects given the selected
	option.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# get
	option = cmds.radioButtonGrp('nmSAK_rigClusterOptionsRBG',q=True,sl=True)
	clusters=[]
	# check
	if sel:
		if (option == 1):
			name = sel[0].split('.')[0]
			cluster = cmds.cluster(n=name,en=1)
			clusters.append(cluster[1])
		else:
			for stuff in sel:
				name = stuff.split('.')[0]
				cluster = cmds.cluster(stuff,n=name,en=1)
				clusters.append(cluster[1])
		if (clusters):
			cmds.select(clusters,r=True)
			# line
			nmGUI_func.nmGUI_runCheck('complete','Selected objects have been clustered.')
		else:
			# line
			nmGUI_func.nmGUI_runCheck('error','No clusters were created.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')
# cluster curve
def nmEasyCluster_clusterCurve():
	'''
	this function will place clusters on all of the cv's on the 
	selected curves.
	'''
	# sel
	sel = cmds.ls(sl=True)
	clusters = []
	# check
	if sel:
		# cycle
		for stuff in sel:
			shapes = cmds.listRelatives(stuff,s=True)
			if (shapes):
				dummyShapes=[]
				for shape in shapes:
					if (cmds.objectType(shape)=='nurbsCurve'):
						dummyShapes.append(shape)
				if (dummyShapes):
					deg = cmds.getAttr(stuff+'.degree')
					span = cmds.getAttr(stuff+'.spans')
					cvNum = deg+span
					# counter
					i=0
					# loop through the cv's and place a cluster
					while (i < cvNum):
						temp = cmds.cluster(stuff+'.cv['+str(i)+']',n=stuff+'_cluster'+str(i),en=1)
						clusters.append(temp[1])
						# counter
						i+=1
		if (clusters):
			# sel clear
			cmds.select(clusters,r=True)
			# line
			nmGUI_func.nmGUI_runCheck('complete','Selected curves have been clustered.')
		else:
			nmGUI_func.nmGUI_runCheck('error','No clusters were created.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one or more curves.')
# pin load mesh
def nmPinUp_loadMesh():
	'''
	this function loads the base mesh for pinning controls or creating
	follicles.
	'''
	# Sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel)==1):
		if (cmds.listRelatives(sel[0],s=True)):
			shapes = cmds.listRelatives(sel[0],s=True)
			types = []
			for stuff in shapes:
				type = cmds.objectType(stuff)
				types.append(type)
			if 'mesh' in types:
				cmds.textFieldGrp('nmSAK_rigPinMeshTFG',e=True,tx=sel[0])
				nmGUI_func.nmGUI_runCheck('complete','Pin mesh loaded.')
			elif 'nurbsSurface' in types:
				cmds.textFieldGrp('nmSAK_rigPinMeshTFG',e=True,tx=sel[0])
				nmGUI_func.nmGUI_runCheck('complete','Pin mesh loaded.')
			elif 'subdiv' in types:
				cmds.textFieldGrp('nmSAK_rigPinMeshTFG',e=True,tx=sel[0])
				nmGUI_func.nmGUI_runCheck('complete','Pin mesh loaded.')
			else:
				nmGUI_func.nmGUI_runCheck('error','Please only load geometry meshes.')
		else:
			nmGUI_func.nmGUI_runCheck('error','Please only load geometry meshes.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one mesh to load.')
# pin selected
def nmPinUp_pin():
	'''
	this function pins the selected objects to the loaded geo mesh.
	'''
	# get
	mesh = cmds.textFieldGrp('nmSAK_rigPinMeshTFG',q=True,tx=True)
	# Sel
	sel = cmds.ls(sl=True)
	# check
	if not (mesh==''):
		if sel:
			# get mesh shape
			meshShape = cmds.listRelatives(mesh,s=True)[0]
			# dupe mesh and get shape
			meshCopy = cmds.duplicate(mesh,n=mesh+'_dupMesh')
			copyShape = cmds.listRelatives(meshCopy[0],s=True)[0]
			# unlock main attrs
			attr = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
			for stuff in attr:
				cmds.setAttr(meshCopy[0]+stuff,l=False)
			# parent to world
			parent = cmds.listRelatives(meshCopy[0],p=True)
			if (parent):
				cmds.parent(meshCopy[0],w=True)
			# cycle
			for stuff in sel:
				# get
				ctrlPivot = cmds.xform(stuff,q=True,ws=True,rp=True)
				# create node
				cposNode = cmds.createNode('closestPointOnMesh',n=stuff+'_cposNode')
				cmds.connectAttr(copyShape+'.outMesh',cposNode+'.inMesh',f=True)
				cmds.setAttr(cposNode+'.inPositionX',ctrlPivot[0])
				cmds.setAttr(cposNode+'.inPositionY',ctrlPivot[1])
				cmds.setAttr(cposNode+'.inPositionZ',ctrlPivot[2])
				u = cmds.getAttr(cposNode+'.parameterU')
				v = cmds.getAttr(cposNode+'.parameterV')
				# create follicle
				folShape = cmds.createNode('follicle',n=stuff+'_follicleShape')
				fol = cmds.listRelatives(folShape,p=True)[0]
				# connect
				cmds.connectAttr(meshShape+'.outMesh',folShape+'.inputMesh')
				cmds.connectAttr(meshShape+'.worldMatrix[0]',folShape+'.inputWorldMatrix')
				cmds.connectAttr(folShape+'.outTranslate',fol+'.translate')
				cmds.connectAttr(folShape+'.outRotate',fol+'.rotate')
				# set
				cmds.setAttr(folShape+'.parameterU',u)
				cmds.setAttr(folShape+'.parameterV',v)
				# place control and connect
				cmds.pointConstraint(fol,stuff,mo=False)
				cmds.delete(stuff,cn=True)
				cmds.xform(stuff,os=True,ro=(0,0,0))
				if not(cmds.objExists(stuff+'_null_1')):
					grp = cmds.group(stuff,n=stuff+'_revNull_0',r=True)
					grp2 = cmds.group(grp,n=stuff+'_null_1',r=True)
					cmds.makeIdentity(grp2,a=True,t=1,r=1,s=1,n=0)
					# pin
					cmds.parentConstraint(fol,grp2,mo=True)
					revMD = cmds.createNode('multiplyDivide',n=stuff+'_rev_MD')
					cmds.setAttr(revMD+".input2X",-1) 
					cmds.setAttr(revMD+".input2Y",-1)
					cmds.setAttr(revMD+".input2Z",-1)
					cmds.connectAttr(stuff+'.t',revMD+'.input1')
					cmds.connectAttr(revMD+'.output',grp+'.t')
				# delete cpos
				cmds.delete(cposNode)
			# delete
			cmds.delete(meshCopy)
			# select
			cmds.select(sel,r=True)
		else:
			nmGUI_func.nmGUI_runCheck('error','Please select one or more controls to pin.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please load a geometry mesh.')

# create Follicle
def nmPinUp_follicle():
	'''
	this function creates a follicle at the selected objects on the
	surface of the loaded geo mesh.
	'''
	# get
	mesh = cmds.textFieldGrp('nmSAK_rigPinMeshTFG',q=True,tx=True)
	# Sel
	sel = cmds.ls(sl=True)
	# check
	if not (mesh==''):
		if sel:
			# get mesh shape
			meshShape = cmds.listRelatives(mesh,s=True)[0]
			# dupe mesh and get shape
			meshCopy = cmds.duplicate(mesh,n=mesh+'_dupMesh')
			copyShape = cmds.listRelatives(meshCopy[0],s=True)[0]
			# unlock main attrs
			attr = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
			for stuff in attr:
				cmds.setAttr(meshCopy[0]+stuff,l=False)
			# parent to world
			parent = cmds.listRelatives(meshCopy[0],p=True)
			if (parent):
				cmds.parent(meshCopy[0],w=True)
			# cycle
			for stuff in sel:
				# get
				ctrlPivot = cmds.xform(stuff,q=True,ws=True,rp=True)
				# create node
				cposNode = cmds.createNode('closestPointOnMesh',n=mesh+'_cposNode')
				cmds.connectAttr(copyShape+'.outMesh',cposNode+'.inMesh',f=True)
				cmds.setAttr(cposNode+'.inPositionX',ctrlPivot[0])
				cmds.setAttr(cposNode+'.inPositionY',ctrlPivot[1])
				cmds.setAttr(cposNode+'.inPositionZ',ctrlPivot[2])
				u = cmds.getAttr(cposNode+'.parameterU')
				v = cmds.getAttr(cposNode+'.parameterV')
				# create follicle
				folShape = cmds.createNode('follicle',n=mesh+'_follicleShape')
				fol = cmds.listRelatives(folShape,p=True)[0]
				# connect
				cmds.connectAttr(meshShape+'.outMesh',folShape+'.inputMesh')
				cmds.connectAttr(meshShape+'.worldMatrix[0]',folShape+'.inputWorldMatrix')
				cmds.connectAttr(folShape+'.outTranslate',fol+'.translate')
				cmds.connectAttr(folShape+'.outRotate',fol+'.rotate')
				# set
				cmds.setAttr(folShape+'.parameterU',u)
				cmds.setAttr(folShape+'.parameterV',v)
				# place control and connect
				loc = cmds.spaceLocator(n=fol+'_loc')[0]
				cmds.pointConstraint(fol,loc,mo=False)
				cmds.orientConstraint(stuff,loc,mo=False)
				cmds.delete(loc,cn=True)
				cmds.parent(loc,fol)
				# lock loc
				attr = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
				for item in attr:
					cmds.setAttr(loc+item,l=True,k=False,cb=True)
				# delete cpos
				cmds.delete(cposNode)
			# delete
			cmds.delete(meshCopy)
			# select
			cmds.select(sel,r=True)
		else:
			nmGUI_func.nmGUI_runCheck('error','Please select one or more objects to place a follicle.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please load a geometry mesh.')
# curve tool
def nmCurves_curveTool():
	'''
	this function brings up the create curve options.
	'''
	# load tool
	mel.eval('CVCurveToolOptions;')
# combine curves
def nmCurves_combine():
	'''
	this function will combine any selected curves.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel) > 1):
		sels = cmds.ls(sl=True)
		sels.remove(sels[0])
		# freeze
		cmds.makeIdentity(a=True,t=1,r=1,s=1,n=0)
		# delete hist
		cmds.delete(ch=True)
		for stuff in sels:
			if (cmds.listRelatives(stuff,s=True)):
				# get shapes
				shape = cmds.listRelatives(stuff,s=True,pa=True)
				# parent
				cmds.parent(shape,sel[0],add=True,s=True)
				# delete old
				cmds.delete(stuff)
		# sel
		cmds.select(sel[0],r=True)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Selected curves have been combined.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select two or more curves.')
# rebuild curve options
def nmCurves_rebuildOptions():
	'''
	this function brings up the rebuild curve options.
	'''
	# load tool
	mel.eval('RebuildCurveOptions;')
# text me section
def nmTextMe_create():
	'''
	this function will create text curves given the font.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# get
	text = cmds.textFieldGrp('nmSAK_rigTextCurvesTFG',q=True,tx=True)
	# create
	if not(text==''):
		if (sel):
			texts = []
			for stuff in sel:
				curves = []
				create = cmds.textCurves(f='Times New Roman',t=text)
				listRel = cmds.listRelatives(create[0],ad=True)
				# cycle
				for item in listRel:
					if (cmds.listRelatives(item,s=True)):
						curves.append(item)
				# combine
				cmds.parent(curves,w=True)
				cmds.delete(create[0])
				cmds.select(curves)
				nmCurves_combine()
				cmds.xform(cp=True)
				cmds.delete(ch=True)
				# move
				temp = cmds.ls(sl=True)
				cmds.parentConstraint(stuff,temp[0],mo=False)
				cmds.delete(temp[0],cn=True)
				texts.append(temp[0])
				cmds.select(cl=True)
				# line
				nmGUI_func.nmGUI_runCheck('complete','Text curves have been created.')
			if (texts):
				cmds.select(texts,r=True)
		else:
			curves = []
			create = cmds.textCurves(f='Times New Roman',t=text)
			listRel = cmds.listRelatives(create[0],ad=True)
			# cycle
			for stuff in listRel:
				if (cmds.listRelatives(stuff,s=True)):
					curves.append(stuff)
			# combine
			cmds.parent(curves,w=True)
			cmds.delete(create[0])
			cmds.select(curves)
			nmCurves_combine()
			cmds.xform(cp=True)
			cmds.delete(ch=True)
			# line
			nmGUI_func.nmGUI_runCheck('complete','Text curves have been created.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please enter a text string to create.')
# text options
def nmTextMe_textOptions():
	'''
	this function will bring up the create text options.
	'''	
	mel.eval('CreateTextOptions;')
# lock and hide
def nmLockHide_lockHide():
	'''
	this function will lock and hide the selected attributes on
	the selected objects.
	'''
	# get trans
	transX = cmds.checkBox('nmSAK_rigLockHideTransXCB',q=True,v=True)
	transY = cmds.checkBox('nmSAK_rigLockHideTransYCB',q=True,v=True)
	transZ = cmds.checkBox('nmSAK_rigLockHideTransZCB',q=True,v=True)
	# get rotate
	rotateX = cmds.checkBox('nmSAK_rigLockHideRotateXCB',q=True,v=True)
	rotateY = cmds.checkBox('nmSAK_rigLockHideRotateYCB',q=True,v=True)
	rotateZ = cmds.checkBox('nmSAK_rigLockHideRotateZCB',q=True,v=True)
	# get scale
	scaleX = cmds.checkBox('nmSAK_rigLockHideScaleXCB',q=True,v=True)
	scaleY = cmds.checkBox('nmSAK_rigLockHideScaleYCB',q=True,v=True)
	scaleZ = cmds.checkBox('nmSAK_rigLockHideScaleZCB',q=True,v=True)
	# get vis
	vis = cmds.checkBox('nmSAK_rigLockHideVisCB',q=True,v=True)
	# set all translate
	if ((transX == 1)and(transY == 1)and(transZ == 1)):
		cmds.checkBox('nmSAK_rigLockHideTransAllCB',e=True,v=1)
	else:
		cmds.checkBox('nmSAK_rigLockHideTransAllCB',e=True,v=0)
	# set all rotate
	if ((rotateX == 1)and(rotateY == 1)and(rotateZ == 1)):
		cmds.checkBox('nmSAK_rigLockHideRotateAllCB',e=True,v=1)
	else:
		cmds.checkBox('nmSAK_rigLockHideRotateAllCB',e=True,v=0)
	# set all scale
	if ((scaleX == 1)and(scaleY == 1)and(scaleZ == 1)):
		cmds.checkBox('nmSAK_rigLockHideScaleAllCB',e=True,v=1)
	else:
		cmds.checkBox('nmSAK_rigLockHideScaleAllCB',e=True,v=0)
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		# cycle
		for stuff in sel:
			try:
				### check for trans
				if (transX == 1):
					cmds.setAttr(stuff+'.tx',l=True)
					cmds.setAttr(stuff+'.tx',k=False)
				else:
					cmds.setAttr(stuff+'.tx',l=False)
					cmds.setAttr(stuff+'.tx',k=True)
				if (transY == 1):
					cmds.setAttr(stuff+'.ty',l=True)
					cmds.setAttr(stuff+'.ty',k=False)
				else:
					cmds.setAttr(stuff+'.ty',l=False)
					cmds.setAttr(stuff+'.ty',k=True)
				if (transZ == 1):
					cmds.setAttr(stuff+'.tz',l=True)
					cmds.setAttr(stuff+'.tz',k=False)
				else:
					cmds.setAttr(stuff+'.tz',l=False)
					cmds.setAttr(stuff+'.tz',k=True)
				### check for rot
				if (rotateX == 1):
					cmds.setAttr(stuff+'.rx',l=True)
					cmds.setAttr(stuff+'.rx',k=False)
				else:
					cmds.setAttr(stuff+'.rx',l=False)
					cmds.setAttr(stuff+'.rx',k=True)
				if (rotateY == 1):
					cmds.setAttr(stuff+'.ry',l=True)
					cmds.setAttr(stuff+'.ry',k=False)
				else:
					cmds.setAttr(stuff+'.ry',l=False)
					cmds.setAttr(stuff+'.ry',k=True)
				if (rotateZ == 1):
					cmds.setAttr(stuff+'.rz',l=True)
					cmds.setAttr(stuff+'.rz',k=False)
				else:
					cmds.setAttr(stuff+'.rz',l=False)
					cmds.setAttr(stuff+'.rz',k=True)
				### check for scl
				if (scaleX == 1):
					cmds.setAttr(stuff+'.sx',l=True)
					cmds.setAttr(stuff+'.sx',k=False)
				else:
					cmds.setAttr(stuff+'.sx',l=False)
					cmds.setAttr(stuff+'.sx',k=True)
				if (scaleY == 1):
					cmds.setAttr(stuff+'.sy',l=True)
					cmds.setAttr(stuff+'.sy',k=False)
				else:
					cmds.setAttr(stuff+'.sy',l=False)
					cmds.setAttr(stuff+'.sy',k=True)
				if (scaleZ == 1):
					cmds.setAttr(stuff+'.sz',l=True)
					cmds.setAttr(stuff+'.sz',k=False)
				else:
					cmds.setAttr(stuff+'.sz',l=False)
					cmds.setAttr(stuff+'.sz',k=True)
				### check for vis
				if (vis == 1):
					cmds.setAttr(stuff+'.visibility',l=True)
					cmds.setAttr(stuff+'.visibility',k=False)
				else:
					cmds.setAttr(stuff+'.visibility',l=False)
					cmds.setAttr(stuff+'.visibility',k=True)
			except:
				pass
		# line
		nmGUI_func.nmGUI_runCheck('complete','Attributes have been set.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')
# lock trans all
def nmLockHide_transAll():
	'''
	this function sets the translate axis boxes to checked or unchecked
	and then runs the lock and hide function.
	'''
	# get all
	all = cmds.checkBox('nmSAK_rigLockHideTransAllCB',q=True,v=True)
	### check all
	if (all == 1):
		cmds.checkBox('nmSAK_rigLockHideTransXCB',e=True,v=1)
		cmds.checkBox('nmSAK_rigLockHideTransYCB',e=True,v=1)
		cmds.checkBox('nmSAK_rigLockHideTransZCB',e=True,v=1)
	else:
		cmds.checkBox('nmSAK_rigLockHideTransXCB',e=True,v=0)
		cmds.checkBox('nmSAK_rigLockHideTransYCB',e=True,v=0)
		cmds.checkBox('nmSAK_rigLockHideTransZCB',e=True,v=0)
	# run lockHide
	nmLockHide_lockHide()
# lock rot all
def nmLockHide_rotAll():
	'''
	this function sets the rotate axis boxes to checked or unchecked
	and then runs the lock and hide function.
	'''
	# get all
	all = cmds.checkBox('nmSAK_rigLockHideRotateAllCB',q=True,v=True)
	### check all
	if (all == 1):
		cmds.checkBox('nmSAK_rigLockHideRotateXCB',e=True,v=1)
		cmds.checkBox('nmSAK_rigLockHideRotateYCB',e=True,v=1)
		cmds.checkBox('nmSAK_rigLockHideRotateZCB',e=True,v=1)
	else:
		cmds.checkBox('nmSAK_rigLockHideRotateXCB',e=True,v=0)
		cmds.checkBox('nmSAK_rigLockHideRotateYCB',e=True,v=0)
		cmds.checkBox('nmSAK_rigLockHideRotateZCB',e=True,v=0)
	# run lockHide
	nmLockHide_lockHide()
# lock scale all
def nmLockHide_scaleAll():
	'''
	this function sets the scale axis boxes to checked or unchecked
	and then runs the lock and hide function.
	'''
	# get all
	all = cmds.checkBox('nmSAK_rigLockHideScaleAllCB',q=True,v=True)
	### check all
	if (all == 1):
		cmds.checkBox('nmSAK_rigLockHideScaleXCB',e=True,v=1)
		cmds.checkBox('nmSAK_rigLockHideScaleYCB',e=True,v=1)
		cmds.checkBox('nmSAK_rigLockHideScaleZCB',e=True,v=1)
	else:
		cmds.checkBox('nmSAK_rigLockHideScaleXCB',e=True,v=0)
		cmds.checkBox('nmSAK_rigLockHideScaleYCB',e=True,v=0)
		cmds.checkBox('nmSAK_rigLockHideScaleZCB',e=True,v=0)
	# run lockHide
	nmLockHide_lockHide()
# set lockNode
def nwToggleLockNode():
	'''
	this function toggles lockNode to lock and unlock any selected
	'''
	# list locked nodes
	locked = cmds.ls (lockedNodes=1)
	# list selection
	sel = cmds.ls (sl=1)
	# check locked/unlocked and toggle
	if sel:
		for nodes in sel:
			if nodes in locked:
				cmds.lockNode((nodes), lock=0)
				print(nodes, 'unlocked')
			else:
				cmds.lockNode((nodes), lock=1)
				print(nodes, 'locked')
		nmGUI_func.nmGUI_runCheck( 'complete', 'lockNode toggle selected, see script editor for details')
	else:
		nmGUI_func.nmGUI_runCheck( 'error', 'Please select one or more nodes.' )
# control color
def nmControlColor_color(num):
	'''
	this function will color the selected controls a given color.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		for stuff in sel:
			try:
				cmds.setAttr(stuff+".overrideEnabled",1)
				cmds.setAttr(stuff+".overrideColor",num)
			except:
				pass
		# line
		nmGUI_func.nmGUI_runCheck('complete','Control color has been set.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one or more controls.')
# controls
# circle
def nmControls_circle():
	'''
	this function will create and place a circle control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1;')
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
			# print line
		nmGUI_func.nmGUI_runCheck('complete','Circle control has been created.')
	else:
		# create square
		mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 1;')
		# rename ctrl
		cmds.rename('circleCrv_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','Circle control has been created.')
# square
def nmControls_square():
	'''
	this function will create and place a square control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = mel.eval('curve -d 1 -p -1 0 1 -p 1 0 1 -p 1 0 -1 -p -1 0 -1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
		# print line
		nmGUI_func.nmGUI_runCheck('complete','Square control has been created.')
	else:
		# create square
		mel.eval('curve -d 1 -p -1 0 1 -p 1 0 1 -p 1 0 -1 -p -1 0 -1 -p -1 0 1 -k 0 -k 1 -k 2 -k 3 -k 4 ;')
		# rename ctrl
		cmds.rename('squareCrv_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','Square control has been created.')
# triangle
def nmControls_triangle():
	'''
	this function will create and place a triangle control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = mel.eval('curve -d 1 -p 0 0 -1 -p -1 0 1 -p 1 0 1 -p 0 0 -1 ;')
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
		# print line
		nmGUI_func.nmGUI_runCheck('complete','Triangle control has been created.')
	else:
		# create square
		mel.eval('curve -d 1 -p 0 0 -1 -p -1 0 1 -p 1 0 1 -p 0 0 -1 ;')
		# rename ctrl
		cmds.rename('triangleCrv_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','Triangle control has been created.')
# locator
def nmControls_locator():
	'''
	this function will create and place a locator control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = cmds.spaceLocator()
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
		# print line
		nmGUI_func.nmGUI_runCheck('complete','Locator has been created.')
	else:
		# create locator
		cmds.spaceLocator()
		# rename ctrl
		cmds.rename('locator_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','Locator has been created.')
# ball
def nwControls_ball():
	'''
	this function will create and place a sphere control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = mel.eval('curve -d 1 -p 0 1 0 -p 0 0.987688 -0.156435 -p 0 0.951057 -0.309017 -p 0 0.891007 -0.453991 -p 0 0.809017 -0.587786 -p 0 0.707107 -0.707107 -p 0 0.587785 -0.809017 -p 0 0.453991 -0.891007 -p 0 0.309017 -0.951057 -p 0 0.156434 -0.987689 -p 0 0 -1 -p 0 -0.156434 -0.987689 -p 0 -0.309017 -0.951057 -p 0 -0.453991 -0.891007 -p 0 -0.587785 -0.809017 -p 0 -0.707107 -0.707107 -p 0 -0.809017 -0.587786 -p 0 -0.891007 -0.453991 -p 0 -0.951057 -0.309017 -p 0 -0.987688 -0.156435 -p 0 -1 0 -p -4.66211e-09 -0.987688 0.156434 -p -9.20942e-09 -0.951057 0.309017 -p -1.353e-08 -0.891007 0.453991 -p -1.75174e-08 -0.809017 0.587785 -p -2.10734e-08 -0.707107 0.707107 -p -2.41106e-08 -0.587785 0.809017 -p -2.65541e-08 -0.453991 0.891007 -p -2.83437e-08 -0.309017 0.951057 -p -2.94354e-08 -0.156434 0.987688 -p -2.98023e-08 0 1 -p -2.94354e-08 0.156434 0.987688 -p -2.83437e-08 0.309017 0.951057 -p -2.65541e-08 0.453991 0.891007 -p -2.41106e-08 0.587785 0.809017 -p -2.10734e-08 0.707107 0.707107 -p -1.75174e-08 0.809017 0.587785 -p -1.353e-08 0.891007 0.453991 -p -9.20942e-09 0.951057 0.309017 -p -4.66211e-09 0.987688 0.156434 -p 0 1 0 -p -0.156435 0.987688 0 -p -0.309017 0.951057 0 -p -0.453991 0.891007 0 -p -0.587785 0.809017 0 -p -0.707107 0.707107 0 -p -0.809017 0.587785 0 -p -0.891007 0.453991 0 -p -0.951057 0.309017 0 -p -0.987689 0.156434 0 -p -1 0 0 -p -0.987689 -0.156434 0 -p -0.951057 -0.309017 0 -p -0.891007 -0.453991 0 -p -0.809017 -0.587785 0 -p -0.707107 -0.707107 0 -p -0.587785 -0.809017 0 -p -0.453991 -0.891007 0 -p -0.309017 -0.951057 0 -p -0.156435 -0.987688 0 -p 0 -1 0 -p 0.156434 -0.987688 0 -p 0.309017 -0.951057 0 -p 0.453991 -0.891007 0 -p 0.587785 -0.809017 0 -p 0.707107 -0.707107 0 -p 0.809017 -0.587785 0 -p 0.891006 -0.453991 0 -p 0.951057 -0.309017 0 -p 0.987688 -0.156434 0 -p 1 0 0 -p 0.951057 0 -0.309017 -p 0.809018 0 -0.587786 -p 0.587786 0 -0.809017 -p 0.309017 0 -0.951057 -p 0 0 -1 -p -0.309017 0 -0.951057 -p -0.587785 0 -0.809017 -p -0.809017 0 -0.587785 -p -0.951057 0 -0.309017 -p -1 0 0 -p -0.951057 0 0.309017 -p -0.809017 0 0.587785 -p -0.587785 0 0.809017 -p -0.309017 0 0.951057 -p -2.98023e-08 0 1 -p 0.309017 0 0.951057 -p 0.587785 0 0.809017 -p 0.809017 0 0.587785 -p 0.951057 0 0.309017 -p 1 0 0 -p 0.987688 0.156434 0 -p 0.951057 0.309017 0 -p 0.891006 0.453991 0 -p 0.809017 0.587785 0 -p 0.707107 0.707107 0 -p 0.587785 0.809017 0 -p 0.453991 0.891007 0 -p 0.309017 0.951057 0 -p 0.156434 0.987688 0 -p 0 1 0 ;')
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
		# print line
		nmGUI_func.nmGUI_runCheck('complete','Spere control has been created.')
	else:
		# create ball
		mel.eval('curve -d 1 -p 0 1 0 -p 0 0.987688 -0.156435 -p 0 0.951057 -0.309017 -p 0 0.891007 -0.453991 -p 0 0.809017 -0.587786 -p 0 0.707107 -0.707107 -p 0 0.587785 -0.809017 -p 0 0.453991 -0.891007 -p 0 0.309017 -0.951057 -p 0 0.156434 -0.987689 -p 0 0 -1 -p 0 -0.156434 -0.987689 -p 0 -0.309017 -0.951057 -p 0 -0.453991 -0.891007 -p 0 -0.587785 -0.809017 -p 0 -0.707107 -0.707107 -p 0 -0.809017 -0.587786 -p 0 -0.891007 -0.453991 -p 0 -0.951057 -0.309017 -p 0 -0.987688 -0.156435 -p 0 -1 0 -p -4.66211e-09 -0.987688 0.156434 -p -9.20942e-09 -0.951057 0.309017 -p -1.353e-08 -0.891007 0.453991 -p -1.75174e-08 -0.809017 0.587785 -p -2.10734e-08 -0.707107 0.707107 -p -2.41106e-08 -0.587785 0.809017 -p -2.65541e-08 -0.453991 0.891007 -p -2.83437e-08 -0.309017 0.951057 -p -2.94354e-08 -0.156434 0.987688 -p -2.98023e-08 0 1 -p -2.94354e-08 0.156434 0.987688 -p -2.83437e-08 0.309017 0.951057 -p -2.65541e-08 0.453991 0.891007 -p -2.41106e-08 0.587785 0.809017 -p -2.10734e-08 0.707107 0.707107 -p -1.75174e-08 0.809017 0.587785 -p -1.353e-08 0.891007 0.453991 -p -9.20942e-09 0.951057 0.309017 -p -4.66211e-09 0.987688 0.156434 -p 0 1 0 -p -0.156435 0.987688 0 -p -0.309017 0.951057 0 -p -0.453991 0.891007 0 -p -0.587785 0.809017 0 -p -0.707107 0.707107 0 -p -0.809017 0.587785 0 -p -0.891007 0.453991 0 -p -0.951057 0.309017 0 -p -0.987689 0.156434 0 -p -1 0 0 -p -0.987689 -0.156434 0 -p -0.951057 -0.309017 0 -p -0.891007 -0.453991 0 -p -0.809017 -0.587785 0 -p -0.707107 -0.707107 0 -p -0.587785 -0.809017 0 -p -0.453991 -0.891007 0 -p -0.309017 -0.951057 0 -p -0.156435 -0.987688 0 -p 0 -1 0 -p 0.156434 -0.987688 0 -p 0.309017 -0.951057 0 -p 0.453991 -0.891007 0 -p 0.587785 -0.809017 0 -p 0.707107 -0.707107 0 -p 0.809017 -0.587785 0 -p 0.891006 -0.453991 0 -p 0.951057 -0.309017 0 -p 0.987688 -0.156434 0 -p 1 0 0 -p 0.951057 0 -0.309017 -p 0.809018 0 -0.587786 -p 0.587786 0 -0.809017 -p 0.309017 0 -0.951057 -p 0 0 -1 -p -0.309017 0 -0.951057 -p -0.587785 0 -0.809017 -p -0.809017 0 -0.587785 -p -0.951057 0 -0.309017 -p -1 0 0 -p -0.951057 0 0.309017 -p -0.809017 0 0.587785 -p -0.587785 0 0.809017 -p -0.309017 0 0.951057 -p -2.98023e-08 0 1 -p 0.309017 0 0.951057 -p 0.587785 0 0.809017 -p 0.809017 0 0.587785 -p 0.951057 0 0.309017 -p 1 0 0 -p 0.987688 0.156434 0 -p 0.951057 0.309017 0 -p 0.891006 0.453991 0 -p 0.809017 0.587785 0 -p 0.707107 0.707107 0 -p 0.587785 0.809017 0 -p 0.453991 0.891007 0 -p 0.309017 0.951057 0 -p 0.156434 0.987688 0 -p 0 1 0 ;')
		# rename ctrl
		cmds.rename('ballCrv_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','Spere control has been created.')
# box
def nmControls_box():
	'''
	this function will create and place a box control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = mel.eval('curve -d 1 -p -1 1 1 -p -1 1 -1 -p 1 1 -1 -p 1 1 1 -p -1 1 1 -p -1 -1 1 -p -1 -1 -1 -p -1 1 -1 -p -1 1 1 -p -1 -1 1 -p 1 -1 1 -p 1 1 1 -p 1 1 -1 -p 1 -1 -1 -p 1 -1 1 -p 1 -1 -1 -p -1 -1 -1 ;')
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
		# print line
		nmGUI_func.nmGUI_runCheck('complete','Box control has been created.')
	else:
		# create box
		mel.eval('curve -d 1 -p -1 1 1 -p -1 1 -1 -p 1 1 -1 -p 1 1 1 -p -1 1 1 -p -1 -1 1 -p -1 -1 -1 -p -1 1 -1 -p -1 1 1 -p -1 -1 1 -p 1 -1 1 -p 1 1 1 -p 1 1 -1 -p 1 -1 -1 -p 1 -1 1 -p 1 -1 -1 -p -1 -1 -1 ;')
		# rename ctrl
		cmds.rename('boxCrv_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','Box control has been created.')
# diamond
def nwControls_diamond():
	'''
	this function will create and place a diamond control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = mel.eval('curve -d 1 -p -0.707107 0 -6.18172e-08 -p -3.09086e-08 0 0.707107 -p 0 1.123751 0 -p 0.707107 0 0 -p 9.27258e-08 0 -0.707107 -p 0 1.123751 0 -p -0.707107 0 -6.18172e-08 -p 9.27258e-08 0 -0.707107 -p 0 -1.123751 0 -p -0.707107 0 -6.18172e-08 -p -3.09086e-08 0 0.707107 -p 0 -1.123751 0 -p -3.09086e-08 0 0.707107 -p 0.707107 0 0 -p 0 -1.123751 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14;')
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
		# print line
		nmGUI_func.nmGUI_runCheck('complete','Diamond control has been created.')
	else:
		# create diamond
		mel.eval('curve -d 1 -p -0.707107 0 -6.18172e-08 -p -3.09086e-08 0 0.707107 -p 0 1.123751 0 -p 0.707107 0 0 -p 9.27258e-08 0 -0.707107 -p 0 1.123751 0 -p -0.707107 0 -6.18172e-08 -p 9.27258e-08 0 -0.707107 -p 0 -1.123751 0 -p -0.707107 0 -6.18172e-08 -p -3.09086e-08 0 0.707107 -p 0 -1.123751 0 -p -3.09086e-08 0 0.707107 -p 0.707107 0 0 -p 0 -1.123751 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14;')
		# rename ctrl
		cmds.rename('diamondCrv_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','Diamond control has been created.')
# eye pin

# d pad
def nmControls_dPad():
	'''
	this function will create and place a d-pad control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = mel.eval('curve -d 1 -p 1 0 -1 -p 3 0 -1 -p 3 0 1 -p 1 0 1 -p 1 0 3 -p -1 0 3 -p -1 0 1 -p -3 0 1 -p -3 0 -1 -p -1 0 -1 -p -1 0 -3 -p 1 0 -3 -p 1 0 -1 ;')
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
		# print line
		nmGUI_func.nmGUI_runCheck('complete','D-pad control has been created.')
	else:
		# create square
		mel.eval('curve -d 1 -p 1 0 -1 -p 3 0 -1 -p 3 0 1 -p 1 0 1 -p 1 0 3 -p -1 0 3 -p -1 0 1 -p -3 0 1 -p -3 0 -1 -p -1 0 -1 -p -1 0 -3 -p 1 0 -3 -p 1 0 -1 ;')
		# rename ctrl
		cmds.rename('dPadCrv_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','D-pad control has been created.')
# arrow pad
def nmControls_arrowPad():
	'''
	this function will create and place an arrow pad control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = mel.eval('curve -d 1 -p -5 0 0 -p -3 0 -2 -p -3 0 -1 -p -1 0 -1 -p -1 0 -3 -p -2 0 -3 -p 0 0 -5 -p 2 0 -3 -p 1 0 -3 -p 1 0 -1 -p 3 0 -1 -p 3 0 -2 -p 5 0 0 -p 3 0 2 -p 3 0 1 -p 1 0 1 -p 1 0 3 -p 2 0 3 -p 0 0 5 -p -2 0 3 -p -1 0 3 -p -1 0 1 -p -3 0 1 -p -3 0 2 -p -5 0 0 ;')
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
		# print line
		nmGUI_func.nmGUI_runCheck('complete','Arrow pad control has been created.')
	else:
		# create square
		mel.eval('curve -d 1 -p -5 0 0 -p -3 0 -2 -p -3 0 -1 -p -1 0 -1 -p -1 0 -3 -p -2 0 -3 -p 0 0 -5 -p 2 0 -3 -p 1 0 -3 -p 1 0 -1 -p 3 0 -1 -p 3 0 -2 -p 5 0 0 -p 3 0 2 -p 3 0 1 -p 1 0 1 -p 1 0 3 -p 2 0 3 -p 0 0 5 -p -2 0 3 -p -1 0 3 -p -1 0 1 -p -3 0 1 -p -3 0 2 -p -5 0 0 ;')
		# rename ctrl
		cmds.rename('arrowPadCrv_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','Arrow pad control has been created.')
# arrow
def nmControls_arrow():
	'''
	this function will create and place an arrow control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = mel.eval('curve -d 1 -p 0 0 3 -p -2 0 1 -p -1 0 1 -p -1 0 -3 -p 1 0 -3 -p 1 0 1 -p 2 0 1 -p 0 0 3 ;')
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
		# print line
		nmGUI_func.nmGUI_runCheck('complete','Arrow control has been created.')
	else:
		# create square
		mel.eval('curve -d 1 -p 0 0 3 -p -2 0 1 -p -1 0 1 -p -1 0 -3 -p 1 0 -3 -p 1 0 1 -p 2 0 1 -p 0 0 3 ;')
		# rename ctrl
		cmds.rename('arrowCrv_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','Arrow control has been created.')
# double arrow
def nmControls_doubleArrow():
	'''
	this function will create and place a double arrow control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = mel.eval('curve -d 1 -p 0 0 5 -p -2 0 3 -p -1 0 3 -p -1 0 -3 -p -2 0 -3 -p 0 0 -5 -p 2 0 -3 -p 1 0 -3 -p 1 0 3 -p 2 0 3 -p 0 0 5 ;')
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
		# print line
		nmGUI_func.nmGUI_runCheck('complete','Double arrow control has been created.')
	else:
		# create square
		mel.eval('curve -d 1 -p 0 0 5 -p -2 0 3 -p -1 0 3 -p -1 0 -3 -p -2 0 -3 -p 0 0 -5 -p 2 0 -3 -p 1 0 -3 -p 1 0 3 -p 2 0 3 -p 0 0 5 ;')
		# rename ctrl
		cmds.rename('doubleArrowCrv_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','Double arrow control has been created.')
# curved arrows

# star

# ninja star
def nmControls_ninjaStar():
	'''
	this function will create and place a ninja star control.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if sel:
		ctrls = []
		for stuff in sel:
			# control
			ctrl = mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0;')[0]
			cv = [ctrl+'.cv[1]',ctrl+'.cv[3]',ctrl+'.cv[5]',ctrl+'.cv[7]']
			cmds.scale(0.0671619,0.0671619,0.0671619,cv,ws=True,r=True,p=(0,0,0))
			cmds.scale(1.862298,1.862298,1.862298,ctrl+'.cv[0:8]',ws=True,r=True,p=(0,0,0))
			# parent
			cmds.parentConstraint(stuff,ctrl,mo=False)
			# del con
			cmds.delete(ctrl,cn=True)
			# rename ctrl
			newName = cmds.rename(stuff+'_ctrl_#')
			# append selection list
			ctrls.append(newName)	
			# select
			cmds.select(ctrls)
		# print line
		nmGUI_func.nmGUI_runCheck('complete','Ninja star control has been created.')
	else:
		# create square
		ctrl = mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0;')[0]
		cv = [ctrl+'.cv[1]',ctrl+'.cv[3]',ctrl+'.cv[5]',ctrl+'.cv[7]']
		cmds.scale(0.0671619,0.0671619,0.0671619,cv,ws=True,r=True,p=(0,0,0))
		cmds.scale(1.862298,1.862298,1.862298,ctrl+'.cv[0:8]',ws=True,r=True,p=(0,0,0))
		# rename ctrl
		cmds.rename('ninjaStarCrv_ctrl_#')
		# line
		nmGUI_func.nmGUI_runCheck('complete','Ninja star control has been created.')
# special controls
# move all
def nmSpecialControls_moveAll():
	'''
	this function will create a move all control with the option of
	having the character name integrated into the control.
	'''
	buildControl = cmds.promptDialog(t='Special Control: Move All',m='Character Name:',b=('     Control + Hierarchy     ','Cancel'),db='     Control + Hierarchy     ',cb='Cancel',ds='Cancel')
	if buildControl == '     Control + Hierarchy     ':
		# text
		text = cmds.promptDialog(q=True,tx=True)
		# dummy
		sText = []
		# circles
		arrowCircle = mel.eval('curve -d 3 -p 0.905661 0 -2.79593 -p 0.73554 0 -2.845522 -p 0.461994 0 -2.916924 -p 5.96046e-008 9.31323e-010 -2.958112 -p -0.461994 0 -2.916924 -p -0.912613 0 -2.808739 -p -1.340761 0 -2.631398 -p -1.735896 0 -2.389259 -p -2.088284 0 -2.088286 -p -2.389257 0 -1.735898 -p -2.631395 0 -1.340764 -p -2.808738 0 -0.912614 -p -2.916924 0 -0.461994 -p -2.953281 9.31323e-010 -5.96046e-008 -p -2.916924 0 0.461994 -p -2.808739 0 0.912613 -p -2.631398 0 1.340761 -p -2.389259 0 1.735896 -p -2.088286 0 2.088284 -p -1.735898 0 2.389257 -p -1.340764 0 2.631395 -p -0.912614 0 2.808738 -p -0.461994 0 2.916924 -p -5.96046e-008 9.31323e-010 2.953281 -p 0.461994 0 2.916924 -p 0.907307 0 2.80156 -p 1.340761 0 2.631398 -p 1.735896 0 2.389259 -p 2.088284 0 2.088286 -p 2.389257 0 1.735898 -p 2.631395 0 1.340764 -p 2.808738 0 0.912614 -p 2.916924 0 0.461994 -p 2.953281 9.31323e-010 5.96046e-008 -p 2.916924 0 -0.461994 -p 2.808739 0 -0.912613 -p 2.631398 0 -1.340761 -p 2.389259 0 -1.735896 -p 2.088286 0 -2.088284 -p 1.735898 0 -2.389257 -p 1.340764 0 -2.631395 -p 1.041685 0 -2.748566 -p 0.905661 0 -2.79593 -p 0.905661 0 -2.79593 -p 0.905661 0 -2.79593 -p 0.920416 0 -2.841418 -p 0.920416 0 -2.841418 -p 0.920416 0 -2.841418 -p 1.01133 0 -2.811657 -p 1.361974 0 -2.67302 -p 1.763358 0 -2.427052 -p 2.121323 0 -2.121321 -p 2.427053 0 -1.763356 -p 2.673022 0 -1.361971 -p 2.853172 0 -0.92705 -p 2.959709 0 -0.483292 -p 2.963068 0 -0.469302 -p 2.976774 0 -0.465561 -p 3.529018 0 -0.314798 -p 3.541694 0 -0.311337 -p 3.541694 0 -0.323634 -p 3.541694 0 -0.538043 -p 3.541694 0 -0.551758 -p 3.553554 0 -0.544265 -p 4.40069 0 -0.00913606 -p 4.415153 -1.39698e-009 5.51343e-007 -p 4.40069 0 0.00913606 -p 3.553554 9.31323e-010 0.544265 -p 3.541694 0 0.551757 -p 3.541694 0 0.538043 -p 3.541694 -5.58794e-009 0.323634 -p 3.541694 0 0.311337 -p 3.529018 0 0.314798 -p 2.976774 0 0.465561 -p 2.963068 0 0.469302 -p 2.959709 0 0.483292 -p 2.853171 0 0.927052 -p 2.67302 0 1.361974 -p 2.427052 0 1.763358 -p 2.121321 0 2.121323 -p 1.763356 0 2.427053 -p 1.361971 0 2.673022 -p 0.921744 0 2.845994 -p 0.483292 0 2.959709 -p 0.469302 0 2.963068 -p 0.465561 0 2.976774 -p 0.314798 0 3.529018 -p 0.311337 0 3.541694 -p 0.323634 0 3.541694 -p 0.538043 0 3.541694 -p 0.551758 0 3.541694 -p 0.544265 0 3.553554 -p 0.00913606 0 4.40069 -p -5.51343e-007 -1.39698e-009 4.415153 -p -0.00913606 0 4.40069 -p -0.544265 9.31323e-010 3.553554 -p -0.551757 0 3.541694 -p -0.538043 0 3.541694 -p -0.323634 -5.58794e-009 3.541694 -p -0.311337 0 3.541694 -p -0.314798 0 3.529018 -p -0.465561 0 2.976774 -p -0.469302 0 2.963068 -p -0.483292 0 2.959709 -p -0.927052 0 2.853171 -p -1.361974 0 2.67302 -p -1.763358 0 2.427052 -p -2.121323 0 2.121321 -p -2.427053 0 1.763356 -p -2.673022 0 1.361971 -p -2.853172 0 0.92705 -p -2.959709 0 0.483292 -p -2.963068 0 0.469302 -p -2.976774 0 0.465561 -p -3.529018 0 0.314798 -p -3.541694 0 0.311337 -p -3.541694 0 0.323634 -p -3.541694 0 0.538043 -p -3.541694 0 0.551758 -p -3.553554 0 0.544265 -p -4.40069 0 0.00913606 -p -4.415153 -1.39698e-009 -5.51343e-007 -p -4.40069 0 -0.00913606 -p -3.553554 9.31323e-010 -0.544265 -p -3.541694 0 -0.551757 -p -3.541694 0 -0.538043 -p -3.541694 -5.58794e-009 -0.323634 -p -3.541694 0 -0.311337 -p -3.529018 0 -0.314798 -p -2.976774 0 -0.465561 -p -2.963068 0 -0.469302 -p -2.959709 0 -0.483292 -p -2.853171 0 -0.927052 -p -2.67302 0 -1.361974 -p -2.427052 0 -1.763358 -p -2.121321 0 -2.121323 -p -1.763356 0 -2.427053 -p -1.361971 0 -2.673022 -p -0.92705 0 -2.853172 -p -0.483292 0 -2.959709 -p -0.469302 0 -2.963068 -p -0.465561 0 -2.976774 -p -0.314798 0 -3.529018 -p -0.311337 0 -3.541694 -p -0.323634 0 -3.541694 -p -0.538043 0 -3.541694 -p -0.551758 0 -3.541694 -p -0.544265 0 -3.553554 -p -0.00913606 0 -4.40069 -p 5.51343e-007 -1.39698e-009 -4.415153 -p 0.00913606 0 -4.40069 -p 0.544265 9.31323e-010 -3.553554 -p 0.551757 0 -3.541694 -p 0.538043 0 -3.541694 -p 0.323634 -5.58794e-009 -3.541694 -p 0.311337 0 -3.541694 -p 0.314798 0 -3.529018 -p 0.465561 0 -2.976774 -p 0.469302 0 -2.963068 -p 0.483292 0 -2.959709 -p 0.845956 0 -2.866662 -p 0.920416 0 -2.841418 -k 0 -k 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 -k 20 -k 21 -k 22 -k 23 -k 24 -k 25 -k 26 -k 27 -k 28 -k 29 -k 30 -k 31 -k 32 -k 33 -k 34 -k 35 -k 36 -k 37 -k 38 -k 39 -k 40 -k 41 -k 42 -k 43 -k 44 -k 45 -k 46 -k 47 -k 48 -k 49 -k 50 -k 51 -k 52 -k 53 -k 54 -k 55 -k 56 -k 57 -k 58 -k 59 -k 60 -k 61 -k 62 -k 63 -k 64 -k 65 -k 66 -k 67 -k 68 -k 69 -k 70 -k 71 -k 72 -k 73 -k 74 -k 75 -k 76 -k 77 -k 78 -k 79 -k 80 -k 81 -k 82 -k 83 -k 84 -k 85 -k 86 -k 87 -k 88 -k 89 -k 90 -k 91 -k 92 -k 93 -k 94 -k 95 -k 96 -k 97 -k 98 -k 99 -k 100 -k 101 -k 102 -k 103 -k 104 -k 105 -k 106 -k 107 -k 108 -k 109 -k 110 -k 111 -k 112 -k 113 -k 114 -k 115 -k 116 -k 117 -k 118 -k 119 -k 120 -k 121 -k 122 -k 123 -k 124 -k 125 -k 126 -k 127 -k 128 -k 129 -k 130 -k 131 -k 132 -k 133 -k 134 -k 135 -k 136 -k 137 -k 138 -k 139 -k 140 -k 141 -k 142 -k 143 -k 144 -k 145 -k 146 -k 147 -k 148 -k 149 -k 150 -k 151 -k 152 -k 153 -k 154 -k 155 -k 156 -k 157 -k 158 -k 159 -k 159 -k 159 ;')
		nmControlColor_color(17)
		cmds.addAttr(longName='geoState',at='enum',en="Normal:Referenced")
		circle = mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 2.5 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0;')[0]
		nmControlColor_color(30)
		# text check
		if not (text == ''):	
			# text curves
			curves = []
			casedText = text.upper()
			sText = text.lower()
			'''
			create = cmds.textCurves(f='Times New Roman',t=casedText)
			listRel = cmds.listRelatives(create[0],ad=True)
			# cycle
			for stuff in listRel:
				if (cmds.listRelatives(stuff,s=True)):
					curves.append(stuff)
			# combine text
			cmds.parent(curves,w=True)
			cmds.delete(create[0])
			cmds.select(curves)
			nmCurves_combine()
			cmds.xform(cp=True)
			cmds.delete(ch=True)
			finText = cmds.ls(sl=True)[0]
			# place text
			cmds.setAttr(finText+'.rx',-90)
			cmds.setAttr(finText+'.sx',.1)
			cmds.setAttr(finText+'.sy',.1)
			cmds.setAttr(finText+'.sz',.1)
			cmds.makeIdentity(finText,a=True,t=1,r=1,s=1,n=0)
			loc = cmds.spaceLocator(p=(0,0,3.2662))[0]
			cmds.xform(cp=True)
			cmds.pointConstraint(loc,finText,mo=False)
			cmds.delete(finText,cn=True)
			cmds.delete(loc)
			cmds.select(finText)
			# create bend
			cmds.nonLinear(type='bend',lowBound=-5.2,highBound=5.2,curvature=.3,ds=True)
			cmds.rotate(0,90,-90,r=True,os=True)
			cmds.delete(finText,ch=True)
			cmds.xform(finText,ws=True,rp=(0,0,0))
			cmds.setAttr(finText+'.ry',-45)
			# duplicate
			secText = cmds.duplicate(finText)[0]
			cmds.setAttr(secText+'.ry',135)
			allCurves.append(secText)
			allCurves.append(finText)
			'''
		if (sText):
			moveAll = cmds.rename(arrowCircle,sText+'_moveAll_ctrl')
			offset = cmds.rename(circle,sText+'_offset_ctrl')
		else:
			moveAll = cmds.rename(arrowCircle,'moveAll_ctrl')
			offset = cmds.rename(circle,'offset_ctrl')
		cmds.connectAttr(moveAll+'.sy',moveAll+'.sx')
		cmds.connectAttr(moveAll+'.sy',moveAll+'.sz')
		cmds.setAttr(moveAll+'.sx',k=False,l=True,cb=False)
		cmds.setAttr(moveAll+'.sz',k=False,l=True,cb=False)
		cmds.setAttr(moveAll+'.v',k=False,l=True,cb=False)
		cmds.setAttr(moveAll+'.geoState',k=False,cb=True)
		# rename shape nodes
		rel = cmds.listRelatives(moveAll,s=True,pa=True)
		for stuff in rel:
			cmds.rename(stuff,moveAll+'Shape')
		# set limit
		cmds.transformLimits(moveAll,sy=(0.01,1),esy=(1,0))
		cmds.group(n=moveAll+'_null_1',em=True)
		cmds.group(moveAll,n=moveAll+'_null_0',p=moveAll+'_null_1')
		# parent and lock offset
		cmds.group(n=offset+'_null_1',em=True)
		cmds.group(offset,n=offset+'_null_0',p=offset+'_null_1')
		cmds.parent(offset+'_null_1',moveAll)
		cmds.setAttr(offset+'.sx',l=True,k=False,cb=False)
		cmds.setAttr(offset+'.sy',l=True,k=False,cb=False)
		cmds.setAttr(offset+'.sz',l=True,k=False,cb=False)
		cmds.setAttr(offset+'.v',l=True,k=False,cb=False)
		# hierarchy
		if (cmds.objExists('cWOLRD')):
			cmds.parent(moveAll+'_null_1','CONTROLS')
		else:
			cmds.group(n='cWOLRD',em=True)
			cmds.group(n='RIG',em=True,p='cWOLRD')
			cmds.group(n='CONTROLS',em=True,p='cWOLRD')
			cmds.parent(moveAll+'_null_1','CONTROLS')
			cmds.group(n='GEOMETRY',em=True,p='cWOLRD')
			cmds.setAttr('GEOMETRY.overrideDisplayType', 2)
			cmds.connectAttr(moveAll+'.geoState','GEOMETRY.overrideEnabled')
			cmds.group(n='BLEND_SHAPES',em=True,p='GEOMETRY')
			cmds.group(n='DEFORMED',em=True,p='GEOMETRY')
			'''
			cmds.group(n='NON_DEFORMED',em=True,p='GEOMETRY')
			cmds.group(n='EXTRAS',em=True,p='cWOLRD')
			'''
			cmds.group(n='DO_NOT_TOUCH',em=True,p='cWOLRD')
			# connect scale
			'''
			gp = ['RIG','CONTROLS','NON_DEFORMED']
			for stuff in gp:
				cmds.connectAttr(name+'.sy',stuff+'.sx',f=True)
				cmds.connectAttr(name+'.sy',stuff+'.sy',f=True)
				cmds.connectAttr(name+'.sy',stuff+'.sz',f=True)
			'''
			# set locked
			gp = ['RIG','BLEND_SHAPES','DO_NOT_TOUCH']
			for stuff in gp:
				cmds.setAttr(stuff+'.v',0,l=True,cb=True)
		# clear sel
		cmds.select(cl=True)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Move all control has been created.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Special control was not created.')
# face gui
def nwSpecialControls_addOffset():
	'''
	this function will create and add a new offset control then parents it under the rig hierarchy; includes option of
	having the character name integrated into the control.
	'''
	buildControl = cmds.promptDialog(t='Special Control: Add Offset',m='Character Name:',b=('     Add to Hierarchy     ','Cancel'),db='     Add to Hierarchy     ',cb='Cancel',ds='Cancel')
	if buildControl == '     Add to Hierarchy     ':
		# text
		text = cmds.promptDialog(q=True,tx=True)
		# hierarchy check
		if (cmds.objExists('cWOLRD')):
			# dummy
			sText = []
			# circle
			circle = mel.eval('circle -c 0 0 0 -nr 0 1 0 -sw 360 -r 2.5 -d 3 -ut 0 -tol 0.01 -s 8 -ch 0;')[0]
			nmControlColor_color(30)
			# text check
			if not (text == ''):	
				# text curves
				curves = []
				casedText = text.upper()
				sText = text.lower()
			# rename control and set attributes
			if (sText):
				offset = cmds.rename(circle,sText+'_offset_ctrl')
			else:
				offset = cmds.rename(circle,'offset_ctrl')
			# parent and lock offset
			cmds.group(n=offset+'_null_1',em=True)
			cmds.group(offset,n=offset+'_null_0',p=offset+'_null_1')
			cmds.setAttr(offset+'.sx',l=True,k=False,cb=False)
			cmds.setAttr(offset+'.sy',l=True,k=False,cb=False)
			cmds.setAttr(offset+'.sz',l=True,k=False,cb=False)
			cmds.setAttr(offset+'.v',l=True,k=False,cb=False)
			# get moveAll ctrl for group
			getCONTROLS = cmds.listRelatives('CONTROLS', ad=1)[0]
			moveAllpar = cmds.listRelatives(getCONTROLS, p=1)[0]
			cmds.parent(offset+'_null_1', moveAllpar)
			# clear sel
			cmds.select(cl=True)
			# line
			nmGUI_func.nmGUI_runCheck('complete','New offset control has been created under moveAll_ctrl.')
		else:
			# line
			nmGUI_func.nmGUI_runCheck('error','No cWorld Hierarchy present. Use "Move All" to build cWorld Hierarchy.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Special control was not created.')
### Face Rig Controls ###
# Edge to joint spline builder
def nwSpecialControls_EdgeJointSpline():
	buildControl = cmds.promptDialog(t='Edges to Control Spline',m='Control Name:',b=('     Make Controls     ','Cancel'),db='     Make Controls     ',cb='Cancel',ds='Cancel')
	if buildControl == '     Make Controls     ':
		# First select the edge(s) or edgeLoop you want to convert to a spline with bonded locators
		sel = cmds.ls(sl=1)
		crv = []
		locs = []
		jnts = []
		# check edges are selected
		edges = cmds.polyEvaluate(ec=1)
		if edges:
			# get name for new spline from transform
			# get text
			text = cmds.promptDialog(q=True,tx=True)
			# dummy
			sText = []
			# text check/set root name
			if text:
				root = text
			else:
				root = 'splCtrl0#'
			# convert edgeToPoly
			cmds.polyToCurve(f=2,dg=1)
			# delete history
			cmds.delete(ch=1)
			# rename
			newName = cmds.rename(root+'_baseCrv0#')
			# store new curve in array
			crv.append(newName)
			# make grps
			mainGrp = cmds.group(n=root+'_baseCrvGrp0#')
			locGrp = cmds.group(em=True, n=root+'_locCtrlGrp0#', p=mainGrp)
			jntGrp = cmds.group(em=True, n=root+'_jntGrp0#', p=mainGrp)
			crvName = crv[0]
			# make locators at edit points
			for ep in crv:
				# get edit point(s)
				deg = cmds.getAttr(crv[0]+'.degree')
				span = cmds.getAttr(crv[0]+'.spans')
				epNum = deg+span
				# counter
				i=0
				# loop through the ep's to place a locator and group
				while (i < epNum):
					u = str(i)
					pos = cmds.pointPosition(crv[0]+'.ep['+u+']')
					loc = cmds.spaceLocator(n=root+'_'+u+'_locCtrl0#')
					cmds.xform(t=pos)
					# set localScale
					cmds.setAttr(str(loc[0])+'Shape'+'.localScale', 0.2, 0.2, 0.2)
					cmds.parent(loc, locGrp)
					locs.append(loc[0])
					# create PCI
					pci = cmds.createNode('pointOnCurveInfo', n=root+'_cv'+u+'_pci_0#')
					# connect ws info to PCI node info
					cmds.connectAttr(crvName + '.worldSpace', pci + '.inputCurve')
					cmds.setAttr(pci + '.parameter', int(u))
					# connect PCI position info to locator translation channels
					cmds.connectAttr(pci + '.position', loc[0] + '.t')
					# counter +1
					i+=1
			# create pointOnCurveInfo node
			for loc in locs:
				# get locator position
				locPos = cmds.xform(loc, q=1, ws=1, t=1)
				# create joint at locator position and group
				jnt = cmds.joint(n=crvName+'_jnt0#', p=locPos)
				# set joint radius
				cmds.setAttr(str(jnt)+'.radius', 0.2)
				cmds.parent(jnt, jntGrp)
				cmds.pointConstraint(loc, jnt)
				jnts.append(jnt)
			print "Completed, Control curve with constrained joints created at selected edges."
		else:
			# error for no edges selected on polymesh
			print 'ERROR: select one or more contiguous edges'
	else:
		print "Error, Spline Joints with Controls was not created."	
# Curve Controls Builder
def nwSpecialControls_CurveControls():
	buildControl = cmds.promptDialog(t='Spline Joints w/Controls',m='Control Name:',b=('     Make Controls     ','Cancel'),db='     Make Controls     ',cb='Cancel',ds='Cancel')
	if buildControl == '     Make Controls     ':
		# get selected type
		selS = cmds.ls(sl=1, typ='nurbsCurve')
		selT = cmds.ls(sl=1, typ='transform')
		crvs = []
		if selS:
			for things in selS:
				crvs.append(str(things[0]))
		if selT:
			for sel in selT:
				shape = cmds.listRelatives(sel, typ='nurbsCurve')
				if shape:
					crvs.append(str(shape[0]))		
		# selected curve check
		if crvs:
			cmds.select(crvs)
			cmds.delete(ch=1)
			cmds.select(cl=1)
			num = len(crvs)
			# text
			text = cmds.promptDialog(q=True,tx=True)
			# dummy
			sText = []
			# text check
			if text:
				# text curves
				root = text
			else:
				root = 'splCtrl0#'
			iz = 0
			while iz < num:
				cmds.select(crvs[iz])
				mainGrp = cmds.group(n=root+'_baseCrvGrp0#')
				ctrlGrp = cmds.group(em=True, n=root+'_CtrlGrp0#', p=mainGrp)
				jntGrp = cmds.group(em=True, n=root+'_jntGrp0#', p=mainGrp)
				cmds.setAttr(jntGrp+'.v', 0)
				joints = []
				deg = cmds.getAttr(crvs[iz]+'.degree')
				span = cmds.getAttr(crvs[iz]+'.spans')
				cvNum = deg+span
				# counter
				i=0
				# loop through the cv's and place a cluster
				while (i < cvNum):
					pos = cmds.pointPosition(crvs[iz]+'.cv['+str(i)+']')
					if i == 0:
						# create box control curve, snap to cluster, and constrain cluster
						ctrl = mel.eval('curve -d 1 -p 0 1 0 -p 0 0.987688 -0.156435 -p 0 0.951057 -0.309017 -p 0 0.891007 -0.453991 -p 0 0.809017 -0.587786 -p 0 0.707107 -0.707107 -p 0 0.587785 -0.809017 -p 0 0.453991 -0.891007 -p 0 0.309017 -0.951057 -p 0 0.156434 -0.987689 -p 0 0 -1 -p 0 -0.156434 -0.987689 -p 0 -0.309017 -0.951057 -p 0 -0.453991 -0.891007 -p 0 -0.587785 -0.809017 -p 0 -0.707107 -0.707107 -p 0 -0.809017 -0.587786 -p 0 -0.891007 -0.453991 -p 0 -0.951057 -0.309017 -p 0 -0.987688 -0.156435 -p 0 -1 0 -p -4.66211e-09 -0.987688 0.156434 -p -9.20942e-09 -0.951057 0.309017 -p -1.353e-08 -0.891007 0.453991 -p -1.75174e-08 -0.809017 0.587785 -p -2.10734e-08 -0.707107 0.707107 -p -2.41106e-08 -0.587785 0.809017 -p -2.65541e-08 -0.453991 0.891007 -p -2.83437e-08 -0.309017 0.951057 -p -2.94354e-08 -0.156434 0.987688 -p -2.98023e-08 0 1 -p -2.94354e-08 0.156434 0.987688 -p -2.83437e-08 0.309017 0.951057 -p -2.65541e-08 0.453991 0.891007 -p -2.41106e-08 0.587785 0.809017 -p -2.10734e-08 0.707107 0.707107 -p -1.75174e-08 0.809017 0.587785 -p -1.353e-08 0.891007 0.453991 -p -9.20942e-09 0.951057 0.309017 -p -4.66211e-09 0.987688 0.156434 -p 0 1 0 -p -0.156435 0.987688 0 -p -0.309017 0.951057 0 -p -0.453991 0.891007 0 -p -0.587785 0.809017 0 -p -0.707107 0.707107 0 -p -0.809017 0.587785 0 -p -0.891007 0.453991 0 -p -0.951057 0.309017 0 -p -0.987689 0.156434 0 -p -1 0 0 -p -0.987689 -0.156434 0 -p -0.951057 -0.309017 0 -p -0.891007 -0.453991 0 -p -0.809017 -0.587785 0 -p -0.707107 -0.707107 0 -p -0.587785 -0.809017 0 -p -0.453991 -0.891007 0 -p -0.309017 -0.951057 0 -p -0.156435 -0.987688 0 -p 0 -1 0 -p 0.156434 -0.987688 0 -p 0.309017 -0.951057 0 -p 0.453991 -0.891007 0 -p 0.587785 -0.809017 0 -p 0.707107 -0.707107 0 -p 0.809017 -0.587785 0 -p 0.891006 -0.453991 0 -p 0.951057 -0.309017 0 -p 0.987688 -0.156434 0 -p 1 0 0 -p 0.951057 0 -0.309017 -p 0.809018 0 -0.587786 -p 0.587786 0 -0.809017 -p 0.309017 0 -0.951057 -p 0 0 -1 -p -0.309017 0 -0.951057 -p -0.587785 0 -0.809017 -p -0.809017 0 -0.587785 -p -0.951057 0 -0.309017 -p -1 0 0 -p -0.951057 0 0.309017 -p -0.809017 0 0.587785 -p -0.587785 0 0.809017 -p -0.309017 0 0.951057 -p -2.98023e-08 0 1 -p 0.309017 0 0.951057 -p 0.587785 0 0.809017 -p 0.809017 0 0.587785 -p 0.951057 0 0.309017 -p 1 0 0 -p 0.987688 0.156434 0 -p 0.951057 0.309017 0 -p 0.891006 0.453991 0 -p 0.809017 0.587785 0 -p 0.707107 0.707107 0 -p 0.587785 0.809017 0 -p 0.453991 0.891007 0 -p 0.309017 0.951057 0 -p 0.156434 0.987688 0 -p 0 1 0 ;')
						ctrlName = cmds.rename(ctrl, root+'_ctrl'+str(i))
						cmds.setAttr(ctrlName+".overrideEnabled",1)
						cmds.setAttr(ctrlName+".overrideColor",13)
						cmds.xform(ctrlName, t=pos)
						cmds.parent(ctrlName, ctrlGrp)
						jntName = (root+'_jnt'+str(i))
						cmds.joint(n=jntName, p=pos)
						cmds.parent(jntName, jntGrp)
						joints.append(jntName)
						cmds.pointConstraint(ctrlName, jntName)
					elif i is not ((cvNum)-1):
						if i %2 == 0:
							# create box control curve, snap to cluster, and constrain cluster
							ctrl = mel.eval('curve -d 1 -p -1 1 1 -p -1 1 -1 -p 1 1 -1 -p 1 1 1 -p -1 1 1 -p -1 -1 1 -p -1 -1 -1 -p -1 1 -1 -p -1 1 1 -p -1 -1 1 -p 1 -1 1 -p 1 1 1 -p 1 1 -1 -p 1 -1 -1 -p 1 -1 1 -p 1 -1 -1 -p -1 -1 -1 ;')
							ctrlName = cmds.rename(ctrl, root+'_ctrl'+str(i))
							cmds.setAttr(ctrlName+".overrideEnabled",1)
							cmds.setAttr(ctrlName+".overrideColor",13)
							cmds.xform(ctrlName, t=pos)
							cmds.parent(ctrlName, ctrlGrp)
							jntName = (root+'_jnt'+str(i))
							cmds.joint(n=jntName, p=pos)
							cmds.parent(jntName, jntGrp)
							joints.append(jntName)
							cmds.pointConstraint(ctrlName, jntName)
						else:
							ctrl = mel.eval('curve -d 1 -p -0.707107 0 -6.18172e-08 -p -3.09086e-08 0 0.707107 -p 0 1.123751 0 -p 0.707107 0 0 -p 9.27258e-08 0 -0.707107 -p 0 1.123751 0 -p -0.707107 0 -6.18172e-08 -p 9.27258e-08 0 -0.707107 -p 0 -1.123751 0 -p -0.707107 0 -6.18172e-08 -p -3.09086e-08 0 0.707107 -p 0 -1.123751 0 -p -3.09086e-08 0 0.707107 -p 0.707107 0 0 -p 0 -1.123751 0 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14;')
							ctrlName = cmds.rename(ctrl, root+'_ctrl'+str(i))
							cmds.setAttr(ctrlName+".overrideEnabled",1)
							cmds.setAttr(ctrlName+".overrideColor",22)
							cmds.xform(ctrlName, t=pos)
							cmds.parent(ctrlName, ctrlGrp)
							jntName = (root+'_jnt'+str(i))
							cmds.joint(n=jntName, p=pos)
							cmds.parent(jntName, jntGrp)
							joints.append(jntName)
							cmds.pointConstraint(ctrlName, jntName)		   
					else:
						# create box control curve, snap to cluster, and constrain cluster
						ctrl = mel.eval('curve -d 1 -p 0 1 0 -p 0 0.987688 -0.156435 -p 0 0.951057 -0.309017 -p 0 0.891007 -0.453991 -p 0 0.809017 -0.587786 -p 0 0.707107 -0.707107 -p 0 0.587785 -0.809017 -p 0 0.453991 -0.891007 -p 0 0.309017 -0.951057 -p 0 0.156434 -0.987689 -p 0 0 -1 -p 0 -0.156434 -0.987689 -p 0 -0.309017 -0.951057 -p 0 -0.453991 -0.891007 -p 0 -0.587785 -0.809017 -p 0 -0.707107 -0.707107 -p 0 -0.809017 -0.587786 -p 0 -0.891007 -0.453991 -p 0 -0.951057 -0.309017 -p 0 -0.987688 -0.156435 -p 0 -1 0 -p -4.66211e-09 -0.987688 0.156434 -p -9.20942e-09 -0.951057 0.309017 -p -1.353e-08 -0.891007 0.453991 -p -1.75174e-08 -0.809017 0.587785 -p -2.10734e-08 -0.707107 0.707107 -p -2.41106e-08 -0.587785 0.809017 -p -2.65541e-08 -0.453991 0.891007 -p -2.83437e-08 -0.309017 0.951057 -p -2.94354e-08 -0.156434 0.987688 -p -2.98023e-08 0 1 -p -2.94354e-08 0.156434 0.987688 -p -2.83437e-08 0.309017 0.951057 -p -2.65541e-08 0.453991 0.891007 -p -2.41106e-08 0.587785 0.809017 -p -2.10734e-08 0.707107 0.707107 -p -1.75174e-08 0.809017 0.587785 -p -1.353e-08 0.891007 0.453991 -p -9.20942e-09 0.951057 0.309017 -p -4.66211e-09 0.987688 0.156434 -p 0 1 0 -p -0.156435 0.987688 0 -p -0.309017 0.951057 0 -p -0.453991 0.891007 0 -p -0.587785 0.809017 0 -p -0.707107 0.707107 0 -p -0.809017 0.587785 0 -p -0.891007 0.453991 0 -p -0.951057 0.309017 0 -p -0.987689 0.156434 0 -p -1 0 0 -p -0.987689 -0.156434 0 -p -0.951057 -0.309017 0 -p -0.891007 -0.453991 0 -p -0.809017 -0.587785 0 -p -0.707107 -0.707107 0 -p -0.587785 -0.809017 0 -p -0.453991 -0.891007 0 -p -0.309017 -0.951057 0 -p -0.156435 -0.987688 0 -p 0 -1 0 -p 0.156434 -0.987688 0 -p 0.309017 -0.951057 0 -p 0.453991 -0.891007 0 -p 0.587785 -0.809017 0 -p 0.707107 -0.707107 0 -p 0.809017 -0.587785 0 -p 0.891006 -0.453991 0 -p 0.951057 -0.309017 0 -p 0.987688 -0.156434 0 -p 1 0 0 -p 0.951057 0 -0.309017 -p 0.809018 0 -0.587786 -p 0.587786 0 -0.809017 -p 0.309017 0 -0.951057 -p 0 0 -1 -p -0.309017 0 -0.951057 -p -0.587785 0 -0.809017 -p -0.809017 0 -0.587785 -p -0.951057 0 -0.309017 -p -1 0 0 -p -0.951057 0 0.309017 -p -0.809017 0 0.587785 -p -0.587785 0 0.809017 -p -0.309017 0 0.951057 -p -2.98023e-08 0 1 -p 0.309017 0 0.951057 -p 0.587785 0 0.809017 -p 0.809017 0 0.587785 -p 0.951057 0 0.309017 -p 1 0 0 -p 0.987688 0.156434 0 -p 0.951057 0.309017 0 -p 0.891006 0.453991 0 -p 0.809017 0.587785 0 -p 0.707107 0.707107 0 -p 0.587785 0.809017 0 -p 0.453991 0.891007 0 -p 0.309017 0.951057 0 -p 0.156434 0.987688 0 -p 0 1 0 ;')
						ctrlName = cmds.rename(ctrl, root+'_ctrl'+str(i))
						cmds.setAttr(ctrlName+".overrideEnabled",1)
						cmds.setAttr(ctrlName+".overrideColor",13)
						cmds.xform(ctrlName, t=pos)
						cmds.parent(ctrlName, ctrlGrp)
						jntName = (root+'_jnt'+str(i))
						cmds.joint(n=jntName, p=pos)
						cmds.parent(jntName, jntGrp)
						joints.append(jntName)
						cmds.pointConstraint(ctrlName, jntName)
					# counter
					i+=1
				crvTrans = cmds.listRelatives(crvs[iz], p=True)
				crvName = cmds.rename(crvTrans, root+'_mainBaseCrv0#')
				cmds.select(crvName, joints)
				cmds.skinCluster(tsb=True)
				iz+=1
				print "Completed, Curve skinned to joints at cvs, with control objects at each joint."
			else:
				print "ERROR, Please select one or more curves."
	else:
		print "Error, Spline Joints with Controls was not created."

### attributes ###
# simple add attribute
def nwAtt_SimpleAdd():
	# sel
	sel = cmds.ls(sl=True)
	if sel:
		# get obj name
		objName = sel[0]
		# get
		longName = cmds.textFieldGrp('nwSAK_longName',q=True,tx=True)
		niceName = cmds.textFieldGrp('nwSAK_niceName',q=True,tx=True)
		# get attribute state and data type
		makeAtt = cmds.radioButtonGrp('nmSAK_makeType',q=True,sl=True)
		dataType = cmds.radioButtonGrp('nwSAK_dataType',q=True,sl=True)
		# float
		if dataType == 1:
			# get default
			default = cmds.textFieldGrp('nwSAK_defProp',q=True,tx=True)
			if default:
				default = float(default)
			else:
				default = 0
			if niceName:
				cmds.addAttr(ln=longName, nn=niceName, at='double', hasMinValue=True, hasMaxValue=True, defaultValue=default)
			else:
				cmds.addAttr(ln=longName, at='double', hasMinValue=True, hasMaxValue=True, defaultValue=default)
			# get numerical attibutes
			minimum = cmds.textFieldGrp('nwSAK_minProp',q=True,tx=True)
			maximum = cmds.textFieldGrp('nwSAK_maxProp',q=True,tx=True)
			if minimum:
				minimum = float(minimum)
				cmds.addAttr(objName+'.'+longName, edit=True, minValue=minimum)
			if maximum:
				maximum = float(maximum)
				cmds.addAttr(objName+'.'+longName, edit=True, maxValue=maximum)
		# boolean
		if dataType == 2:
			if niceName:
				cmds.addAttr(ln=longName, nn=niceName, at='bool')
			else:
				cmds.addAttr(ln=longName, at='bool')
		# enum
		if dataType == 3:
			eName = []
			count = 0
			while (count < 7):
				name = cmds.textFieldGrp('nwSAK_enumName'+str(count),q=True,tx=True)
				if name:
					eName.append(name)
				else:
					break
				count = count+1
			if not eName:
				# line
				nmGUI_func.nmGUI_runCheck('error','Enter at least one Enum name')
			# check nice name
			if niceName:
				cmds.addAttr(ln=longName, nn=niceName, at='enum', en=':'.join(eName))
			else:
				cmds.addAttr(ln=longName, at='enum', en=':'.join(eName))
		# set channel box vis
		if makeAtt == 1:
			cmds.setAttr(objName+'.'+longName, k=1)
		if makeAtt == 2:
			cmds.setAttr(objName+'.'+longName, channelBox=1)
		if makeAtt == 3:
			cmds.setAttr(objName+'.'+longName, k=0, channelBox=0)
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','No object selected')
		
#///////////////////////////////////////////////////////////////////////////////////#
#sk_attrShift
#created by: Sean Kealey (skealeye@gmail.com)
#ammended by: Nic Wiederhold (ghostnic8@gmail.com)
#4.15.11
#version: 1.1
#about: shift custom attributes in channel box up/dn
#to use:  select attributes, shift
#to run:  import sk_attrShift as skattr;skattr.sk_attrShiftUI()
#return:  none
#source: none
#********************************************************************#
#notes: -need select and highlight in channel box after shift 
#update history: ----------
#///////////////////////////////////////////////////////////////////////////////////#

#shift up
def nwAtt_Shiftup():
	obj = cmds.channelBox('mainChannelBox',q=True,mol=True)
	if obj:
		attr = cmds.channelBox('mainChannelBox',q=True,sma=True)
		if attr:
			for eachObj in obj:
				udAttr = cmds.listAttr(eachObj,ud=True)
				if not attr[0] in udAttr:
					sys.exit('selected attribute is static and cannot be shifted')
				#temp unlock all user defined attributes
				attrLock = cmds.listAttr(eachObj,ud=True,l=True)
				if attrLock:
					for alck in attrLock:
						cmds.setAttr(eachObj + '.' + alck,lock=0)
				#shift up
				for i in attr:
					attrLs = cmds.listAttr(eachObj,ud=True)
					attrSize = len(attrLs)
					attrPos = attrLs.index(i)
					if attrLs[attrPos-1]:
						cmds.deleteAttr(eachObj,at=attrLs[attrPos-1])
						cmds.undo()
					for x in range(attrPos+1,attrSize,1):
						cmds.deleteAttr(eachObj,at=attrLs[x])
						cmds.undo()
				#relock all user defined attributes			
				if attrLock:
					for alck in attrLock:
						cmds.setAttr(eachObj + '.' + alck,lock=1)
def nwAtt_ShiftDown():
	obj = cmds.channelBox('mainChannelBox',q=True,mol=True)
	if obj:
		attr = cmds.channelBox('mainChannelBox',q=True,sma=True)
		if attr:
			for eachObj in obj:
				udAttr = cmds.listAttr(eachObj,ud=True)
				if not attr[0] in udAttr:
					sys.exit('selected attribute is static and cannot be shifted')
				#temp unlock all user defined attributes
				attrLock = cmds.listAttr(eachObj,ud=True,l=True)
				if attrLock:
					for alck in attrLock:
						cmds.setAttr(eachObj + '.' + alck,lock=0)
				#shift down
				if len(attr) > 1:
					attr.reverse()
					sort = attr
				if len(attr) == 1:
					sort = attr 
				for i in sort:
					attrLs = cmds.listAttr(eachObj,ud=True)
					attrSize = len(attrLs)
					attrPos = attrLs.index(i)
					cmds.deleteAttr(eachObj,at=attrLs[attrPos])
					cmds.undo()
					for x in range(attrPos+2,attrSize,1):
						cmds.deleteAttr(eachObj,at=attrLs[x])
						cmds.undo()
				#relock all user defined attributes			
				if attrLock:
					for alck in attrLock:
						cmds.setAttr(eachObj + '.' + alck,lock=1)
						
### skinning ###
# mode
# object
def nmMode_object():
	'''
	this function switches the selection type to object.
	'''
	pass
# component
def nmMode_component():
	'''
	this function switches the selection type to component.
	'''
	pass
# edge
def nmMode_edge():
	'''
	this function switches the selection type to edge.
	'''
	pass

# weight lifter
# load mesh
def nmWeightLifter_loadMesh():
	'''
	this function will load the selected mesh and its skin cluster
	and the affected joints.
	'''
	
	# sel
	sel = cmds.ls(sl=True)
	# check sel for geo
	if (len(sel) == 1):
		if (cmds.listRelatives(sel[0],s=True)):
			rel = cmds.listRelatives(sel[0],s=True,pa=True)
			geo = []
			for stuff in rel:
				shape = stuff.split(sel[0])[-1]
				if 'Orig' not in shape:
					# only set up for polygons not nurbs or subdiv
					if cmds.objectType(stuff,i='mesh'):
						geo.append(stuff)
			if (geo):
				con = cmds.listConnections(geo[0],s=True,d=False)
				if (con):
					skin = []
					clust = []
					for stuff in con:
						if (cmds.objectType(stuff)=='skinCluster'):
							skin.append(stuff)
						elif (cmds.objectType(stuff)=='cluster'):
							clust.append(stuff)
					if (skin):
						if (len(skin)==1):
							# add mesh and skin cluster
							cmds.textFieldGrp('nmSAK_rigSkinMeshTFG',e=True,tx=sel[0])
							cmds.textFieldGrp('nmSAK_rigSkinClusterTFG',e=True,tx=skin[0])
							# find joints and append to tsl
    						inf = cmds.skinCluster(skin[0],q=True,inf=True)
    						# clear tsl
    						cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,ra=True)
    						cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,ra=True)
    						if (inf):
    							inf.sort()
    							for stuff in inf:
									print cmds.objectType(stuff)
									cmds.setAttr(stuff+'.liw',1)
									'''cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,a=stuff)
								# weights complete
								nmGUI_func.nmGUI_runCheck('complete','Bound mesh information as been loaded.')'''
							else:
								nmGUI_func.nmGUI_runCheck('error','Loaded skin cluster is broken.')
						else:
							nmGUI_func.nmGUI_runCheck('error','Multiple skinClusters found.')
					elif (clust):
						nmGUI_func.nmGUI_runCheck('error','Please remove clusters and reload bound mesh.')
					else:
						nmGUI_func.nmGUI_runCheck('error','Please load one bound mesh.')
				else:
					nmGUI_func.nmGUI_runCheck('error','Please load one bound mesh.')
			# no usable shape nodes	
			else:
				nmGUI_func.nmGUI_runCheck('error','No usable shape nodes.')
		# no shape nodes
		else:
			nmGUI_func.nmGUI_runCheck('error','Please load one bound mesh.')
	# number of selected doesn't match 1
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one bound mesh to load.')

# unlock joints
def nmWeightLifter_unlock():
	'''
	this function will move the selected lock joints into the
	active tsl and unlock the joints.
	'''
	sel = cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',q=True,si=True)
	index = []
	if (sel):
		# get index
		index.extend(cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',q=True,sii=True))
		# move
		for stuff in sel:
			if (cmds.objExists(stuff)):
				cmds.setAttr(stuff+'.liw',0)
				cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,a=stuff)
				cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,ri=stuff)
		# refocus locked tsl
		if (index):
			index.sort()
			cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,shi=index[0])
		# organize tsl
		new = cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',q=True,ai=True)
		if (new):
			new.sort()
			cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,ra=True)
			for stuff in new:
				cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,a=stuff)
			
		# keep selected
		cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,da=True)
		cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,si=sel)
		# focus selected
		index = cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',q=True,sii=True)
		index.sort()
		cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,shi=index[0])
		# complete
		nmGUI_func.nmGUI_runCheck('complete','Selected joints are now active.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one or more joints to activate.')
# unlock joints
def nmWeightLifter_lock():
	'''
	this function will move the selected active joints into the
	locked tsl and lock the joints.
	'''	
	sel = cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',q=True,si=True)
	if (sel):
		# move
		newSel = []
		for stuff in sel:
			if (cmds.objExists(stuff.split(' (Locked)')[0])):
				cmds.setAttr(stuff.split(' (Locked)')[0]+'.liw',1)
				cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,a=stuff.split(' (Locked)')[0])
				cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,ri=stuff)
				newSel.append(stuff.split(' (Locked)')[0])
		# organize tsl
		new = cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',q=True,ai=True)
		if (new):
			new.sort()
			cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,ra=True)
			for stuff in new:
				cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,a=stuff)
		if (newSel):
			# keep selected
			cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,da=True)
			cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,si=newSel)
		# focus selected
		index = cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',q=True,sii=True)
		index.sort()
		cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,shi=index[0])
		# complete
		nmGUI_func.nmGUI_runCheck('complete','Selected joints are now locked.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one or more joints to lock.')
# selection
def nmWeightLifter_lockSelect():
	'''
	this function will deselect the active joint tsl.
	'''
	cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,da=True)
def nmWeightLifter_actiSelect():
	'''
	this function will deselect the locked joint tsl.
	'''
	cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,da=True)	
# toggle lock
def nmWeightLifter_lockToggle():
	'''
	this function will toggle weight lock on the selected active joint.
	'''
	sel = cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',q=True,si=True)
	if (sel):
		newSel = []
		for stuff in sel:
			if (cmds.objExists(stuff.split(' (Locked)')[0])):
				cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,da=True)
				cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,si=stuff)
				index = cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',q=True,sii=True)[0]
				if ' (Locked)' in stuff:
					split = stuff.split(' (Locked)')[0]
					cmds.setAttr(split+'.liw',0)
					cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,ri=stuff)
					cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,ap=(index,split))
					newSel.append(split)
				else:
					cmds.setAttr(stuff+'.liw',1)
					cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,ri=stuff)
					cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,ap=(index,stuff+' (Locked)'))
					newSel.append(stuff+' (Locked)')
				
				# select 
				if (newSel):
					cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,da=True)
					cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,si=newSel)	
				# complete
				nmGUI_func.nmGUI_runCheck('complete','Lock weights toggled.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one or more joints to lock.')
# add influence
def nmWeightLifter_add():
	'''
	this function adds joints to the loaded skinCluster.
	'''
	# get
	skin = cmds.textFieldGrp('nmSAK_rigSkinClusterTFG',q=True,tx=True)
	# sel
	sel = cmds.ls(sl=True)
	# check sel for geo
	if sel:
		joints = []
		for stuff in sel:
			if (cmds.objectType(stuff)=='joint'):
				inf = []
				current = cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',q=True,ai=True)
				active = cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',q=True,ai=True)
				if (current):
					inf.extend(current)
				if (active):
					inf.extend(active)
				if stuff not in inf:
					cmds.skinCluster(skin,e=True,dr=4,lw=True,wt=0,ai=stuff)
					# add to list
					cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,a=stuff)
					joints.append(stuff)
		if (joints):
			# organize tsl
			new = cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',q=True,ai=True)
			if (new):
				new.sort()
				cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,ra=True)
				for stuff in new:
					cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,a=stuff)
			# select the newly added joints
			cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,da=True)
			cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',e=True,da=True)
			cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,si=joints)
			# focus selected
			index = cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',q=True,sii=True)
			index.sort()
			cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,shi=index[0])
			# complete
			nmGUI_func.nmGUI_runCheck('complete','Selected joints added to the skin cluster.')
		else:
			nmGUI_func.nmGUI_runCheck('error','No valid joints were added to the skin cluster.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one or more joints to add to the skin cluster.')
# remove influence
def nmWeightLifter_remove():
	'''
	this function removes joints from the loaded skinCluster.
	'''
	# get
	skin = cmds.textFieldGrp('nmSAK_rigSkinClusterTFG',q=True,tx=True)
	# sel
	sel = cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',q=True,si=True)
	# check sel for geo
	if (sel):
		for stuff in sel:
			cmds.skinCluster(skin,e=True,ri=stuff)
			cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',e=True,ri=stuff)
		# complete
		nmGUI_func.nmGUI_runCheck('complete','Selected joints removed from the skin cluster.')
	else:
		nmGUI_func.nmGUI_runCheck('error','Please select one or more joints to remove from the skin cluster.')	
# reload joint activity
def nmWeightLifter_reloadActivity():
	'''
	this function reloads the active and locked status of the loaded
	joints.
	'''
	active = cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',q=True,ai=True)
	locked = cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',q=True,ai=True)
	temp = []
	# cycle
	if (active):
		temp.extend(active)
		for stuff in active:
			if ' (Locked)' in stuff:
				split = stuff.split(' (Locked)')[0]
				if (cmds.objExists(split)):
					cmds.setAttr(split+'.liw',1)
			else:
				if (cmds.objExists(stuff)):
					cmds.setAttr(stuff+'.liw',0)
	if (locked):
		temp.extend(locked)
		for stuff in locked:
			if (cmds.objExists(stuff)):
				cmds.setAttr(stuff+'.liw',1)
	if (temp):
		nmGUI_func.nmGUI_runCheck('complete','Joint activity reloaded.')
	else:
		nmGUI_func.nmGUI_runCheck('error','No joint activity to reload.')
		
#

#

# la z boy
# mirror

# copy

### auto ###	
