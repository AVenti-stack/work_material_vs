#Linked List
class Node:
    def __init__(self, value= None):
        self.data = value   
        self.next  = None

class LinkedList:
    
    def __init__(self):
        #visual for a linked list, node pointing to none is
        #the last value in the list
        # [1] -> [2] -> [3] -> None
        self.head = None
        
    
    def get(self, index: int) -> int:
        # [1] -> [2] -> [3] -> None
        curr  = self.head
        count = 0
        while curr is not None:
            if count == index:
                return curr.data
            curr = curr.next
            count+=1
        return -1
        
    def insertHead(self, val: int) -> None:
        # [1] -> [2] -> [3] -> None
        new_node = Node(val)
        new_node.next  = self.head
        self.head  = new_node


    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        #if the list if empty then we add the 
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        #traverse to to the end of the list
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
		
    def delete_value(self, val):
        if not self.head:
            return
        # If head node is target
        if self.head.val == val:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return
            curr = curr.next

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr  = self.head
        count = 0
        while curr.next is not None:
            if count + 1 == index:
                curr.next = curr.next.next
                return True
            curr = curr.next
            count+=1
        return False

    def getValues(self) -> List[int]:
        values  = []
        curr = self.head
        while curr:
            values.append(curr.data)
            curr = curr.next
        return values

#Double Linked List 
class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None 

    def get(self, index: int) -> int:
        curr = self.head
        count = 0 

        while curr is not None:
            if count == index:
                return curr.data
            count+=1
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        #create new node
        new_node = Node(val)
        if self.head is None:
            #if the list is empty then the new node become the new head and tail
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addAtTail(self, val: int) -> None:
        #create a new node 
        new_node = Node(val)
        #if the list is empty the new node become the head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        #if index is 0 use add at head
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        count = 0 
        #travese to the node just before where we need to insert
        while curr is not None and count < index - 1:
            curr = curr.next
            count+=1
        #if the curr is none, then the index is out of bounds
        if curr is None:
            return
        new_node= Node(val)
        temp = curr.next
        new_node.next = temp
        new_node.prev = curr
        curr.next = new_node
        if temp is not None:
            temp.prev = new_node
        else:
            self.tail = new_node
        

    def deleteAtIndex(self, index: int) -> None:
        #check to see if the list is empty return false 
        if self.head is None:
            return 
        #if index is 0 remove the head node
        if index is 0:
            self.head = self.head.next
            if self.head is not None:
                #this is how we know its the first node
                self.head.prev = None
            else:
                #if this list is now empty
                self.tail = None
            return 
        curr = self.head
        count = 0 
        while curr is not None: 
            if count == index:
                #we found the node we need to delete
                curr.prev.next = curr.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                else: 
                    #removing the tail node
                    self.tail = curr.prev
                return
            curr = curr.next
            count+=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Doubly LinkedList browser history
class Node:
    def __init__(self, url):
        self.data = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        #current page
        self.current_page = Node(homepage)
        

    def visit(self, url: str) -> None:
        #adding a new node to the tail of the linked list
        new_website = Node(url)
        self.current_page.next = new_website
        new_website.prev = self.current_page
        self.current_page = new_website
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.current_page.prev is not None:
            self.current_page = self.current_page.prev
            steps -= 1
        return self.current_page.data
        

    def forward(self, steps: int) -> str:
        while steps > 0  and self.current_page.next is not None:
            self.current_page = self.current_page.next
            steps -= 1
        return self.current_page.data

		
#Deque using a doubly linked list
class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        #use a double linked list to track the head and the tail
        #dummy nodes
        self.head = Node(-1)
        self.tail = Node(-1)
        self.tail.prev = self.head
        self.head.next = self.tail

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev
        
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        first_node.prev = new_node
        new_node.next = first_node
        new_node.prev = self.head
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        value = last_node.data
        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        value = first_node.data
        next_node = first_node.next

        next_node.prev = self.head
        self.head.next = next_node 

        return value

