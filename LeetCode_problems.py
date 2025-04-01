#----------------------------------------------TOP K ELEMENTS -------------------------------------------------
#Top K Frequent Elements total time would be O(n + k log k)
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #creates a counter to count the frequency of each number
    freqs = Counter(nums)  # o(n) time, goes through each element and count the occurences
    #this will return the array of most common numbers
    return [freq for freq,cnt in freqs.most_common(k)] #O(k log k)
    

#-----------------------ARRAYS-----------------------------------------------
#Products of Array Except Itself (Medium)
#using prefix/postfix method for 0(n) time // combo of used prefix sum and array manipulation
#the time complexity of this is O(n + n + n) which is O(3n) which condenses to O(n)
def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums) #O(n)

    #find the prefix first
    #O(n)
    prefix = 1
    for index in range(1, len(nums)):
        res[index] = res[index-1] * nums[index-1]

    #find the postfix sums
    #O(n)
    postfix = 1
    left,right =  0,len(nums)-1

    for num in reversed(res):
        #print(num, postfix)
        res[right] = num * postfix
        postfix*=nums[right]
        right-=1       

    return res

# ROTATE ARRAY (EASY) 
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# this was the one i did in the interview
def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        # Since rotating ( n ) times brings the array back to its original state, 
        # ( k ) can be reduced to ( k \mod n ).
        k %= n 
        # reverse the entire array
        nums.reverse() # [7,6,5,4,3,2,1]
        # reverse the elements from the start to k
        nums[:k] = reversed(nums[:k]) # [5,6,7,4,3,2,1]
        # now revesrse the elements from k to the end
        nums[k:] = reversed(nums[k:]) # [5,6,7,1,2,3,4]

# Moves Zero (easy), inplace moves, swaps all zeros to the end while maintain the order of the other numbers
# nums = [0,1,0,3,12] -> output = [1,3,12,0,0]
def moveZeroes(self, nums: List[int]) -> None:
        j = 0 #variable that holds first index of nums
        for index in range(len(nums)):
            # if the nums[index] is 0 we continue
            if nums[index]==0:
                continue
            else:
                # if the nums[index] != 0 
                temp = nums[index] # temporary holds value nums[index]
                nums[index] = nums[j] # sets nums[index] to the first index of nums
                nums[j] = temp # index j now has the temp that is not a 0
                j+=1 #increments j after the swap

# Majority Element(EASY) - given array nums return the most common element
def majorityElement(self, nums: List[int]) -> int:
        #cheating method that uses the counter and most common function
        majority_count = Counter(nums).most_common(1)
        return majority_count[0][0]
        
        #method using a counter
        counter = 0
        candidate = None
        for num in nums:
            if counter == 0:
                #candidate becomes the first scene num and swaos to new one once it show up less
                candidate = num
            #add one if same num is seen else -1 if new number seen
            counter += (1 if num == candidate else -1) 
        return candidate

# Remove Duplicate from Sorted Array (EASY) - in, place swap duplicate to the end, keep other numbers inorder
def removeDuplicates(self, nums: List[int]) -> int:
        left  = 1
        # right pointer moves with the iterator so that we can go through every element in nums
        for right in range(1, len(nums)):
            #if num[r] is not equal to the previous element
            if nums[right] != nums[right-1]:
                # swap nums[l] and nums[r]
                nums[left] = nums[right]
                # increment left
                left +=1
        return left

#Best time to buy and sell stocks (EASY)
def maxProfit(self, prices: List[int]) -> int:
    #Keep track of max_profit and cheapest stock we can buy at each day, initalize that as the first stock
    max_profit, min_stock = 0,prices[0]
    for index in range(1, len(prices)):  
        # get the max_profit of the current maxp and the the daily sell price and the cheapest stock prior
        max_profit = max(max_profit, prices[index]-min_stock) 
        # update the min stock if today's price is cheaper
        min_stock = min(min_stock, prices[index])
    return max_profit

# Best time to buy and sell stocks II (Medium)
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. 
# You can only hold at most one share of the stock at any time. 
# However, you can buy it then immediately sell it on the same day. 
# Find and return the maximum profit you can achieve.
def maxProfit(self, prices: List[int]) -> int:
        # track the total profit 
        profit = 0
    
        # skipping the index 0 becuase for every index we compare with previous
        # and 0 does not have a previous
        for index in range (1, len(prices)):
            #check that it is not in decreasing order, we only add profit is its increasing
            if prices[index] > prices [index - 1]:
                profit += (prices[index]-prices[index-1]) #this is profit selling in 1 day
        return profit

