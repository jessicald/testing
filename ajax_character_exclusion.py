""" A script for calculating the string needed by urllib.quote()'s 'safe' for Google's AJAX HTML snapshots.
https://developers.google.com/webmasters/ajax-crawling/docs/specification
Section: Escaping characters in the bidirectional mapping

See https://github.com/colons/pyfoot-plugins/blob/master/http.py ajax_url() for its use in context.

"""

# Note: range(0,10) == [0,1,2,3,4,5,6,7,8,9], so all ranges are one over the spec's.

# The characters required by Google's AJAX URL parsing to be escaped in the _escaped_fragment_.
escaped = range(0x00,0x21) + [0x23,0x25,0x26,0x2B] + range(0x7F,0x100)
# The characters urllib.quote() never escapes: 0-9, A-Z, a-z, -._ (in order below)
alphanum = range(0x30, 0x3A) + range(0x41, 0x5B) + range(0x61, 0x7B) + [0x2D, 0x2E, 0x5F]
# The list of all characters in the first byte of UTF-8 (and by technical exclusion, ASCII).
allchar = range(0x00,0x100)

# The combined set of escaped characters and characters never escaped (both of which are not needed in the 'safe' parameter).
# set() ensures there are no duplicates.
unsafechar = set(escaped + alphanum)

# A list of proper ASCII characters that are considered by Google to not need escaping.
safechar = [chr(x) for x in allchar if x not in unsafechar]
# Finally, the string that can be pasted into urllib.quote() 'safe'.
print repr(''.join(safechar))
