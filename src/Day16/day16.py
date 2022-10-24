import math

with open('day16.txt', 'r') as f:
    for line in f:
        hex_str = line
        res = bin(int(hex_str, 16))[2:].zfill(len(hex_str)*4)


MAX_LEN = len(res) + 1
packet_id_dic = {
    0: "SUM",
    1: "PRODUCT",
    2: "MIN",
    3: "MAX",
    5: "GT",
    6: "LT",
    7: "EQ"
}


def type4(bits):
    type_4_val = 0
    _pos = 0
    while True:
        stop_bit = bits[_pos]
        b = int(bits[_pos+1:_pos+5], 2)
        type_4_val = type_4_val * 16 + b
        _pos += 5
        if stop_bit == '0':
            break
    return type_4_val, _pos


pos = 0
sum_versions = 0
count = 0


def decode(bits, gap=""):
    global pos
    global count
    global sum_versions
    count += 1
    print(gap, " " * pos + "v")
    print(gap, bits)
    print(gap, "Packet #" + str(count), "at position", pos)
    version = int(bits[pos:pos+3], 2)
    pos = pos + 3
    sum_versions += version
    packet_id = int(bits[pos:pos+3], 2)
    pos = pos + 3
    print(gap, "Version", version, "Type", packet_id)
    if packet_id == 4:
        value, _pos = type4(bits[pos:])
        pos = pos + _pos
        print(gap, "Value", value)
        return value
    else:
        series = []
        _len = 0
        if bits[pos] == '0':
            # length type 0 means the next 15 bits are the length in bits of the sub-packet
            length = int(bits[pos+1:pos+1+15], 2)
            print(gap, "Length", length)
            pos = pos + 16
            start_pos = pos
            while pos - start_pos < length:
                series.append(decode(bits, gap + "  "))
        else:
            # length type 1 means the next 11 bits are the number of sub-packets
            num_sub_packets = int(bits[pos+1:pos+1+11], 2)
            print(gap, "Number of sub-packets", num_sub_packets)
            pos = pos + 12
            for i in range(num_sub_packets):
                series.append(decode(bits, gap + "  "))
        value = 0
        match packet_id:
            case 0:
                value = sum(series)
            case 1:
                value = math.prod(series)
            case 2:
                value = min(series)
            case 3:
                value = max(series)
            case 5:
                if (len(series)) != 2:
                    raise Exception("Number of arguments is not 2", packet_id, series)
                value = 1 if series[0] > series[1] else 0
            case 6:
                if (len(series)) != 2:
                    raise Exception("Number of arguments is not 2", packet_id, series)
                value = 1 if series[0] < series[1] else 0
            case 7:
                if (len(series)) != 2:
                    raise Exception("Number of arguments is not 2", packet_id, series)
                value = 1 if series[0] == series[1] else 0
        print(gap, packet_id_dic.get(packet_id), series, "=", value)
        return value


val = decode(res)
print("Sum of versions:", sum_versions)
print("Value:", val)
