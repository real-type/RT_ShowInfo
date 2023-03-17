from GlyphsApp import *
import os,sys

def data(font):
	
	li =[]
	
	dic_zui ={}
	allLayerWidth = 0
	for glyph in font.glyphs:
		for layer in glyph.layers:
			try:
				allLayerWidth+=layer.width
				if layer.bounds.size.width>0:
					#最大字宽
					maxLayerWidth= dic_zui.get('maxLayerWidth')
					currentLayerWidth = layer.width
					if maxLayerWidth:
						if currentLayerWidth>maxLayerWidth[1]:
							dic_zui['maxLayerWidth'] = (glyph,currentLayerWidth)
					else:
						dic_zui.setdefault('maxLayerWidth',(glyph,currentLayerWidth))

					#最小字宽
					minLayerWidth= dic_zui.get('minLayerWidth')
					currentLayerWidth = layer.width
					if currentLayerWidth>0:
						if maxLayerWidth:
							if currentLayerWidth<minLayerWidth[1]:
								dic_zui['minLayerWidth']=(glyph,currentLayerWidth)
						else:
							dic_zui.setdefault('minLayerWidth',(glyph,currentLayerWidth))

				
		
					#最多轮廓
					maxPaths = dic_zui.get('maxPaths')
					currentPaths = len(layer.paths)
					if maxPaths:
						if currentPaths>maxPaths[1]:
							dic_zui['maxPaths'] = (glyph,currentPaths)
					else:
						dic_zui.setdefault('maxPaths',(glyph,currentPaths))

					#最多部件
					maxComponents= dic_zui.get('maxComponents')
					currentComponents = len(layer.components)
					
					if currentComponents:
						if currentComponents>maxComponents[1]:
							dic_zui['maxComponents']=(glyph,currentComponents)
					else:
						dic_zui.setdefault('maxComponents',(glyph,currentComponents))

					x,y,w,h = layer.bounds.origin.x,layer.bounds.origin.y,layer.bounds.size.width,layer.bounds.size.height
					#minX
					minX = dic_zui.get('minX')
					if minX:
						if x<minX[1]:
							dic_zui['minX']=(glyph,x)
					else:
						dic_zui.setdefault('minX',(glyph,x))
					
					#minY
					minY = dic_zui.get('minY')
					if minY:
						if y<minY[1]:
							dic_zui['minY']=(glyph,y)
					else:
						dic_zui.setdefault('minY',(glyph,y))
					
					#maxX
					maxX = dic_zui.get('maxX')
					currentMaxX = x+w
					if maxX:
						if currentMaxX>maxX[1]:
							dic_zui['maxX']=(glyph,currentMaxX)
					else:
						dic_zui.setdefault('maxX',(glyph,currentMaxX))
					
					#maxY
					maxY = dic_zui.get('maxY')
					currentMaxY = y+h
					if maxY:
						if currentMaxY>maxY[1]:
							dic_zui['maxY']=(glyph,currentMaxY)
					else:
						dic_zui.setdefault('maxY',(glyph,currentMaxY))
			
					#最宽字符
					maxWdith = dic_zui.get('maxWidth')
					if maxWdith:
						if w>maxWdith[1]:
							dic_zui['maxWidth']=(glyph,w)
							
					else:
						dic_zui.setdefault('maxWidth',(glyph,w))
			
					#最窄非空字符
					minWidth = dic_zui.get('minWidth')
					if w>0:
						if minWidth:
							if  w<minWidth[1]:
								dic_zui['minWidth']=(glyph,w)
						else:
							dic_zui.setdefault('minWidth',(glyph,w))
		
					#最高字符
					maxHeight = dic_zui.get('maxHeight')
					if maxHeight:
						if h>maxHeight[1]:
							dic_zui['maxHeight']=(glyph,h)
					else:
						dic_zui.setdefault('maxHeight',(glyph,h))
			
					#最矮非空字符
					minHeight = dic_zui.get('minHeight')
					if h>0:
						if minWidth:
							if  h<minHeight[1]:
								dic_zui['minHeight']=(glyph,h)
						else:
							dic_zui.setdefault('minHeight',(glyph,h))

					#最大左边距
					maxLSB = dic_zui.get('maxLSB')
					currentLSB = layer.LSB
					if maxLSB:
						if currentLSB>maxLSB[1]:
							dic_zui['maxLSB']=(glyph,currentLSB)
					else:
						dic_zui.setdefault('maxLSB',(glyph,currentLSB))
		
					#最大右边距
					maxRSB = dic_zui.get('maxRSB')
					currentRSB = layer.RSB
					if maxRSB:
						if currentRSB>maxRSB[1]:
							dic_zui['maxRSB']=(glyph,currentRSB)
					else:
						dic_zui.setdefault('maxRSB',(glyph,currentRSB))
		
					#最小左边距
					minLSB = dic_zui.get('minLSB')
					currentLSB = layer.LSB
					if minLSB:
						if currentLSB<minLSB[1]:
							dic_zui['minLSB']=(glyph,currentLSB)
					else:
						dic_zui.setdefault('minLSB',(glyph,currentLSB))
					#最小右边距
					minRSB = dic_zui.get('minRSB')
					currentRSB = layer.RSB
					if minRSB:
						if currentRSB<minRSB[1]:
							dic_zui['minRSB']=(glyph,currentRSB)
					else:
						dic_zui.setdefault('minRSB',(glyph,currentRSB))
		
					#最矮非空字符
					minHeight = dic_zui.get('minHeight')
					if h>0:
						if minWidth:
							if  h<minHeight[1]:
								dic_zui['minHeight']=(glyph,h)
						else:
							dic_zui.setdefault('minHeight',(glyph,h))
		
		
					nodes=0
					for path in layer.paths:
						nodes+=len(path.nodes)

					#最多点
					maxNodes = dic_zui.get('maxNodes')
					if maxNodes:
						if nodes>maxNodes[1]:
							dic_zui['maxNodes']=(glyph,nodes)
					else:
						dic_zui.setdefault('maxNodes',(glyph,nodes))
					
					#最少点
					minNodes = dic_zui.get('minNodes')
					if minNodes:
						if nodes<minNodes[1]:
							dic_zui['minNodes']=(glyph,nodes)
					else:
						dic_zui.setdefault('minNodes',(glyph,nodes))
			except:
				print("Unexpected error:", sys.exc_info())
				pass
	
	try:
		dit ={}
		dit.setdefault(u"名称",u"文件路径")
		dit.setdefault(u"值",font.filepath)
		li.append(dit)
  
		#文件名
		dit ={}
		dit.setdefault(u"名称",u"文件名")
		dit.setdefault(u"值",os.path.basename(font.filepath))
		li.append(dit)
		#文件格式
		fileExt = os.path.splitext(font.filepath)[-1]
		dit ={}
		dit.setdefault(u"名称",u"文件格式")
		dit.setdefault(u"值",fileExt)
		li.append(dit)
		#FamilyName
		dit ={}
		dit.setdefault(u"名称",u"默认家族名")
		dit.setdefault(u"值",font.familyName)
		li.append(dit)
		#字符数
		dit ={}
		dit.setdefault(u"名称",u"字符数")
		dit.setdefault(u"值",str(len(font.glyphs)))
		li.append(dit)
		
		
		#最多节点
		maxNodes = dic_zui.get('maxNodes')
		if maxNodes:
			dit ={}
			dit.setdefault(u"名称",u"最多节点")
			dit.setdefault(u"值",str(maxNodes[1]))
			dit.setdefault(u"字形",maxNodes[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",maxNodes[0].unicode)
			dit.setdefault(u"name",maxNodes[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
	
		#最少节点
		minNodes = dic_zui.get('minNodes')
		if minNodes:
			dit ={}
			dit.setdefault(u"名称",u"最少节点")
			dit.setdefault(u"值",str(minNodes[1]))
			dit.setdefault(u"字形",minNodes[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",minNodes[0].unicode)
			dit.setdefault(u"name",minNodes[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
	
		#最多轮廓
		maxPaths = dic_zui.get('maxPaths')
		if maxPaths:
			dit ={}
			dit.setdefault(u"名称",u"最多轮廓")
			dit.setdefault(u"值",str(maxPaths[1]))
			dit.setdefault(u"字形",maxPaths[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",maxPaths[0].unicode)
			dit.setdefault(u"name",maxPaths[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
	
		#最多部件
		maxComponents = dic_zui.get('maxComponents')
		if maxComponents:
			dit ={}
			dit.setdefault(u"名称",u"最多部件")
			dit.setdefault(u"值",str(maxComponents[1]))
			if maxComponents[1]>0:
				dit.setdefault(u"字形",maxComponents[0].glyphInfo.unicharString())
				dit.setdefault(u"unicode",maxComponents[0].unicode)
				dit.setdefault(u"name",maxComponents[0].name)
				dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
		
		#最大字框宽度
		maxLayerWidth = dic_zui.get('maxLayerWidth')
		if maxLayerWidth:
			dit ={}
			dit.setdefault(u"名称",u"最大字框宽度")
			dit.setdefault(u"值",str(maxLayerWidth[1]))
			dit.setdefault(u"字形",maxLayerWidth[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",maxLayerWidth[0].unicode)
			dit.setdefault(u"name",maxLayerWidth[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
		
		#最小非0字框宽度
		
		minLayerWidth = dic_zui.get('minLayerWidth')
		if minLayerWidth:
			dit ={}
			dit.setdefault(u"名称",u"最小非0字框宽度")
			dit.setdefault(u"值",str(minLayerWidth[1]))
			dit.setdefault(u"字形",minLayerWidth[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",minLayerWidth[0].unicode)
			dit.setdefault(u"name",minLayerWidth[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
		
		#最大字符宽度
		maxWidth= dic_zui.get('maxWidth')
		if maxWidth:
			dit ={}
			dit.setdefault(u"名称",u"最大字符宽度")
			dit.setdefault(u"值",str(maxWidth[1]))
			dit.setdefault(u"字形",maxWidth[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",maxWidth[0].unicode)
			dit.setdefault(u"name",maxWidth[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
	
		#最小非0字符宽度
		minWidth= dic_zui.get('minWidth')
		if minWidth:
			dit ={}
			dit.setdefault(u"名称",u"最小非0字符宽度")
			dit.setdefault(u"值",str(minWidth[1]))
			dit.setdefault(u"字形",minWidth[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",minWidth[0].unicode)
			dit.setdefault(u"name",minWidth[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
		
		#最大字符高度
		maxHeight= dic_zui.get('maxHeight')
		if maxHeight:
			dit ={}
			dit.setdefault(u"名称",u"最大字符高度")
			dit.setdefault(u"值",str(maxHeight[1]))
			dit.setdefault(u"字形",maxHeight[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",maxHeight[0].unicode)
			dit.setdefault(u"name",maxHeight[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
	
		#最小非0字符高度
		minHeight= dic_zui.get('minHeight')
		if  minHeight:
			dit ={}
			dit.setdefault(u"名称",u"最小非0字符高度")
			dit.setdefault(u"值",str(minHeight[1]))
			dit.setdefault(u"字形",minHeight[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",minHeight[0].unicode)
			dit.setdefault(u"name",minHeight[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
	
		#minX
		minX = dic_zui.get('minX')
		if minX:
			dit ={}
			dit.setdefault(u"名称",u"minX")
			dit.setdefault(u"值",str(minX[1]))
			dit.setdefault(u"字形",minX[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",minX[0].unicode)
			dit.setdefault(u"name",minX[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
		
		#maxX
		maxX = dic_zui.get('maxX')
		if maxX:
			dit ={}
			dit.setdefault(u"名称",u"maxX")
			dit.setdefault(u"值",str(maxX[1]))
			dit.setdefault(u"字形",maxX[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",maxX[0].unicode)
			dit.setdefault(u"name",maxX[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
		
		#minY
		minY = dic_zui.get('minY')
		if minY:
			dit ={}
			dit.setdefault(u"名称",u"minY")
			dit.setdefault(u"值",str(minY[1]))
			dit.setdefault(u"字形",minY[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",minY[0].unicode)
			dit.setdefault(u"name",minY[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
		
		#maxY
		maxY = dic_zui.get('maxY')
		if maxY:
			dit ={}
			dit.setdefault(u"名称",u"maxY")
			dit.setdefault(u"值",str(maxY[1]))
			dit.setdefault(u"字形",maxY[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",maxY[0].unicode)
			dit.setdefault(u"name",maxY[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
		
	
		#minLSB
		minLSB = dic_zui.get('minLSB')
		if minLSB:
			dit ={}
			dit.setdefault(u"名称",u"最小左边距")
			dit.setdefault(u"值",str(minLSB[1]))
			dit.setdefault(u"字形",minLSB[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",minLSB[0].unicode)
			dit.setdefault(u"name",minLSB[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
		
		#minRSB
		maxRSB = dic_zui.get('minRSB')
		if maxRSB:
			dit ={}
			dit.setdefault(u"名称",u"最小右边距")
			dit.setdefault(u"值",str(minRSB[1]))
			dit.setdefault(u"字形",minRSB[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",minRSB[0].unicode)
			dit.setdefault(u"name",minRSB[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
		
		#maxLSB
		maxLSB = dic_zui.get('maxLSB')
		if maxLSB:
			dit ={}
			dit.setdefault(u"名称",u"最大左边距")
			dit.setdefault(u"值",str(maxLSB[1]))
			dit.setdefault(u"字形",maxLSB[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",maxLSB[0].unicode)
			dit.setdefault(u"name",maxLSB[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)

		#maxRSB
		maxRSB = dic_zui.get('maxRSB')
		if maxRSB:
			dit ={}
			dit.setdefault(u"名称",u"最大右边距")
			dit.setdefault(u"值",str(maxRSB[1]))
			dit.setdefault(u"字形",maxRSB[0].glyphInfo.unicharString())
			dit.setdefault(u"unicode",maxRSB[0].unicode)
			dit.setdefault(u"name",maxRSB[0].name)
			dit.setdefault(u"操作",u"双击打开")
			li.append(dit)
	except:
		print(sys.exc_info()[0])
	return li;

def export(filepath,items):
	try:
		fileExt = os.path.splitext(filepath)[-1]
		filePath = GetSaveFile(message=u"保存数据", ProposedFileName=filepath.replace(fileExt, '_RTGlyphsInfo.txt'), filetypes=["txt"])
		if filePath:
			with open(filePath,'w') as f:
				for item in items:
					if item.get("name"):
						f.write(u"{}:{}[字形:{},unicode:{},name:{}]\r\n".format(item.get(u"名称"),item.get(u"值"),item.get(u"字形"),item.get("unicode"),item.get("name")))
					else:
						f.write(u"{}:{}\r\n".format(item.get(u"名称"),item.get(u"值")))
				Message(title=u"操作完成", message=u'数据保存', OKButton=u"OK")
	except:
		print(sys.exc_info()[0])