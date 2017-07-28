#!/bin/bash

echo
echo "Homebridge install script for Hassbian"
echo

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run with sudo. Use \"sudo ${0} ${*}\"" 1>&2
   exit 1
fi

echo "Running apt-get preparation"
apt-get update
sudo apt-get install -y libavahi-compat-libdnssd-dev

echo "Getting node.js setup source"
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
sudo apt-get install -y nodejs

echo "Installing homebridge with npm"
sudo npm install -g --unsafe-perm homebridge

echo "Installing homebridge-homeassistant with npm"
sudo npm install -g homebridge-homeassistant

echo "Adding homeabridge user"
useradd --system homebridge

echo "Adding homebridge configuration directory and homeassistant config.json"
echo "Change the password n /var/lib/homebridge/config.json to match your Home Assistant password"
sudo mkdir /var/lib/homebridge
sudo cat >> /var/lib/homebridge/config.json <<'EOF'
{
    "bridge": {
        "name": "Homebridge",
        "username": "CC:22:3D:E3:CE:30",
        "port": 51826,
        "pin": "031-45-154"
    },

"platforms": [
  {
    "platform": "HomeAssistant",
    "name": "HomeAssistant",
    "host": "http://127.0.0.1",
    "password": "YOURAPIPASSWORD",
    "supported_types": ["binary_sensor", "climate", "cover", "device_tracker", "fan", "input_boolean", "light", "lock", "media_player", "scene", "sensor", "switch"],
    "logging": true
  }
]
}
EOF
sudo chown -R homebridge:homebridge /var/lib/homebridge

echo "Adding homebridge service"
sudo cat >> /etc/default/homebridge <<'EOF'
# Defaults / Configuration options for homebridge
# The following settings tells homebridge where to find the config.json file and where to persist the data (i.e. pairing and others)
HOMEBRIDGE_OPTS=-U /var/lib/homebridge

# If you uncomment the following line, homebridge will log more
# You can display this via systemd's journalctl: journalctl -f -u homebridge
# DEBUG=*
EOF

sudo cat >> /etc/systemd/system/homebridge.service <<'EOF'
[Unit]
Description=Node.js HomeKit Server
After=syslog.target network-online.target

[Service]
Type=simple
User=homebridge
EnvironmentFile=/etc/default/homebridge
# Adapt this to your specific setup (could be /usr/bin/homebridge)
# See comments below for more information
ExecStart=/usr/bin/homebridge $HOMEBRIDGE_OPTS
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target
EOF

# TODO: not sure where to put this... doesn't work here
# https://github.com/home-assistant/homebridge-homeassistant#using-with-self-signed-ssl-certificates
#export NODE_TLS_REJECT_UNAUTHORIZED=0

systemctl daemon-reload
systemctl enable homebridge
systemctl start homebridge

echo
echo "Installation done."
echo
echo "Configuration is now available at /var/lib/homebridge"
echo