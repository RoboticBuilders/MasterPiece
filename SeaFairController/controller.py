import spikerfcomm
repl = SpikePrimeREPL('A8:E2:C1:9B:12:C3') # Replace with BT Address of your own hub.
print("According to Robot Inventor, 1+1=", repl.run("print(1+1)"))

# This Library estabilishes an RFCOMM socket over Bluetooth classic with
# a SPIKE Prime or MINDSTORMS Robot Inventor hub.
# You can either read the telemetry using SpikePrimeStreamReader
# ...or send micropython commands over raw REPL using SpikePrimeREPL

# Author: Anton's Mindstorms
# Based on this PyBricks bt code: https://github.com/pybricks/pybricks-projects

from uctypes import addressof, sizeof
from uctypes import struct as cstruct
from usocket import socket, SOCK_STREAM

from _thread import start_new_thread

from pybricks.bluetooth import (
    str2ba,
    sockaddr_rc,
    AF_BLUETOOTH,
    BTPROTO_RFCOMM
)
from pybricks.tools import wait, StopWatch

# Robot Inventor does not capitalize bools :/
true=True
false=False

def get_bluetooth_rfcomm_socket(address, channel):
    # Create an empty byte array to fit a struct as defined in the sockaddr_rc dictionary
    addr_data = bytearray(sizeof(sockaddr_rc))
    # Create c structure with the fields as in sockaddr, at the address of the empty array
    addr = cstruct(addressof(addr_data), sockaddr_rc)
    # Fill the rc_famiy field
    addr.rc_family = AF_BLUETOOTH
    # Fill the rc_bdaddr field with a string to bt address converson
    str2ba(address, addr.rc_bdaddr)
    # Fill the channel field.
    addr.rc_channel = channel
    # New socket
    sock = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM)
    # Connect the socket to the newly created address in memort
    sock.connect(addr_data)
    return sock


class SpikePrimeREPL():
    def __init__(self, address, debug=True):
        self.DEBUG=debug
        try:
            self.sock = get_bluetooth_rfcomm_socket(address, 1)
        except OSError as e:
            print("Turn on Bluetooth on the EV3 and on SPIKE.")
            raise e

        watch = StopWatch()
        while watch.time() < 2000:
            data = self.sock.recv(1024)
            if data is not None:
                break
            wait(100)
        if not data:
            print("Error: no data")

        self.sock.send(b'\x03')
        wait(100)
        self.sock.send(b'\x01')
        data = self.sock.recv(1024)
        if not data[-14:] == b'L-B to exit\r\n>':
            print("Raw REPL failed (response: %r)" % data)

       

    def run(self, command, reply=True, raw_paste=False):
        command_bytes_left = bytes(command, "utf-8")
        window = 128

        if raw_paste:
            self.sock.send(b"\x05A\x01") # Try raw paste
            result = self.sock.recv(2)
            if self.DEBUG: print(result)
            if result == b'R\x01':
                raw_paste = True
                result = self.sock.recv(3) # Should be b'x80\x00\x01' where \x80 is the window size
                window = result[0]
            else:
                raw_paste = False
                self.flush()

        # if platform==SPIKE:
        #     window = 32

        while len(command_bytes_left) > window:
            self.sock.send(command_bytes_left[:window]) # Write our MicroPython command and ctrl-D to execute
            sleep_ms(4)
            result = self.sock.recv(1)
            command_bytes_left = command_bytes_left[window:]
        self.sock.send(command_bytes_left+b'\x04')

        if raw_paste:
            data = self.sock.recv(1)
            if data != b'\x04':
                print("could not exec command (response: %r)" % data)
        else:
            wait(10)
            # check if we could exec command
            data = self.sock.recv(2)
            if data != b"OK":
                print("could not exec command (response: %r)" % data)

        if reply:
            result = b""
            decoded = []
            while not len(decoded) >= 3: # We need at least 3x'\x04'
                result += self.sock.recv(1024)
                decoded = result.decode("utf-8").split("\x04")
            try:
                value, error, _ = decoded # The last 5 bytes are b'\r\n\x04\x04>' Between the \x04's there can be an exception.
            except:
                print("Unexpected answer from repl: {}".format(result))
            if error:
                if self.DEBUG: print(error)
                return error.strip() # using strip() to remove \r\n at the end.
            elif value:
                return value.strip()
            else:
                return

    def exit(self):
        self.sock.send(b"\x02") # Ctrl-B

class SpikePrimeStreamReader():
    def __init__(self, address):

        try:
            self.sock = get_bluetooth_rfcomm_socket(address, 1)
        except OSError as e:
            print("Turn on Bluetooth on the EV3 and on SPIKE.")
            raise e

        self._values = None

        start_new_thread(self.reader, ())

        watch = StopWatch()
        while watch.time() < 2000:
            if self.values() is not None:
                return
            wait(100)
        raise OSError("No data received")

    def disconnect(self):
        self.sock.close()

    def reader(self):
        while True:
            try:
                raw = self.sock.recv(1024)
            except OSError:
                break
            try:
                # print(raw)
                data = eval(raw)
                if data['m'] == 0:
                    self._values = data['p']
            except (SyntaxError, KeyError):
                pass

    def values(self):
        return self._values

    def device(self, port):
        if 'A' <= port <= 'F':
            return self.values()[ord(port)-ord('A')][1]
        else:
            raise ValueError

    def acceleration(self):
        return self.values()[6]

    def gyro(self):
        return self.values()[7]

    def orientation(self):
        return self.values()[8]