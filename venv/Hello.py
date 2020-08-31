import collections
import functools
import re
import sys
from typing import *

def ss(x : List[str]):
    return x.split()[1],x.split()[0]

lisst = ["2 A", "1 B" , "2 C"]



logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(type(logs))

def reorderLogFiles(logs: List[str]) -> List[str]:
    letters , digits = [],[]

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters.sort(key=lambda x:(x.split()[1:], x.split()[0]))
    return letters + digits

reorderLogFiles(logs)
# reorderLogFiles(logs)


strs = ["eat","tea","tan","ate","nat","bat"]
strs.pop(strs.index("bat"))

print(strs)
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams["".join(sorted(word))].append(word)
        print('join > ', "".join(sorted(word)))
        print('word ->? ',word)
        print('dict-> ',anagrams)
    return anagrams.values()

print(groupAnagrams(strs))



nums = [2,7,11,15]
target = 9


def twoSum(nums : List[int] , target : int):
    for i in range(len(nums)):
        for j in range(i+1 ,  len(nums)):
            if nums[i] + nums[j] == target:
                return i,j


def twoSum2(nums : List[int] , target : int) -> List[int]:
    for i , n in enumerate(nums):
        complemnet = target - n

        if complemnet in nums[i + 1:]:
           return nums.index(n) , nums[i+1:].index(complemnet) + (i + 1)


def twoSum3(nums : List[int] , target : int) -> List[int]:
    nums_map = {}
    # key , value change in dict

    for i , num in enumerate(nums):
        nums_map[num] = i
        print('nums_map-> ',nums_map)
    for i , num in enumerate(nums):
        print( nums_map[target-num],i)
        if target - num in nums_map and i != nums_map[target-num]:
            return nums.index(num) , nums_map[target-num]

def twoSum4(nums : List[int] , target : int) -> List[int]:
    nums_map = {}
    # key , value change in dict
    for i , num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i




print(twoSum4(nums,target))







print(twoSum3(nums,target))


str = "BCDEITUQHJSMNMA"
str = "".join(sorted(str))
print(type(str))
