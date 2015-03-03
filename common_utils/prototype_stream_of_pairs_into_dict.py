amember_keys = ['Username', 'Date', 'Status', 'provider.cnbc', 'provider.xfinity']
amember_values = ['testuser', '6/11/2014', 'active', '1234567890', 'asdfhagsdfah']

from itertools import izip
print dict(izip(amember_keys, amember_values))


