import os
import time
from datetime import datetime

target = input('Target: ').strip()
tot = input('Time of test [5 seconds]: ').strip()
if tot == '':
    tot = '5'

tbt = input('Time between tests [5 minutes]: ').strip()
if tbt == '':
    tbt = '5'

now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
f = open(f'test_{target}_{now}.csv', 'a')
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
    f.write(f'{now}\t{bandwidthRx} {bandwidthRxM}\t{bandwidthTx} {bandwidthTxM}\n')
    time.sleep(int(tbt)*60)
