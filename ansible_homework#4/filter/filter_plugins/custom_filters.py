#!/usr/bin/python
import re

from ansible.errors import (
    AnsibleFilterTypeError
)

def mac_filter(mac):
    '''
        split string into list of strings with particular separator
    '''
    if not isinstance(mac, str):
        raise AnsibleFilterTypeError("String type is expected "
                                     "got type %s instead" % type(mac))
    
    if len(mac) != 12:
        raise AnsibleFilterTypeError("MAC address must be 12-character, you entered: %s" % len(mac))
    
    if not re.match("[0-9A-Fa-f]{12}$", mac):
         raise AnsibleFilterTypeError("Invalid MAC address format, you entered: %s" % mac)
                                     

    return (mac[0:2] + ':' + mac[2:4] + ':' + mac[4:6] + ':' + mac[6:8] + ':' + mac[8:10] + ':' + mac[10:12]).upper()

class FilterModule(object):
    def filters(self):
        return {
            'mac_filter': mac_filter
        }
