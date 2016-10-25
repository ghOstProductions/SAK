'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
================================================================================
================================================================================
Author: Nole Murphy
Ammended: Nic Wiederhold
Script: nmGUI_func.py
Collection: ghOst_SwissArmyKnife
Website: www.NM3D.net
Date Created: 9/2/2010
Last Updated: 10/7/2016
================================================================================
================================================================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#=======================#
#      MAIN IMPORTS	#
#=======================#
# import maya commands
import maya.cmds as cmds 
# import maya mel commands
import maya.mel as mel
# import sys
mel.eval('python("import sys")')
# operating system path
import os.path
#=======================#
#    MAIN VARIABLES	#
#=======================#
# script name variable
sn=__name__
#=======================#
#    IMPORT FUNCTIONS	#
#=======================#
import nmObjShow_func
import nmGeneralTab_func
import nwModelingTab_func
import nmRiggingTab_func
import nwCleanerTab_func
import nwAnimTab_func
#=======================#
#        CLASSES	#
#=======================#
# callback class for compressing functions into one command
class Callback():
	_callData = None
	def __init__(self,func,*args,**kwargs):
		self.func = func
		self.args = args
		self.kwargs = kwargs
	def __call__(self, *args):
		Callback._callData = (self.func, self.args, self.kwargs)
		mel.eval('global proc py_%s(){python("sys.modules[\'%s\'].Callback._doCall()");}'
			%(self.func.__name__, __name__))
		try:
			mel.eval('py_%s()'%self.func.__name__)
		except RuntimeError:
			pass
		if isinstance(Callback._callData, Exception):
			raise Callback._callData
		return Callback._callData 
	@staticmethod
	def _doCall():
		(func, args, kwargs) = Callback._callData
		Callback._callData = func(*args, **kwargs)
#############################################################################
# callback multiple functions
#def combine_funcs(*funcs):
#   def combined_func(*args, **kwargs):
#       for f in funcs:
#           f(*args, **kwargs)
#   return combined_func
#=======================#
#     GUI FUNCTIONS	#
#=======================#
##############################################################################
# create function to open website
def nmGUI_website():
	'''
	
	'''
	cmds.showHelp('http://www.nm3d.net/',a=True)
##############################################################################
# error function
def nmGUI_runCheck(type,message):
	'''
	
	'''
	if (type == 'complete'):
		cmds.textField('nmSAK_mainPrintTFG',e=True,tx=message)
		cmds.textField('nmSAK_mainPrintTFG',e=True,bgc=(0,0,0))
	elif (type == 'error'):
		cmds.textField('nmSAK_mainPrintTFG',e=True,tx=message)
		cmds.textField('nmSAK_mainPrintTFG',e=True,bgc=(1.0,0.353,0.353))
##############################################################################
# off for order
def nmMatchMaker_average():
	'''
	
	'''
	# get checkbox
	avg = cmds.checkBox('nmSAK_movAvgCHBX',q=True,v=True)
	###
	if (avg == 1):
		cmds.checkBox('nmSAK_movOrdCHBX',e=True,v=0)
##############################################################################
# off for order
def nmMatchMaker_order():
	'''
	
	'''
	# get checkbox
	ordr = cmds.checkBox('nmSAK_movOrdCHBX',q=True,v=True)
	###
	if (ordr == 1):
		cmds.checkBox('nmSAK_movAvgCHBX',e=True,v=0)
##############################################################################
# freeze check boxes
def nmMrFreeze_box():
	'''
	
	'''
	# get trans
	trans = cmds.checkBoxGrp('nmSAK_frzCBG',q=True,v1=True)
	# get rot
	rot = cmds.checkBoxGrp('nmSAK_frzCBG',q=True,v2=True)
	# get scl
	scl = cmds.checkBoxGrp('nmSAK_frzCBG',q=True,v3=True)
	### check for all
	if ((trans == 1)and(rot == 1)and(scl == 1)):
		cmds.checkBox('nmSAK_frzAllCB',e=True,v=1)
	else:
		cmds.checkBox('nmSAK_frzAllCB',e=True,v=0)
##############################################################################		
# freeze check boxes
def nmMrFreeze_allBox():
	'''
	
	'''
	# get all
	all = cmds.checkBox('nmSAK_frzAllCB',q=True,v=True)
	### check all
	if (all == 1):
		cmds.checkBoxGrp('nmSAK_frzCBG',e=True,v1=1,v2=1,v3=1)
	else:
		cmds.checkBoxGrp('nmSAK_frzCBG',e=True,v1=0,v2=0,v3=0)
##############################################################################		
# freeze check boxes
def nwMrFreezeMod_box():
	'''
	
	'''
	# get trans
	trans = cmds.checkBoxGrp('nwSAK_modfrzCBG',q=True,v1=True)
	# get rot
	rot = cmds.checkBoxGrp('nwSAK_modfrzCBG',q=True,v2=True)
	# get scl
	scl = cmds.checkBoxGrp('nwSAK_modfrzCBG',q=True,v3=True)
	### check for all
	if ((trans == 1)and(rot == 1)and(scl == 1)):
		cmds.checkBox('nwSAK_modfrzAllCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modfrzAllCB',e=True,v=0)
##############################################################################	
# freeze check boxes
def nwMrFreezeMod_allBox():
	'''
	
	'''
	# get all
	all = cmds.checkBox('nwSAK_modfrzAllCB',q=True,v=True)
	### check all
	if (all == 1):
		cmds.checkBoxGrp('nwSAK_modfrzCBG',e=True,v1=1,v2=1,v3=1)
	else:
		cmds.checkBoxGrp('nwSAK_modfrzCBG',e=True,v1=0,v2=0,v3=0)
##############################################################################
# renamer pad get
def nmRenamer_get():
	'''
	
	'''
	# sel
	sel = cmds.ls(sl=True)
	temp = str(len(sel))
	# check
	if (len(sel)>0):
		# set
		cmds.intFieldGrp('nmSAK_renPadIFG',e=True,v1=len(temp))
##############################################################################
# WST check boxes
def WSTcheckboxAll():
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
	# get vis
	#vis = cmds.checkBox('nwSAK_modWorldSpaceVisCB',q=True,v=True)
	# set all translate
	if ((transX == 1)and(transY == 1)and(transZ == 1)):
		cmds.checkBox('nwSAK_modWorldSpaceTransAllCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceTransAllCB',e=True,v=0)
	# set all rotate
	if ((rotateX == 1)and(rotateY == 1)and(rotateZ == 1)):
		cmds.checkBox('nwSAK_modWorldSpaceRotateAllCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceRotateAllCB',e=True,v=0)
	# set all scale
	if ((scaleX == 1)and(scaleY == 1)and(scaleZ == 1)):
		cmds.checkBox('nwSAK_modWorldSpaceScaleAllCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceScaleAllCB',e=True,v=0)
def WSTcheckboxAni():
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
	# get vis
	#vis = cmds.checkBox('nwSAK_modWorldSpaceAniVisCB',q=True,v=True)
	# set all translate
	if ((transX == 1)and(transY == 1)and(transZ == 1)):
		cmds.checkBox('nwSAK_modWorldSpaceAniTransAllCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceAniTransAllCB',e=True,v=0)
	# set all rotate
	if ((rotateX == 1)and(rotateY == 1)and(rotateZ == 1)):
		cmds.checkBox('nwSAK_modWorldSpaceAniRotateAllCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceAniRotateAllCB',e=True,v=0)
	# set all scale
	if ((scaleX == 1)and(scaleY == 1)and(scaleZ == 1)):
		cmds.checkBox('nwSAK_modWorldSpaceAniScaleAllCB',e=True,v=1)
	else:
		cmds.checkBox('nwSAK_modWorldSpaceAniScaleAllCB',e=True,v=0)

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################

##############################################################################
# create windows GUI function
def nmSAK_gui():
	'''
	
	'''
	# create call for GUI
	winGUI = 'nm_swissArmyKnife'
	### check to see if the window exists, delete and create new at same position
	if cmds.window(winGUI, exists=True):
		# get position
		pos = cmds.window(winGUI,q=True,tlc=True)
		# get tab
		mainTabSel = cmds.tabLayout('nmSAK_mainTab',q=True,st=True)
		rigTabSel = cmds.tabLayout('nmSAK_mainRigTab',q=True,st=True)
		# delete window
		cmds.deleteUI(winGUI)
		# create window with position
		cmds.window(winGUI, t='ghOst_SwissArmyKnife  v 0.7',tlb=True,mb=True, 
			s=True,rtf=True,tlc=pos)
	else:
		# create window
		cmds.window(winGUI, t='ghOst_nmSwissArmyKnife  v 0.7',tlb=True,mb=True, 
			s=True,rtf=True)
		# get tab
		mainTabSel = 'nmSAK_gen'
		rigTabSel = 'nmSAK_rigControls'
	# create the menu bar
