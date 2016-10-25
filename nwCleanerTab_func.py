'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
================================================================================
================================================================================
Author: Nic Wiederhold
Script: nwCleanerTab_func.py
Collection: nmSwissArmyKnife.py
Website: NA
Date Created: 8/29/14
Last Updated: 10/6/14
================================================================================
================================================================================
				    FUNCTIONS:
nwDeleteDuplicatePanels
nwDeleteUnusedIntermediates
nwDeleteEmptyTransforms
nwDeleteUnknown
nwKilltheTURTLE
nwDoAllClean
nwGlobalDupRename









================================================================================
				    HOW TO RUN:
import nwCleanerTab_func
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
#      FUNCTION	#
#=======================#
# Delete duplicate panel
def nwDeleteDuplicatePanels():
	''' 
	This script deletes duplicate panels from the "panels" menu in the modelPanel window menu 
	AND also deletes the the panel's children.
	'''
	# list all panels
	panelList = cmds.lsUI( panels=1 )
	# get all modelPanels
	selMPanels = cmds.getPanel( type='modelPanel' )
	# get all blendShapePanels
	selBSPanels = cmds.getPanel( type='blendShapePanel' )
	# get all info Nodes:
	extras = cmds.ls(type="hyperView")
	# shotListManager?
	shotlistManager = cmds.ls('shotlistScriptNode')
	# deleted duplicate panels list
	duplicatePanels = []
	# lock shotlistScriptNode
	if shotlistManager:
		cmds.lockNode('shotlistScriptNode', lock=1)
	# kill hyperView extras
	for extra in extras:
		duplicatePanels.append(extra)
		cmds.delete(extra)
	# delete duplicate modelPanels
	for panels in selMPanels:
		split = panels.split('modelPanel')
		num = split[-1]
		numList = int(num)
		if ((numList) > 4):
			duplicatePanels.append(panels)
			cmds.deleteUI( panels, panel=1 )
	# delete duplicate blendShapePanels
	for panels in selBSPanels:
		split = panels.split('blendShapePanel')
		num = split[-1]
		numList = int(num)
		if ((numList) > 1):
			duplicatePanels.append(panels)
			cmds.deleteUI( panels, panel=1 )
	# delete duplicate hyperGraphPanels and nodeEditorPanels
	for panels in panelList:
		if "hyperGraphPanel" in panels:
			split = panels.split('hyperGraphPanel')
			num = split[-1]
			numList = int(num)
			if ((numList) > 1):
				duplicatePanels.append(panels)
				cmds.deleteUI( panels, panel=1 )
		elif "nodeEditorPanel" in panels:
			split = panels.split('nodeEditorPanel')
			num = split[-1]
			numList = int(num)
			if ((numList) > 1):
				duplicatePanels.append(panels)
				cmds.deleteUI( panels, panel=1 )
	# line
	if (duplicatePanels):
		dupPanelCount = int(len(duplicatePanels))
		nmGUI_func.nmGUI_runCheck( 'complete','{0} Duplicate panels deleted. See script editor for deleted panels list.'.format(dupPanelCount))
		print '\n'.join(duplicatePanels)
		print dupPanelCount,'Duplicate Panels Deleted'
	else:
		nmGUI_func.nmGUI_runCheck( 'complete', 'No duplicate panels detected.' )
# Delete orphan orig nodes
def nwDeleteUnusedIntermediates():
	'''
	This script deletes orphan intermediate nodes with no connections (unused)
	'''
	# get orphan intermediate nodes:
	IOnodes = cmds.ls(type='mesh',io=True)
	unused = []
	for nodes in IOnodes:
		if not cmds.listConnections(nodes):
			unused.append(nodes)
			cmds.delete(nodes)
	if (unused):
		totalOrphans = int(len(unused))
		nmGUI_func.nmGUI_runCheck( 'complete','{0} Unused intermediate nodes deleted. See script editor for list.'.format(totalOrphans))
		print '\n'.join(unused)
		print totalOrphans,'Orphan orig shapes deleted'
	else:
		nmGUI_func.nmGUI_runCheck( 'complete', 'No unused intermediate nodes detected.' )
