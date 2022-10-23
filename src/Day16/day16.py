with open('day16.txt', 'r') as f:
    for line in f:
        hex_str = line
        res = bin(int(hex_str, 16))[2:].zfill(len(hex_str)*4)


def type4(bits):
    val = 0
    _pos = 0
    while True:
        stop_bit = bits[_pos]
        b = int(bits[_pos+1:_pos+5], 2)
        val = val * 16 + b
        _pos += 5
        if stop_bit == '0':
            break
    return val, _pos


pos = 0
sum_versions = 0
count = 0


def decode(bits):
    global pos
    global count
    global sum_versions
    if int(bits[pos:]) == 0:
        return 0, 0, len(bits) + 1
    count += 1
    print(" " * pos + "v")
    print(bits)
    print("Packet #" + str(count), "at position", pos)
    version = int(bits[pos:pos+3], 2)
    pos = pos + 3
    sum_versions += version
    packet_id = int(bits[pos:pos+3], 2)
    pos = pos + 3
    print("Version", version, "Type", packet_id)
    if packet_id == 4:
        val, _pos = type4(bits[pos:])
        pos = pos + _pos
        print("Value", val)
        return version, val, _pos
    else:
        if bits[pos] == '0':
            # length type 0 means the next 15 bits are the length in bits of the sub-packet
            length = int(bits[pos+1:pos+1+15], 2)
            print("Length", length)
            pos = pos + 16
            _len = 0
            while _len < length:
                ver, v, p = decode(bits)
                _len += p
            return version, 0, _len
        else:
            # length type 1 means the next 11 bits are the number of sub-packets
            num_sub_packets = int(bits[pos+1:pos+1+11], 2)
            print("Number of sub-packets", num_sub_packets)
            pos = pos + 12
            for i in range(num_sub_packets):
                decode(bits)
            return version, 0, 0


decode(res)
print("Sum of versions:", sum_versions)