# NUMBERS of zero-filled subaaray (MEDIUM)
# Given an integer array nums, return the number of subarrays filled with 0.
# A subarray is a contiguous non-empty sequence of elements within an array.
def zeroFilledSubarray(self, nums: List[int]) -> int:
        index, res = 0, 0 
        while index < len(nums):
            # count is holding the zeros that we encounter
            count = 0
            # while index is inbound and nums[i] is zero
            while index < len(nums) and nums[index] == 0:
                count += 1 # we increment the zero_counter
                index+= 1 # we increment the index to move to the next zero
                res+= count # we add the zero count of this subarray to the result 
            index +=1 #increment index to move to the next element if its not a zero
        return res

# Increasing the triplet subsequence (MEDIUM)
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
# such that i < j < k and nums[i] < nums[j] < nums[k]. 
# If no such indices exists, return false.
def increasingTriplet(self, nums: List[int]) -> bool:
        # we are looking for nums[i] < nums[j] < nums[k] and i< j < k
        i = j = float('inf') # set both of these to holders 
        # loop through all the numbers in nums 
        for k in nums:
            # if k is less the i, i is now k 
            if  k <= i:
                i = k
            # if k is less the j, j is now k 
            elif k <= j:
                j = k
            # else we need k is less than i and j so we can found our triplet
            else:
                return True 
        return False

#-----------------------------STRINGS-----------------------------------------
# Is Sequence (EASY)
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
def isSubsequence(self, s: str, t: str) -> bool:
        # both counters start a 0
        i, j = 0 , 0
        while i < len(s)  and j < len(t):
            # if we found the char t[j] at s[i] we increment the i index
            if s[i] == t[j]:
                i+=1
            j+=1 #j is increment regardless of comparison

        # returns False if we loop through all of s and found no matching char for t  
        return True if i==len(s) else False

#Longest Common Prefix (EASY)
def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        # this loops through every index of the first string
        for i in range(len(strs[0])):
    # now go through all the string to make sure they start with same prefix
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

# Zigzag Conversion (MEDIUM)
def convert(self, s: str, numRows: int) -> str:
        if numRows ==  1 : return s # base case if there is only 1 row return the string
        res = "" # build the result
        # for every row we are checking
        for r in range(numRows): 
            # this is the formula to go zigzag to jump for this problem 
            increment = 2 * (numRows - 1)
            # tracking position in the string, start at r and go and the amount we increment
            for i in range(r, len(s), increment):
                res+= s[i] # add to the result the value 
                # this will make sure we do not miss the extra character if we are in the middle and 
                # we want to make sure it is inbound so that is this formula in the if: 
                if (r > 0 and r < numRows -1 and i + increment -2 * r < len(s)):
                    res+= s[i + increment - 2 * r]
        return res

# Reverse Words in a String (MEDIUM)
def reverseWords(self, s: str) -> str:
        new_str = " ".join(s.split()) #splits and joins the strings together removing the extra and trailing space
        new_str = new_str.split(" ") # splits it again and puts it in a array
        new_str.reverse() # reverse the array
        new_str = " ".join(new_str) # now join the reversed array into a single string
        return new_str # returns the string

#Longest Substring Without Repeating Characters 
def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    left = 0
    res = 0
    for right in range(len(s)):
        #if right char is duplicate (in the set) we must update our window
        while s[right] in charSet:
            #we will keep going until the duplicates are all removed
            charSet.remove(s[left])
            left+=1
        charSet.add(s[right])
        #right -left + 1 is the window size
        res = max(res, right - left + 1)
    return res

#Valid Parenthesis using stack
def isValid(self, s: str) -> bool:
    stack = []
    for item in s:
        if stack and stack[-1] == "{" and item == "}":
            stack.pop()
        elif stack and stack[-1] == "[" and item == "]":
            stack.pop()
        elif stack and stack[-1] == "(" and item == ")":
            stack.pop()
        else:
            stack.append(item)
    return not stack

# Valid Anagram (Easy)
# Use Counter() to easily count the char and check to see if they can be anagrams and have same characters
# This is O(n) time
def isAnagram(self, s: str, t: str) -> bool:
    return True if Counter(s) == Counter(t) else False

