import sys

#ch = sys.stdin.buffer.read(1)
def mailbox_gen():
  while True:
    len_bin = sys.stdin.buffer.read(4)
    if len(len_bin) != 4: return None
    (length,) = struct.unpack('!I',len_bin)
    yield decode(sys.stdin.buffer.read(length))
mailbox_gen()
