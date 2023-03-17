# encoding: utf-8

###########################################################################################################
#
#
#	General Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/General%20Plugin
#   Autrhor: RealType
#   Copyright: RealType
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
from vanilla import *
import RTShowInfoData
import os

class RTShowInfo(GeneralPlugin):

	@objc.python_method
	def settings(self):
		self.name = u"RT数据统计"

	@objc.python_method
	def start(self):
		newMenuItem = NSMenuItem(self.name, self.showWindow_)
		Glyphs.menu[EDIT_MENU].append(newMenuItem)

	def showWindow_(self, sender):
		titles =[
					{"title": u"名称",  "width": 120}, 
					{"title": u"值","editable":True}, 
					{"title": u"字形", "width": 30}, 
					{"title": "unicode", "width": 50}, 
					{"title": "name", "width": 80}, 
					{"title": u"操作",  "width": 70}
				]
		self.w = Window((550, 620), title = "RT数据统计")
		self.w.label1 = TextBox((10,10,-40,20),u'*显示数据是基于当前Gyphs文件统计，可能会与生成字库后的数据有误差。')
		self.w.label2 = TextBox((10,30,-40,20),u'*可以双击打开选择(支持多选)的字符。')
		self.w.label3 = TextBox((10,50,-40,20),u'*如有需求，可以在公众号中直接留言，如可行，我会添加进去。')
		self.w.rtImg = ImageView((470,10,-10,60))
		self.w.rtImg.setImage(os.path.join(os.path.dirname(__file__),'rtqrcode.jpg'))
		self.items = RTShowInfoData.data(Glyphs.font)
		self.w.glyphList = List((10, 80, -10, 500), self.items, columnDescriptions = titles, showColumnTitles = True, rowHeight = 20, drawFocusRing = False, enableDelete = False,doubleClickCallback=self.doubleClickItem)
		self.w.refresh = Button((10,590,80,20),u'刷新数据',callback=self.refresh)
		self.w.exportTxt = Button((100,590,80,20),u'导出数据',callback=self.exportTxt)
		self.w.open()

	
  
	@objc.python_method
	def doubleClickItem(self,sender):
		selection = sender.getSelection()
		tabs = []
		for index in selection:
			name = self.items[index].get("name")
			if name:
				tabs.append(name)
		if len(tabs)>0:
			newTab = "/"+"/".join(tabs)
			Glyphs.font.newTab(newTab)
   
	@objc.python_method
	def refresh(self,sender):
		self.w.glyphList.set(RTShowInfoData.data(Glyphs.font))
  
	@objc.python_method
	def exportTxt(self,sender):
		RTShowInfoData.export(Glyphs.font.filepath,self.items)
	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