# Group Anagram (Medium)    
# Using hashtable to optimized. Mainly we want to map each key to each char in the alphabet
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#created a default dictionary that will hold the list of anagrams
    anagrams = defaultdict(list)
    for s in strs:
        count  = [0] * 26 # this will hold the 6 alphabets in lowercase numbers
        for c in s:
            #ord(c)-ord(a) will help us get what location it is in the alphbet as a is number 0
            count[ord(c)-ord("a")]+=1
        # the reason we use tuple is becuase default dict does not let us just have the interger as key
        anagrams[tuple(count)].append(s)
    return list(anagrams.values())

#valid palindrome
class Palindrome:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

#longest substring without repeating characters
#given a string s, find the length of the longest subdivision without duplicate characters
def lengthOfLongestSubstring(self, s: str) -> int:
        #this is using sliding window
        # will store the chars to make sure they do not repeat
        char_set = set()
        left = 0
        res = 0 

        #the right pointer will visit every char
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            #gets the current size of the longest sequence minus the dulplicate:right-left+1
            res = max(res, right-left+1)
        return res

#Longest Repeating Character Replacement 
# Given a string s and an interger k, you can choose any character of the string and change it to any other uppercase English charcter.  
# You can perform this operation at most k times
# Return the length of the longest substring containing the same letter you can get after performing the above operations.
def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left, maxf = 0,0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)
            maxf = max(maxf, count[s[right]])

            while (right-left +1) - maxf > k:
                count[s[left]]-=1
                left +=1
            res = max(res, right-left+1)
        return res

#Word Break Variant
def word_break(s, word_dict):
    """
    Return True if s can be segmented into words in word_dict.
    """
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True  # empty string is always 'segmented'
    
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[n]

    # Example Usage
    dictionary = {"leet", "code"}
    print(word_break("leetcode", dictionary))  # True
    print(word_break("leetcodea", dictionary)) # False


#----------------------------------------------HASHMAPS---------------------------------------------------
# Contains Duplicate (EASY)
# Using Hash sets to keep i o(n)
def hasDuplicate(self, nums: List[int]) -> bool:
    #use hashset top track ducplicates
    duplicates = set()

    for num in nums:
        if num in duplicates:
            return True
        else:
            duplicates.add(num)
    return False

#Contains Duplicate II (Medium)
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    window = set()
    left = 0
    for right in range(len(nums)):
        if right - left > k:
            window.remove(nums[left])
            left+=1
        if nums[right] in window:
            return True
        window.add(nums[right])
    return False
        
#  Two Sum (Easy)
# use hashmap to find the difference which is the target - num[index] to keep it O(n) and optimized
def twoSum(self, nums: List[int], target: int) -> List[int]:
    differences = {} #value -> index
    for index, num in enumerate(nums):
        difference = target - num
        #print (index, conjugate)
        if difference in differences:
            return [differences[difference], index]
        differences[num] = index
    return []

# Two Sum II with ordered list using two pointer method
def twoSumII(self, nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums)-1
    while left < right:
        two_sum = nums[left] + nums[right]
        if two_sum == target:
            return [left+1, right+1]
        elif two_sum < target:
            left+=1
        else:
            right-=1

#ThreeSum combination of 2sum I and 2sum II hashset and 2 pointer
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for index, num in enumerate(nums):
        #check to make sure the first digit is not duplicated make sure the triples are not the same
        if index > 0 and nums[index-1] == num:
            continue
        left, right = index+1, len(nums)-1
        while left < right:
            three_sum = num + nums[left]+ nums[right]
            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left+=1
            else:
                res.append([num, nums[left], nums[right]])
                left+=1
                while left < right and nums[left] == nums[left-1]:
                    left+=1
    return res

