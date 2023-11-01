#!/usr/bin/python3
# prints the ASCII alphabet, in reverse order, alternating lowercase
# and uppercase
sep = ""
print(sep.join(['{:c}'.format(cap - 32 if cap % 2 else cap)
               for cap in range(ord('z'), ord('a') - 1, -1)]), end="")
