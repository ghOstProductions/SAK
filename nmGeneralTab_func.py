'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
================================================================================
================================================================================
Author: Nole Murphy
Ammended: Nic Wiederhold
Script: nmGeneralTab_func.py
Collection: nmSwissArmyKnife.py
Website: www.nm3d.net
Date Created: 3/6/2011
Last Updated: 10/6/2014
================================================================================
================================================================================
				    FUNCTIONS:
nmManipulator_local
nmManipulator_world
nmGrouper_group
nmGrouper_ungroup
nmMatchMaker_ab
nmMatchMaker_ba
nmHistory_delete
nmCenter_center
nmMrFreeze_freeze
nmMrFreeze_zero
nmRenamer_searchReplace
nmRenamer_prefix
nmRenamer_suffix
nmRenamer_rename
nmOuterSpace_refresh
nmOuterSpace_create
nmOuterSpace_setSel
nmOuterSpace_remove
================================================================================
				    HOW TO RUN:
import nmGeneralTab_func
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
### manipulator ###
# object
def nmManipulator_object():
	'''
	this function will set all the transform tools to local space.
	'''
	cmds.manipMoveContext('Move',e=True,mode=0)
	cmds.manipRotateContext('Rotate',e=True,mode=0)
	try:
		cmds.manipScaleContext('Scale',e=True,mode=0)
	except:
		pass
	# line
	nmGUI_func.nmGUI_runCheck('complete','Manipulator tools have been set to object space.')
# local
def nmManipulator_local():
	'''
	this function will set all the transform tools to local space.
	'''
	cmds.manipMoveContext('Move',e=True,mode=1)
	cmds.manipRotateContext('Rotate',e=True,mode=0)
	try:
		cmds.manipScaleContext('Scale',e=True,mode=1)
	except:
		pass
	# line
	nmGUI_func.nmGUI_runCheck('complete','Manipulator tools have been set to local space.')
# world
def nmManipulator_world():
	'''
	this function will set all the transform tools to world space.
	'''
	cmds.manipMoveContext('Move',e=True,mode=2)
	cmds.manipRotateContext('Rotate',e=True,mode=1)
	try:
		cmds.manipScaleContext('Scale',e=True,mode=2)
	except:
		pass
	# line
	nmGUI_func.nmGUI_runCheck('complete','Manipulator tools have been set to world space.')

### grouper ###
# group
def nmGrouper_group():
	'''
	this function will group the selected objects either at its
	position or at the origin. will also auto name the group
	depending if there is a group below that has the same naming
	convention. can do multiple objects with different numbered
	null groups.
	'''
	# get
	place = cmds.radioButtonGrp('nmSAK_grpRBG',q=True,sl=True)
	# sel
	sel = cmds.ls(sl=True)
	if (len(sel) > 0):
		# group list
		groups = []
		# group selected
		for stuff in sel:
			par = cmds.listRelatives(stuff,p=True)
			if '_null_' in stuff:
				# split obj
				split = stuff.split('_null_')
				objName = split[0]
				num = split[-1]
				new = int(num) + 1
				if not(cmds.objExists(objName+'_null_'+str(new))):
					# create group
					cmds.group(n=objName+'_null_'+str(new),em=True)
					if (place == 1):
						cmds.parentConstraint(stuff,objName+'_null_'+str(new),mo=False,n='tEmPbLaHbLaH')
						cmds.delete('tEmPbLaHbLaH')
					cmds.parent(stuff,objName+'_null_'+str(new))
					groups.append(objName+'_null_'+str(new))
					if (par):
						cmds.parent(objName+'_null_'+str(new),par[0])
					cmds.select(cl=True)
			else:
				if (cmds.objExists(stuff+'_null_0')==0):
					cmds.group(n=stuff+'_null_0',em=True)
					if (place == 1):
						cmds.parentConstraint(stuff,stuff+'_null_0',mo=False,n='tEmPbLaHbLaH')
						cmds.delete('tEmPbLaHbLaH')
					cmds.parent(stuff,stuff+'_null_0')
					groups.append(stuff+'_null_0')
					if (par):
						cmds.parent(stuff+'_null_0',par[0])
					cmds.select(cl=True)
		# sel groups
		if (groups):
			cmds.select(groups,r=True)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Selected objects have been grouped.')
	else:
		# create empty group
		cmds.group(em=True)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Null group has been created.')
