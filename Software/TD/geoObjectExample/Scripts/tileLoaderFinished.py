def onOffToOn(channel, sampleIndex, val, prev):

	print('Loaded')

	# update the cache value
	op('cache1').par.activepulse.pulse()

	# set the finished loading value
	me.parent().par.Loaded = 1
	me.parent().par.Loading = 0

	return


def onOnToOff(channel, sampleIndex, val, prev):

	print('Ready')

	me.parent().par.Ready = 1
	me.parent().par.Loading = 0

	return