#!/usr/bin/python

"""Convert all of your Viscosity connections into OVPN configuration files for OpenVPN
https://gist.github.com/ishahid/693c2c97b3236a3c2416fc09ab170244
"""


import re
import glob
from os.path import expanduser, dirname

home = expanduser('~')
config_files = glob.glob('%s/Library/Application Support/Viscosity/OpenVPN/*/config.conf' % home)

for file in config_files:
    certificate_files = ['ca', 'cert', 'key', 'tls-auth']
    config_dir        = dirname(file)
    connection_name   = None
    new_config        = list()

    f = open(file, 'r')
    for line in f:
        line = line.strip()

        if line.startswith('#viscosity name'):
            connection_name = re.split('#viscosity name (.*)', line)[1]
            continue

        if line.startswith('#'):
            continue

        try:
            key, value = line.split(' ', 1)

        except:
            key, value = line, ''

        if key in certificate_files:
            # Special case for tls-auth which is "key direction"
            if key == 'tls-auth':
                # add direction to config
                value, direction = value.split(' ')
                if direction: new_config.append('key-direction %s' % direction)

            cf = open('%s/%s' % (config_dir, value), 'r')
            certificate = cf.read()
            new_config.append('<%s>' % key)
            new_config.append(certificate)
            new_config.append('</%s>' % key)
            continue

        new_config.append(line)

    if not connection_name:
        print "Unable to find connection name in #{file}. Aborting."
        exit(1)

    new_config.insert(0, '# OpenVPN Config for %s' % connection_name)
    out_file = '%s.ovpn' % connection_name
    of = open(out_file, 'w')
    of.write('\n'.join(new_config) + '\n')
    print 'wrote %s' % out_file