# ungroup
def nmGrouper_ungroup():
	'''
	This function will attempt to ungroup the selected items.
	'''
	# sel
	sel = cmds.ls(sl=True)
	if (len(sel) > 0):
		# ungroup selected
		for stuff in sel:
			if (cmds.listRelatives(stuff,c=True)):
				cmds.ungroup(stuff)
				# line
				nmGUI_func.nmGUI_runCheck('complete','Selected objects have been ungrouped.')
			else:
				# line
				nmGUI_func.nmGUI_runCheck('error','Please select a parent node to ungroup.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')

### match maker ###
# a to b
def nmMatchMaker_ab():
	'''
	this function will move the selected item "a's" tranforms or 
	pivot to other selected items "b". this move can be done with 
	several options. nothing checked will do the move normally. with
	average checked, "a" will be averaged with selection "b". 
	checking order will allow you to selected multiple a-b
	and do the moves all at once.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# get checkbox
	avg = cmds.checkBox('nmSAK_movAvgCHBX',q=True,v=True)
	ordr = cmds.checkBox('nmSAK_movOrdCHBX',q=True,v=True)
	types = cmds.radioButtonGrp('nmSAK_movTypeRBG',q=True,sl=True)
	# check
	if (len(sel) > 1):
		if (types==1):
			if (avg == 1):
				if (len(sel) > 1):
					sels = cmds.ls(sl=True)
					sels.remove(sels[0])
					cmds.parentConstraint(sels,sel[0],mo=False,n='tEmPbLaHbLaH')
					cmds.delete('tEmPbLaHbLaH')
			elif (ordr == 1):
				if ((len(sel))%2):
					nmGUI_func.nmGUI_runCheck('error','An odd number of objects are selected.')
				else:
					i = 0
					# move selected
					while (i < len(sel)-1):
						cmds.parentConstraint(sel[i+1],sel[i],mo=False,n='tEmPbLaHbLaH')
						cmds.delete('tEmPbLaHbLaH')
						# counter
						i += 2
			else:
				i = 0
				# move selected
				while (i < len(sel)-1):
					cmds.parentConstraint(sel[-1],sel[i],mo=False,n='tEmPbLaHbLaH')
					cmds.delete('tEmPbLaHbLaH')
					# counter
					i += 1
		else:
			if (avg == 1):
				if (len(sel) > 1):
					sels = cmds.ls(sl=True)
					sels.remove(sels[0])
					cmds.spaceLocator(n='ImJuStTeMpOrArYmK')
					cmds.parentConstraint(sels,'ImJuStTeMpOrArYmK',mo=False,n='tEmPbLaHbLaH')
					cmds.delete('tEmPbLaHbLaH')
					get = cmds.xform('ImJuStTeMpOrArYmK',q=True,rp=True,ws=True)
					cmds.xform(sel[0],p=True,ws=True,rp=(get[0],get[1],get[2]))
					cmds.xform(sel[0],p=True,ws=True,sp=(get[0],get[1],get[2]))
					cmds.delete('ImJuStTeMpOrArYmK')
					cmds.select(sel)
			elif (ordr == 1):
				if ((len(sel))%2):
					nmGUI_func.nmGUI_runCheck('error','An odd number of objects are selected.')
				else:
					i = 0
					# move selected
					while (i < len(sel)-1):
						get = cmds.xform(sel[i+1],q=True,rp=True,ws=True)
						cmds.xform(sel[i],p=True,ws=True,rp=(get[0],get[1],get[2]))
						cmds.xform(sel[i],p=True,ws=True,sp=(get[0],get[1],get[2]))
						# counter
						i += 2
			else:
				get = cmds.xform(sel[-1],q=True,rp=True,ws=True)
				# set
				i = 0
				# move selected
				while (i < len(sel)-1):
					cmds.xform(sel[i],p=True,ws=True,rp=(get[0],get[1],get[2]))
					cmds.xform(sel[i],p=True,ws=True,sp=(get[0],get[1],get[2]))
					# counter
					i += 1
		# line
		nmGUI_func.nmGUI_runCheck('complete','Match has been made from a to b.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select two or more objects.')
# b to a
def nmMatchMaker_ba():
	'''
	this function will move the selected item "b's" tranforms or 
	pivot to other selected items "b". this move can be done with 
	several options. nothing checked will do the move normally. with
	average checked, "b" will be averaged with selection "a". 
	checking order will allow you to selected multiple b-a
	and do the moves all at once.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# get checkbox
	avg = cmds.checkBox('nmSAK_movAvgCHBX',q=True,v=True)
	ordr = cmds.checkBox('nmSAK_movOrdCHBX',q=True,v=True)
	types = cmds.radioButtonGrp('nmSAK_movTypeRBG',q=True,sl=True)
	# check
	if (len(sel) > 1):
		if (types==1):
			if (avg == 1):
				if (len(sel) > 1):
					sels = cmds.ls(sl=True)
					sels.remove(sels[-1])
					cmds.parentConstraint(sels,sel[-1],mo=False,n='tEmPbLaHbLaH')
					cmds.delete('tEmPbLaHbLaH')
			elif (ordr == 1):
				if ((len(sel))%2):
					nmGUI_func.nmGUI_runCheck('error','An odd number of objects are selected.')
				else:
					i = 0
					# move selected
					while (i < len(sel)-1):
						cmds.parentConstraint(sel[i],sel[i+1],mo=False,n='tEmPbLaHbLaH')
						cmds.delete('tEmPbLaHbLaH')
						# counter
						i += 2
			else:
				i = 1
				# move selected
				while (i < len(sel)):
					cmds.parentConstraint(sel[0],sel[i],mo=False,n='tEmPbLaHbLaH')
					cmds.delete('tEmPbLaHbLaH')
					# counter
					i += 1
		else:
			if (avg == 1):
				if (len(sel) > 1):
					sels = cmds.ls(sl=True)
					sels.remove(sels[-1])
					cmds.spaceLocator(n='ImJuStTeMpOrArYmK')
					cmds.parentConstraint(sels,'ImJuStTeMpOrArYmK',mo=False,n='tEmPbLaHbLaH')
					cmds.delete('tEmPbLaHbLaH')
					get = cmds.xform('ImJuStTeMpOrArYmK',q=True,rp=True,ws=True)
					cmds.xform(sel[-1],p=True,ws=True,rp=(get[0],get[1],get[2]))
					cmds.xform(sel[-1],p=True,ws=True,sp=(get[0],get[1],get[2]))
					cmds.delete('ImJuStTeMpOrArYmK')
					cmds.select(sel)
			elif (ordr == 1):
				if ((len(sel))%2):
					nmGUI_func.nmGUI_runCheck('error','An odd number of objects were selected.')
				else:
					i = 0
					# move selected
					while (i < len(sel)-1):
						get = cmds.xform(sel[i],q=True,rp=True,ws=True)
						cmds.xform(sel[i+1],p=True,ws=True,rp=(get[0],get[1],get[2]))
						cmds.xform(sel[i+1],p=True,ws=True,sp=(get[0],get[1],get[2]))
						# counter
						i += 2
			else:
				get = cmds.xform(sel[0],q=True,rp=True,ws=True)
				# set
				i = 1
				# move selected
				while (i < len(sel)):
					cmds.xform(sel[i],p=True,ws=True,rp=(get[0],get[1],get[2]))
					cmds.xform(sel[i],p=True,ws=True,sp=(get[0],get[1],get[2]))
					# counter
					i += 1
		# line
		nmGUI_func.nmGUI_runCheck('complete','Match has been made from b to a.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select two or more objects.')

### history ###
def nmHistory_delete():
	'''
	this function deletes history on the selected objects. options
	are all history or non-deformer history.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# get deformer check box
	check = cmds.checkBox('nmSAK_hisCHBX',q=True,v=True)
	# check
	if (len(sel) > 0):
		for stuff in sel:
			# check for non def
			if (check == 1):
				try:
					mel.eval('doBakeNonDefHistory( 1,{"prePost"});')
				except:
					pass
			else:
				cmds.delete(stuff,ch=True)
		# line
		nmGUI_func.nmGUI_runCheck('complete','History has been deleted.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')

### center ###
def nmCenter_center():
	'''
	this functions centers the rotation and scale pivots on the
	selected objects.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel) > 0):
		for stuff in sel:
			cmds.xform(stuff,cp=True)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Pivots have been centered.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')

### mr. freeze ###
# freeze
def nmMrFreeze_freeze():
	'''
	this function will freeze transforms on the selected objects
	given the checked options.
	'''
	# get trans
	trans = cmds.checkBoxGrp('nmSAK_frzCBG',q=True,v1=True)
	# get rot
	rot = cmds.checkBoxGrp('nmSAK_frzCBG',q=True,v2=True)
	# get scl
	scl = cmds.checkBoxGrp('nmSAK_frzCBG',q=True,v3=True)
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
	trans = cmds.checkBoxGrp('nmSAK_frzCBG',q=True,v1=True)
	# get rot
	rot = cmds.checkBoxGrp('nmSAK_frzCBG',q=True,v2=True)
	# get scl
	scl = cmds.checkBoxGrp('nmSAK_frzCBG',q=True,v3=True)
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
		
### renamer ###
# search and replace
def nmRenamer_searchReplace():
	'''
	this function will search through the selected objects and find
	the search string and replace it with the replace string. also
	works with having the replace blank so you can get rid of strings
	you dont want or need in the selected.
	'''
	# sel
	sel = cmds.ls(sl=True)
	sel.sort()
	sel.reverse()
	# get
	search = cmds.textFieldGrp('nmSAK_renSearchTFG',q=True,tx=True)
	replace = cmds.textFieldGrp('nmSAK_renReplaceTFG',q=True,tx=True)
	searLen = len(search)
	# check
	if (len(sel) > 0):
		if not(search == ''):
			for stuff in sel:
				new = stuff.split('|')[-1]
				if search in new:
					start = new.find(search)
					after = start+searLen
					# rename
					cmds.rename(stuff,new[:start]+replace+new[after:])
			# line
			nmGUI_func.nmGUI_runCheck('complete','"'+search+'" has been replaced with "'+replace+'".')
		else:
			# line
			nmGUI_func.nmGUI_runCheck('error','Please specify a search string to be replaced.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')
# prefix
def nmRenamer_prefix():
	'''
	this function will add a prefix to the selected objects.
	'''
	# sel
	sel = cmds.ls(sl=True)
	sel.sort()
	sel.reverse()
	# get
	prefix = cmds.textFieldGrp('nmSAK_renPrefixTFG',q=True,tx=True)
	# check
	if (len(sel) > 0):
		if not(prefix == ''):
			for stuff in sel:
				new = stuff.split('|')[-1]
				cmds.rename(stuff,prefix+new)
			# line
			nmGUI_func.nmGUI_runCheck('complete','Prefix "'+prefix+'" has been added.')
		else:
			# line
			nmGUI_func.nmGUI_runCheck('error','Please specify a string to be added as a prefix.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')
# suffix
def nmRenamer_suffix():
	'''
	this function will add a prefix to the selected objects.
	'''
	# sel
	sel = cmds.ls(sl=True)
	sel.sort()
	sel.reverse()
	# get
	suffix = cmds.textFieldGrp('nmSAK_renSuffixTFG',q=True,tx=True)
	# check
	if (len(sel) > 0):
		if not(suffix == ''):
			for stuff in sel:
				new = stuff.split('|')[-1]
				cmds.rename(stuff,new+suffix)
			# line
			nmGUI_func.nmGUI_runCheck('complete','Suffix "'+suffix+'" has been added.')
		else:
			# line
			nmGUI_func.nmGUI_runCheck('error','Please specify a string to be added as a suffix.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')
# rename
def nmRenamer_rename():
	'''
	this function will rename the selected objects given the start
	counter and the padding.
	'''
	# sel
	sel = cmds.ls(sl=True,l=True)
	numRange = []
	# get
	name = cmds.textFieldGrp('nmSAK_renNameTFG',q=True,tx=True)
	start = cmds.intFieldGrp('nmSAK_renStartIFG',q=True,v1=True)
	pad = cmds.intFieldGrp('nmSAK_renPadIFG',q=True,v1=True)
	count = '%0'+str(pad)+'d'
	# rename
	if (len(sel)>0):
		if not(name == ''):
			for stuff in sel:
				numRange.append(start)
				start+=1
			i=0
			while (i<len(numRange)):
				sel = cmds.ls(sl=True,l=True)
				cmds.rename(sel[i],name+count %numRange[i])
				i+=1
			# line
			nmGUI_func.nmGUI_runCheck('complete','Selected objects have been renamed "'+name+'*".')
		else:
			# line
			nmGUI_func.nmGUI_runCheck('error','Please specify a rename string.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')

### outer space ###
# refresh
def nmOuterSpace_refresh():
	'''
	this function will get all the namespaces in the scene and add them
	dynamically to the drop down menu for selection.
	'''
	# get
	current = cmds.namespaceInfo(lon=True)
	curNames = cmds.optionMenuGrp('nmSAK_namespaceOMG',q=True,ill=True)
	curNames.remove(curNames[0])
	# remove all
	if (curNames):
		for stuff in curNames:
			cmds.deleteUI(stuff,mi=True)
	# add
	if (current):
		for stuff in current:
			cmds.setParent('nmSAK_namespaceOMG')
			cmds.menuItem(l=stuff)
# create namespace
def nmOuterSpace_create():
	'''
	this function will add the given string as a namespace to the scene.
	'''
	# get
	namespace = cmds.textFieldGrp('nmSAK_genNameSpcTFG',q=True,tx=True)
	# create
	if not(namespace==''):
		if not(cmds.namespace(ex=namespace)):
			cmds.namespace(add=namespace)
			nmGUI_func.nmGUI_runCheck('complete','Namespace "'+namespace+'" has been created.')
			nmOuterSpace_refresh()
		else:
			# line
			nmGUI_func.nmGUI_runCheck('error','Namespace already exists.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please specify a namespace string to be created.')
# set selected
def nmOuterSpace_setSel():
	'''
	this function will set the current selected objects under the given
	namespace.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# get
	curSel = cmds.optionMenuGrp('nmSAK_namespaceOMG',q=True,sl=True)
	if (curSel == 1):
		curName = ':'
	else:
		curName = cmds.optionMenuGrp('nmSAK_namespaceOMG',q=True,v=True)+':'
	# check
	if (len(sel)>0):
		# set
		for stuff in sel:
			split = stuff.split(':')[-1]
			cmds.rename(stuff,curName+split)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Selected objects have been set to "'+curName+'".')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')

# remove
def nmOuterSpace_remove():
	'''
	this function will remove all namespaces from the selected objects.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# check
	if (len(sel)>0):
		for stuff in sel:
			split = stuff.split(':')[-1]
			cmds.rename(stuff,':'+split)
		# line
		nmGUI_func.nmGUI_runCheck('complete','Namespaces have been removed from the selected objects.')
	else:
		# line
		nmGUI_func.nmGUI_runCheck('error','Please select one or more objects.')