#	cmds.menuBarLayout()
#	cmds.menu(l='Interface')
#	cmds.menu(l='Scripts')
#	cmds.menu(l='Windows')
#	cmds.menu(l='Help')
	
	
	
	# main gui
	cmds.rowColumnLayout('nmSAK_mainGUIRC',nc=2,cw=[(1,348),(2,140)])
	cmds.columnLayout('nmSAK_mainGUICol',p='nmSAK_mainGUIRC')
	cmds.columnLayout('nmSAK_mainSideCol',p='nmSAK_mainGUIRC')
	# create side show
	cmds.text(l='',h=21)
	cmds.frameLayout(lv=False,p='nmSAK_mainSideCol',mh=2,mw=2,li=2)
	cmds.columnLayout()
	# isolate select
	cmds.checkBox('nmSAK_mainIsolateCB',l='Isolate Selected',cc=Callback(nmObjShow_func.nmShow_isolate))
	cmds.button(l='Add Selected',w=124,h=22,c=Callback(nmObjShow_func.nmShow_add))
	cmds.button(l='Remove Selected',w=124,h=22,c=Callback(nmObjShow_func.nmShow_remove))
	cmds.text(l='',h=2)
	# separator
	cmds.separator(w=124)
	cmds.text(l='',h=2)
	# rot axis show
	cmds.button(l='Local Rotation Axis',w=124,h=22,c=Callback(nmObjShow_func.nmShow_rotationAxis))
	cmds.text(l='',h=2)
	# separator
	cmds.separator(w=124)
	cmds.text(l='',h=2)
	# check options
	cmds.checkBox('nmSAK_alo',l='All',cc=Callback(nmObjShow_func.nmShow_showAll))
	# object types
	cmds.checkBox('nmSAK_nc',l='NURBS Curves',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_nc'))
	cmds.checkBox('nmSAK_ns',l='NURBS Surfaces',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_ns'))
	cmds.checkBox('nmSAK_pm',l='Polygons',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_pm'))
	cmds.checkBox('nmSAK_sds',l='Subdiv Surfaces',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_sds'))
	cmds.checkBox('nmSAK_pl',l='Planes',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_pl'))
	cmds.checkBox('nmSAK_lt',l='Lights',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_lt'))
	cmds.checkBox('nmSAK_ca',l='Cameras',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_ca'))
	cmds.checkBox('nmSAK_j',l='Joints',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_j'))
	cmds.checkBox('nmSAK_ikh',l='IK Handles',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_ikh'))
	cmds.checkBox('nmSAK_df',l='Deformers',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_df'))
	cmds.checkBox('nmSAK_dy',l='Dynamics',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_dy'))
	cmds.checkBox('nmSAK_fl',l='Fluids',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_fl'))
	cmds.checkBox('nmSAK_hs',l='Hair Systems',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_hs'))
	cmds.checkBox('nmSAK_fo',l='Follicles',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_fo'))
	cmds.checkBox('nmSAK_ncl',l='nCloths',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_ncl'))
	cmds.checkBox('nmSAK_npa',l='nParticles',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_npa'))
	cmds.checkBox('nmSAK_nr',l='nRigids',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_nr'))
	cmds.checkBox('nmSAK_dc',l='Dynamic Constraints',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_dc'))
	cmds.checkBox('nmSAK_lc',l='Locators',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_lc'))
	cmds.checkBox('nmSAK_dim',l='Dimensions',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_dim'))
	cmds.checkBox('nmSAK_pv',l='Pivots',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_pv'))
	cmds.checkBox('nmSAK_ha',l='Handles',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_ha'))
	cmds.checkBox('nmSAK_tx',l='Textures',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_tx'))
	cmds.checkBox('nmSAK_str',l='Strokes',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_str'))
	cmds.checkBox('nmSAK_m',l='Manipulators',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_m'))
	# separator
	cmds.separator(w=124)
	# gui hud
	cmds.checkBox('nmSAK_cv',l='NURBS CVs',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_cv'))
	cmds.checkBox('nmSAK_hu',l='NURBS Hulls',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_hu'))
	cmds.checkBox('nmSAK_gr',l='Grid',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_gr'))
	cmds.checkBox('nmSAK_hud',l='HUD',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_hud'))
	cmds.checkBox('nmSAK_sel',l='Selection Highlighting',cc=Callback(nmObjShow_func.nmShow_showHide,'nmSAK_sel'))
	# create print line
	cmds.textField('nmSAK_mainPrintTFG',h=25,w=488,ed=False,bgc=(0,0,0),p='nmSAK_mainGUIRC')
	# create main tab
	cmds.tabLayout('nmSAK_mainTab',p='nmSAK_mainGUICol')
	# create rigging col
	cmds.columnLayout('nmSAK_gen',p='nmSAK_mainTab')
	# create modeling col
	cmds.columnLayout('nwSAK_mod',p='nmSAK_mainTab')
	# create rigging col
	cmds.columnLayout('nmSAK_rig',p='nmSAK_mainTab')
	# create animation col
	cmds.columnLayout('nmSAK_ani',p='nmSAK_mainTab')
	# create dynamic col
	cmds.columnLayout('nmSAK_dyn',p='nmSAK_mainTab')
	# create scene cleaner col
	cmds.columnLayout('nwSAK_cln',p='nmSAK_mainTab')
	# edit names
	cmds.tabLayout('nmSAK_mainTab',e=True,tl=[('nmSAK_gen','GEN'),('nwSAK_mod','MOD'),('nmSAK_rig','RIG'),('nmSAK_ani','ANI'),('nmSAK_dyn','DYN'),('nwSAK_cln', 'CLEAN')])
	# sel last tab
	cmds.tabLayout('nmSAK_mainTab',e=True,st=mainTabSel)
	##############################################################################
	# GENERAL TAB 
	##############################################################################
	# general section frame
	cmds.columnLayout('nmSAK_mainGenCol',p='nmSAK_gen')
	##############################################################################
	# hist,center, mover
	cmds.rowColumnLayout('nmSAK_genMainRC',nc=2,cw=[(1,166),(2,166)],cs=(2,2),p='nmSAK_mainGenCol')
	cmds.columnLayout('nmSAK_genLeftCol',p='nmSAK_genMainRC')
	cmds.columnLayout('nmSAK_genRightCol',p='nmSAK_genMainRC')
	##############################################################################
	# create manipulator
	cmds.frameLayout(l='Manipulator:',mh=2,mw=2,li=2,p='nmSAK_genLeftCol')
	cmds.columnLayout('nmSAK_manipCol')
	# center
	cmds.rowColumnLayout(nc=3,cw=[(1,52),(2,51),(3,52)])
	cmds.button(h=25,l='Object',c=Callback(nmGeneralTab_func.nmManipulator_object))
	cmds.button(h=25,l='Local',c=Callback(nmGeneralTab_func.nmManipulator_local))
	cmds.button(h=25,l='World',c=Callback(nmGeneralTab_func.nmManipulator_world))
	##############################################################################
	# create grouper
	cmds.frameLayout(l='Grouper:',mh=2,mw=2,li=2,p='nmSAK_genLeftCol')
	cmds.columnLayout('nmSAK_grpCol')
	# check box for origin
	cmds.radioButtonGrp('nmSAK_grpRBG',cw2=(78,77),nrb=2,la2=('Object','Origin'),sl=1)
	cmds.text(l='',h=3)
	# create buttons
	cmds.rowColumnLayout(nc=2,cw=[(1,78),(2,77)])
	cmds.button(l='Group',h=25,c=Callback(nmGeneralTab_func.nmGrouper_group))
	cmds.button(l='Ungroup',h=25,c=Callback(nmGeneralTab_func.nmGrouper_ungroup))
	##############################################################################
	# create history
	cmds.frameLayout(l='History:',mh=2,mw=2,li=2,p='nmSAK_genRightCol')
	cmds.columnLayout('nmSAK_hisCol')
	# create offset check box
	cmds.checkBox('nmSAK_hisCHBX',l='Non-Deformer')
	# create buttons
	cmds.rowColumnLayout(nc=1,cw=(1,155))
	cmds.button(l='Delete History',h=25,c=Callback(nmGeneralTab_func.nmHistory_delete))
	##############################################################################
	# create center
	cmds.frameLayout(l='Center:',mh=2,mw=2,li=2,p='nmSAK_genRightCol')
	cmds.columnLayout('nmSAK_cenCol')
	# center
	cmds.rowColumnLayout(nc=1,cw=(1,155))
	cmds.button(h=25,l='Center Pivot',c=Callback(nmGeneralTab_func.nmCenter_center))
	##############################################################################
	# create matchMaker
	cmds.frameLayout(l='Match Maker:',mh=2,mw=2,li=2,p='nmSAK_genLeftCol')
	cmds.columnLayout('nmSAK_matMakCol')
	# type
	cmds.radioButtonGrp('nmSAK_movTypeRBG',nrb=2,la2=('Transform','Pivot'),cw2=(78,77),sl=1)
	# sep
	cmds.text(l='',h=5)
	cmds.separator(w=156)
	cmds.text(l='',h=5)
	# col
	cmds.rowColumnLayout(nc=2,cw=[(1,78),(2,77)],p='nmSAK_matMakCol')
	# average
	cmds.checkBox('nmSAK_movAvgCHBX',l='Average',cc=Callback(nmMatchMaker_average))
	cmds.checkBox('nmSAK_movOrdCHBX',l='Order',cc=Callback(nmMatchMaker_order))
	cmds.text(l='',h=3)
	# create buttons
	cmds.rowColumnLayout(nc=2,cw=[(1,78),(2,77)],p='nmSAK_matMakCol')
	cmds.button(l='A to B',h=25,c=Callback(nmGeneralTab_func.nmMatchMaker_ab))
	cmds.button(l='B to A',h=25,c=Callback(nmGeneralTab_func.nmMatchMaker_ba))
	##############################################################################
	# create freeze
	cmds.frameLayout(l='Mr. Freeze:',mh=2,mw=2,li=2,p='nmSAK_genRightCol')
	cmds.columnLayout('nmSAK_frzCol')
	# create all
	cmds.checkBox('nmSAK_frzAllCB',l='All',v=1,cc=Callback(nmMrFreeze_allBox))
	# create tran rot scl
	cmds.checkBoxGrp('nmSAK_frzCBG',ncb=3,cw3=(57,50,48),la3=['Trans','Rot','Scl'],v1=1,v2=1,v3=1,cc=Callback(nmMrFreeze_box))
	# freeze
	cmds.rowColumnLayout(nc=1,cw=(1,155))
	cmds.button(h=25,l='Freeze Selected',c=Callback(nmGeneralTab_func.nmMrFreeze_freeze))
	cmds.button(h=25,l='Zero Selected',c=Callback(nmGeneralTab_func.nmMrFreeze_zero))
	##############################################################################
	# create renamer
	# new col
	cmds.columnLayout('nmSAK_newGenCol',p='nmSAK_mainGenCol',co=('left',1))
	# create renaming section
	cmds.frameLayout(l='Renamer:',mh=2,mw=2,li=2,p='nmSAK_newGenCol')
	cmds.columnLayout('nmSAK_renameCol')
	cmds.rowColumnLayout('nmSAK_renameRC',nc=2,cw=[(1,207),(2,110)],co=(2,'left',5))
	cmds.columnLayout(p='nmSAK_renameRC')
	# search and replace
	cmds.textFieldGrp('nmSAK_renSearchTFG',l='Search:',cw2=(45,158))
	cmds.textFieldGrp('nmSAK_renReplaceTFG',l='Replace:',cw2=(45,158))
	cmds.columnLayout(p='nmSAK_renameRC')
	cmds.button(l='Search \nand Replace',h=44,w=109,c=Callback(nmGeneralTab_func.nmRenamer_searchReplace))
	cmds.text(l='',p='nmSAK_renameCol',h=2)
	cmds.separator(w=325,p='nmSAK_renameCol')
	cmds.text(l='',p='nmSAK_renameCol',h=2)
	# prefix
	cmds.rowColumnLayout(nc=2,cw=[(1,207),(2,110)],co=(2,'left',5),p='nmSAK_renameCol')
	cmds.textFieldGrp('nmSAK_renPrefixTFG',l='Prefix:',cw2=(45,158))
	cmds.button(h=25,l='Add Prefix',c=Callback(nmGeneralTab_func.nmRenamer_prefix))
	cmds.text(l='',p='nmSAK_renameCol',h=2)
	cmds.separator(w=325,p='nmSAK_renameCol')
	cmds.text(l='',p='nmSAK_renameCol',h=2)
	# suffix
	cmds.rowColumnLayout(nc=2,cw=[(1,207),(2,110)],co=(2,'left',5),p='nmSAK_renameCol')
	cmds.textFieldGrp('nmSAK_renSuffixTFG',l='Suffix:',cw2=(45,158))
	cmds.button(h=25,l='Add Suffix',c=Callback(nmGeneralTab_func.nmRenamer_suffix))
	cmds.text(l='',p='nmSAK_renameCol',h=2)
	cmds.separator(w=325,p='nmSAK_renameCol')
	cmds.text(l='',p='nmSAK_renameCol',h=2)
	# rename
	cmds.rowColumnLayout('nmSAK_renNameRC',nc=2,cw=[(1,207),(2,110)],co=(2,'left',5),p='nmSAK_renameCol')
	cmds.columnLayout(p='nmSAK_renNameRC')
	cmds.textFieldGrp('nmSAK_renNameTFG',l='Rename:',cw2=(45,158))
	cmds.rowColumnLayout(nc=2,cw=[(1,134),(2,50)])
	cmds.intFieldGrp('nmSAK_renStartIFG',l='Start #:',cw2=(45,80),v1=1)
	cmds.text(l='')
	cmds.intFieldGrp('nmSAK_renPadIFG',l='Padding:',cw2=(45,80),v1=0)
	cmds.button(l='Get',c=Callback(nmRenamer_get))
	cmds.columnLayout(p='nmSAK_renNameRC')
	cmds.button(l='Rename',h=68,w=109,c=Callback(nmGeneralTab_func.nmRenamer_rename))
	##############################################################################
	# create outer space
	cmds.text(l='',h=3,p='nmSAK_newGenCol')
	cmds.frameLayout(l='Outer Space:',mh=2,mw=2,li=2,p='nmSAK_newGenCol')
	cmds.columnLayout('nmSAK_genNamSpcCol')
	# create spaces
	cmds.text(h=2,l='',p='nmSAK_genNamSpcCol')
	cmds.rowColumnLayout(nc=2,cw=[(1,223),(2,100)],p='nmSAK_genNamSpcCol')
	cmds.textFieldGrp('nmSAK_genNameSpcTFG',l='Namespace:  ',cw2=(72,148))
	cmds.button(l='Create',h=25,c=Callback(nmGeneralTab_func.nmOuterSpace_create))
	# remove
	cmds.text(h=2,l='',p='nmSAK_genNamSpcCol')
	cmds.separator(w=325,p='nmSAK_genNamSpcCol')
	cmds.text(h=2,l='',p='nmSAK_genNamSpcCol')
	# create name space
	cmds.rowColumnLayout(nc=2,cw=[(1,241),(2,77)],co=(2,'left',5),p='nmSAK_genNamSpcCol')
	cmds.optionMenuGrp('nmSAK_namespaceOMG',l='Scene Namespaces:  ',cw2=(112,100))
	cmds.menuItem(l='           Default           ')
	cmds.button(h=25,l='Refresh',c=Callback(nmGeneralTab_func.nmOuterSpace_refresh))
	cmds.text(l='',h=3)
	cmds.button(h=25,l='Set Selected',p='nmSAK_genNamSpcCol',w=324,c=Callback(nmGeneralTab_func.nmOuterSpace_setSel))
	cmds.text(h=2,l='',p='nmSAK_genNamSpcCol')
	cmds.separator(w=325,p='nmSAK_genNamSpcCol')
	cmds.text(h=2,l='',p='nmSAK_genNamSpcCol')
	cmds.button(h=25,l='Kill Namespace',p='nmSAK_genNamSpcCol',w=324,c=Callback(nmGeneralTab_func.nmOuterSpace_remove))
	##############################################################################
	# MODELING TAB 
	##############################################################################
	# modeling section frame
	cmds.columnLayout('nwSAK_mainModCol',p='nwSAK_mod')
	#########################
	# hist,center, mover
	cmds.rowColumnLayout('nwSAK_modMainRC',nc=2,cw=[(1,166),(2,166)],cs=(2,2),p='nwSAK_mainModCol')
	cmds.columnLayout('nwSAK_modLeftCol',p='nwSAK_modMainRC')
	cmds.columnLayout('nwSAK_modRightCol',p='nwSAK_modMainRC')
	#########################
	# create manipulator
	cmds.frameLayout(l='Manipulator:',mh=2,mw=2,li=2,p='nwSAK_modLeftCol')
	cmds.columnLayout('nwSAK_modmanipCol')
	# center
	cmds.rowColumnLayout(nc=3,cw=[(1,52),(2,51),(3,52)])
	cmds.button(h=25,l='Object',c=Callback(nmGeneralTab_func.nmManipulator_object))
	cmds.button(h=25,l='Local',c=Callback(nmGeneralTab_func.nmManipulator_local))
	cmds.button(h=25,l='World',c=Callback(nmGeneralTab_func.nmManipulator_world))
	########################
	# create grouper
	cmds.frameLayout(l='Grouper:',mh=2,mw=2,li=2,p='nwSAK_modLeftCol')
	cmds.columnLayout('nwSAK_modgrpCol')
	# check box for origin
	cmds.radioButtonGrp('nwSAK_modgrpRBG',cw2=(78,77),nrb=2,la2=('Object','Origin'),sl=1)
	cmds.text(l='',h=3)
	# create buttons
	cmds.rowColumnLayout(nc=2,cw=[(1,78),(2,77)])
	cmds.button(l='Group',h=25,c=Callback(nmGeneralTab_func.nmGrouper_group))
	cmds.button(l='Ungroup',h=25,c=Callback(nmGeneralTab_func.nmGrouper_ungroup))
	#########################
	# create history
	cmds.frameLayout(l='History:',mh=2,mw=2,li=2,p='nwSAK_modRightCol')
	cmds.columnLayout('nwSAK_modhisCol')
	# create offset check box
	cmds.checkBox('nwSAK_modhisCHBX',l='Non-Deformer')
	# create buttons
	cmds.rowColumnLayout(nc=1,cw=(1,155))
	cmds.button(l='Delete History',h=25,c=Callback(nmGeneralTab_func.nmHistory_delete))
	#########################
	# create center
	cmds.frameLayout(l='Center:',mh=2,mw=2,li=2,p='nwSAK_modRightCol')
	cmds.columnLayout('nwSAK_modcenCol')
	# center
	cmds.rowColumnLayout(nc=1,cw=(1,155))
	cmds.button(h=25,l='Center Pivot',c=Callback(nmGeneralTab_func.nmCenter_center))
	#########################
	# create matchMaker
	cmds.frameLayout(l='Match Maker:',mh=2,mw=2,li=2,p='nwSAK_modLeftCol')
	cmds.columnLayout('nwSAK_modmatMakCol')
	# type
	cmds.radioButtonGrp('nwSAK_modmovTypeRBG',nrb=2,la2=('Transform','Pivot'),cw2=(78,77),sl=1)
	# sep
	cmds.text(l='',h=5)
	cmds.separator(w=156)
	cmds.text(l='',h=5)
	# col
	cmds.rowColumnLayout(nc=2,cw=[(1,78),(2,77)],p='nwSAK_modmatMakCol')
	# average
	cmds.checkBox('nwSAK_modmovAvgCHBX',l='Average',cc=Callback(nmMatchMaker_average))
	cmds.checkBox('nwSAK_modmovOrdCHBX',l='Order',cc=Callback(nmMatchMaker_order))
	cmds.text(l='',h=3)
	# create buttons
	cmds.rowColumnLayout(nc=2,cw=[(1,78),(2,77)],p='nwSAK_modmatMakCol')
	cmds.button(l='A to B',h=25,c=Callback(nmGeneralTab_func.nmMatchMaker_ab))
	cmds.button(l='B to A',h=25,c=Callback(nmGeneralTab_func.nmMatchMaker_ba))
	###########################
	# create freeze
	cmds.frameLayout(l='Mr. Freeze:',mh=2,mw=2,li=2,p='nwSAK_modRightCol')
	cmds.columnLayout('nwSAK_modfrzCol')
	# create all
	cmds.checkBox('nwSAK_modfrzAllCB',l='All',v=1,cc=Callback(nwMrFreezeMod_allBox))
	# create tran rot scl
	cmds.checkBoxGrp('nwSAK_modfrzCBG',ncb=3,cw3=(57,50,48),la3=['Trans','Rot','Scl'],v1=1,v2=1,v3=1,cc=Callback(nwMrFreezeMod_box))
	# freeze
	cmds.rowColumnLayout(nc=1,cw=(1,155))
	cmds.button(h=25,l='Freeze Selected',c=Callback(nwModelingTab_func.nmMrFreeze_freeze))
	cmds.button(h=25,l='Zero Selected',c=Callback(nwModelingTab_func.nmMrFreeze_zero))

	################################
	# set pivot tool
	# set pivot
	#cmds.frameLayout(l='Set Pivot To Manipulator',mh=2,mw=2,li=2,p='nwSAK_mainModCol')
	#cmds.columnLayout('nwSAK_setPivotCol')
	# sample space
	#cmds.floatFieldGrp('nwSAK_manipPos',numberOfFields=3,l='Manipulator Position:',precision=4,cw=[(1,135),(2,50),(3,50),(4,50)],p='nwSAK_setPivotCol')
	#cmds.rowColumnLayout('nwSAK_setPivotButtons',nc=2,cw=[(1,163),(2,163)],p='nwSAK_setPivotCol')
	#cmds.button(l='Capture Pivot Position',h=25,p='nwSAK_setPivotButtons',c=Callback(nwModelingTab_func.captureManipPiv))
	#cmds.button(l='Apply to Selected',h=25,p='nwSAK_setPivotButtons',c=Callback(nwModelingTab_func.setPivotToManip))
	################################
	# world space tool
	# create world space frame
	cmds.frameLayout(l='WorldSpaceTool:',mh=2,mw=2,li=2,p='nwSAK_mainModCol')
	cmds.columnLayout('nwSAK_modWorldSpaceMainCol')
	cmds.floatFieldGrp('nwSAK_manipPivot',l='Pivots',numberOfFields=3,precision=4,cw=[(1,160),(2,50),(3,50),(4,50)],p='nwSAK_modWorldSpaceMainCol',vis=1)
	cmds.floatFieldGrp('nwSAK_transPivots',l='Translate',numberOfFields=3,precision=4,cw=[(1,160),(2,50),(3,50),(4,50)],p='nwSAK_modWorldSpaceMainCol',vis=1)
	cmds.floatFieldGrp('nwSAK_rotPivots',l='Rotate',numberOfFields=3,precision=4,cw=[(1,160),(2,50),(3,50),(4,50)],p='nwSAK_modWorldSpaceMainCol',vis=1)
	cmds.floatFieldGrp('nwSAK_scalePivots',l='Scale',numberOfFields=3,precision=4,cw=[(1,160),(2,50),(3,50),(4,50)],p='nwSAK_modWorldSpaceMainCol',vis=1)
	cmds.rowColumnLayout('nwSAK_modWorldSpaceMainRC',nc=4,cw=[(1,50),(2,50),(3,50),(4,175)],co=(4,'left',12))
	# create trans
	cmds.frameLayout(p='nwSAK_modWorldSpaceMainRC',l='Trans:',li=1,mh=2,mw=2)
	cmds.columnLayout('nwSAK_modWorldSpaceTransCol',rs=-5)
	# all
	cmds.checkBox('nwSAK_modWorldSpaceTransAllCB',l='All',cc=Callback(nwModelingTab_func.setPivotToManip_transAll))
	# create x
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceTransCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(1,0,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceTransXCB',l='X',cc=Callback(WSTcheckboxAll))
	# create y
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceTransCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,1,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceTransYCB',l='Y',cc=Callback(WSTcheckboxAll))
	# create z
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceTransCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,0,1),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceTransZCB',l='Z',cc=Callback(WSTcheckboxAll))
	# create rot
	cmds.frameLayout(p='nwSAK_modWorldSpaceMainRC',l='Rotate:',li=0,mh=2,mw=2)
	cmds.columnLayout('nwSAK_modWorldSpaceRotateCol',rs=-5)
	# all
	cmds.checkBox('nwSAK_modWorldSpaceRotateAllCB',l='All',cc=Callback(nwModelingTab_func.setPivotToManip_rotAll))
	# create x
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceRotateCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(1,0,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceRotateXCB',l='X',cc=Callback(WSTcheckboxAll))
	# create y
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceRotateCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,1,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceRotateYCB',l='Y',cc=Callback(WSTcheckboxAll))
	# create z
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceRotateCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,0,1),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceRotateZCB',l='Z',cc=Callback(WSTcheckboxAll))
	# create scl
	cmds.frameLayout(p='nwSAK_modWorldSpaceMainRC',l='Scale:',li=2,mh=2,mw=2)
	cmds.columnLayout('nwSAK_modWorldSpaceScaleCol',rs=-5)
	# all
	cmds.checkBox('nwSAK_modWorldSpaceScaleAllCB',l='All',cc=Callback(nwModelingTab_func.setPivotToManip_scaleAll))
	# create x
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceScaleCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(1,0,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceScaleXCB',l='X',cc=Callback(WSTcheckboxAll))
	# create y
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceScaleCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,1,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceScaleYCB',l='Y',cc=Callback(WSTcheckboxAll))
	# create z
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceScaleCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,0,1),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceScaleZCB',l='Z',cc=Callback(WSTcheckboxAll))
	# create vis
	#cmds.frameLayout(p='nwSAK_modWorldSpaceMainCol',lv=False,li=2,mh=2,mw=2)
	#cmds.rowColumnLayout(nc=1,cw=(1,146))
	# visibility
	#cmds.checkBox('nwSAK_modWorldSpaceVisCB',h=17,l='Visibility',cc=Callback(nwModelingTab_func.setPivotToManip_apply))
	# capture transforms
	cmds.columnLayout(p='nwSAK_modWorldSpaceMainRC')
	cmds.button(h=25,w=154,l='Capture',c=Callback(nwModelingTab_func.captureManipPiv))
	# select mode
	cmds.radioButtonGrp('nwSAK_modmovTypeSelect',nrb=2,la2=('Transform','Pivot'),cw2=(90,77),h=25,sl=1)
	# apply transforms
	cmds.button(h=24,w=154,l='Apply',c=Callback(nwModelingTab_func.setPivotToManip_apply))
	# average transforms
	cmds.button(h=24,w=154,l='Average')
	########################
	# UV hooker
	# uv transfer
	cmds.frameLayout(l='UV Hooker: Not Running',mh=2,mw=2,li=2,p='nwSAK_mainModCol')
	cmds.columnLayout('nwSAK_modUVTransCol')
	# sample space
	cmds.radioButtonGrp('nwSAK_modUVTransRBG',l='Sample Space: ',nrb=4,la4=('Component','World','Local','UV'),cw5=(82,82,57,53,53),sl=1)
	cmds.rowColumnLayout(nc=2,cw=[(1,163),(2,163)])
	cmds.button(l='Transfer A to B',h=25)
	cmds.button(l='Transfer B to A',h=25)

	##############################################################################
	# RIGGING TAB 
	##############################################################################
	# main rig tabs
	cmds.tabLayout('nmSAK_mainRigTab',p='nmSAK_rig')
	# tabs
	cmds.columnLayout('nmSAK_rigControls',p='nmSAK_mainRigTab')
	cmds.columnLayout('nwSAK_rigAttributes',p='nmSAK_mainRigTab')
	cmds.columnLayout('nmSAK_rigJoints',p='nmSAK_mainRigTab')
	cmds.columnLayout('nmSAK_rigSkinning',p='nmSAK_mainRigTab')
	cmds.columnLayout('nmSAK_rigAuto',p='nmSAK_mainRigTab')
	# edit tab labels
	cmds.tabLayout('nmSAK_mainRigTab',e=True,tl=[('nmSAK_rigControls','Controls'),('nwSAK_rigAttributes','Attributes'),('nmSAK_rigJoints','Joints'),('nmSAK_rigSkinning','Skinning'),('nmSAK_rigAuto','Auto')])
	# edit tab selection
	cmds.tabLayout('nmSAK_mainRigTab',e=True,st=rigTabSel)
	# control column setup
	cmds.rowColumnLayout('nmSAK_rigControlMainRC',nc=2,cw=[(1,163),(2,163)],cs=(2,2),p='nmSAK_rigControls')
	cmds.columnLayout('nmSAK_rigControlLeftCol',p='nmSAK_rigControlMainRC')
	cmds.columnLayout('nmSAK_rigControlRightCol',p='nmSAK_rigControlMainRC')
	# attribute column setup
	cmds.rowColumnLayout('nmSAK_rigAttMainRC',nc=1,cw=(1,328),p='nwSAK_rigAttributes')
	cmds.columnLayout('nwSAK_rigAttCol',p='nwSAK_rigAttributes')
	# joint column setup
	cmds.rowColumnLayout('nmSAK_rigJointsMainRC',nc=2,cw=[(1,163),(2,163)],cs=(2,2),p='nmSAK_rigJoints')
	cmds.columnLayout('nmSAK_rigJointsLeftCol',p='nmSAK_rigJointsMainRC')
	cmds.columnLayout('nmSAK_rigJointsRightCol',p='nmSAK_rigJointsMainRC')
	# skinning column setup
	cmds.rowColumnLayout('nmSAK_rigSkinningMainRC',nc=1,cw=(1,328),p='nmSAK_rigSkinning')
	cmds.columnLayout('nmSAK_rigSkinningMainCol',p='nmSAK_rigSkinningMainRC')
	
	##############################################################################
	## controls tab ##
	# create constraints
	cmds.frameLayout(l='Constraints:',mh=2,mw=2,li=2,p='nmSAK_rigControlLeftCol')
	cmds.columnLayout('nmSAK_rigConstrolMainCol')
	# create offset check box
	cmds.checkBox('nmSAK_rigConOffSetCB',l='Maintain Offset',v=1,h=26)
	# create buttons
	cmds.rowColumnLayout(p='nmSAK_rigConstrolMainCol',nc=3,cw=[(1,51),(2,51),(3,50)])
	cmds.button(l='Point',h=25,c=Callback(nmRiggingTab_func.nmConstraints_point))
	cmds.button(l='Orient',h=25,c=Callback(nmRiggingTab_func.nmConstraints_orient))
	cmds.button(l='Scale',h=25,c=Callback(nmRiggingTab_func.nmConstraints_scale))
	cmds.rowColumnLayout(p='nmSAK_rigConstrolMainCol',nc=2,cw=[(1,76),(2,76)])
	cmds.button(l='Parent',h=25,c=Callback(nmRiggingTab_func.nmConstraints_parent))
	cmds.button(l='Pole Vector',h=25,c=Callback(nmRiggingTab_func.nmConstraints_poleVector))
	# aim constraint
	cmds.button(h=25,w=154,l='Aim Options',p='nmSAK_rigConstrolMainCol',c=Callback(nmRiggingTab_func.nmConstraints_aimOptions))
	# spacer
	cmds.text(h=2,l='',p='nmSAK_rigConstrolMainCol')
	# create divider
	cmds.separator(p='nmSAK_rigConstrolMainCol',w=154)
	# spacer
	cmds.text(h=2,l='',p='nmSAK_rigConstrolMainCol')
	# create delete button
	cmds.button(l='Delete Constraint',p='nmSAK_rigConstrolMainCol',w=154,h=25,c=Callback(nmRiggingTab_func.nmConstraints_deleteConstraints))
	##############################################################################
	# create curve section
	cmds.frameLayout(l='Curves:',mh=2,mw=2,li=2,p='nmSAK_rigControlLeftCol')
	cmds.columnLayout()
	# create button
	cmds.button(w=154,h=25,l='Curve Tool',c=Callback(nmRiggingTab_func.nmCurves_curveTool))
	cmds.button(w=154,h=25,l='Combine Curves',c=Callback(nmRiggingTab_func.nmCurves_combine))
	cmds.button(w=154,h=25,l='Rebuild Options',c=Callback(nmRiggingTab_func.nmCurves_rebuildOptions))
	##############################################################################
	# create text section
	cmds.frameLayout(l='Text Me:',mh=2,mw=2,li=2,p='nmSAK_rigControlLeftCol')
	cmds.columnLayout('nmSAK_rigTextMeMainCol')
	cmds.rowColumnLayout(nc=1,cw=(1,152))
	cmds.textFieldGrp('nmSAK_rigTextCurvesTFG',l='Text: ',cw2=(31,120))
	cmds.text(h=2,l='')
	# spacer
	cmds.button(l='Create Text Curves',h=25,w=154,p='nmSAK_rigTextMeMainCol',c=Callback(nmRiggingTab_func.nmTextMe_create))
	# spacer
	cmds.text(h=2,l='',p='nmSAK_rigTextMeMainCol')
	# create divider
	cmds.separator(w=154,p='nmSAK_rigTextMeMainCol')
	# spacer
	cmds.text(h=2,l='',p='nmSAK_rigTextMeMainCol')
	cmds.button(l='Text Options',h=25,w=154,p='nmSAK_rigTextMeMainCol',c=Callback(nmRiggingTab_func.nmTextMe_textOptions))
	##############################################################################
	# easy cluster
	cmds.frameLayout(l='Easy Cluster:',mh=2,mw=2,li=2,p='nmSAK_rigControlLeftCol')
	cmds.columnLayout()
	# options
	cmds.radioButtonGrp('nmSAK_rigClusterOptionsRBG',h=27,nrb=2,la2=('Single','Multiple'),cw2=(68,76),sl=True)
	# create buttons
	cmds.button(w=154,h=25,l='Cluster',c=Callback(nmRiggingTab_func.nmEasyCluster_cluster))
	# spacer
	cmds.text(h=2,l='')
	# create divider
	cmds.separator(w=154)
	# spacer
	cmds.text(h=2,l='')
	cmds.button(w=154,h=25,l='Cluster Curve',c=Callback(nmRiggingTab_func.nmEasyCluster_clusterCurve))
	##############################################################################
	# pin up section
	cmds.frameLayout(l='Pin Up:',mh=2,mw=2,li=2,p='nmSAK_rigControlLeftCol')
	cmds.columnLayout('nmSAK_rigPinMeMainCol')
	cmds.rowColumnLayout(nc=2,cw=[(1,132),(2,20)])
	cmds.textFieldGrp('nmSAK_rigPinMeshTFG',l='Mesh: ',ed=False,cw2=(34,95))
	cmds.button(l='<',h=25,c=Callback(nmRiggingTab_func.nmPinUp_loadMesh))
	cmds.text(h=2,l='')
	cmds.button(w=154,h=25,l='Create Follicle',p='nmSAK_rigPinMeMainCol',c=Callback(nmRiggingTab_func.nmPinUp_follicle))
	# create follicle
	cmds.button(w=154,h=25,l='Pin Control',p='nmSAK_rigPinMeMainCol',c=Callback(nmRiggingTab_func.nmPinUp_pin))
	##############################################################################
	# create lock and hide
	cmds.frameLayout(l='Lock and Hide:',mh=2,mw=2,li=2,p='nmSAK_rigControlRightCol')
	cmds.columnLayout('nmSAK_rigLockHideMainCol')
	cmds.rowColumnLayout('nmSAK_rigLockHideMainRC',nc=3,cw=[(1,50),(2,52),(3,50)])
	# create trans
	cmds.frameLayout(p='nmSAK_rigLockHideMainRC',l='Trans:',li=1,mh=2,mw=2)
	cmds.columnLayout('nmSAK_rigLockHideTransCol',rs=-5)
	# all
	cmds.checkBox('nmSAK_rigLockHideTransAllCB',l='All',cc=Callback(nmRiggingTab_func.nmLockHide_transAll))
	# create x
	cmds.rowColumnLayout(p='nmSAK_rigLockHideTransCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(1,0,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nmSAK_rigLockHideTransXCB',l='X',cc=Callback(nmRiggingTab_func.nmLockHide_lockHide))
	# create y
	cmds.rowColumnLayout(p='nmSAK_rigLockHideTransCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,1,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nmSAK_rigLockHideTransYCB',l='Y',cc=Callback(nmRiggingTab_func.nmLockHide_lockHide))
	# create z
	cmds.rowColumnLayout(p='nmSAK_rigLockHideTransCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,0,1),h=15)
	cmds.text(l='')
	cmds.checkBox('nmSAK_rigLockHideTransZCB',l='Z',cc=Callback(nmRiggingTab_func.nmLockHide_lockHide))
	# create rot
	cmds.frameLayout(p='nmSAK_rigLockHideMainRC',l='Rotate:',li=0,mh=2,mw=2)
	cmds.columnLayout('nmSAK_rigLockHideRotateCol',rs=-5)
	# all
	cmds.checkBox('nmSAK_rigLockHideRotateAllCB',l='All',cc=Callback(nmRiggingTab_func.nmLockHide_rotAll))
	# create x
	cmds.rowColumnLayout(p='nmSAK_rigLockHideRotateCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(1,0,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nmSAK_rigLockHideRotateXCB',l='X',cc=Callback(nmRiggingTab_func.nmLockHide_lockHide))
	# create y
	cmds.rowColumnLayout(p='nmSAK_rigLockHideRotateCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,1,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nmSAK_rigLockHideRotateYCB',l='Y',cc=Callback(nmRiggingTab_func.nmLockHide_lockHide))
	# create z
	cmds.rowColumnLayout(p='nmSAK_rigLockHideRotateCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,0,1),h=15)
	cmds.text(l='')
	cmds.checkBox('nmSAK_rigLockHideRotateZCB',l='Z',cc=Callback(nmRiggingTab_func.nmLockHide_lockHide))
	# create scl
	cmds.frameLayout(p='nmSAK_rigLockHideMainRC',l='Scale:',li=2,mh=2,mw=2)
	cmds.columnLayout('nmSAK_rigLockHideScaleCol',rs=-5)
	# all
	cmds.checkBox('nmSAK_rigLockHideScaleAllCB',l='All',cc=Callback(nmRiggingTab_func.nmLockHide_scaleAll))
	# create x
	cmds.rowColumnLayout(p='nmSAK_rigLockHideScaleCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(1,0,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nmSAK_rigLockHideScaleXCB',l='X',cc=Callback(nmRiggingTab_func.nmLockHide_lockHide))
	# create y
	cmds.rowColumnLayout(p='nmSAK_rigLockHideScaleCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,1,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nmSAK_rigLockHideScaleYCB',l='Y',cc=Callback(nmRiggingTab_func.nmLockHide_lockHide))
	# create z
	cmds.rowColumnLayout(p='nmSAK_rigLockHideScaleCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,0,1),h=15)
	cmds.text(l='')
	cmds.checkBox('nmSAK_rigLockHideScaleZCB',l='Z',cc=Callback(nmRiggingTab_func.nmLockHide_lockHide))
	# create vis
	cmds.frameLayout(p='nmSAK_rigLockHideMainCol',lv=False,li=2,mh=2,mw=2)
	cmds.rowColumnLayout(nc=1,cw=(1,146))
	# visibility
	cmds.checkBox('nmSAK_rigLockHideVisCB',h=17,l='Visibility',cc=Callback(nmRiggingTab_func.nmLockHide_lockHide))
	# lock and hide
	cmds.button(h=25,w=154,l='Set Selected',p='nmSAK_rigLockHideMainCol',c=Callback(nmRiggingTab_func.nmLockHide_lockHide))
	# select locked nodes
	cmds.button(h=24,w=154,l='toggle lockNode',p='nmSAK_rigLockHideMainCol',c=Callback(nmRiggingTab_func.nwToggleLockNode))
	##############################################################################
	# create control color
	cmds.frameLayout(l='Control Color:',mh=2,mw=2,li=2,p='nmSAK_rigControlRightCol')
	cmds.columnLayout()
	# create buttons
	cmds.rowColumnLayout('nmSAK_rigControlColorRC',nc=8,cw=[(1,19),(2,19),(3,19),(4,19),(5,19),(6,19),(7,19),(8,19)])
	cmds.canvas(h=20,bgc=(0.627,0.627,0.627),pc=Callback(nmRiggingTab_func.nmControlColor_color,0))
	cmds.canvas(h=20,bgc=(0,0,0),pc=Callback(nmRiggingTab_func.nmControlColor_color,1))
	cmds.canvas(h=20,bgc=(0.247,0.247,0.247),pc=Callback(nmRiggingTab_func.nmControlColor_color,2))
	cmds.canvas(h=20,bgc=(0.498,0.498,0.498),pc=Callback(nmRiggingTab_func.nmControlColor_color,3))
	cmds.canvas(h=20,bgc=(0.608,0,0.157),pc=Callback(nmRiggingTab_func.nmControlColor_color,4))
	cmds.canvas(h=20,bgc=(0,0.016,0.373),pc=Callback(nmRiggingTab_func.nmControlColor_color,5))
	cmds.canvas(h=20,bgc=(0,0,1),pc=Callback(nmRiggingTab_func.nmControlColor_color,6))
	cmds.canvas(h=20,bgc=(0,0.275,0.094),pc=Callback(nmRiggingTab_func.nmControlColor_color,7))
	cmds.canvas(h=20,bgc=(0.145,0,0.263),pc=Callback(nmRiggingTab_func.nmControlColor_color,8))
	cmds.canvas(h=20,bgc=(0.78,0,0.78),pc=Callback(nmRiggingTab_func.nmControlColor_color,9))
	cmds.canvas(h=20,bgc=(0.537,0.278,0.2),pc=Callback(nmRiggingTab_func.nmControlColor_color,10))
	cmds.canvas(h=20,bgc=(0.243,0.133,0.122),pc=Callback(nmRiggingTab_func.nmControlColor_color,11))
	cmds.canvas(h=20,bgc=(0.6,0.145,0),pc=Callback(nmRiggingTab_func.nmControlColor_color,12))
	cmds.canvas(h=20,bgc=(1,0,0),pc=Callback(nmRiggingTab_func.nmControlColor_color,13))
	cmds.canvas(h=20,bgc=(0,1,0),pc=Callback(nmRiggingTab_func.nmControlColor_color,14))
	cmds.canvas(h=20,bgc=(0,0.255,0.6),pc=Callback(nmRiggingTab_func.nmControlColor_color,15))
	cmds.canvas(h=20,bgc=(1,1,1),pc=Callback(nmRiggingTab_func.nmControlColor_color,16))
	cmds.canvas(h=20,bgc=(1,1,0),pc=Callback(nmRiggingTab_func.nmControlColor_color,17))
	cmds.canvas(h=20,bgc=(0.388,0.863,1),pc=Callback(nmRiggingTab_func.nmControlColor_color,18))
	cmds.canvas(h=20,bgc=(0.263,1,0.635),pc=Callback(nmRiggingTab_func.nmControlColor_color,19))
	cmds.canvas(h=20,bgc=(1,0.686,0.686),pc=Callback(nmRiggingTab_func.nmControlColor_color,20))
	cmds.canvas(h=20,bgc=(0.98,0.675,0.475),pc=Callback(nmRiggingTab_func.nmControlColor_color,21))
	cmds.canvas(h=20,bgc=(1,1,0.384),pc=Callback(nmRiggingTab_func.nmControlColor_color,22))
	cmds.canvas(h=20,bgc=(0,0.6,0.325),pc=Callback(nmRiggingTab_func.nmControlColor_color,23))
	cmds.canvas(h=20,bgc=(0.627,0.412,0.188),pc=Callback(nmRiggingTab_func.nmControlColor_color,24))
	cmds.canvas(h=20,bgc=(0.62,0.627,0.188),pc=Callback(nmRiggingTab_func.nmControlColor_color,25))
	cmds.canvas(h=20,bgc=(0.408,0.627,0.188),pc=Callback(nmRiggingTab_func.nmControlColor_color,26))
	cmds.canvas(h=20,bgc=(0.188,0.627,0.365),pc=Callback(nmRiggingTab_func.nmControlColor_color,27))
	cmds.canvas(h=20,bgc=(0.188,0.627,0.627),pc=Callback(nmRiggingTab_func.nmControlColor_color,28))
	cmds.canvas(h=20,bgc=(0.188,0.404,0.627),pc=Callback(nmRiggingTab_func.nmControlColor_color,29))
	cmds.canvas(h=20,bgc=(0.435,0.188,0.627),pc=Callback(nmRiggingTab_func.nmControlColor_color,30))
	cmds.canvas(h=20,bgc=(0.627,0.188,0.412),pc=Callback(nmRiggingTab_func.nmControlColor_color,31))
	##############################################################################
	# create control section
	cmds.frameLayout(l='Controls:',mh=2,mw=2,li=2,p='nmSAK_rigControlRightCol')
	cmds.columnLayout()
	# create layout
	cmds.rowColumnLayout(nc=2,cw=[(1,76),(2,76)])
	cmds.button(h=24,l='Circle',c=Callback(nmRiggingTab_func.nmControls_circle))
	cmds.button(h=24,l='Square',c=Callback(nmRiggingTab_func.nmControls_square))
	cmds.button(h=24,l='Triangle',c=Callback(nmRiggingTab_func.nmControls_triangle))
	cmds.button(h=24,l='Locator',c=Callback(nmRiggingTab_func.nmControls_locator))
	cmds.button(h=24,l='Ball',c=Callback(nmRiggingTab_func.nwControls_ball))
	cmds.button(h=24,l='Box',c=Callback(nmRiggingTab_func.nmControls_box))
	cmds.button(h=24,l='Diamond',c=Callback(nmRiggingTab_func.nwControls_diamond))
	cmds.button(h=24,l='Eye Pin')
	cmds.button(h=25,l='D Pad',c=Callback(nmRiggingTab_func.nmControls_dPad))
	cmds.button(h=25,l='Arrow Pad',c=Callback(nmRiggingTab_func.nmControls_arrowPad))
	cmds.button(h=25,l='Arrow',c=Callback(nmRiggingTab_func.nmControls_arrow))
	cmds.button(h=25,l='Dbl Arrow',c=Callback(nmRiggingTab_func.nmControls_doubleArrow))
	cmds.button(h=25,l='Crvd Arrows')
	# cmds.button(h=25,l='Star')
	cmds.button(h=25,l='Ninja Star',c=Callback(nmRiggingTab_func.nmControls_ninjaStar))
	# cmds.button(h=25,l='')
	# cmds.button(h=24,l='')
	# cmds.button(h=24,l='')
	##############################################################################
	# create special controls
	cmds.frameLayout(l='Special Controls:',mh=2,mw=2,li=2,p='nmSAK_rigControlRightCol')
	cmds.columnLayout()
	cmds.rowColumnLayout(nc=2,cw=[(1,76),(2,76)])
	cmds.button(h=25,l='Move All',c=Callback(nmRiggingTab_func.nmSpecialControls_moveAll))
	cmds.button(h=25,l='Add Offset',c=Callback(nmRiggingTab_func.nwSpecialControls_addOffset))
	# spacer
	cmds.text(h=6,l='')
	# spacer
	cmds.text(h=6,l='')
	cmds.button(h=25,l='Edge Joints',c=Callback(nmRiggingTab_func.nwSpecialControls_EdgeJointSpline))
	cmds.button(h=25,l='Crv Controls',c=Callback(nmRiggingTab_func.nwSpecialControls_CurveControls))
	##############################################################################
	# attributes tab #
	# create naming section
	cmds.frameLayout(l='Simple Add Attribute:',mh=2,mw=2,li=2,p='nwSAK_rigAttCol')
	cmds.columnLayout('nwSAK_addAttCol')
	cmds.rowColumnLayout('nwSAK_attName',nc=1,cw=[(1,318)])
	cmds.columnLayout(p='nwSAK_attName')
	# name attribute options
	cmds.textFieldGrp('nwSAK_longName',l='Long Name:',cw2=(65,260))
	cmds.textFieldGrp('nwSAK_niceName',l='Nice Name:',cw2=(65,260))
	cmds.radioButtonGrp('nmSAK_makeType',h=27,nrb=3,la3=('Keyable','Displayable','Hidden'),cw3=(68,93,65),co3=(50,5,5),sl=True)
	cmds.text(l='',p='nwSAK_attName',h=2)
	cmds.separator(w=325,p='nwSAK_attName')
	cmds.text(l='',p='nwSAK_attName',h=2)
	cmds.columnLayout(p='nwSAK_attName')
	cmds.radioButtonGrp('nwSAK_dataType',h=27,nrb=3,la3=('Float','Boolean','Enum'),cw3=(68,93,65),sl=True)
	cmds.text(l='',p='nwSAK_attName',h=2)
	cmds.separator(w=325,p='nwSAK_attName')
	cmds.text(l='',p='nwSAK_attName',h=2)
	cmds.columnLayout(p='nwSAK_attName')
	cmds.rowColumnLayout(nc=3,cw=[(1,109),(2,109),(3,110)])
	cmds.textFieldGrp('nwSAK_minProp',l='Minimum:',cw2=(56,45))
	cmds.textFieldGrp('nwSAK_maxProp',l='Maximum:',cw2=(60,45))
	cmds.textFieldGrp('nwSAK_defProp',l='Default:',cw2=(50,45))
	cmds.separator(w=325,p='nwSAK_attName')
	cmds.text(l='',p='nwSAK_attName',h=2)
	cmds.columnLayout(p='nwSAK_attName')
	cmds.rowColumnLayout(nc=2,cw=[(1,280),(2,40)])
	cmds.text(l='Enum Names:')
	cmds.text(l='Value:')
	cmds.textFieldGrp('nwSAK_enumName0',cw1=(280))
	cmds.text(l='0')
	cmds.textFieldGrp('nwSAK_enumName1',cw1=(280))
	cmds.text(l='1')
	cmds.textFieldGrp('nwSAK_enumName2',cw1=(280))
	cmds.text(l='2')
	cmds.textFieldGrp('nwSAK_enumName3',cw1=(280))
	cmds.text(l='3')
	cmds.textFieldGrp('nwSAK_enumName4',cw1=(280))
	cmds.text(l='4')
	cmds.textFieldGrp('nwSAK_enumName5',cw1=(280))
	cmds.text(l='5')
	cmds.textFieldGrp('nwSAK_enumName6',cw1=(280))
	cmds.text(l='6')
	cmds.columnLayout(p='nwSAK_attName')
	cmds.button(h=25,w=328,l='Add Attribute',c=Callback(nmRiggingTab_func.nwAtt_SimpleAdd))
	##############################################################################
	# create shift attribute
	cmds.frameLayout(l='Shift Attribute:',mh=2,mw=2,li=2,p='nwSAK_rigAttCol')
	cmds.columnLayout()
	cmds.rowColumnLayout(nc=2,cw=[(1,159),(2,159)])
	cmds.button(h=25,l='Up',c=Callback(nmRiggingTab_func.nwAtt_Shiftup))
	cmds.button(h=25,l='Down',c=Callback(nmRiggingTab_func.nwAtt_ShiftDown))
	##############################################################################
	### joints tab ###
	# joints
	cmds.frameLayout(l='Joints:',mh=2,mw=2,li=2,p='nmSAK_rigJointsLeftCol')
	cmds.columnLayout('nmSAK_rigJointJntCol')
	# joint tool
	cmds.button(h=25,w=154,l='Joint Tool',p='nmSAK_rigJointJntCol',c=Callback(nmRiggingTab_func.nmJoints_joint))
	# orient tool
	cmds.button(h=25,w=154,l='Orient Options',p='nmSAK_rigJointJntCol',c=Callback(nmRiggingTab_func.nmJoints_orientJoint))
	# insert joint
	cmds.button(h=25,w=154,l='Insert Joint',p='nmSAK_rigJointJntCol',c=Callback(nmRiggingTab_func.nmJoints_insertJoint))
	# remove joint
	cmds.button(h=25,w=154,l='Remove Joint',p='nmSAK_rigJointJntCol',c=Callback(nmRiggingTab_func.nmJoints_removeJoint))
	##############################################################################
	# mirror joint with search and replace
	cmds.frameLayout(l='Mirror Joint:',mh=2,mw=2,li=2,p='nmSAK_rigJointsLeftCol')
	cmds.columnLayout('nmSAK_rigMirrorMainCol')
	cmds.text(l='',h=2)
	# radio for axis
	cmds.radioButtonGrp('nmSAK_rigMirrorAxis',nrb=3,la3=['XY','YZ','XZ'],cw=[(1,50),(2,50),(3,30)],sl=2)
	# radio for function
	cmds.radioButtonGrp('nmSAK_rigMirrorAction',nrb=2,la2=['Behavior','Orientation'],cw=[(1,62),(2,20)],sl=1)
	# rc
	cmds.text(l='',h=2)
	cmds.rowColumnLayout(nc=1,cw=(1,152))
	# search
	cmds.textFieldGrp('nmSAK_rigMirrorSearch',l='Search: ',cw2=(48,102))
	# replace
	cmds.textFieldGrp('nmSAK_rigMirrorReplace',l='Replace: ',cw2=(48,102))
	# space
	cmds.text(l='',h=2)
	# button
	cmds.button(l='Mirror',h=25,p='nmSAK_rigMirrorMainCol',w=154,c=Callback(nmRiggingTab_func.nmMirrorJoint_mirror))
	##############################################################################
	# create local joint scale
	cmds.frameLayout(l='Local Joint Scale:',mh=2,mw=2,li=2,p='nmSAK_rigJointsRightCol')
	cmds.columnLayout()
	# create radio
	cmds.radioButtonGrp('nmSAK_rigJntLocalSel',nrb=2,la2=('Selected','Hierarchy'),cw2=(72,70),sl=1)
	# set joint radius
	cmds.floatSliderGrp('nmSAK_rigJntLocFLG',min=0.01,max=2,f=True,cw=[(1,48),(2,98)],pre=2,v=.5,cc=Callback(nmRiggingTab_func.nmLocalJointScale_scale),dc=Callback(nmRiggingTab_func.nmLocalJointScale_scale))
	##############################################################################
	# create global joint scale
	cmds.frameLayout(l='Global Joint Scale:',mh=2,mw=2,li=2,p='nmSAK_rigJointsRightCol')
	cmds.columnLayout()
	# int slider
	cmds.floatSliderGrp('nmSAK_rigJntGlobScale',min=0.01,max=5,f=True,cw=[(1,48),(2,98)],pre=2,v=1,cc=Callback(nmRiggingTab_func.nmGlobalJointScale_scale),dc=Callback(nmRiggingTab_func.nmGlobalJointScale_scale))
	##############################################################################
	# create chain blender
	cmds.frameLayout(l='Blender:',mh=2,mw=2,li=2,p='nmSAK_rigJointsRightCol')
	cmds.columnLayout('nmSAK_rigBlenderMainCol')
	# create check box
	cmds.checkBox('nmSAK_rigBlendWholeChainCB',l='Whole Chain',v=1)
	# create blend section
	cmds.rowColumnLayout(nc=2,cw=[(1,132),(2,20)])
	# create bind
	cmds.textFieldGrp('nmSAK_rigBlendBndTFG',l='Bind: ',ed=False,cw2=(27,100))
	cmds.button(l='<',h=25,c=Callback(nmRiggingTab_func.nmBlender_bind))
	# create ik
	cmds.textFieldGrp('nmSAK_rigBlendIkTFG',l='IK: ',ed=False,cw2=(27,100))
	cmds.button(l='<',h=25,c=Callback(nmRiggingTab_func.nmBlender_ik))
	# create fk
	cmds.textFieldGrp('nmSAK_rigBlendFkTFG',l='FK: ',ed=False,cw2=(27,100))
	cmds.button(l='<',h=25,c=Callback(nmRiggingTab_func.nmBlender_fk))
	cmds.text(l='',h=2,p='nmSAK_rigBlenderMainCol')
	# button
	cmds.button(h=25,w=154,l='Create Blend',p='nmSAK_rigBlenderMainCol',c=Callback(nmRiggingTab_func.nmBlender_blend))
	##############################################################################
	# skinning tab #
	# mode
	cmds.frameLayout(l='Mode:',mh=2,mw=2,li=2,p='nmSAK_rigSkinningMainCol')
	cmds.rowColumnLayout(nc=3,cw=[(1,106),(2,107),(3,106)])
	cmds.button(l='Object',h=25,c=Callback(nmRiggingTab_func.nmMode_object))
	cmds.button(l='Component',h=25,c=Callback(nmRiggingTab_func.nmMode_component))
	cmds.button(l='Edge',h=25,c=Callback(nmRiggingTab_func.nmMode_edge))
	##############################################################################
	# weight lifter
	cmds.frameLayout(l='Weight Lifter:',mh=2,mw=2,li=2,p='nmSAK_rigSkinningMainCol')
	cmds.columnLayout('nmSAK_rigWeightsMainCol')
	# mesh
	cmds.frameLayout(lv=False,mh=2,mw=2,li=2,p='nmSAK_rigWeightsMainCol')
	cmds.rowColumnLayout('nmSAK_rigSkinMeshRC',nc=2,cw=[(1,251),(2,60)])
	cmds.columnLayout(p='nmSAK_rigSkinMeshRC')
	cmds.textFieldGrp('nmSAK_rigSkinMeshTFG',l='Mesh: ',ed=False,cw2=(64,180))
	cmds.textFieldGrp('nmSAK_rigSkinClusterTFG',l='Skin Cluster: ',cw2=(64,180),ed=False)
	cmds.button(l='Load',h=42,p='nmSAK_rigSkinMeshRC',c=Callback(nmRiggingTab_func.nmWeightLifter_loadMesh))
	# separator
	cmds.frameLayout(lv=False,mh=2,mw=2,li=2,p='nmSAK_rigWeightsMainCol')
	# joints
	cmds.rowColumnLayout('nmSAK_rigWeightJointRC',nc=2,cw=[(1,155),(2,155)],cs=(2,1))
	cmds.text(l='Active Joints:')
	cmds.text(l='Locked Joints:')
	cmds.text(l='',h=2)
	cmds.text(l='',h=2)
	cmds.textScrollList('nmSAK_rigWeightActiveJointTSL',h=150,ams=True,sc=Callback(nmRiggingTab_func.nmWeightLifter_actiSelect))
	cmds.textScrollList('nmSAK_rigWeightLockedJointTSL',h=150,ams=True,sc=Callback(nmRiggingTab_func.nmWeightLifter_lockSelect))
	cmds.button(l='Lock Toggle',h=18,c=Callback(nmRiggingTab_func.nmWeightLifter_lockToggle))
	cmds.rowColumnLayout(nc=2,cw=[(1,77),(2,77)])
	cmds.button(l='Add',h=18,c=Callback(nmRiggingTab_func.nmWeightLifter_add))
	cmds.button(l='Remove',h=18,c=Callback(nmRiggingTab_func.nmWeightLifter_remove))
	cmds.text(l='',h=2,p='nmSAK_rigWeightJointRC')
	cmds.text(l='',h=2,p='nmSAK_rigWeightJointRC')
	cmds.button(l='> > >',h=25,p='nmSAK_rigWeightJointRC',c=Callback(nmRiggingTab_func.nmWeightLifter_lock))
	cmds.button(l='< < <',h=25,p='nmSAK_rigWeightJointRC',c=Callback(nmRiggingTab_func.nmWeightLifter_unlock))
	# update joints listed
	cmds.frameLayout(lv=False,mh=2,mw=2,li=2,p='nmSAK_rigWeightsMainCol')
	cmds.rowColumnLayout(nc=1,cw=(1,311))
	cmds.button(l='Reload Joint Activity',h=25,c=Callback(nmRiggingTab_func.nmWeightLifter_reloadActivity))
	# value set
	cmds.frameLayout(lv=False,mh=2,mw=2,li=2,p='nmSAK_rigWeightsMainCol')
	cmds.rowColumnLayout(nc=1,cw=(1,311))
	
	##############################################################################
	
	##############################################################################
	# lazy boy
	cmds.frameLayout(l='La-Z-Boy:',mh=2,mw=2,li=2,p='nmSAK_rigSkinningMainCol')
	cmds.columnLayout('nmSAK_rigLaZBoyMainCol')
	cmds.rowColumnLayout('nmSAK_rigLaZBoyMainRC',nc=2,cw=[(1,158),(2,158)],cs=(2,1))
	cmds.button(l='Mirror Weights',h=25)
	cmds.button(l='Copy Weights',h=25)
	##############################################################################
	
	##############################################################################
	
	##############################################################################
	
	##############################################################################
	
	##############################################################################
	
	
	
	
	
	
	
	
	
	
	##############################################################################
	# ANIMATION TAB 
	##############################################################################
	# animation tab main
	cmds.columnLayout('nmSAK_mainAnimCol',p='nmSAK_ani')
	# world space tool
	# create world space frame
	cmds.frameLayout(l='WorldSpaceTool:',mh=2,mw=2,li=2,p='nmSAK_mainAnimCol')
	cmds.columnLayout('nwSAK_modWorldSpaceAniCol')
	cmds.floatFieldGrp('nwSAK_manipPivotAni',l='Pivots',numberOfFields=3,precision=4,cw=[(1,160),(2,50),(3,50),(4,50)],p='nwSAK_modWorldSpaceAniCol',vis=0)
	cmds.floatFieldGrp('nwSAK_transPivotsAni',l='Translate',numberOfFields=3,precision=4,cw=[(1,160),(2,50),(3,50),(4,50)],p='nwSAK_modWorldSpaceAniCol',vis=0)
	cmds.floatFieldGrp('nwSAK_rotPivotsAni',l='Rotate',numberOfFields=3,precision=4,cw=[(1,160),(2,50),(3,50),(4,50)],p='nwSAK_modWorldSpaceAniCol',vis=0)
	cmds.floatFieldGrp('nwSAK_scalePivotsAni',l='Scale',numberOfFields=3,precision=4,cw=[(1,160),(2,50),(3,50),(4,50)],p='nwSAK_modWorldSpaceAniCol',vis=0)
	cmds.rowColumnLayout('nwSAK_modWorldSpaceAniRC',nc=4,cw=[(1,50),(2,50),(3,50),(4,175)],co=(4,'left',12))
	# create trans
	cmds.frameLayout(p='nwSAK_modWorldSpaceAniRC',l='Trans:',li=1,mh=2,mw=2)
	cmds.columnLayout('nwSAK_modWorldSpaceAniTransCol',rs=-5)
	# all
	cmds.checkBox('nwSAK_modWorldSpaceAniTransAllCB',l='All',cc=Callback(nwAnimTab_func.setPivotToManip_transAll))
	# create x
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceAniTransCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(1,0,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceAniTransXCB',l='X',cc=Callback(WSTcheckboxAni))
	# create y
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceAniTransCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,1,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceAniTransYCB',l='Y',cc=Callback(WSTcheckboxAni))
	# create z
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceAniTransCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,0,1),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceAniTransZCB',l='Z',cc=Callback(WSTcheckboxAni))
	# create rot
	cmds.frameLayout(p='nwSAK_modWorldSpaceAniRC',l='Rotate:',li=0,mh=2,mw=2)
	cmds.columnLayout('nwSAK_modWorldSpaceAniRotateCol',rs=-5)
	# all
	cmds.checkBox('nwSAK_modWorldSpaceAniRotateAllCB',l='All',cc=Callback(nwAnimTab_func.setPivotToManip_rotAll))
	# create x
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceAniRotateCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(1,0,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceAniRotateXCB',l='X',cc=Callback(WSTcheckboxAni))
	# create y
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceAniRotateCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,1,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceAniRotateYCB',l='Y',cc=Callback(WSTcheckboxAni))
	# create z
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceAniRotateCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,0,1),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceAniRotateZCB',l='Z',cc=Callback(WSTcheckboxAni))
	# create scl
	cmds.frameLayout(p='nwSAK_modWorldSpaceAniRC',l='Scale:',li=2,mh=2,mw=2)
	cmds.columnLayout('nwSAK_modWorldSpaceAniScaleCol',rs=-5)
	# all
	cmds.checkBox('nwSAK_modWorldSpaceAniScaleAllCB',l='All',cc=Callback(nwAnimTab_func.setPivotToManip_scaleAll))
	# create x
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceAniScaleCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(1,0,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceAniScaleXCB',l='X',cc=Callback(WSTcheckboxAni))
	# create y
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceAniScaleCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,1,0),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceAniScaleYCB',l='Y',cc=Callback(WSTcheckboxAni))
	# create z
	cmds.rowColumnLayout(p='nwSAK_modWorldSpaceAniScaleCol',nc=3,cw=[(1,5),(2,5),(3,28)])
	cmds.canvas(w=5,rgb=(0,0,1),h=15)
	cmds.text(l='')
	cmds.checkBox('nwSAK_modWorldSpaceAniScaleZCB',l='Z',cc=Callback(WSTcheckboxAni))
	cmds.separator(w=325,p='nmSAK_mainAnimCol')
	# cmds.frameLayout(l='',mw=168,p='nmSAK_mainAnimCol')
	# create vis
	#cmds.frameLayout(p='nwSAK_modWorldSpaceAniCol',lv=False,li=2,mh=2,mw=2)
	#cmds.rowColumnLayout(nc=1,cw=(1,146))
	# visibility
	#cmds.checkBox('nwSAK_modWorldSpaceAniVisCB',h=17,l='Visibility',cc=Callback(nwModelingTab_func.setPivotToManip_apply))
	# capture transforms
	cmds.columnLayout(p='nwSAK_modWorldSpaceAniRC')
	cmds.button(h=25,w=154,l='Capture',c=Callback(nwAnimTab_func.captureManipPiv))
	# select mode
	cmds.radioButtonGrp('nwSAK_animovTypeSelect',nrb=2,la2=('Transform','Pivot'),cw2=(90,77),h=25,sl=1)
	# apply transforms
	cmds.button(h=24,w=154,l='Apply',c=Callback(nwAnimTab_func.setPivotToManip_apply))
	# average transforms
	cmds.button(h=24,w=154,l='Average')
	# add spacer
	##############################################################################
	# create smooth preview box
	cmds.rowColumnLayout('nmSAK_animSmoothMain',nc=2,cw=[(1,163),(2,163)],cs=(2,2),p='nmSAK_mainAnimCol')
	cmds.columnLayout('nwSAK_aniLeftCol',p='nmSAK_animSmoothMain')
	cmds.columnLayout('nwSAK_aniRightCol',p='nmSAK_animSmoothMain')
	cmds.frameLayout(l='Smooth Mesh Preview:',mh=2,mw=2,li=2,p='nwSAK_aniLeftCol')
	cmds.columnLayout('nwSAK_smoothCol')
	# center
	cmds.rowColumnLayout(nc=1,cw=(1,155))
	cmds.button(h=25,l='Smooth Preview Toggle',c=Callback(nwAnimTab_func.smoothPreviewToggle))
	##############################################################################
	# create xray toggle utilities box
	cmds.frameLayout(l='Xray View Utlilities:',mh=2,mw=2,li=2,p='nwSAK_aniLeftCol')
	cmds.columnLayout('nwSAK_xrayUtlCol')
	# center
	cmds.rowColumnLayout(nc=1,cw=(1,155))
	cmds.button(h=25,l='Xray Selected Toggle',c=Callback(nwAnimTab_func.nwXraySelectedToggle))
	cmds.rowColumnLayout(nc=1,cw=(1,155))
	cmds.button(h=25,l='Xray All Toggle',c=Callback(nwAnimTab_func.nwXrayAllToggle))
	##############################################################################
	cmds.frameLayout(l='Create ghOstCamera:',mh=2,mw=2,li=2,p='nwSAK_aniRightCol')
	cmds.columnLayout('nwSAK_ghOstCamCol')
	# center
	cmds.rowColumnLayout(nc=1,cw=(1,155))
	cmds.button(h=25,l='Summon ghOstCam',c=Callback(nwAnimTab_func.nwCreateghOstCam))
	
	cmds.rowColumnLayout(nc=1,cw=(1,155))
	cmds.button(h=25,l='Bake for AE',c=Callback(nwAnimTab_func.nwAEcameraSetup))
	
	##############################################################################
	# DYNAMICS TAB 
	##############################################################################
	
	
	
	
	
	
	
	
	##############################################################################
	# CLEANER TAB 
	##############################################################################
	# create Scene Cleaner
	# new col
	cmds.columnLayout('nwSAK_mainClnCol',p='nwSAK_cln')
	##############################################################################
	# uv transfer
	cmds.frameLayout(l='Scene Cleaner:',mh=2,mw=2,li=2,p='nwSAK_mainClnCol')
	cmds.columnLayout('nwSAK_clnButtonsCol')
	# delete dup panels button:
	cmds.rowColumnLayout(nc=1,cw=[(1,320)])
	cmds.button(l='Delete Duplicate Panels',h=25,c=Callback(nwCleanerTab_func.nwDeleteDuplicatePanels))
	# delete unused intermediate nodes (orig, particles, shapes, etc)
	cmds.button(l='Delete Unused Intermediate Nodes',h=25,c=Callback(nwCleanerTab_func.nwDeleteUnusedIntermediates))
	# delete empty transforms/groups
	cmds.button(l='Delete Empty Transforms/Groups',h=25,c=Callback(nwCleanerTab_func.nwDeleteEmptyTransforms))
	# delete non-referenced locked and unlocked unknown nodes
	cmds.button(l='Delete Unknown Nodes',h=25,c=Callback(nwCleanerTab_func.nwDeleteUnknown))
	# delete non-referenced locked and unlocked unknown nodes
	cmds.button(l='Kill TURTLE!!',h=25,c=Callback(nwCleanerTab_func.nwKilltheTURTLE))
	# spacer
	cmds.text(h=6,l='')
	# create divider
	cmds.separator(w=320)
	# spacer
	cmds.text(h=6,l='')
	# do all button
	cmds.button(l='Do All',h=25, c=Callback(nwCleanerTab_func.nwDoAllClean))
		# spacer
	cmds.text(h=6,l='')
	# create divider
	cmds.separator(w=320)
	# spacer
	cmds.text(h=6,l='')
	# do all button
	cmds.button(l='Global Unique Rename of Duplicates',h=25, c=Callback(nwCleanerTab_func.nwGlobalDupRename))
	##############################################################################
	# GUI UPDATE FUNCTIONS
	##############################################################################
	# get scene show list
	nmObjShow_func.nmShow_refresh()
	# get isolate state
	nmObjShow_func.nmShow_isolateCheck()
	# refresh namespaces
	nmGeneralTab_func.nmOuterSpace_refresh()
	
	## show windows version GUI ##
	cmds.showWindow(winGUI)

nm_about = cmds.about(os=True)
if (nm_about == 'mac'):
	print ('\n***************************************************************\nINNOVATED MOTION\nCopywrite: 2011\nScript: nmSwissArmyKnife.py\nAuthor: Nole Murphy\nVersion: OSX\n***************************************************************\n')
	nmSAK_gui()
elif (nm_about == 'linux'):
	print ('\n***************************************************************\nINNOVATED MOTION\nCopywrite: 2011\nScript: nmSwissArmyKnife.py\nAuthor: Nole Murphy\nVersion: Linux\n***************************************************************\n')
	nmSAK_gui()
else:
	print ('\n***************************************************************\nINNOVATED MOTION\nCopywrite: 2011\nScript: nmSwissArmyKnife.py\nAuthor: Nole Murphy\nVersion: Windows\n***************************************************************\n')
	nmSAK_gui()