# stacks for students and sandwhiches
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stack = []
        students_count, sandwiches_count = 0,0
        for i in range(len(students)):
            stack.append(sandwiches[len(sandwiches)-i-1])
            if students[i] == 0:
                students_count+=1
            else:  
                sandwiches_count+=1
        while len(stack) != 0:
            if stack[-1] == 0 and students_count > 0:
                students_count-=1
                stack.pop()
            elif stack[-1]==1 and sandwiches_count > 0:
                sandwiches_count
                stack.pop()
            else:
                break
        if len(stack) != 0:
            return len(stack)
        return 0

#implement stacks using queues (this is using a deque)
class MyStack:

    def __init__(self):
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0
		
#factorial using recursion
def factorial(n):
    # Base case: n = 0 or 1
    if n <= 1:
        return 1

    # Recursive case: n! = n * (n - 1)!
    return n * factorial(n - 1)
	
#Creating simple twitter using deque queues
class Twitter:
    #tweet order: most recent to to lease recent -> use timestamps or some other ordering method
    #news Feed: pull from multiple users's tweet list
    

    def __init__(self):
        self.follows = defaultdict(set)
        self.feed = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.appendleft((userId, tweetId))
            
    
    #asking for the top 10 recent tweeks by the user and followees
    def getNewsFeed(self, userId: int) -> List[int]:
            return [ tweetId for user, tweetId in self.feed if userId == user or user in self.follows[userId]] [:10]

    def follow(self, followerId: int, followeeId: int) -> None:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
            self.follows[followerId].discard(followeeId)
			
#MinStacks using array
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return min(self.stack)
		
#encode and decode Strings
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for words in strs:
            res += str(len(words)) + "#" + words
        #print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            #holds the integer of how long word is 
            length = int(s[i:j])
            #j is currently at the delimiter character so we always want to look at j+1
            #if s[j] is currently not a "#"
            i = j + 1 
            j = i + length
            res.append(s[i:j])
            #this can be the end of the strong or start of next word
            i = j
 
        return res
		
#Design a Custom Iterator:  create a customer iterator over an internal data strucutre 
# Iterator has a has_next() and a next()
class CustomIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0
    
    def has_next(self):
        return self.index < len(self.items)
    
    def next(self):
        if not self.has_next():
            raise StopIteration("No more items")
        val = self.items[self.index]
        self.index += 1
        return val

# Example Usage
iterator = CustomIterator(["a", "b", "c"])
while iterator.has_next():
    print(iterator.next())  # prints "a", "b", "c"
#Explanation: We store the list items and a pointer index. has_next checks if we’re within bounds, and next returns the current item then increments. You can integrate __iter__ and __next__ to align with Python’s iterator protocol if you want true Pythonic iteration.

#CASE Study - Class Diagram : "You have a scenario of a Library Management System with Books, Authors, Members, and Librarians. Show me a class design and breif code to illustrate. Hint: Focus on showing high-level relationships

class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author  # could be an Author object
        self.available = True

class Author:
    def __init__(self, name):
        self.name = name
        # potential for more details like list of authored books

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

class Librarian:
	#Book references author
	#A Member can hvae multiple borrowed books 
	# Librarian can check out and return books. 
    def __init__(self, name):
        self.name = name
    
    def check_out_book(self, book: Book, member: Member):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book: Book, member: Member):
        book.available = True
        if book in member.borrowed_books:
            member.borrowed_books.remove(book)
'''
#Simple Twitter Clone
Problem: Design a simplified version of Twitter where users can post tweets, follow or unfollow other users, and view a news feed of recent tweets. We need to support operations like posting a tweet, following/unfollowing, and retrieving the top N (e.g., 10) most recent tweets in a user's feed​
FAVTUTOR.COM
. This should be implemented in an object-oriented way (e.g., a Twitter class managing users and tweets).
KEY Strucutres: Users -> Follow Mapping. Tweet Storage -> (timestamp, user_id, text). Timestamp Counter: Global Timestamp or counter to get teh top 10 recent
'''
class Twitter:
    def __init__(self):
        self.following = {}          # user_id -> set of followee_ids
        self.tweets = []             # list of (timestamp, user_id, tweet_text)
        self.time = 0                # simple timestamp counter for ordering

    def post_tweet(self, user_id, tweet_text):
        """User posts a new tweet."""
        self.tweets.append((self.time, user_id, tweet_text))
        self.time += 1

    def follow(self, follower_id, followee_id):
        """Follower starts following followee."""
        if follower_id not in self.following:
            self.following[follower_id] = set()
        self.following[follower_id].add(followee_id)

    def unfollow(self, follower_id, followee_id):
        """Follower stops following followee."""
        if follower_id in self.following:
            self.following[follower_id].discard(followee_id)

    def get_news_feed(self, user_id, limit=10):
        """Retrieve the most recent tweets from the user and people they follow."""
        # Determine which users' tweets to include (user's own and those they follow)
        followed_users = self.following.get(user_id, set()) | {user_id}
        # Filter tweets to only those from followed users
        feed_tweets = [text for (t, uid, text) in self.tweets if uid in followed_users]
        # Get the `limit` most recent tweets (sorted by timestamp descending)
        feed_tweets.sort(key=lambda x: x[0] if isinstance(x, tuple) else 0, reverse=True)
        return feed_tweets[:limit]

#Design a Rate Limiter
'''Problem: Implement a rate limiter that restricts how frequently a certain action can be performed. For example, allow at most N requests per user per minute. A rate limiter will allow or deny each request based on the history of recent requests​
TRYEXPONENT.COM
. This could be designed as a class with a method like is_allowed(user_id) that returns True/False depending on the user's request rate.

Timestamp log for each user (dictionary for API key or IP address ETC), Queue FIFO or Deque to efficiently add new timestamps and discard old ones. Counters/thresholds tp store max allowed requests (if max_calls is exceeded further requests are blocked)
'''
import time
from collections import deque

class RateLimiter:
    def __init__(self, max_calls, period):
        """Initialize rate limiter with max calls per time period (seconds)."""
        self.max_calls = max_calls
        self.period = period
        self.requests = {}  # user_id -> deque of recent request timestamps

    def is_allowed(self, user_id):
        """Return True if the user can make a request at the current time, else False."""
        now = time.time()
        if user_id not in self.requests:
            self.requests[user_id] = deque()
        dq = self.requests[user_id]
        # Remove timestamps older than the allowed period from the left
        while dq and now - dq[0] > self.period:
            dq.popleft()
        # Check how many requests are in the current window
        if len(dq) < self.max_calls:
            dq.append(now)       # log this request
            return True          # allowed
        else:
            return False         # too many requests in window, rate limit exceeded


#Design a Logger (Message Rate Limiter)
'''Problem: Design a logging system that prints messages to the console only if the same message hasn’t been printed in the last N seconds. In other words, if a message repeats too frequently, the logger should suppress it. This is sometimes known as a "logger rate limiter" problem. For example, if N=10 seconds and the message "Error" was just printed, any new "Error" messages within the next 10 seconds should be dropped​
Last-seen timestamp map (hashmap), time checking logic (check the dictonary for each incoming message with timestamp, if the message is not present of was last sceene longer than N seconds ago, it can be logged)
'''
class Logger:
    def __init__(self, limit_seconds):
        """limit_seconds is the minimum interval between same-message prints."""
        self.limit = limit_seconds
        self.last_printed = {}  # message -> last printed timestamp

    def should_print(self, timestamp, message):
        """Return True if the message can be printed at this timestamp (not printed in the last `limit` seconds)."""
        if message in self.last_printed:
            last_time = self.last_printed[message]
            if timestamp - last_time < self.limit:
                return False  # too soon since last print of this message
        # Otherwise, log this message and update last seen time
        self.last_printed[message] = timestamp
        return True

#Design a Cache with LRu Eviction
'''Problem: Design a cache that stores key-value pairs with a fixed capacity and evicts the Least Recently Used (LRU) item when the capacity is exceeded. The cache should support fast lookup (get) and update/insert (put) operations. This is a classic design where you might be asked to implement an LRUCache class with methods get(key) and put(key, value).

Hashmap + LinkedList (common way to implement a LRU Cache), Ordered dict (simplfy LRU Cache implemenation, it maintains key order by insertion use), Capacity Counter (stores the max capacity and track the current size)

from collections import OrderedDict'''

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()  # stores key -> value

    def get(self, key):
        if key not in self.cache:
            return None  # or -1 if specifying that for a miss
        # Move the key to the end to mark it as recently used
        value = self.cache[key]
        self.cache.move_to_end(key)
        return value

    def put(self, key, value):
        if key in self.cache:
            # Update existing key and mark as recent
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            # Add new key-value
            self.cache[key] = value
        # If over capacity, remove the oldest item (FIFO order in OrderedDict)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # pop the first item (least recently used)

#designing a parking lot system
''' Problem: Design an object-oriented parking lot system. For example, a parking lot can have multiple levels, each level has multiple parking spots, and different types of vehicles (car, bike, etc.) might occupy spots of appropriate size. The system should be able to park a vehicle in an available spot and free a spot when the vehicle leaves. We need to determine the classes and data structures to represent this system​
MEDIUM.COM

Vehicle and spot classes, parking log layout (a level class), overall parkinglot class(manages multiple levels and provides an interface to park or retrieve vehicles), datastructure for availableility (within each level you can scan a list of spots to find an available one).
'''

class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate

class ParkingSpot:
    def __init__(self, spot_id):
        self.id = spot_id
        self.vehicle = None  # None if spot is free

    def is_free(self):
        return self.vehicle is None

    def park(self, vehicle):
        if self.is_free():
            self.vehicle = vehicle
            return True
        return False

    def leave(self):
        self.vehicle = None

class Level:
    def __init__(self, level_num, num_spots):
        self.level_num = level_num
        # Initialize a list of spots for this level
        self.spots = [ParkingSpot(i) for i in range(num_spots)]

    def find_free_spot(self):
        """Find the first free spot on this level (linear scan)."""
        for spot in self.spots:
            if spot.is_free():
                return spot
        return None

class ParkingLot:
    def __init__(self, num_levels, spots_per_level):
        self.levels = [Level(i, spots_per_level) for i in range(num_levels)]

    def park_vehicle(self, vehicle):
        """Park vehicle in the first available spot (returns (level, spot_id) or None)."""
        for level in self.levels:
            spot = level.find_free_spot()
            if spot:
                spot.park(vehicle)
                return (level.level_num, spot.id)
        return None  # no free spot

    def free_spot(self, level_num, spot_id):
        """Free up the given spot on a level (when a vehicle leaves)."""
        if 0 <= level_num < len(self.levels):
            level = self.levels[level_num]
            if 0 <= spot_id < len(level.spots):
                level.spots[spot_id].leave()


#Design an elevator System
''' Problem: Design an elevator system for a building. This involves handling requests (people calling the elevator to go up or down from a floor, and people inside selecting destination floors), moving the elevator cab, and stopping at requested floors. We need to model one or multiple elevators, and ensure that the elevator services requests in an efficient order (e.g., serve all requests in one direction, then switch direction)​

. The design should identify the main classes and how to manage the queue of requests.

Elevator cab class (elevator clas represents a single elevator), request queues (use 1 or 2 priority queues or list to manage the destination. Common appoach is to maintain two sets of request -one for up one for down), elevator controller (if there are multiple elevators and elevatorsystem or controller can decide which floor handles the request and state managerment (the elevator needs to update its state as it moves, simulate movement ste-by-step and each floor arrival check if that floor was requested. 
import heapq
from collections import deque
'''
class Elevator:
    def __init__(self, elevator_id, max_floor):
        self.id = elevator_id
        self.current_floor = 0
        self.max_floor = max_floor
        self.direction = 0  # 1 for up, -1 for down, 0 for idle
        # Using two heaps for up and down requests
        self.up_requests = []    # min-heap of floors above current
        self.down_requests = []  # max-heap implemented as min-heap of negative floors

    def request_floor(self, floor):
        """Add a floor request for this elevator."""
        if floor == self.current_floor:
            return  # already here (could open door immediately)
        if floor > self.current_floor:
            heapq.heappush(self.up_requests, floor)
        else:
            # use negative for down direction to create max-heap
            heapq.heappush(self.down_requests, -floor)

    def step(self):
        """Move the elevator one step towards the next requested floor."""
        # Determine next target floor if not already decided
        if not self.up_requests and not self.down_requests:
            self.direction = 0
            return  # no requests
        if self.direction != -1 and self.up_requests:
            # If currently going up or idle and have up requests
            target = self.up_requests[0]  # peek smallest up-request
            self.direction = 1
        elif self.down_requests:
            target = -self.down_requests[0]  # peek largest down-request (stored as negative)
            self.direction = -1
        else:
            # No requests in current direction, switch direction
            if self.direction == 1 and self.down_requests:
                target = -self.down_requests[0]
                self.direction = -1
            elif self.direction == -1 and self.up_requests:
                target = self.up_requests[0]
                self.direction = 1
            else:
                self.direction = 0
                return

        # Move one floor towards the target
        if self.current_floor < target:
            self.current_floor += 1
        elif self.current_floor > target:
            self.current_floor -= 1

        # If reached target floor, remove it from the queue
        if self.current_floor == target:
            if self.direction == 1:
                heapq.heappop(self.up_requests)
            elif self.direction == -1:
                heapq.heappop(self.down_requests)
            # If there are no more requests in current direction, direction will update on next call

class ElevatorSystem:
    def __init__(self, num_elevators, max_floor):
        self.elevators = [Elevator(i, max_floor) for i in range(num_elevators)]

    def send_request(self, floor):
        """Handle an external request (e.g., someone at `floor` pressed the call button)."""
        # Simple strategy: assign to elevator with fewest pending requests
        best_elevator = min(self.elevators, key=lambda e: len(e.up_requests) + len(e.down_requests))
        best_elevator.request_floor(floor)

    def step_all(self):
        """Advance all elevators by one step (simulating time)."""
        for elevator in self.elevators:
            elevator.step()

#design shopping cart example:
'''
We want a user to be able to:

Browse and select products (each with a name, price).

Add or remove products in a cart.

Calculate total cost.

Possibly checkout (where you’d do payment, etc.).

This system is small, but you can talk about how you’d extend it for real scenarios.'''

class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.product_id}, name={self.name}, price={self.price})"

class Cart:
    def __init__(self):
        self.cart_items = []      # list of (Product, quantity)
        self.total_price = 0.0

    def add_product(self, product: Product, quantity=1):
        """
        Adds 'quantity' of the given product to the cart.
        If it already exists in the cart, increase quantity.
        """
        for i, (prod, qty) in enumerate(self.cart_items):
            if prod.product_id == product.product_id:
                self.cart_items[i] = (prod, qty + quantity)
                self._recalculate_total()
                return
        
        # If product not found in cart, add new tuple
        self.cart_items.append((product, quantity))
        self._recalculate_total()

    def remove_product(self, product_id: int, quantity=1):
        """
        Removes 'quantity' of the product by product_id from the cart.
        If quantity exceeds what's in the cart, remove the product entirely.
        """
        for i, (prod, qty) in enumerate(self.cart_items):
            if prod.product_id == product_id:
                new_qty = qty - quantity
                if new_qty <= 0:
                    self.cart_items.pop(i)
                else:
                    self.cart_items[i] = (prod, new_qty)
                self._recalculate_total()
                return

    def _recalculate_total(self):
        self.total_price = 0.0
        for prod, qty in self.cart_items:
            self.total_price += prod.price * qty

    def calculate_total(self):
        """
        Returns the current total price of the cart.
        """
        return self.total_price

    def show_cart(self):
        """
        Print the items and their quantities, plus total cost.
        """
        print("---- Cart Contents ----")
        for product, quantity in self.cart_items:
            line_price = product.price * quantity
            print(f"{product.name} x {quantity} = {line_price:.2f}")
        print(f"Total Price: {self.total_price:.2f}\n")

if __name__ == "__main__":
    # Example usage:
    p1 = Product(101, "Laptop", 899.99)
    p2 = Product(102, "Mouse", 19.99)
    p3 = Product(103, "USB-C Cable", 9.99)

    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2, quantity=2)
    cart.show_cart()

    cart.remove_product(102, quantity=1)
    cart.add_product(p3, quantity=3)
    cart.show_cart()

    print("Final total:", cart.calculate_total())
