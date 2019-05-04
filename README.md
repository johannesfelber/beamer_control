# Beamer Control
A small python script for Raspberry Pi to control a projector via RS232 over sACN (E1.31) or Art-Net.

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
