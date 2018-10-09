from NetworkUtil import NetworkUtility

network = NetworkUtility()

print (network.count_usable_address("203.189.120.0", 24))

print (network.get_network_address_byslash("10.0.0.67", 26))

print (network.get_broadcast_address_byslash("10.0.0.67", 26))

print (network.get_slash_by_subnet("255.255.255.0"))
