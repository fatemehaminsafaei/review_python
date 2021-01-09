"""Packing and Unpacking
In packing, we place value into a new tuple while
in unpacking we extract those values back into variables."""
import binascii
import struct
from random import random
from oauthlib import common
from python.String_cases import string

x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
# print(company)
# print(emp)
# print(profile)


def cmh_autotune(self, module, message, additional_data, cm):
    message = message[len(self.CONTROL_AUTOTUNE) + 2:]
    # get tune type, requested record type, length and encoding for crafting the answer
    (query_type, RRtype, length, encode_class) = struct.unpack("<BHHH", message[0:7])
    if self.DNS_proto.get_RR_type(RRtype)[0] == None:
        return True

    # extra parameters added to be able to response in the proper way
    additional_data = additional_data + (
    True, self.download_encoding_list[encode_class], self.DNS_proto.get_RR_type(RRtype)[0])
    if (query_type == 0) or (query_type == 3):
        # record && downstream length discovery
        message = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    if query_type == 1:
        # A record name length discovery
        message = struct.pack("<i", binascii.crc32(message[7:]))
    if query_type == 2:
        # checking download encoding, echoing back request payload
        message = message[7:]

    module.send(common.CONTROL_CHANNEL_BYTE, self.CONTROL_AUTOTUNE_CLIENT + message, additional_data)
    return True