# Delete empty transforms and groups
def nwDeleteEmptyTransforms():
	'''
	This script deletes empty transforms including empty groups
	'''
	transforms =  cmds.ls(type='transform')
	deleteList = []
	for tran in transforms:
		if cmds.nodeType(tran) == 'transform':
			children = cmds.listRelatives(tran, c=True)
			connections = cmds.listConnections(tran)
			if connections == None:
				if children == None:
					deleteList.append(tran)
					cmds.delete(tran)
	if deleteList:
		totalTrans = int(len(deleteList))
		nmGUI_func.nmGUI_runCheck( 'complete','{0} Empty transforms/groups deleted. See script editor for list.'.format(totalTrans))
		print '\n'.join(deleteList)
		print totalTrans,'Empty transforms/groups deleted'
	else:
		nmGUI_func.nmGUI_runCheck( 'complete', 'No empty transforms/groups detected.' )
# Delete unknown nodes
def nwDeleteUnknown():
	unknowns = cmds.ls(type='unknown')
	deleteUnknown = []
	unknownRef = []
	if unknowns:
		for unknown in unknowns:
			ref = cmds.referenceQuery(unknown, isNodeReferenced=True)
			if ref == False:
				cmds.lockNode(unknowns, lock=0)
				deleteUnknown.append(unknown)
				cmds.delete(unknown)
			else:
				unknownRef.append(unknown)
	if unknownRef:
		totalUnknownRef = int(len(unknownRef))
		print '\n'.join(unknownRef)
		print totalUnknownRef, 'Unknown nodes are referenced and NOT removed'
		if deleteUnknown:
			totalUnknown = int(len(deleteUnknown))
			nmGUI_func.nmGUI_runCheck( 'error','{0} Unknown nodes deleted. Referenced file(s) contain unknown node(s)'.format(totalUnknown))
		else:
			nmGUI_func.nmGUI_runCheck( 'error','Referenced file(s) contain {0} unknown node(s)'.format(totalUnknownRef))
	elif deleteUnknown:
		totalUnknown = int(len(deleteUnknown))
		print '\n'.join(deleteUnknown)
		print totalUnknown,'Empty transforms/groups deleted'
		if unknownRef:
			nmGUI_func.nmGUI_runCheck( 'error','{0} Unknown nodes deleted. Referenced file(s) contain unknown node(s)'.format(totalUnknown))
		else:
			nmGUI_func.nmGUI_runCheck( 'complete','{0} Unknown nodes deleted. See script editor for list.'.format(totalUnknown))
	else:
		nmGUI_func.nmGUI_runCheck( 'complete', 'No unknown nodes detected.' )
# Unload TURTLE and delete shelf
def nwKilltheTURTLE():
	tShelf = cmds.shelfLayout('TURTLE', exists=True)
	turtle = cmds.pluginInfo('Turtle.mll', loaded=True, q=True)
	if turtle:
		types = cmds.pluginInfo('Turtle.mll', dependNode=True, q=True)
		nodes = cmds.ls(type=types, long=True)
		if nodes:
			cmds.lockNode(nodes, lock=False)
			cmds.delete(nodes)
		cmds.flushUndo()
		cmds.unloadPlugin('Turtle.mll')
	else:
		nmGUI_func.nmGUI_runCheck( 'error','TURTLE already unloaded' )
	if tShelf:
		mel.eval('deleteShelfTab "TURTLE";')
		nmGUI_func.nmGUI_runCheck( 'complete','TURTLE unloaded and shelf deleted.' )
	else:
		nmGUI_func.nmGUI_runCheck( 'error','TURTLE shelf already deleted' )
# doAll
def nwDoAllClean():
	def combine_funcs(*funcs):
		def combined_func(*args, **kwargs):
			for f in funcs:
				f(*args, **kwargs)
		return combined_func
	combine_funcs(nwKilltheTURTLE(), nwDeleteUnknown(), nwDeleteEmptyTransforms(), nwDeleteUnusedIntermediates(), nwDeleteDuplicatePanels())
	print "I worked"

#def doIT():
#	pass
# Global rename duplicate objects with unique names
def nwGlobalDupRename():
	# get all transforms
	allObjects = cmds.ls(transforms=True)
	dup=[]
	dupName=[]
	# get duplicates
	for thing in allObjects:
		name=thing.split('|')[-1]
		num=len(cmds.ls(name))
		if num > 1:
			dup.append(thing)
			if not name in dupName:
				dupName.append(name)
	# rename duplicates
	for dups in dupName:
		temp=cmds.ls(dups)
		i=1
		for thing in temp:
			if (cmds.ls(thing, transforms=True)):
				newName=thing.split('|')[-1]
				cmds.rename(thing, newName+str(i))
				i+=1
			# rename shape if matches transform
			if (cmds.ls(thing, shapes=True)):
				newName=thing.split('|')[-1]
				cmds.rename(thing, newName+'shape'+str(i))
				i+=1






