from sys import argv, exit
from struct import unpack, pack
from binascii import hexlify

if len(argv) != 2:
  print 'Usage: python', argv[0], '<fontfile>'
  exit()

fontfile = argv[1]
fp = open(fontfile, 'rb')

def ulong(offset):
  fp.seek(offset)
  buf = fp.read(4)
  buf = unpack('>I', buf)[0]
  return buf

def ushort(offset):
  fp.seek(offset)
  buf = fp.read(2)
  buf = unpack('>H', buf)[0]
  return buf

def version(buf):
  buf = pack('>I', buf)
  buf = hexlify(buf)
  buf = '0x' + buf
  return buf

def id(buf):
  buf = pack('>I', buf)
  return buf
  
# Offset Table
sfntVersion = version(ulong(0))
numTables = ushort(4)
searchRange = ushort(6)
entrySelector = ushort(8)
rangeShift = ushort(10)

# Table Record
tag = id(ulong(0xc))
checkSum = ulong(0x10)
offset = ulong(0x14)
length = ulong(0x18)

print '[+] Offset Table'
print '  [-] sfntVersion      :', sfntVersion
print '  [-] Number of tables :', numTables
print '  [-] searchRange      :', searchRange
print '  [-] entrySelector    :', entrySelector
print '  [-] rangeShift       :', rangeShift

print '[+] Table Record'
print '  [-] Tag      :', tag
print '  [-] CheckSum :', checkSum
print '  [-] Offset   :', hex(offset)
print '  [-] Length   :', hex(length)
