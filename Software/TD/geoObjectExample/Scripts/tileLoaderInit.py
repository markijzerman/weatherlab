

def onOnToOff(channel, sampleIndex, val, prev):
	me.parent().par.Loaded = 0
	me.parent().par.Loading = 0
	me.parent().par.Ready = 1
	op('cache1').par.resetpulse.pulse()
	op('movieFileEngine').par.File = ''
	return

