# Beamer Control
A small python script for Raspberry Pi to control a BenQ projector via RS232 over sACN (E1.31) or Art-Net (or any other OLA input).
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
5. Reboot `sudo ./install.sh`
6. Add input device to OLA via web interface: http://ip:9090

Beamer control will be startet automatically after sytem boot.

## Configuration
The configuration stored in */opt/beamer_control/config.py*

### Address and universe

Per default beamer control listens on universe 1 at address 1. Update `address` and `universe` in dict `ola` according to your requirements

### Serial settings
The serial settings can be updated in dict `serial`. The default values are used by BenQ projectors

### Commands
All commands are customizable. Just update `presets` according to your needs. `xrange(n, m)` defines the dmx values for this preset, the value is a string, which is sent to the projector. The predefined values work with most BenQ projectors.
