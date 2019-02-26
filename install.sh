# Install script for beamer_control
# Author: Johannes Felber www.johannes-felber.at

# Copy files to /opt/beamer_control
mkdir /opt/beamer_control
cp beamer.py config.py /opt/beamer_control/

# Install Service
sed -i '/^exit 0/i \
\#beamer_control autostart\
/usr/bin/python /opt/beamer_control/beamer.py &' /etc/rc.local
