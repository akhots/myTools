#!/usr/bin/env python3

import os
import time
from datetime import datetime

target = input('Target: ').strip()
# --- input ---
tot = input('Time of test [5 seconds]: ').strip()
# --- input ---
if tot == '':
    tot = '5'

tbt = input('Time between tests [5 minutes]: ').strip()
# --- input ---
if tbt == '':
    tbt = '5'

nowM = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

with open(f'test_{target}_{nowM}.csv', 'a') as f:
    f.write(f'\tTarget - {target}\n\
    \tTime of test in each direction - {tot} seconds\n\
    \tTime between tests - {tbt} minutes\n\n')
    f.write('Datetime\tBandwidth receive\tBandwidth send\n')


print('\nDatetime                Bandwidth receive    Bandwidth send')

while True:
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    print(f'{now}', end='')
    resRx = os.popen(f'iperf3 -c {target} -t{tot} -R').read()
    resRx = resRx.split('\n')
    resRx = resRx[-4].split()
    bandwidthRx = resRx[-3]
    bandwidthRxM = resRx[-2]
    transferRx = resRx[-5]
    transferRxM = resRx[-4]
    print(f'{bandwidthRx:>10} {bandwidthRxM:<10}', end='')
    resTx = os.popen(f'iperf3 -c {target} -t{tot}').read()
    resTx = resTx.split('\n')
    resTx = resTx[-4].split()
    bandwidthTx = resTx[-3]
    bandwidthTxM = resTx[-2]
    transferTx = resTx[-5]
    transferTxM = resTx[-4]
    print(f'{bandwidthTx:>10} {bandwidthTxM:<10}')
    with open(f'test_{target}_{nowM}.csv', 'a') as f:
        f.write(f'{now}\t{bandwidthRx} {bandwidthRxM}\t{bandwidthTx} {bandwidthTxM}\n')
    time.sleep(int(tbt)*60)

