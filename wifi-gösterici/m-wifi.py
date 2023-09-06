#!/usr/bin/env python3
#*- coding: utf-8 -*--
#Coded by Morbius.os

AUTHOR = 'Morbius.os'
GİTHUB = 'https://github.com/morbius-os'
INSTAGRAM= '@morbius.os'

Mor = '\033[95m'
Cyan = '\033[96m'
KoyuMavi = '\033[1;34m'
Mavi = '\033[94m'
Yeşil = '\033[92m'
Sarı = '\033[93m'
Kırmızı = '\033[91m'
Kalın = '\033[1m'
AltıÇizili = '\033[4m'
Bitir = '\033[0m'
Beyaz ='\033[1;37m'

import os
import subprocess

result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [line.split(':')[1][1:-1] for line in result if "All User Profile" in line]

for profile in profiles:
    try:
        password_result = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
        password = [line.split(':')[1][1:-1] for line in password_result if "Key Content" in line][0]
        print(f"{Beyaz}WiFi Ağı: {Yeşil}{profile}{Beyaz}{Kalın} |{Bitir} Şifre: {Yeşil}{password}{Beyaz}")
    except IndexError:
        print(f"{Beyaz}WiFi Ağı: {Yeşil}{profile}{Beyaz}, Şifre: {Yeşil}Bulunamadı{Beyaz}")
