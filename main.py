import math

def get_subnet_info(num_subnets, subnet_mask):
    max_subnets = 2(32-subnet_mask)
    if num_subnets > max_subnets:
        raise ValueError(f"Maske {subnet_mask} kann höchstens {max_subnets} Subnetze. {num_subnets} braucht man.")
    bits_to_borrow = int(round(math.log2(num_subnets)))
    new_mask = subnet_mask + bits_to_borrow
    hosts_per_subnet = 2(32-new_mask) - 2
    return new_mask, hosts_per_subnet

num_subnets = int(input("Wie viele Subnetze benötigen sie: "))
subnet_mask = int(input("Aktuelle Subnetzmaske in Bits: "))

try:
    new_mask, hosts_per_subnet = get_subnet_info(num_subnets, subnet_mask)
    print("Neue Subnetzmaske: /{}".format(new_mask))
    print("Mögliche Hosts pro Netzwerk: {}".format(hosts_per_subnet))
except ValueError as error:
    print("Fehler: {}".format(error))