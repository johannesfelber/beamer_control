import serial

serial = dict(
    port='/dev/ttyAMA0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
ola = dict(
    universe=1,
    address=469
)

# Presets for rs232 commands
presets = {
    xrange(0, 23): 'nothing',
    xrange(23, 46): '*pow=on#',
    xrange(46, 69): '*pow=off#',
    xrange(69, 92): '*sour=RGB#',
    xrange(92, 115): '*sour=RGB2#',
    xrange(115, 138): '*sour=vid#',
    xrange(138, 161): '*sour=svid#',
    xrange(161, 184): '*mute=on#',
    xrange(184, 207): '*mute=off#',
    xrange(207, 230): '*lampm=lnor#',
    xrange(230, 256): '*lampm=eco#',
}