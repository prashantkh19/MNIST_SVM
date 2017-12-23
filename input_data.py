import binascii


# Input Images
def get_images(filename, bol=False, length=10000):
    # Parameters -
    #  1. filename - FORMAT: filepath/filename
    #  2. bol - (default -False)-- get images for full length or not
    #  3. length of input images (default=10000)
    length = length*784
    with open(filename,'rb') as f:
        byte_=f.read()
        i = 16
        data = []
        while True:
            byte = byte_[i:i+1]
            if len(byte) == 0:
                break
            if i == length+16 and bol==False:
                break
            val = int.from_bytes(byte,byteorder='big', signed=False)
            data.append(val/255)
            i=i+1
    return data


# Input Lables
def get_labels(filename):
    # Parameters -
    #  1. filename - FORMAT: filepath/filename
    with open(filename,'rb') as f:
        byte_=f.read()
        i = 8
        data = []
        while True:
            byte = byte_[i:i+1]
            if len(byte) == 0:
                break
            hexadecimal = binascii.hexlify(byte)
            decimal = int(hexadecimal, 16)
            data.append(decimal)
            i = i+1
    return data
