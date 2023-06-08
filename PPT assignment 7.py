#!/usr/bin/env python
# coding: utf-8

# In[1]:


#answer 1

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        if s[i] in s_to_t:
            if s_to_t[s[i]] != t[i]:
                return False
        else:
            s_to_t[s[i]] = t[i]

        if t[i] in t_to_s:
            if t_to_s[t[i]] != s[i]:
                return False
        else:
            t_to_s[t[i]] = s[i]

    return True


# In[2]:


s = "egg"
t = "add"
print(isIsomorphic(s, t))


# In[3]:


#answer 2

def isStrobogrammatic(num):
    left = 0
    right = len(num) - 1
    mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

    while left <= right:
        left_digit = num[left]
        right_digit = num[right]

        if left_digit not in mapping or mapping[left_digit] != right_digit:
            return False

        left += 1
        right -= 1

    return True


# In[5]:


num = "69"
print(isStrobogrammatic(num))


# In[14]:


#Answer3


def addstring(num1, num2):
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = ""
    
    while i >= 0 or j >= 0 or carry > 0:
        x = num1[i] if i >= 0 else '0'
        y = num2[j] if j >= 0 else '0'
        digitsum = int(x) + int(y) + carry 
        currentDigit = digitsum % 10
        result = str(currentDigit) + result
        carry = digitsum // 10
        i -= 1
        j -= 1
        
    if carry > 0:
        result = str(carry) + result
        
    return result


# In[15]:


num1 = "11"
num2 = "123"
print(addstring(num1, num2))


# In[16]:


#Answer 4

def reverseWords(s):
    words = s.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)


# In[17]:


s = "let's take Leetcode contest"
print(reverseWords(s))


# In[18]:


#Answer 5

def reverseStr(s, k):
    result = ""

    for i in range(0, len(s), 2 * k):
        chunk = s[i:i + 2 * k]
        reversed_chunk = chunk[:k][::-1] + chunk[k:]
        result += reversed_chunk

    return result


# In[19]:


s = "abcdefg"
k = 2
print(reverseStr(s, k))


# In[23]:


#Answer 6.

def rotateString(s, goal):
    if len(s) != len(goal):
        return False
        
    s_concat = s + s
    return goal in s_concat


# In[24]:


s = "abcde"
goal = "cdeab"
print(rotateString(s, goal))


# In[26]:


#Answer 7. 

def backspaceCompare(s, t):
    def processString(string):
        result = []
        for char in string:
            if char != '#':
                result.append(char)
            elif result :
                result.pop()
        return ''.join(result)
    
    return processString(s) == processString(t)


# In[27]:


s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))


# In[28]:


#Answer 8.

def checkStraightLine(coordinates):
    if len(coordinates) <= 2:
        return True

    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (y - y1) * (x - x2) != (y - y2) * (x - x1):
            return False

    return True


# In[29]:


coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates)) 


# In[ ]:




