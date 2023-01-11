def whileOn(channel, sampleIndex, val, prev):
	
	if me.parent().par.Ready == 1:
    
		print('Load')
  
		me.parent().par.Ready = 0
		me.parent().par.Loading = 1
		me.parent().par.Loaded = 0
		
		tableIndex = me.parent().par.Tableindex
		op('movieFileEngine').par.File = me.parent(2).op('tableTileURL')[tableIndex, 0]
	
		# set the parent talbe values
		me.parent(2).op('tableTileURL')[tableIndex, 3] = 1
		me.parent(2).op('tableTileURL')[tableIndex, 4] = 0

		# start the actual loading
		op('movieFileEngine').par.Reloadpulse.pulse()

	return
