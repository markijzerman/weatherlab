def onOffToOn(channel, sampleIndex, val, prev):
  
  print('Clear')

  me.parent().par.Loaded = 0
  me.parent().par.Loading = 0
  op('movieFileEngine').par.File = ''
  op('movieFileEngine').par.Unload.pulse()

  return
