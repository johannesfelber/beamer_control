# Install script for beamer_control
# Author: Johannes Felber www.johannes-felber.at

# Install dependencies
sudo apt update
sudo apt install ola-python

# Copy files to /opt/beamer_control
mkdir /opt/beamer_control
cp beamer.py config.py /opt/beamer_control/

# Install Service
sed -i '/^exit 0/i \
\#beamer_control autostart\
printf "Starting Beamer Control ..."\
/usr/bin/python /opt/beamer_control/beamer.py &' /etc/rc.local
