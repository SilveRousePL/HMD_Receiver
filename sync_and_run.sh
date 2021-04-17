#!/bin/bash

IP=192.168.1.100

ssh pi@${IP} 'sudo rm -rf HMD_Receiver && mkdir HMD_Receiver'
scp -r * pi@${IP}:~/HMD_Receiver/
ssh pi@${IP} -t 'sudo ./HMD_Receiver/src/main.py'
