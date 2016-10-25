'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
================================================================================
================================================================================
Author: Nole Murphy
Script: nmObjShow_func.py
Collection: nmSwissArmyKnife.py
Website: www.nm3d.net
Date Created: 4/4/2011
Last Updated: 4/4/2011
================================================================================
================================================================================
				    FUNCTIONS:














================================================================================
				    HOW TO RUN:
import nmObjShow_func
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
# isolate check
def nmShow_isolateCheck():
	'''
	this function will check to see if the selection is isolated upon
	calling the GUI.
	'''
	# get panel
	panel = cmds.getPanel(wf=True)
	# get/set state
	if ((panel=='modelPanel1')or(panel=='modelPanel2')or(panel=='modelPanel3')or(panel=='modelPanel4')):
		state = cmds.isolateSelect(panel,q=True,s=True)
		# edit
		cmds.checkBox('nmSAK_mainIsolateCB',e=True,v=state)
# isolate selected
def nmShow_isolate():
	'''
	this function isolates the selected objects.
	'''
	# get check box
	check = cmds.checkBox('nmSAK_mainIsolateCB',q=True,v=True)
	# get current panel
	panel = cmds.getPanel(wf=True)
	# isolate
	if ((panel=='modelPanel1')or(panel=='modelPanel2')or(panel=='modelPanel3')or(panel=='modelPanel4')):
		cmds.isolateSelect(panel,s=check)
		cmds.isolateSelect(panel,addSelected=True)
		mel.eval('isoSelectAutoAddNewObjs '+panel+' true;')
		mel.eval('setFilterScript "initialShadingGroup";')
		mel.eval('setFilterScript "initialParticleSE";')
		mel.eval('setFilterScript "defaultLightSet";')
		mel.eval('setFilterScript "defaultObjectSet";')
		mel.eval('updateModelPanelBar '+panel+';')
	else:
		cmds.checkBox('nmSAK_mainIsolateCB',e=True,v=0)
# add selected
def nmShow_add():
	'''
	this function adds the selected objects to isolation.
	'''
	# get panel
	panel = cmds.getPanel(wf=True)
	# add selected
	if ((panel=='modelPanel1')or(panel=='modelPanel2')or(panel=='modelPanel3')or(panel=='modelPanel4')):
		cmds.isolateSelect(panel,addSelected=True)
		mel.eval('setFilterScript "initialShadingGroup";')
		mel.eval('setFilterScript "initialParticleSE";')
		mel.eval('setFilterScript "defaultLightSet";')
		mel.eval('setFilterScript "defaultObjectSet";')
# remove selected
def nmShow_remove():
	'''
	this function removes the selected objects to isolation.
	'''
	# get panel
	panel = cmds.getPanel(wf=True)
	# add selected
	if ((panel=='modelPanel1')or(panel=='modelPanel2')or(panel=='modelPanel3')or(panel=='modelPanel4')):
		cmds.isolateSelect(panel,rs=True)
		mel.eval('setFilterScript "initialShadingGroup";')
		mel.eval('setFilterScript "initialParticleSE";')
		mel.eval('setFilterScript "defaultLightSet";')
		mel.eval('setFilterScript "defaultObjectSet";')
# show rotation axis
def nmShow_rotationAxis():
	'''
	this function will show the selected objects' local rotation axis.
	'''
	# sel
	sel = cmds.ls(sl=True)
	# lists
	off = ['blah']
	on = ['blah']
	# check
	if (len(sel)>0):
		for stuff in sel:
			if ((cmds.objectType(stuff)=='transform')or(cmds.objectType(stuff)=='joint')):
				if (cmds.getAttr(stuff+'.displayLocalAxis')==0):
					off.append(stuff)
				else:
					on.append(stuff)
		for stuff in sel:
			if ((cmds.objectType(stuff)=='transform')or(cmds.objectType(stuff)=='joint')):
				# average
				if (len(on) > len(off)):
					cmds.setAttr(stuff+'.displayLocalAxis',0)
				elif (len(on) < len(off)):
					cmds.setAttr(stuff+'.displayLocalAxis',1)
				else:
					cmds.setAttr(stuff+'.displayLocalAxis',0)
	else:
		pass
# show all
def nmShow_showAll():
	'''
	this function edits the check boxes and the visibility state
	of the given objects and check boxes.
	'''
	# get
	check = cmds.checkBox('nmSAK_alo',q=True,v=True)
	if check == 0:
		state = 'false'
	else:
		state = 'true'
	# list
	objList = ['nc','ns','pm','sds','pl','lt','ca','j','ikh','df','dy','fl','hs',
		'fo','ncl','npa','nr','dc','lc','dim','pv','ha','tx','str']
	for stuff in objList:
		cmds.checkBox('nmSAK_'+stuff,e=True,v=check)
		mel.eval('modelEditor -e -'+stuff+' '+state+' modelPanel4;')
# all
def nmShow_all():
	'''
	this function checks the all button if the list of check boxes
	are all checked.
	'''
	# refresh all
	count = 0
	# list
	objList = ['nc','ns','pm','sds','pl','lt','ca','j','ikh','df','dy','fl','hs',
		'fo','ncl','npa','nr','dc','lc','dim','pv','ha','tx','str']
	# update
	for stuff in objList:
		val = cmds.checkBox('nmSAK_'+stuff,q=True,v=True)
		count += val
	# check all
	if (count == 24):
		cmds.checkBox('nmSAK_alo',e=True,v=1)
	else:
		cmds.checkBox('nmSAK_alo',e=True,v=0)
# refresh
def nmShow_refresh():
	'''
	this function gathers what is visible in the persp view and
	applies it to the GUI show check boxes.
	'''
	# list
	objList = ['nc','ns','pm','sds','pl','lt','ca','j','ikh','df','dy','fl','hs',
		'fo','ncl','npa','nr','dc','lc','dim','pv','ha','tx','str','m','cv','hu','gr',
		'hud','sel']
	# update
	for stuff in objList:
		val = mel.eval('modelEditor -q -'+stuff+' modelPanel4;')
		cmds.checkBox('nmSAK_'+stuff,e=True,v=val)
	# refresh all
	nmShow_all()
# show or hide
def nmShow_showHide(control):
	'''
	this function shows/hides the given objects.
	'''
	# split
	var = control.split('nmSAK_')[-1]
	# edit
	if (cmds.checkBox(control,q=True,v=True)==1):
		mel.eval('modelEditor -e -'+var+' true modelPanel4;')
	else:
		mel.eval('modelEditor -e -'+var+' false modelPanel4;')
	# update from scene
	nmShow_refresh()
	# refresh all
	nmShow_all()