#valid sudoku using hashsets
def isValidSudoku(self, board: List[List[str]]) -> bool:
    board_rows = defaultdict(set)
    board_cols = defaultdict(set)
    board_cube = defaultdict(set)

    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            if (board[row][col] in board_rows[row] or 
            board[row][col] in board_cols[col] or 
            board[row][col] in board_cube[(row // 3, col // 3)]):
                return False
            board_rows[row].add(board[row][col])
            board_cols[col].add(board[row][col])
            board_cube[(row // 3, col // 3)].add(board[row][col])

            #print(board[row][col])
        #print("end of the row ", row)
    return True    

#----------------------------------------------TWO POINTER---------------------------------------------------



#----------------------------------------------PREFIX SUMS---------------------------------------------------
#Range Sum Query - Immutable
#given an integer array nums, handle multiple queries of the following type
#caculate the sum or between the left and right in integers inclusive 
# with prefix sum so that we are not looping too much and kep it 0(n)
class Range_Sum_Query_Immutable:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1)  
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left] 

# Minimum Size Subarray Sum
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    left = 0
    curr_sum = 0
    res = float("inf")
    for right in range(len(nums)):
        curr_sum+=nums[right]
        #print(nums[left:right], curr_sum)
        while curr_sum >= target:
            res = min(res, right-left+1)
            curr_sum-=nums[left]
            left+=1

    return 0 if res == float("inf") else res

#subarray sum equals k
#given a subarray nums and interger k, return the total number of subarrays whose sum equals k
def subarraySum(self, nums: List[int], k: int) -> int:
        res, currSum = 0,0
        prefixSums = {0 : 1}

        for n in nums:
            currSum += n #adds the current n in nums to the current sum
            diff = currSum - k # get the difference of the curr sum and K

            res += prefixSums.get(diff, 0) #returns 0 if the value is not in prefixSums
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0) #increment the res that has this sum
        
        return res

#subarray sums divisible by K
#given an interger array nums and integer k, return the number of non-empty subarrays that have a sum divisble by K
def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #current (prefix sum) and the count of the subarrays
        prefix_sum, res = 0,0
        prefix_cnt = defaultdict(int) #hashmap to hold the subarrays
        prefix_cnt[0] = 1 #single pair mapping 0 to 1 first thing added to hashmap

        for n in nums:
            prefix_sum +=n #getting the current sum as we traverse nums
            remain = prefix_sum % k #calculate the remainder
            
            #if the remainder is in prefix_cnt we add it to res
            if remain in prefix_cnt: #technically we dont need this cause we use defualt dict
                res += prefix_cnt[remain]
            
            prefix_cnt[remain] += 1

        return res

#continuous subarray sum
#given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise
# a good subarray is where: length is at lease 2, sum of the elements of the subarray is a multiple of k
def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0:-1} #mapping the remainder -> end index of that subarray we are looking at
        total = 0

        #we need index and the value
        for i, n in enumerate(nums):
            total+= n #get the running total
            r = total % k #calculate the remainder

            #is remainder in the hashmap or not?
            if r not in remainder:
                remainder[r] = i
            #checking if the length is greater than 1 and that we found the solution
            elif i - remainder[r] > 1:
                return True            
            #if we find subarray with remainder of 0 and length of 1
            #we found solutions which is the hashmap that we mapped

        return False

#Contiguous Array
#given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1
def findMaxLength(self, nums: List[int]) -> int:
        #111 000
        # How do we know to shrink window or increase?
        # Have to split, thus recursive and worst than O(n^2)
        
        # Not every result starts at beginning, eg
        # 111 00

        # Is it possible to know exactly where 
        # the first 1 was , and verify that after it
        # count[1] == count[0]?

        # Map each index to pair (count[0], count[1])
        # Use diff between counts for O(1) lookup of what we need

        zero, one, res = 0,0, 0
        diff_index = {} # diff (count[1] - count[0]) -> index

        for i, n in enumerate(nums):
            if n == 0:
                zero+=1
            else:
                one += 1

            #if this is not in hashmap we put it in
            if one - zero not in diff_index:
                diff_index[one-zero] = i
            
            if one == zero:
                res = one + zero
            #if its already in we can find the new fixed size of the window
            else:
                idx = diff_index[one-zero]
                res= max(i-idx, res) # i -idx gets the new window that might be bigger than the res
        return res 

#---------------------------------------------KADANE'S ALGORITHM---------------------------------------------------

#----------------------------------------------SLIDING WINDOW (FIXED SIZE)---------------------------------------------------
# Maximum Average Subarray I

# find all Anagrams in a String

# Permutation in String


#----------------------------------------------SLIDING WINDOW (DYNAMIC SIZE)---------------------------------------------------

#----------------------------------------------lINKED LIST-------------------------------------------------
#----------------------------------------------FAST AND SLOW POINTERS-------------------------------------------------

#----------------------------------------------STACKS-------------------------------------------------

#----------------------------------------------SORTS-------------------------------------------------

#----------------------------------------------SEARCHS-------------------------------------------------

#----------------------------------------------BACKTRACKING-------------------------------------------------

#----------------------------------------------TREE TRAVERSAL BASICS-------------------------------------------------

#----------------------------------------------HEAPS-------------------------------------------------

#----------------------------------------------INTERVALS-------------------------------------------------



#Carfleet Problem (medium)
def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    pair = [(p, s) for p, s in zip(position, speed)]
    pair.sort(reverse=True)
    stack = []
    for p, s in pair:  # Reverse Sorted Order
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
		
#reversed Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #first traverse to the last node
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
		
#Remove Element array manipluation
def removeElement(self, nums: List[int], val: int) -> int:
    res = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[res] = nums[i]
            res+=1
    return res


#longest Consecutive Sequence
def longestConsecutive(self, nums: List[int]) -> int:
    #changing it to a set will remove dulicates and sort it 
    # this is O(n) time 
    num_set = set(nums)
    longest = 0 
    for num in num_set:
        if (num - 1) not in num_set:
            length = 1
            while (num + length) in num_set:
                length += 1
            longest = max(length, longest)
    return longest


# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    count = 0
    #this is a shortcut to get the sum of the first 2 elements
    curr_sum = sum(arr[:k-1])
    #checking all of the valid subarrays of size k: len(arr)-k+1
    for left in range(len(arr)-k+1):
    #left+k-1 is 1 the last spot for the size of k 
        curr_sum += arr[left+k-1]
        if (curr_sum/k) >= threshold:
            count+=1
        curr_sum -= arr[left]
    #print (curr_sum)
    return count


#Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the min length of a subarray 
# whose sum is greater than or equal to targer. If there is no such subarray, return 0 instead
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum = 0
        res = float("inf")
        for right in range(len(nums)):
            curr_sum+=nums[right]
            #print(nums[left:right], curr_sum)
            while curr_sum >= target:
                res = min(res, right-left+1)
                curr_sum-=nums[left]
                left+=1

        return 0 if res == float("inf") else res

# Maximum Subaaray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.
def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum  = 0
        for num in nums:
            if curr_sum < 0 and num > curr_sum:
                curr_sum = num
            
            else:
                curr_sum+=num
            max_sum = max(max_sum,curr_sum)
        return max_sum

# Maximum Sum Circular Subarray
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
def maxSubarraySumCircular(self, nums: List[int]) -> int:
    #use Kadmae algo from #53 and then figure out a solutions for the edge cases
        max_sum,min_sum = nums[0],nums[0] 
        curr_max,curr_min = 0,0
        total = 0 

        for num in nums: 
            curr_max = max(num, curr_max+num)
            curr_min = min(num, curr_min+num)
            total+=num
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)
        
        return max(max_sum, total-min_sum) if max_sum > 0 else max_sum  

