Proxy server for IoT devices.
=========================

# Requirements

- flask
- pyyaml

# Quickstart
1. Install libraries with pip, i.e. `pip install flask`
1. Copy `default.settings.yaml` to `settings.yaml`
1. Open `settings.yaml` and add your devices

## Start with Docker (on RPi)
1. `docker build -t local/iot-proxy`
1. Copy `default.settings.yaml` to `settings.yaml`
1. Open `settings.yaml` and add your devices
1. `docker run -dP --volume $(pwd)/settings.yaml:/var/www/html/settings.yaml local/iot-proxy`

# Status
proof of concept
