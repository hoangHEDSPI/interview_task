# class struct_like_c(object):
#     __slots__ = ['fo', 'numberofso']
    
def firstNotRepeatingCharacter(s):
   b = []
   c = []
   ans = ''
   for i in range(26):
      b.append(0)
      c.append(0)
   for i in range(len(s)):
      b[ord(s[i])-97] += 1
      c[ord(s[i])-97] = i
   a = b.count(1)
   if a==0:
      ans='_'
   elif a==1:
      for i in range(26):
         if b[i] == 1:
            ans = chr(i+97)
   elif a > 1:
      m = 26
      for i in range(26):
         if b[i] == 1:
            m = min(m, c[i])
      for i in range(26):
         if c[i] == m:
            ans = chr(i+97)
   return ans