# Maximum Product Subarray
# Given an integer array nums, find a subarray that has the largest product, and return the product.
def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) #incase we have an array of 1 so this would be out max e,g 0->[-1]
        curr_min, curr_max = 1,1 # 1 is a neutral value
        for n in nums:
            # we do not want to multiple the product with zero
            if n  == 0:
                #instead just reset the curr min and max to 1 and continue
                curr_min, curr_max = 1,1
                continue
            tmp = curr_max * n #we need this or else the curr_min will use the new curr_max
            curr_max = max(n*curr_min, curr_max*n, n) # we put in n incase of negatives
            curr_min = min(n*curr_min, tmp, n)
            res = max(res, curr_max)
        return res

# Best Sightseeing Pair
# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. 
# Two sightseeing spots i and j have a distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.
def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0 # will hold the max score for the sightseeing pair
        curr_max = values[0] - 1
        for i in range(1, len(values)):
            res = max(res, values[i]+curr_max)
            curr_max = max(curr_max-1, values[i] - 1)

        return res

# Max Consecutive Ones III
# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
def longestOnes(self, nums: List[int], k: int) -> int:
        # max window length, number of zeros so far, length of nums, left pointer
        max_w, num_zeros, n, left = 0,0,len(nums),0

        #right pointer in the iterator
        for right in range(n):
            #as we expand our window if nums[r] is a zero we increate num_zero
            if nums[right] == 0:
                nums_zero +=1
            
            #this will keep running while our window is invalid
            #invalid when the number of zero is greater than k 
            while nums_zero > k:
                # if nums[l] is 1 then we can flip it and get rid of nums[r] in the window
                if nums[left] == 0:
                    nums_zero-=1
                left+=1
            
            #after while loop the window will become valid 
            w = right - left + 1 #calculate window length
            max_w = max(max_w, w)

        return max_w

