# ============================================
# dict() - Standard Dictionary
# ============================================
# - Key-value storage
# - Raises KeyError if key is missing

my_dict = dict()
my_dict["apple"] = 2
print(my_dict["apple"])    # Output: 2
# print(my_dict["banana"]) # Raises KeyError

# Use .get() to avoid errors
print(my_dict.get("banana", 0))  # Output: 0

# ============================================
# defaultdict() - Dictionary with Default Values
# ============================================
# - Auto-creates missing keys with a default value
# - Use it to simplify counting, grouping, etc.

from collections import defaultdict

counts = defaultdict(int)  # Default value is 0
counts["apple"] += 1
print(counts["apple"])  # Output: 1
print(counts["banana"]) # Output: 0 (auto-created)

# Using a list as default
grouped_items = defaultdict(list)
grouped_items["fruits"].append("apple")
print(grouped_items["fruits"])  # Output: ['apple']
print(grouped_items["veggies"]) # Output: [] (auto-created)

# ============================================
# set() - Unique Collection of Elements
# ============================================
# - Stores only unique items
# - Supports fast lookups and set operations

my_set = set([1, 2, 3])
my_set.add(2)       # No change, since 2 is already in the set
my_set.remove(3)    # Removes 3
print(2 in my_set)  # Output: True
print(5 in my_set)  # Output: False
my_set.clear()      # Output: {}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: {3}

# ============================================
# Counter() - Specialized Dictionary for Counting
# ============================================
# - Automatically counts occurrences of elements
# - Returns 0 for missing keys instead of KeyError

from collections import Counter

letter_counts = Counter("banana")
print(letter_counts)         # Output: Counter({'a': 3, 'n': 2, 'b': 1})
print(letter_counts['a'])    # Output: 3
print(letter_counts['z'])    # Output: 0 (no KeyError)

# Get most common elements
print(letter_counts.most_common(1))  # Output: [('a', 3)]

# ============================================
# Summary of Differences
# ============================================

# dict() - General key-value storage, KeyError if key is missing
# defaultdict() - Auto-creates missing keys with a default value
# set() - Stores only unique items, fast membership checks
# Counter() - Counts occurrences, returns 0 for missing keys


# JAVA SCRIPT Language Basics
'''
Var(function scoped, only accesible in the function or globally if declared outside the function. Can be updated and redeclared within their scope) vs Let(blocked scooped only accesible within the block {} where they are defined, can be updated but not redefined within the same scope) vs const(blocked scooped only accesible within the block {} where they are defined. variables cannot be update or redeclared after assignment)
Data types and types coercion (automatic conversion of a value form one data to another)
	== (abstract equality, check for value equality) vs === (checks for type and value equality)
	How does JS perform Coercion for null, unidentified vs NaN
	console.log(5 == "5");   // true, because "5" is coerced to a number
	console.log(5 === "5");  // false, because the types are different

	console.log(null == undefined); // true, due to type coercion
	console.log(null === undefined); // false, different types

	console.log(0 == false); // true, boolean is coerced to number
	console.log(0 === false); // false, different types
Hoisting: where variable and function declarations are moved to the top of their scope before code execution

Functions and Closure
Closure:  a function that “remembers” its lexical scope, even if called in a different context. Interviewers may want an example, such as a function returning another function that captures a variable from the outer scope.

this keyword: refers to the object that is currently executing the code. Its value is determined by how a function is called

arrow functions:
// Traditional function expression
const add = function(a, b) {
  return a + b;
};

// Arrow function equivalent
const addArrow = (a, b) => a + b;

'''

