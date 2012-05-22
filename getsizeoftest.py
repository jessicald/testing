from sys import getsizeof
from random import choice

user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
    ]
agentkey = 'User-Agent'
agent = choice(user_agents)

print '#'
print "# Calculates the number of bytes used by various structures containing:\n# Key: '%s' ; Value: '%s'\n# \n# Keeps a running total of usage.\n# " % (agentkey, agent)
print '# For reference, the baselines in bytes are:'
print "# '' = %d" % getsizeof('')
print "# u'' = %d" % getsizeof(u'')
print '# () = %d' % getsizeof(())
print '# [] = %d' % getsizeof([])
print '# {} = %d' % getsizeof({})
print "#\n# Note: The number returned by getsizeof() for lists, tuples, and dicts only shows the memory\n# taken by the structure, not its contents; this is the reason for a running total. For example:\n# "
print "# >>> getsizeof(('key', 'value')) == getsizeof(('longer', 'strings'))\n# True\n# >>> getsizeof(('key', 'value')) == getsizeof(('key', 'value', 'anotherkey'))\n# False\n# >>> getsizeof([('key', 'value')]) == getsizeof([('key', 'value', 'anotherkey')])\n# True\n#\n"


print "string: '%s'" % agentkey
sizeof_agentkey =  getsizeof(agentkey)
print "%d bytes\n" % sizeof_agentkey

print "string: '%s'" % agent
sizeof_agent =  getsizeof(agent)
print "%d bytes\n" % sizeof_agent

print "Running total"
sizeof_strings = sizeof_all = sizeof_agentkey + sizeof_agent
print "%d bytes\n" % sizeof_all

print "2-tuple of strings: ('%s', '%s')" % (agentkey, agent)
sizeof_tuple = getsizeof((agentkey, agent))
print "%d bytes\n" % sizeof_tuple

print "Running total"
sizeof_all += sizeof_tuple
print "%d bytes\n" % sizeof_all

print "List of one tuple: [('%s', '%s')]" % (agentkey, agent)
sizeof_list = getsizeof([(agentkey, agent)])
print "%d bytes\n" % sizeof_list

print "Running total"
sizeof_all += sizeof_list
print "%d bytes\n\n\n" % sizeof_all

print "Dictionary created from one list of one tuple of strings: dict([('%s', '%s')])" % (agentkey, agent)
dict1 = dict([(agentkey, agent)])
sizeof_dict1 = getsizeof(dict1)
print 'Result: %s' % repr(dict1)
print "%d bytes\n" % sizeof_dict1

print "Total"
print "%d bytes\n" % (sizeof_all + sizeof_dict1)

print "Dictionary created from one list of two tuples of strings: dict([('%s', '%s'), ('%s', '%s')])" % (agentkey, agent, agent, agentkey)
dict2 = dict([(agentkey, agent), (agent, agentkey)])
sizeof_dict2 = getsizeof(dict2)
print 'Result: %s' % repr(dict2)
print "%d bytes\n" % sizeof_dict2

print "Total"
print "%d bytes\n\n\n" % ((sizeof_strings + sizeof_tuple)*2 + sizeof_list + sizeof_dict2)


print "Bonus:"
big_list = lambda x: [(n, 0) for n in xrange(x)]
print "Size of list of 15461 2-tuples of ints:"
print "%f MiB" % (float((getsizeof(15461) + getsizeof(0) + getsizeof((15460, 0)))*15461 + getsizeof(big_list(15461))) / 1024**2)
print "Size of list of 15462 2-tuples of ints:"
print "%f MiB" % (float((getsizeof(15462) + getsizeof(0) + getsizeof((15461, 0)))*15462 + getsizeof(big_list(15462))) / 1024**2)
print "Size of dict of list of 15461 2-tuples of ints:"
print "%f MiB" % (float((getsizeof(15461) + getsizeof(0) + getsizeof((15460, 0)))*15461 + getsizeof(big_list(15461)) + getsizeof(dict(big_list(15461)))) / 1024**2)
print "Size of dict of list of 15462 2-tuples of ints:"
print "%f MiB" % (float((getsizeof(15462) + getsizeof(0) + getsizeof((15461, 0)))*15462 + getsizeof(big_list(15462)) + getsizeof(dict(big_list(15461)))) / 1024**2)