#linked List Cycle Detection (Fast and Slow Pointers)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def hasCycle(self, head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

#Find the Minimum in a rotated array (using binary search)
def findMin(self, nums: List[int]) -> int:
    min_num = nums[0]
    left, right = 0, len(nums)-1
    while left <= right:
        if nums[left] < nums[right]:
            min_num = min(min_num, nums[left])
            break
        middle = (left + right) //2
        min_num = min(min_num, nums[middle])
        if nums[middle] >= nums[left]:
            left = middle +1
        else:
            right = middle - 1
    return min_num 


#reverse an array list IN-PLACE
def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    # Example Usage
    arr = [1,2,3,4,5,6,7]
    rotate_array(arr, 3)
    print(arr)  # Output: [5,6,7,1,2,3,4]


#rectangle Overlap
def rectangles_overlap(rec1, rec2):
    """
    Return True if rec1 overlaps with rec2; False otherwise.
    rec1, rec2 are tuples like (x1, y1, x2, y2).
    """
    x1a, y1a, x2a, y2a = rec1
    x1b, y1b, x2b, y2b = rec2
    
    # If one rectangle is entirely to the left or right => no overlap
    if x2a <= x1b or x2b <= x1a:
        return False
    # If one rectangle is entirely above or below => no overlap
    if y2a <= y1b or y2b <= y1a:
        return False
    
    return True

    # Example Usage
    rectA = (0, 0, 2, 2)  # bottom-left=(0,0), top-right=(2,2)
    rectB = (1, 1, 3, 3)
    print(rectangles_overlap(rectA, rectB))  # True
    rectC = (3,3,5,5)
    print(rectangles_overlap(rectA, rectC))  # False

#Linked List Sorting by Absolute value
#Given a linked list containing possibly negative integers, sort it by the absolute value of its nodes.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_by_abs(head):
    """
    Returns the head of a new list sorted by absolute values of node.val.
    """
    # Convert to list
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    
    # Sort by absolute value
    arr.sort(key=abs)
    
    # Create a new sorted linked list
    dummy = ListNode()
    curr = dummy
    for value in arr:
        curr.next = ListNode(value)
        curr = curr.next
    return dummy.next

    # Example Usage
    # Creating a list:  3 -> -2 -> 5 -> -8 -> 1
    head = ListNode(3, ListNode(-2, ListNode(5, ListNode(-8, ListNode(1)))))
    sorted_head = sort_by_abs(head)
    # Expected order by abs: [1, -2, 3, 5, -8]  # since abs(1)=1, abs(-2)=2, abs(3)=3, abs(5)=5, abs(-8)=8

#common Elements in 2 sorted list (2 pointer approach)
def common_elements_sorted(a, b):
    """
    Return a list of common elements between two sorted lists a and b.
    """
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return result

    # Example Usage
    listA = [1,2,3,5,7,9]
    listB = [2,3,4,5,10]
    print(common_elements_sorted(listA, listB))  # [2,3,5]

#Count Negatives in a sorted Matrix
def count_negatives(matrix):
    """
    matrix has rows sorted in non-increasing order, so negative values
    are on the right or bottom side. We'll do a linear scan from bottom-left.
    """
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    count = 0
    r, c = rows - 1, 0
    
    while r >= 0 and c < cols:
        if matrix[r][c] < 0:
            # Everything to the right of c is also negative
            count += (cols - c)
            r -= 1
        else:
            c += 1
    return count

    # Example Usage
    mat = [
        [ 5,  3,  2,  0],
        [ 2,  1, -1, -3],
        [ 1,  0, -2, -4],
        [-1, -2, -3, -5]
    ]
    print(count_negatives(mat))  # e.g. 8

#Merge 2 arrays in sorted order (easy)
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        middle, next_largest, right =  m-1, n-1, m+n-1
        while next_largest >=0:
            if middle >= 0 and nums1[middle] > nums2[next_largest]:
                nums1[right] = nums1[middle]
                middle -=1
            else:
                nums1[right] = nums2[next_largest]
                next_largest -= 1 
            right-=1

#trapping rain water
#Given n non-negative integers representing an elevation map where the width of each bar is 1, 
#compute how much water it can trap after raining.
def trap(self, height: List[int]) -> int:
        if not height: return 0
        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res+= leftMax -height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res+= rightMax -height[right]
        return res

