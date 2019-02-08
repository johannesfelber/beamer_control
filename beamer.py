# Beamer Control
import config
import time
from ola.ClientWrapper import ClientWrapper
import serial
import threading
import signal

class Job(threading.Thread):
    def __init__(self,*args):
        threading.Thread.__init__(self)
        self.args = args
        self.shutdown_flag = threading.Event()
    
    def run(self):
        firstUpdate = time.time()
        global ser

        # wait for 5 seconds
        while not self.shutdown_flag.is_set() and firstUpdate + 5 > time.time():
            time.sleep(0.5)

        if not self.shutdown_flag.is_set():
            print('Executing command %s' % self.args[0])
            ser.write('\r%s\r' % self.args[0])

lastValue = 0
j = None
address = config.ola['address'] - 1
ser = serial.Serial(
    port=config.serial['port'],
    baudrate = config.serial['baudrate'],
    parity=config.serial['parity'],
    stopbits=config.serial['stopbits'],
    bytesize=config.serial['bytesize'],
    timeout=1
)

class ServiceExit(Exception):
    pass
 
def service_shutdown(signum, frame):
    print('Received signal %d\nShutting down ...' % signum)
    raise ServiceExit

def getCommand(value):
    for key in config.presets:
        if value in key:
            return config.presets[key]
    return 'nothing'

def NewData(data):
    global j
    global lastValue
    global address
    command = getCommand(data[address])
    if command != lastValue:
        if j is not None:
            j.shutdown_flag.set()
            j.join()
        if command != 'nothing':
            j = Job(command)
            j.start()
        lastValue = command

def main():
    global j
    signal.signal(signal.SIGTERM, service_shutdown)
    signal.signal(signal.SIGINT, service_shutdown)
    try:
        wrapper = ClientWrapper()
        client = wrapper.Client()
        client.RegisterUniverse(config.ola['universe'], client.REGISTER, NewData)
        print('Listening on universe %d at address %d' % (config.ola['universe'], config.ola['address']))
        wrapper.Run()

    except ServiceExit:
        if j is not None:
            j.shutdown_flag.set()
            j.join()

if __name__ == '__main__':
    main()