import socket
import struct
import time
import random

class CAT240Simulator:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 4433
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.azimuth = 0
        self.counter = 0

    # CORRECTED FSPEC
    def fspec(self):
        # 0xE7 = 1110 0111 -> Bits 1, 2, 3, 6, 7 are ON (plus FX bit 8)
        # 0x50 = 0101 0000 -> Bits 10 and 12 are ON
        return struct.pack("!BB", 0xE7, 0x50)

    # FRN 1: I240/010 Data Source
    def data_source_id(self):
        return struct.pack("!BB", 1, 1)

    # FRN 2: I240/000 Message Type
    def message_type(self):
        return struct.pack("!B", 2)

    # FRN 3: I240/020 Video Record Header
    def video_record_header(self):
        self.counter += 1
        return struct.pack("!I", self.counter)

    # FRN 6: I240/041 Video Header Femto (Provides start/end Azimuth)
    def video_header_femto(self):
        start_az = int((self.azimuth / 360.0) * 65535)
        end_az   = int(((self.azimuth + 1) / 360.0) * 65535)
        return struct.pack("!HHII", start_az, end_az, 0, 1000)

    # FRN 7: I240/049 Counters
    def counters(self):
        return struct.pack("!BI", 1, self.counter)

    # FRN 10: I240/051 Video Block Medium (🔥 SHIPS MOVED HERE)
    def video_block_medium(self):
        cells = 256
        # 🌊 Sea clutter
        data = [random.randint(10, 40) for _ in range(cells)]

        # 🚢 Ships (azimuth, range)
        ships = [(90, 120), (150, 80), (220, 160)]
        for az, rng in ships:
            if abs(self.azimuth - az) < 2:
                for i in range(-5, 6):
                    idx = rng + i
                    if 0 <= idx < cells:
                        data[idx] = random.randint(200, 255)

        # 🏝 Coastline
        for i in range(200, 230):
            data[i] = random.randint(150, 200)

        blocks = 1
        # Standard ASTERIX block: 1 byte REP (number of blocks) + raw cell data
        return struct.pack("!B", blocks) + bytes(data)

    # FRN 12: I240/140 Time of Day
    def time_of_day(self):
        now = time.time() % 86400
        tod = int(now * 128)
        return struct.pack("!I", tod)[1:]

    # Build Packet
    def build_packet(self):
        data = b''
        # THE APPEND ORDER MUST EXACTLY MATCH THE FSPEC BITS
        data += self.data_source_id()       # Bit 1
        data += self.message_type()         # Bit 2
        data += self.video_record_header()  # Bit 3
        data += self.video_header_femto()   # Bit 6
        data += self.counters()             # Bit 7
        data += self.video_block_medium()   # Bit 10
        data += self.time_of_day()          # Bit 12

        fspec = self.fspec()
        length = 3 + len(fspec) + len(data)
        header = struct.pack("!B H", 240, length)

        return header + fspec + data

    def run(self):
        print("Sending Corrected Marine Radar CAT240...")
        while True:
            pkt = self.build_packet()
            self.sock.sendto(pkt, (self.ip, self.port))
            self.azimuth = (self.azimuth + 1) % 360
            time.sleep(0.05)

if __name__ == "__main__":
    sim = CAT240Simulator()
    sim.run()