# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Visualchart Export Manager", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"VisualChart Base Data Directory (.../VisualChart/RealServer/Data/)" ), wx.VERTICAL )
		
		self.m_dirPickerBaseDir = wx.DirPickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_DIR_MUST_EXIST )
		sbSizer6.Add( self.m_dirPickerBaseDir, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer15.Add( sbSizer6, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Data Sources" ), wx.VERTICAL )
		
		self.m_treeCtrlSources = wx.TreeCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 175,300 ), wx.TR_DEFAULT_STYLE|wx.TR_HAS_BUTTONS|wx.TR_HIDE_ROOT )
		sbSizer2.Add( self.m_treeCtrlSources, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"Add selected >", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.m_button2, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_button22 = wx.Button( self.m_panel1, wx.ID_ANY, u"Add all >>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button22.Enable( False )
		
		bSizer28.Add( self.m_button22, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )
		
		
		sbSizer2.Add( bSizer28, 0, wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		self.m_staticline16 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer4.Add( self.m_staticline16, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Values to convert" ), wx.VERTICAL )
		
		self.m_listCtrlDst = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 350,-1 ), wx.LC_HRULES|wx.LC_REPORT|wx.LC_VRULES )
		sbSizer21.Add( self.m_listCtrlDst, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticline18 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer21.Add( self.m_staticline18, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Conversion Profile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer31.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		m_choiceConvProfilesChoices = []
		self.m_choiceConvProfiles = wx.Choice( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceConvProfilesChoices, 0 )
		self.m_choiceConvProfiles.SetSelection( 0 )
		bSizer31.Add( self.m_choiceConvProfiles, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		sbSizer21.Add( bSizer31, 0, wx.EXPAND, 5 )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button121 = wx.Button( self.m_panel1, wx.ID_ANY, u"Convert active", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button121, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 5 )
		
		self.m_button12 = wx.Button( self.m_panel1, wx.ID_ANY, u"Convert selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_button13 = wx.Button( self.m_panel1, wx.ID_ANY, u"Convert all", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button13, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_staticline17 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer14.Add( self.m_staticline17, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.m_button47 = wx.Button( self.m_panel1, wx.ID_ANY, u"Edit Profiles ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button47, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		sbSizer21.Add( bSizer14, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer4.Add( sbSizer21, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button212 = wx.Button( self.m_panel1, wx.ID_ANY, u"Edit ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_button212, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticline61 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer30.Add( self.m_staticline61, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_button21 = wx.Button( self.m_panel1, wx.ID_ANY, u"Remove selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_button21, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_button213 = wx.Button( self.m_panel1, wx.ID_ANY, u"Remove active", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_button213, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_button2131 = wx.Button( self.m_panel1, wx.ID_ANY, u"Remove non active", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_button2131, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_button211 = wx.Button( self.m_panel1, wx.ID_ANY, u"Remove all", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_button211, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		bSizer30.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button51 = wx.Button( self.m_panel1, wx.ID_ANY, u"About", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_button51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		bSizer4.Add( bSizer30, 0, wx.TOP|wx.EXPAND, 5 )
		
		
		bSizer15.Add( bSizer4, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )
		
		
		self.m_panel1.SetSizer( bSizer15 )
		self.m_panel1.Layout()
		bSizer15.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menuTreeSources = wx.Menu()
		self.m_menuItemEditAlias = wx.MenuItem( self.m_menuTreeSources, wx.ID_ANY, u"Edit Market Alias ...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuTreeSources.AppendItem( self.m_menuItemEditAlias )
		
		self.m_menuTreeSources.AppendSeparator()
		
		self.m_menuItemResetAlias = wx.MenuItem( self.m_menuTreeSources, wx.ID_ANY, u"Reset alias", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuTreeSources.AppendItem( self.m_menuItemResetAlias )
		
		self.m_menuItemResetAllAliases = wx.MenuItem( self.m_menuTreeSources, wx.ID_ANY, u"Reset all aliases", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menuTreeSources.AppendItem( self.m_menuItemResetAllAliases )
		
		self.Bind( wx.EVT_RIGHT_DOWN, self.MainFrameOnContextMenu ) 
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_dirPickerBaseDir.Bind( wx.EVT_DIRPICKER_CHANGED, self.OnDirChangedBaseDir )
		self.m_treeCtrlSources.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.OnTreeItemActivatedSource )
		self.m_treeCtrlSources.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.OnTreeItemRightClickSources )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnButtonClickAdd )
		self.m_button22.Bind( wx.EVT_BUTTON, self.OnButtonClickAdd )
		self.m_listCtrlDst.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.OnListItemActivatedDst )
		self.m_button121.Bind( wx.EVT_BUTTON, self.OnButtonClickConvertActive )
		self.m_button12.Bind( wx.EVT_BUTTON, self.OnButtonClickConvert )
		self.m_button13.Bind( wx.EVT_BUTTON, self.OnButtonClickConvertAll )
		self.m_button47.Bind( wx.EVT_BUTTON, self.OnButtonClickEditProfiles )
		self.m_button212.Bind( wx.EVT_BUTTON, self.OnButtonClickEdit )
		self.m_button21.Bind( wx.EVT_BUTTON, self.OnButtonClickRemove )
		self.m_button213.Bind( wx.EVT_BUTTON, self.OnButtonClickRemoveActive )
		self.m_button2131.Bind( wx.EVT_BUTTON, self.OnButtonClickRemoveNonActive )
		self.m_button211.Bind( wx.EVT_BUTTON, self.OnButtonClickRemoveAll )
		self.m_button51.Bind( wx.EVT_BUTTON, self.OnButtonClickAbout )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionTreeSourcesEditAlias, id = self.m_menuItemEditAlias.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionTreeSourcesResetAlias, id = self.m_menuItemResetAlias.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuSelectionTreeSourcesResetAllAliases, id = self.m_menuItemResetAllAliases.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnDirChangedBaseDir( self, event ):
		event.Skip()
	
	def OnTreeItemActivatedSource( self, event ):
		event.Skip()
	
	def OnTreeItemRightClickSources( self, event ):
		event.Skip()
	
	def OnButtonClickAdd( self, event ):
		event.Skip()
	
	
	def OnListItemActivatedDst( self, event ):
		event.Skip()
	
	def OnButtonClickConvertActive( self, event ):
		event.Skip()
	
	def OnButtonClickConvert( self, event ):
		event.Skip()
	
	def OnButtonClickConvertAll( self, event ):
		event.Skip()
	
	def OnButtonClickEditProfiles( self, event ):
		event.Skip()
	
	def OnButtonClickEdit( self, event ):
		event.Skip()
	
	def OnButtonClickRemove( self, event ):
		event.Skip()
	
	def OnButtonClickRemoveActive( self, event ):
		event.Skip()
	
	def OnButtonClickRemoveNonActive( self, event ):
		event.Skip()
	
	def OnButtonClickRemoveAll( self, event ):
		event.Skip()
	
	def OnButtonClickAbout( self, event ):
		event.Skip()
	
	def OnMenuSelectionTreeSourcesEditAlias( self, event ):
		event.Skip()
	
	def OnMenuSelectionTreeSourcesResetAlias( self, event ):
		event.Skip()
	
	def OnMenuSelectionTreeSourcesResetAllAliases( self, event ):
		event.Skip()
	
	def MainFrameOnContextMenu( self, event ):
		self.PopupMenu( self.m_menuTreeSources, event.GetPosition() )
		

###########################################################################
## Class AboutDialog
###########################################################################

class AboutDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About Visualchart Export Manager", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Export VisualChart (daily) data files to text (csv) formats", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText5.Wrap( -1 )
		sbSizer7.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer7.Add( self.m_staticline8, 0, wx.EXPAND, 5 )
		
		self.m_hyperlink1 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"http://code.google.com/p/vcexportmanager", u"http://code.google.com/p/vcexportmanager", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		sbSizer7.Add( self.m_hyperlink1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer7.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"(C) 2012 Sensible Odds Ltd.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		sbSizer7.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer14.Add( sbSizer7, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()
		bSizer14.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.OnButtonClickOk )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonClickOk( self, event ):
		event.Skip()
	

###########################################################################
## Class ConvProfileDialog
###########################################################################

class ConvProfileDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Conversion Profiles", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Profiles" ), wx.HORIZONTAL )
		
		m_listBoxProfilesChoices = []
		self.m_listBoxProfiles = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxProfilesChoices, wx.LB_ALWAYS_SB|wx.LB_SORT )
		sbSizer12.Add( self.m_listBoxProfiles, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button15 = wx.Button( self, wx.ID_ANY, u"Add ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Edit ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer12.Add( bSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.LEFT, 5 )
		
		
		bSizer7.Add( sbSizer12, 1, wx.EXPAND|wx.BOTTOM, 5 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		
		bSizer7.Add( m_sdbSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button15.Bind( wx.EVT_BUTTON, self.OnButtonClickAdd )
		self.m_button16.Bind( wx.EVT_BUTTON, self.OnButtonClickEdit )
		self.m_button17.Bind( wx.EVT_BUTTON, self.OnButtonClickDelete )
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.OnCancelButtonClick )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.OnOKButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonClickAdd( self, event ):
		event.Skip()
	
	def OnButtonClickEdit( self, event ):
		event.Skip()
	
	def OnButtonClickDelete( self, event ):
		event.Skip()
	
	def OnCancelButtonClick( self, event ):
		event.Skip()
	
	def OnOKButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class DataConversionDialog
###########################################################################

class DataConversionDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Data Conversion", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer23.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlSrcName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.m_textCtrlSrcName.SetMaxLength( 0 ) 
		bSizer23.Add( self.m_textCtrlSrcName, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		bSizer7.Add( bSizer23, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Output Name" ), wx.VERTICAL )
		
		self.m_textCtrlDstName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlDstName.SetMaxLength( 0 ) 
		sbSizer13.Add( self.m_textCtrlDstName, 0, wx.EXPAND|wx.TOP|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer7.Add( sbSizer13, 0, wx.EXPAND|wx.BOTTOM|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer20 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Comment" ), wx.VERTICAL )
		
		self.m_textCtrlComment = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,75 ), wx.TE_MULTILINE )
		self.m_textCtrlComment.SetMaxLength( 0 ) 
		sbSizer20.Add( self.m_textCtrlComment, 0, wx.EXPAND, 5 )
		
		
		bSizer7.Add( sbSizer20, 1, wx.EXPAND|wx.BOTTOM, 5 )
		
		self.m_checkBoxActive = wx.CheckBox( self, wx.ID_ANY, u"Active for export", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_checkBoxActive, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer7.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button41 = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_button41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_buttonCancel, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		bSizer24.Add( bSizer25, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_panelMulti = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panelMulti.Hide()
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_buttonMultiNext = wx.Button( self.m_panelMulti, wx.ID_ANY, u"Edit Next", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_buttonMultiNext, 0, wx.ALL, 5 )
		
		self.m_buttonMultiSkip = wx.Button( self.m_panelMulti, wx.ID_ANY, u"Skip All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_buttonMultiSkip, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		self.m_panelMulti.SetSizer( bSizer27 )
		self.m_panelMulti.Layout()
		bSizer27.Fit( self.m_panelMulti )
		bSizer24.Add( self.m_panelMulti, 1, wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer24, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer7 )
		self.Layout()
		bSizer7.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button41.Bind( wx.EVT_BUTTON, self.OnButtonClickSave )
		self.m_buttonCancel.Bind( wx.EVT_BUTTON, self.OnButtonClickCancel )
		self.m_buttonMultiNext.Bind( wx.EVT_BUTTON, self.OnButtonClickMultiNext )
		self.m_buttonMultiSkip.Bind( wx.EVT_BUTTON, self.OnButtonClickMultiSkip )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonClickSave( self, event ):
		event.Skip()
	
	def OnButtonClickCancel( self, event ):
		event.Skip()
	
	def OnButtonClickMultiNext( self, event ):
		event.Skip()
	
	def OnButtonClickMultiSkip( self, event ):
		event.Skip()
	

###########################################################################
## Class EditConvProfileDialog
###########################################################################

class EditConvProfileDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add/Edit Conversion Profile", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Profile Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer1.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlName.SetMaxLength( 0 ) 
		fgSizer1.Add( self.m_textCtrlName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"File Extension", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer1.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_textCtrlExt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlExt.SetMaxLength( 0 ) 
		fgSizer1.Add( self.m_textCtrlExt, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText141 = wx.StaticText( self, wx.ID_ANY, u"Vol Divisor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )
		fgSizer1.Add( self.m_staticText141, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrlVolDiv = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrlVolDiv.SetMaxLength( 0 ) 
		fgSizer1.Add( self.m_textCtrlVolDiv, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		bSizer32.Add( fgSizer1, 0, wx.EXPAND, 5 )
		
		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Output Directory" ), wx.VERTICAL )
		
		self.m_dirPickerOutDir = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		sbSizer21.Add( self.m_dirPickerOutDir, 0, wx.EXPAND, 5 )
		
		
		bSizer32.Add( sbSizer21, 0, wx.EXPAND, 5 )
		
		sbSizer23 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Format" ), wx.HORIZONTAL )
		
		bSizer34 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_radioBtnSierraChart = wx.RadioButton( self, wx.ID_ANY, u"SierraChart", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.m_radioBtnSierraChart.SetValue( True ) 
		bSizer34.Add( self.m_radioBtnSierraChart, 0, wx.ALL, 5 )
		
		self.m_radioBtn10 = wx.RadioButton( self, wx.ID_ANY, u"Custom", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn10.Enable( False )
		
		bSizer34.Add( self.m_radioBtn10, 0, wx.ALL, 5 )
		
		
		sbSizer23.Add( bSizer34, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Custom Formats", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer36.Add( self.m_staticText15, 0, wx.RIGHT|wx.LEFT, 5 )
		
		m_listBoxCustomFormatsChoices = []
		self.m_listBoxCustomFormats = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxCustomFormatsChoices, 0 )
		bSizer36.Add( self.m_listBoxCustomFormats, 0, wx.EXPAND|wx.BOTTOM, 5 )
		
		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button48 = wx.Button( self, wx.ID_ANY, u"Add ...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.m_button48.Enable( False )
		
		bSizer37.Add( self.m_button48, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_button49 = wx.Button( self, wx.ID_ANY, u"Edit ...", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.m_button49.Enable( False )
		
		bSizer37.Add( self.m_button49, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button50 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.m_button50.Enable( False )
		
		bSizer37.Add( self.m_button50, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer36.Add( bSizer37, 1, wx.EXPAND, 5 )
		
		
		sbSizer23.Add( bSizer36, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer32.Add( sbSizer23, 1, wx.EXPAND|wx.BOTTOM, 5 )
		
		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
		self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();
		
		bSizer32.Add( m_sdbSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )
		
		
		self.SetSizer( bSizer32 )
		self.Layout()
		bSizer32.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button48.Bind( wx.EVT_BUTTON, self.OnButtonClickAddFormat )
		self.m_button49.Bind( wx.EVT_BUTTON, self.OnButtonClickEditFormat )
		self.m_button50.Bind( wx.EVT_BUTTON, self.OnButtonClickDelFormat )
		self.m_sdbSizer4Cancel.Bind( wx.EVT_BUTTON, self.OnCancelButtonClick )
		self.m_sdbSizer4OK.Bind( wx.EVT_BUTTON, self.OnOKButtonClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnButtonClickAddFormat( self, event ):
		event.Skip()
	
	def OnButtonClickEditFormat( self, event ):
		event.Skip()
	
	def OnButtonClickDelFormat( self, event ):
		event.Skip()
	
	def OnCancelButtonClick( self, event ):
		event.Skip()
	
	def OnOKButtonClick( self, event ):
		event.Skip()
	

