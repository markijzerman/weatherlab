class TileManager:
	
	"""
	TileManager description
	"""
	
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.Initialize()

		return


	def Initialize(self):
		
		# get tileLoader ready
		op('tileLoader').par.Initialize.pulse()

		return


	def LoadTiles(self):

		# Clear the texture3D
		op('tex3d1').par.resetpulse.pulse()

		# Fill the 'tableTileURL' with data
		rows = int(op('par1')['Rows'])
		cols = int(op('par1')['Columns'])
		amtTiles = rows * cols
		
		middleTileX = rows/2
		middleTileY = cols/2
		
		op('tableTileURL').clear(keepFirstRow=True)
		
		for x in range(cols):
			xTile = int((x + int(op('par1')['Tilexy1'])) - middleTileX)
			for y in range(rows):
				yTile = int(y + int(op('par1')['Tilexy2']) - middleTileY)
				tileURL = me.parent().par.Apilinkstart + str(int(op('par1')['Zoomlevel'])) + '/' + str(xTile) + '/' + str(yTile) + me.parent().par.Apilinkend

				op('tableTileURL').appendRow([tileURL,x,y,0,0])

		return


	def LoadNextTile(self):

		if me.parent().par.Gettiles:

			# Start the index at one so it skips the header
			index = 1
			tableIndex = 0

			while index < op("tableTileURL").numRows and tableIndex < 1:
				if op("tableTileURL")[index,3] == 0 and op("tableTileURL")[index,4] == 0:
					tableIndex = index
				index += 1

			if tableIndex > 0:

				print("LoadNextTile: " + str(tableIndex))

				op('tileLoader').par.Tableindex = tableIndex
				op('tileLoader').par.Load.pulse()

			else:

				print('ALL DONE!')
				me.parent().par.Gettiles = False

			return


	def PlaceTile(self, tableIndex):

		x = op('tableTileURL')[tableIndex,1]
		y = op('tableTileURL')[tableIndex,2]

		rows = me.parent().par.Rows
		columns = me.parent().par.Columns
		index = (rows - y - 1) * columns + x
		op('tex3d1').par.replaceindex = index
		op('tex3d1').par.replacesinglepulse.pulse()

		return

	def CheckStatus(self):

		if op('tileLoader').par.Loaded == 1 and op('tileLoader').par.Ready == 0:

				# set the loaded values in the table
				tableIndex = op('tileLoader').par.Tableindex

				if op('tableTileURL')[tableIndex, 3] == 1:
					op('tableTileURL')[tableIndex, 3] = 0
					op('tableTileURL')[tableIndex, 4] = 1

					# place the tile
					self.PlaceTile(tableIndex)
        
				else:

					op('tileLoader').par.Clear.pulse()

		elif op('tileLoader').par.Loaded == 0 and op('tileLoader').par.Loading == 0 and op('tileLoader').par.Ready == 1:

				print("self.LoadNextTile")
				self.LoadNextTile()

		return