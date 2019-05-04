# Beamer Control
A small python script for Raspberry Pi to control a projector via RS232 over sACN (E1.31) or Art-Net (or any other OLA input).
Commands are executed if DMX values are hold for more than 5 seconds.

## Prerequisites
1. A serial to ttl adapter (MAX3232) is connected to GPIO pin 14 & 15 
2. Serial login shell has to be disabled (use raspi-config)
3. serial interface must be enabled

## Installation
1. Clone repository: `git clone https://github.com/johannesfelber/beamer_control.git`
2. Change into *beamer_control*: `cd beamer_control`
3. Make install script executable: `chmod a+x install.sh`
4. Execute install script: `sudo ./install.sh`
5. Reboot `sudo reboot`
6. Add input device to OLA via web interface: http://ip:9090

Beamer control will be startet automatically after sytem boot.

## Configuration
The configuration is stored in */opt/beamer_control/config.py*

### Address and universe

Per default beamer control listens on universe 1 at address 1. Update `address` and `universe` in dict `ola` according to your requirements.

### Serial settings
The serial settings can be updated in dict `serial`. The default values are tested with BenQ projectors.

### Commands
All commands are customizable. Just update `presets` according to your needs. `xrange(n, m)` defines the DMX values for this preset, the value is a string, which is sent to the projector. The predefined values work with most BenQ projectors.

## DMX Chart
Hold value for 5 seconds to activate function.

|From|To|Function|Command|
|---|---|---|---|
|0|23|No Function|-|
|24|46|Power On|\*pow=on#|
|46|69|Power Off|\*pow=off#|
|69,|92|Source VGA 1 (RGB)|\*sour=RGB#|
|92,|115|Source VGA 2 (RGB)|\*sour=RGB2#|
|115|138|Source Composite|\*sour=vid#|
|138|161|Source S-Video|\*sour=svid#|
|161|184|Audio Mute|\*mute=on#|
|184|207|Audio Unmute|\*mute=off#|
|207|230|Lampmode Normal|\*lampm=lnor#|
|230|256|Lampmode Eco|\*lampm=eco#|
