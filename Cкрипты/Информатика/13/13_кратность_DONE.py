import random
import ipaddress

# функция для подбора рандомного адреса сети к заданной маске
def random_network(mask):
    if '/' in mask:
        prefix = int(mask.strip('/'))
    else:
        prefix = ipaddress.IPv4Network(f'0.0.0.0/{mask}').prefixlen

    net_bits = prefix
    host_bits = 32 - net_bits

    net_int = random.getrandbits(net_bits) << host_bits
    network = ipaddress.IPv4Network((net_int, prefix))

    return str(network)

# маска
mask_bits = random.randint(18, 28)
# адрес сети
network_ip = random_network(f'/{mask_bits}').replace('/', ' ').split()[0]
# строка маски для text
mask = ipaddress.IPv4Network(f'0.0.0.0/{mask_bits}').netmask

question = random.choice([
    'Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса не кратно',
    'Сколько в этой сети IP-адресов, для которых количество единиц в двоичной записи IP-адреса кратно'
])

num = random.randint(3, 7)
question += ' ' + str(num) + '?'

text = f"""
В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая – к адресу узла в этой сети. 
Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и его маске.
Широковещательным адресом называется специализированный адрес, в котором на месте нулей в маске стоят единицы. 
Адрес сети и широковещательный адрес не могут быть использованы для адресации сетевых устройств.
Сеть задана IP-адресом {network_ip} и сетевой маской {mask}.
{question} 
""".strip()

# решение
network = ipaddress.ip_network(f'{network_ip}/{mask}', 0)
cnt = 0
for ip in network:
    b = '0' * (32 - len(bin(int(ip))[2:])) + bin(int(ip))[2:]
    if "не" in question:
        if b.count('1') % num != 0:
            cnt += 1
    else:
        if b.count('1') % num == 0:
            cnt += 1
right_answer = cnt

# текст решения
if 'не' in question:
    text_of_solve = f"""
import ipaddress

network = ipaddress.ip_network(f'{network_ip}/{mask}', 0)
cnt = 0
for ip in network:
    b = '0' * (32 - len(bin(int(ip))[2:])) + bin(int(ip))[2:]
    if b.count('1') % {num} != 0:           
        cnt += 1
print(cnt)
"""
else:
    text_of_solve = f"""
import ipaddress

network = ipaddress.ip_network(f'{network_ip}/{mask}', 0)
cnt = 0
for ip in network:
    b = '0' * (32 - len(bin(int(ip))[2:])) + bin(int(ip))[2:]
    if b.count('1') % {num} == 0:           
        cnt += 1
print(cnt)
"""

print(text)
print(f'Answer = {right_answer}')
print('___________________________')
print(text_of_solve)