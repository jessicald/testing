#!/usr/bin/env python3.2
class Tricky():
    def __init__(self, update_with):
        self.integer = 5
        self.longstring = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. Praesent et diam eget libero egestas mattis sit amet vitae augue. Nam tincidunt congue enim, ut porta lorem lacinia consectetur.'
        print('self.integer = %d' % self.integer)
        print('self.longstring = ' + self.longstring)
        print()

        # The first loop works with an iterable of 2-tuples, so if we get
        # a dictionary, convert it to an iterable of 2-tuples.
        try:
            update_with = update_with.items()
        except AttributeError:
            pass

        # ***
        # The actual trick; all the rest is setup and display.
        for key, value in update_with:
            setattr(self, key, value)
        # ***
        # The second loop works with a dictionary itself, so if we get
        # an iterable, convert it to a dictionary.
        # This is the slower method.
        #dict(update_with)
        #for key in update_with.keys():
        #    setattr(self, key, update_with[key])
        # ***


if __name__ == '__main__':
    # Testing with a dictionary.
    assimilate_these = {
            'longstring': '\uff0f\u4eba\u25d5 \u203f\u203f \u25d5\u4eba\uff3c  \uff37\uff2f\uff2e\u2019\uff34\u3000\uff39\uff2f\uff35\u3000\uff22\uff25\uff23\uff2f\uff2d\uff25\u3000\uff21\u3000\uff2d\uff21\uff27\uff29\uff23\uff21\uff2c\u3000\uff27\uff29\uff32\uff2c\uff1f',
            'shortstring': 'http://daringfireball.net/projects/markdown/',
            'integer': 10,
            'floater': 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679,
            }
    print('Passing the following to Tricky(): ' + repr(assimilate_these) + '\n')
    tricky = Tricky(assimilate_these)
    print('tricky.integer = %d' % tricky.integer)
    print('tricky.longstring = ' + tricky.longstring)
    print('tricky.shortstring = ' + tricky.shortstring)
    print('tricky.floater = %f' % tricky.floater)

# Speed tests
# Using iterable
# $ python3.2 -mtimeit -s"class Testing():" -s" def __init__(self, update_with):" -s"  for key, value in update_with:" -s"   setattr(self, key, value)" -s"fire = list({'floater': 3.141592653589793, 'integer': 10, 'shortstring': 'http://daringfireball.net/projects/markdown/', 'longstring': '／人◕ ‿‿ ◕人＼  ＷＯＮ’Ｔ\u3000ＹＯＵ\u3000ＢＥＣＯＭＥ\u3000Ａ\u3000ＭＡＧＩＣＡＬ\u3000ＧＩＲＬ？'}.items())" "tricky = Testing(fire)"
# 100000 loops, best of 3: 3.72 usec per loop
#
# Using dictionary
# $ python3.2 -mtimeit -s"class Testing():" -s" def __init__(self, update_with):" -s"  for key in update_with.keys():" -s"   setattr(self, key, update_with[key])" -s"fire = {'floater': 3.141592653589793, 'integer': 10, 'shortstring': 'http://daringfireball.net/projects/markdown/', 'longstring': '／人◕ ‿‿ ◕人＼  ＷＯＮ’Ｔ\u3000ＹＯＵ\u3000ＢＥＣＯＭＥ\u3000Ａ\u3000ＭＡＧＩＣＡＬ\u3000ＧＩＲＬ？'}" "tricky = Testing(fire)"
# 100000 loops, best of 3: 4.29 usec per loop
