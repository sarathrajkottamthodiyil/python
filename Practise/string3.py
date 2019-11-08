s =  "strings are awesome!"
print("length of s = %d" % len(s))
print("the first occurrence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))
print("the first five characters are '%s'" % s[:5])
print("the next five characters are '%s'" % s[5:10])
print("the thirteenth character is'%s'" % s[12])
print("the character with odd index are '%s'" % s[1::2])
print("the last five characters are '%s'" % s[-5:])