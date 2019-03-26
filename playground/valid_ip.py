
_OCTET_COUNT = 4
_HEXTET_COUNT = 8
_DECIMAL_DIGITS = frozenset('0123456789')
_HEX_DIGITS = frozenset('0123456789ABCDEFabcdef')

def is_valid_ipv4(ip_str):
    """Validates IPv4 addresses.
    """
    octets = ip_str.split('.')
    if len(octets) != _OCTET_COUNT:
	return False
    packed_ip = 0
    for oc in octets:
	try:
            octet_int = _parse_octet(oc)
            if octet_int is not None:
                packed_ip = (packed_ip << 8) | octet_int
            else:
                return False
	except ValueError:
	    return False
    return packed_ip

def _parse_octet(octet_str):
    """Convert a decimal octet into an integer.
    Args:
        octet_str: A string, the number to parse.
    Returns:
        The octet as an integer.
    """
    # Whitelist the characters, since int() allows a lot of bizarre stuff.
    if not _DECIMAL_DIGITS.issuperset(octet_str):
        print "Neither"
    octet_int = int(octet_str, 10)
    # Disallow leading zeroes, because no clear standard exists on
    # whether these should be interpreted as decimal or octal.
    if octet_int > 255 or (octet_str[0] == '0' and len(octet_str) > 1):
        return None
    return octet_int

def is_valid_ipv6(ip_str):
    """Turn an IPv6 ip_str into an integer.
    Args:
        ip_str: A string, the IPv6 ip_str.
    Returns:
        A long, the IPv6 ip_str.
    """
    parts = ip_str.split(':')
    # An IPv6 address needs at least 2 colons (3 parts).
    if len(parts) < 3:
        return False
    # If the address has an IPv4-style suffix, convert it to hexadecimal.
    if '.' in parts[-1]:
        ipv4_int = is_valid_ipv4(ip_str)
        if not ipv4_int:
            return False
        else:
            parts.append('%x' % ((ipv4_int >> 16) & 0xFFFF))
            parts.append('%x' % (ipv4_int & 0xFFFF))
    # An IPv6 address can't have more than 8 colons (9 parts).
    if len(parts) > _HEXTET_COUNT + 1:
        return False
    # Disregarding the endpoints, find '::' with nothing in between.
    # This indicates that a run of zeroes has been skipped.
    try:
        skip_index, = (
            [i for i in xrange(1, len(parts) - 1) if not parts[i]] or
            [None])
    except ValueError:
        # Can't have more than one '::'
        return False

    # parts_hi is the number of parts to copy from above/before the '::'
    # parts_lo is the number of parts to copy from below/after the '::'
    if skip_index is not None:
        # If we found a '::', then check if it also covers the endpoints.
        parts_hi = skip_index
        parts_lo = len(parts) - skip_index - 1
        if not parts[0]:
            parts_hi -= 1
            if parts_hi:
                return False  # ^: requires ^::
        if not parts[-1]:
            parts_lo -= 1
            if parts_lo:
                return False  # :$ requires ::$
        parts_skipped = _HEXTET_COUNT - (parts_hi + parts_lo)
        if parts_skipped < 1:
            return False
    else:
        # Otherwise, allocate the entire address to parts_hi.  The endpoints
        # could still be empty, but _parse_hextet() will check for that.
        if len(parts) != _HEXTET_COUNT:
            return False
        parts_hi = len(parts)
        parts_lo = 0
        parts_skipped = 0
    try:
        # Now, parse the hextets into a 128-bit integer.
        ip_int = long(0)
        for i in xrange(parts_hi):
            ip_int <<= 16
            hextet_int = _parse_hextet(parts[i])
            if hextet_int is not None:
                ip_int |= _parse_hextet(parts[i])
            else:
                return False
        ip_int <<= 16 * parts_skipped
        for i in xrange(-parts_lo, 0):
            ip_int <<= 16
            hextet_int = _parse_hextet(parts[i])
            if hextet_int is not None:
                ip_int |= _parse_hextet(parts[i])
            else:
                return False
        return ip_int
    except ValueError:
        return False

def _parse_hextet(hextet_str):
    """Convert an IPv6 hextet string into an integer.
    Args:
	hextet_str: A string, the number to parse.
    Returns:
	The hextet as an integer.
    """
    # Whitelist the characters, since int() allows a lot of bizarre stuff.
    if not _HEX_DIGITS.issuperset(hextet_str):
	return None
    if len(hextet_str) > 4:
      return None
    hextet_int = int(hextet_str, 16)
    if hextet_int > 0xFFFF:
	return None
    return hextet_int

if __name__ == "__main__":
    ip = str(raw_input("ip: "))
    if ip is not None:
        if ":" in ip:
            #assuming this is for ipv6 validation..
            if not is_valid_ipv6(ip):
                print "Neither"
            else:
                print "IPv6"
        else:
            #assuming this is for ipv4 validation..
            if not is_valid_ipv4(ip):
                print "Neither"
            else:
                print "IPv4"
    else:
        print "Invalid Input"
