#!/bin/bash

jack_control start
jack_control ds alsa
jack_control dps device hw:PCH0
jack_control dps rate 48000
jack_control dps nperiods 2
jack_control dps period 1024
sleep 10
