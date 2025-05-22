# source: https://www.finalroundai.com/blog/low-level-design-interview-questions
# https://www.geeksforgeeks.org/top-10-system-design-interview-questions-and-answers/
# https://github.com/ashishps1/awesome-low-level-design

#-----------------------------------EASY LLD------------------------------------------------
# Encode and Decode TinyURL with hashmap backing (MEDIUM)
# LLD Questions Easy
class Encode_Decode_TinyURL:
    def __init__(self) -> None:
        self.URL_Map = {}
        self.counter = 0
    
    def hash_URL(self, url:str) -> str:
        new_url = "bitlil.com/" + str(self.counter)
        self.URL_Map[new_url] = url
        self.counter+=1
        return new_url

    def encode(self, longUrl: str) -> str:
        return self.hash_URL(longUrl)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.URL_Map[shortUrl]

 
# IMPLEMENT SIMPLE IRL SHORTENER -> Descibe what data structure oyu would use to store the mappings
'''
This question evaluates you understanding of dta stuctures and alogorithms, as well as your ability to design and efficient and scalable system

How to answer this question:
1. Identify the core components such as URLShortener, URLMapping, and Database
    - URLShortener -> This handles the user requests for shortening URLS and redirecting them back to the original URLs
    - URLMapping -> Strucutre to store the mapping between the long URL and its short code
    - Database -> For persistance, though in a simple implemation we can start with an in - memory data strucure. 
2. Explain the choice of data structure that you would use like: hash table for storage and retrieval of URL Mapping
    - For this implementation i would use the hash table as the primiary datastructure for fast look-ups and retrieval O(1) 
    - Mapping is short_code -> long_url when user acess the short url the short code will look up in the hash table retrieve og and perform a redirect
    - For encoding i would use the and auto-incrementing counter and convert it to a Base62 string (using digits, lowercase, and uppercase)
3. Dicuss the methods for creating, storing and retrieving shortented URLS
    Ensure they cover essential functions like encoding and decoding URLS then other ones like hashing the URL if needed
4. Scalability: This design is very simple, efficient and scalable. In Production systems i can use persistent key-value store (like redis or a NoSQL database) instead of an in-memory dictionary to handle persistence and high loads

Example Answer:
" To implement a simple URL shortener, I would use a hash table to store the mappings between original URLs and their shortened versions. This allows for efficient storage and retrieval, ensuring quick access to the original URLs when given a shortened link."
'''

# Creating a Class to Represent a Library
'''
Create a class to represent a libary, this class must include methods for adding books, checking out books, and returning books

This evaluates you ability to design a system with multiple functionalities and interactions to demonstrate your understanding of oop principles

1. Identify the core components such as Libaray, Book, and Member
    - Library: books are in the libaray and who has what book checked out hashmap isbn -> member number
    - Book: has isbn, titltle, author and checkout status
    - Memeber: memeber id and books they have checked out: has id number and the books they have checked out
2. Explain the mehods for adding books, checking out books, and returning books, ensuring they cover essential functions
    - add_books(book) : will be adding new books to the libary
    - check_out_books(book, memeber) : remove book from available inv, marks book as checkout, records which mem check out which book, and adds the book to the members list of checkedout book
    - return_book(book) : checks if book is recorded as checked out, remove the book form the member's checkout list and lib record, marks books as available and adds it back to the inv
3. Dicuss the relationships and interactions between these classes, like how Library manages Book invenotry and Memeber Transactions
    - Data Structures: The inventory for books can be set of dictionary for fast lookups and check-out records are maintina in dictionary too
    - Scalability: for a simple design, a list and dict are enough. In a real system we can consider using a database to persist inv and checkout record to handle conccurent updates
    - Relationships: lib manages both the inv (available books) and the checkout process (mapping books to memebers). Memeber class maintain a personal record of their checked-out books, which ties into the lib records
    - Tradeoff: design is simple using so we use dicts, for real systems consider a transcation management, concurrency control and persisten storage

Example answer:
"To create a class representing a library, I would define methods for adding books, checking out books, and returning books. The Library class would manage the inventory of books and track member transactions."

'''

# E-Commerce Shopping Cart
'''
Example Answer:
"To design a basic e-commerce shopping cart, I would create three main classes: Item, ShoppingCart, and Order. The Item class represents a product with an ID, name, and price. The ShoppingCart class maintains a dictionary mapping items to their quantities and provides methods like add_item, remove_item, and checkout. During checkout, the cart calculates the total cost, creates an Order object with the cart’s content, and then clears the cart. This design efficiently handles user operations and can be extended with additional features such as discount handling, inventory checks, or persistence in a database for scalability."

Core Components: 
    - Item: Represents a product that can be purchased
    - Shopping Cart: Manages a collection of items that a user wishes to purchase
    - Order: Represent the finalized purchase, created when the user checks out
Key Methods:
    - add_item(item, quantity): adds a specified item (and its quantity) to the cart
    - remove_item(item, quantity): removes a specified quantity  of an item; if quantity reaches zero, remove the item entirely
    - checkout(): process the items in the cart to create an order, calculate total cost, and possibly clear the cart
Design Considerations:
    - Datastructure: Using a hash map(dict) within the ShoppingCart to map items (or item IDs) to their quantities. This allows for efficient lookups, adds, and removes
    - Scalability: For production systems, the ShoppingCart might be persisted in a database or cache and orders will be stored in a dedicated OrderManagement System
    - Interactions: Shopping card manages the list of item instance. During checkout, it calculates the total cost and creates and Order instance. The Order class would include details like items purchased, total price, and timestamps.

    Class Item:
    Function __init__(item_id, name, price):
        Set self.item_id = item_id
        Set self.name = name
        Set self.price = price

Class ShoppingCart:
    Function __init__():
        // Dictionary mapping item_id to (Item, quantity)
        Set self.items = {}

    Function add_item(item, quantity=1):
        If item.item_id exists in self.items:
            Increase quantity by given amount
        Else:
            Add item to self.items with given quantity

    Function remove_item(item, quantity=1):
        If item.item_id exists in self.items:
            Subtract quantity from existing quantity
            If new quantity <= 0:
                Remove item from self.items
        Else:
            Print "Item not in cart"

    Function checkout():
        total = 0
        For each (item, quantity) in self.items:
            total += item.price * quantity
        Create Order with self.items and total
        Clear self.items (or mark as checked out)
        Return Order

Class Order:
    Function __init__(order_id, items, total, timestamp):
        Set self.order_id = order_id
        Set self.items = items  // the cart items at checkout
        Set self.total = total
        Set self.timestamp = timestamp


'''

# Basic Bank Account
'''
Example answer: "To create a class for a basic bank account, I would define a BankAccount class with an attribute for the balance and a transaction history log. The class would include a deposit method to add money, ensuring the deposit amount is positive, a withdraw method to subtract money while checking that the account has sufficient funds, and a check_balance method to return the current balance. This design clearly separates the financial operations and allows for easy extension, such as recording detailed transaction logs or integrating with other banking services."

Core Components
    - BankAccount: Represents a bank account with an account balance and transaction history
Key Methods
    - deposit(amount): adds funds to the accoutn fi the amount is positive
    - withdraw(amount): subtracts funds form teh account if the amount is pos and not greater than balance
    - check_balance(): return the current balance
Design Considerations
    - Datastructure: used simple class (int) to hold the balance. A list (log) that might be used to store transcation history
    - Scalability: Real world systems, each account's data would be stored in a database with transaction management to ensure consistency, especially under concurrent operations
    - Interactions: BankAccount class directly manages its balance through deposits and withdrawals

    Class BankAccount:
    Function __init__(initial_balance=0):
        Set self.balance = initial_balance
        Set self.transaction_history = []  // list to store transactions

    Function deposit(amount):
        If amount > 0:
            self.balance += amount
            Append ("deposit", amount) to self.transaction_history

    Function withdraw(amount):
        If amount > 0 and amount <= self.balance:
            self.balance -= amount
            Append ("withdraw", amount) to self.transaction_history
        Else:
            Print "Insufficient funds or invalid amount"

    Function check_balance():
        Return self.balance
'''

# Chat Application (like whats apps or fb messender)
'''
"To design a simple chat application, I would include components such as User, Message, and ChatRoom. The User component would handle user authentication and profiles, while the Message component would manage the sending and receiving of messages, and the ChatRoom component would facilitate real-time communication between users.

Explain that when a user sends a message, the ChatRoom stores it and then pushes it to all connected users. For scalability, mention that in production you might use a message broker (e.g., Redis Pub/Sub) to manage chat messages and scale out chat servers." 

Core Components:
    - User: Represents a user (id, name, status, etc)
    - Message: Represents and individual message (content, timestamp, sender)
    - Chatroom: Represents a coversation where multiple people can send and receive messages 
Key Functions:
    - send_message(user, message): user sends a message 
    - receive_message() : methid to get new messages (via push/pull)
    - store_message(message) : save the message in a persistant storage
Desgign and considerations:
    - Real-time communication: use websockets or similar protocal to maintain a persistant bidirectional connection between the clietns and server
    - Mesage Storage: simple system we can use database table that stores it (built-in) for scale use a distributed database
    - Scalability: for many users, use a pub/sub system (redis/kafks) so messages can be braodcst to all participants in the chatroom
    - Tradeoffs: a push mode (server sends message as they arrive) provides for low latency but rquires managing many openin connections

    Persistent Connections: Use an event-driven, non-blocking server (e.g. Node.js, or Python’s asyncio with WebSockets) to handle thousands of simultaneous connections.

    Message Broker: For large-scale systems, integrate a distributed pub/sub system (e.g., Redis Pub/Sub or Apache Kafka) to route messages among servers.

    Horizontal Scaling: Deploy multiple chat server instances behind a load balancer; use sticky sessions or a shared session store to map users to their active connections.

    Data Storage: For chat history, use a scalable NoSQL database that supports fast writes and retrievals, with sharding by chat room or user.

    Fault Tolerance: Ensure that if a server fails, user connections can be seamlessly transferred to another server, and messages aren’t lost (e.g., by persisting messages before broadcasting).`

    Class User:
    Function __init__(user_id, name):
        Set self.user_id = user_id
        Set self.name = name
        Set self.connection = None  // WebSocket or similar connection

Class Message:
    Function __init__(sender, content, timestamp):
        Set self.sender = sender
        Set self.content = content
        Set self.timestamp = timestamp

Class ChatRoom:
    Function __init__(room_id):
        Set self.room_id = room_id
        Set self.users = []          // List of User objects in the room
        Set self.messages = []       // List of Message objects

    Function join(user):
        Append user to self.users

    Function leave(user):
        Remove user from self.users

    Function send_message(sender, content):
        Create message with sender, content, and current timestamp
        Append message to self.messages
        For each user in self.users:
            // If using real-time push, send message via connection
            user.connection.send(message)

    Function get_history():
        Return self.messages

'''

# TO-DO LIST
'''
"To create a class representing a simple to-do list, I would define methods for adding tasks, removing tasks, and marking tasks as complete. The ToDoList class would manage the list of tasks and ensure accurate task handling.

Explain that the ToDoList class is responsible for managing task operations. For an interview, you can note that additional features (like sorting tasks, persistence to a file or database, or due dates) could be added as needed."

Core Components:
    - Task: Represent the todo list task with a description and status
    - List: hold all of the todo-tasks 
Key Functions:
    - Check_todo(): check the status of the todo task (done or not)  OPTIONAL
    - Done(task) : marks the task as dont and crosses it off the list
    - remove(task) : remove the task if it is marked done
    - add(task): add a new task to the list
Scalability:
    - Persistence: for production , store task in database so data is not list between sessions
    - Concurrency: for high usage, ensure updates (makring a task complete) are transactionally safe, especially if multiple people update at once
    - API Layer: Wrap the todo list functionality behind a rest API to serve multiple users and scale horizontally 


Class Task:
    Function __init__(task_id, description):
        Set self.task_id = task_id
        Set self.description = description
        Set self.is_complete = False

    Function mark_complete():
        Set self.is_complete = True

Class ToDoList:
    Function __init__():
        Set self.tasks = []  // List to hold Task objects

    Function add_task(task):
        Append task to self.tasks

    Function remove_task(task_id):
        For each task in self.tasks:
            If task.task_id equals task_id:
                Remove task from self.tasks
                Break

    Function mark_task_complete(task_id):
        For each task in self.tasks:
            If task.task_id equals task_id:
                task.mark_complete()
                Break

    Function list_tasks():
        Return self.tasks

'''

# Basic File Transfer
'''
"To design a basic file system, I would create classes such as File, Directory, and FileSystem. The File class would handle file-specific operations, while the Directory class would manage collections of files and subdirectories.

Explain that the FileSystem class holds the root Directory, and navigation changes the current working directory. The Directory class manages collections of files and subdirectories. In a full design, you’d store metadata (permissions, timestamps) and handle edge cases (like circular links or deletion of non-empty directories)."

Core Components:
    - File: Represents a file with a name and content 
    - Directory: holds all the files and sub-directories 
    - FileSystem: Manages the hierachy of the directories and files
Key Method:
    - create_file(name, content): creates a new file
    - delete_file(name) : delete the file
    - create_directory(name): delete the directory
    - navigate(path) : change current working directory

    Persistence & Metadata: In real file systems, metadata (permissions, timestamps) is stored in a persistent database or a dedicated filesystem structure.

    Performance: For fast file access, file systems use caching (in-memory caches) and efficient indexing of directories.

    Concurrency: Handle concurrent file operations by locking directories or using transactions to ensure consistency, especially when multiple users are interacting with the system simultaneously.

    Hierarchical Storage: A real system must manage storage space, file fragmentation, and possible network storage. Distributed file systems (like HDFS) or cloud storage systems are used at scale.

    Extensibility: The design can be extended to support file versioning, search capabilities, and integration with security and user authentication systems.

Class File:
    Function __init__(name, content=""):
        Set self.name = name
        Set self.content = content

Class Directory:
    Function __init__(name):
        Set self.name = name
        Set self.files = {}         // Map: file name -> File
        Set self.subdirectories = {} // Map: directory name -> Directory

    Function add_file(file):
        Set self.files[file.name] = file

    Function remove_file(file_name):
        If file_name in self.files:
            Delete self.files[file_name]

    Function add_subdirectory(directory):
        Set self.subdirectories[directory.name] = directory

    Function remove_subdirectory(directory_name):
        If directory_name in self.subdirectories:
            Delete self.subdirectories[directory_name]

Class FileSystem:
    Function __init__():
        Set self.root = Directory("root")
        Set self.current_directory = self.root

    Function create_file(name, content=""):
        Create file = File(name, content)
        self.current_directory.add_file(file)

    Function delete_file(name):
        self.current_directory.remove_file(name)

    Function create_directory(name):
        Create directory = Directory(name)
        self.current_directory.add_subdirectory(directory)

    Function change_directory(path):
        // If path is "..", move up; if a directory name, move down into it.
        If path equals "..":
            // Logic to move up to parent (assuming we store parent pointers)
            self.current_directory = self.current_directory.parent  // if exists
        Else if path in self.current_directory.subdirectories:
            Set self.current_directory = self.current_directory.subdirectories[path]
        Else:
            Print "Directory not found."

'''

# Game Scoreboard
'''
"To create a class for a simple game scoreboard, I would define methods for adding players and updating scores. The GameScoreboard class would manage the list of players and ensure accurate score tracking for each player.

Explain that the GameScoreboard class keeps track of players and their scores using a dictionary for efficient lookups. When updating the score, it simply adjusts the score field, and when retrieving the scoreboard, it sorts the players by their score. This is simple but can be extended (e.g., maintaining a sorted data structure for real-time updates, supporting pagination, or handling concurrent updates in a distributed system)."

Core Components:
    - Player: name, score
    - Game: holds the player, tracks player score
Key Methods:
    - add_player(player): add a player to the game
    - update_score(player,score): update the players score
    - get_scoreboard(): get all the score of all players (sorted)

Scalability Considerations:

    For a chat app, mention using WebSockets, load balancing, and distributed message brokers.

    For the shopping cart and to-do list, discuss persistence and handling concurrent modifications using transactions or in-memory caches.

    For the file system, highlight the need for caching, distributed storage, and metadata indexing.

    For the scoreboard, mention data structures (like Redis Sorted Sets) for real-time updates and scaling with large numbers of players.

Class Player:
    Function __init__(player_id, name):
        Set self.player_id = player_id
        Set self.name = name
        Set self.score = 0

    Function update_score(points):
        Set self.score += points

Class GameScoreboard:
    Function __init__():
        Set self.players = {}  // Map: player_id -> Player

    Function add_player(player):
        Set self.players[player.player_id] = player

    Function update_score(player_id, points):
        If player_id in self.players:
            self.players[player_id].update_score(points)
        Else:
            Print "Player not found."

    Function get_scoreboard():
        Return sorted list of self.players.values() by score in descending order

'''

# Notification System
'''
"To design a notification system, I would include components such as Notification, User, and DeliveryMethod. The Notification component would handle the creation and management of notifications, while the User component would manage user preferences and the DeliveryMethod component would handle the delivery channels like email, SMS, and push notifications."

Core Components:
    - Notifications: Represent a single notification (mesage, type, timestamp,etc)
    - Users: Represent the recipent, incliding preferences (preferred delivery)
    - DeliveryMethod: Represents delivery channel (email, sns, push notification)
    - Notification Service: main service that creates, manages, and sends notifications

Key Methods:
    - create_notications(user, message, type): create new notifications
    - send_noticiation(notification): determine the user's preference and send the notification via the chosen delievery method
    - manage_notification(user): allows the user to view, mark as read or delete notifications

Scalability and Real-World Considerations:
    - Event-Driven Architecture: For high volume, notifications are processed via a message queue (e.g., Kafka, RabbitMQ) so that creation and delivery can be decoupled and scaled independently.

    - Delivery Channels: Each channel (email, SMS, push) is handled by separate microservices that can be scaled according to load.

    - User Preferences & Filtering: A caching layer (e.g., Redis) might store user preferences for fast lookup.

    - High Availability: Redundant notification servers and a distributed queue ensure that notifications are delivered even if one component fails.

Class Notification:
    Function __init__(notification_id, message, type, timestamp):
        Set self.notification_id = notification_id
        Set self.message = message
        Set self.type = type
        Set self.timestamp = timestamp
        Set self.is_read = False

Class User:
    Function __init__(user_id, name, preferences):
        Set self.user_id = user_id
        Set self.name = name
        Set self.preferences = preferences  // e.g., {"email": True, "sms": False, "push": True}
        Set self.notifications = []         // List of Notification objects

Class DeliveryMethod:
    // Abstract base or interface
    Function send(user, notification):
        // Implementation depends on channel (email, SMS, push)

Class NotificationService:
    Function __init__():
        // Could be backed by a database or in-memory store
        Set self.notification_store = {}  // Map: notification_id -> Notification
        Set self.next_notification_id = 1

    Function create_notification(user, message, type):
        notification = new Notification(self.next_notification_id, message, type, current_time)
        self.notification_store[self.next_notification_id] = notification
        self.next_notification_id += 1
        Append notification to user.notifications
        Return notification

    Function send_notification(user, notification):
        For each channel, enabled in user.preferences:
            Call DeliveryMethod[channel].send(user, notification)

    Function mark_as_read(user, notification_id):
        Find notification in user.notifications matching notification_id and set is_read = True



'''

# Simple Social Media Post (twitter, fb , isntagram)
'''
Core Components:
    -SocialMediaPost: represent the post with content, likes, and comments
    -like: record of users who liked their post (maybe)
    - comment( comment on post and timestamp, and commenter)
Key Methods:
    -like(): increment like count
    -comment(text): append new comment
    - get_post_details(): returns the number of likes, commenter, and content

Scalability and Real-World Considerations:
    High Read and Write Volume: For a popular post, likes and comments can be very frequent. In production, likes might be stored in a distributed counter (e.g., Redis Sorted Sets) to handle rapid updates.

    Caching: Frequently viewed posts can be cached to reduce database load.

    Denormalization: Comments might be stored separately in a NoSQL store for fast retrieval, with a reference in the post.

    Data Partitioning: If posts become numerous, partition by user or post ID ranges.

Class SocialMediaPost:
    Function __init__(post_id, content):
        Set self.post_id = post_id
        Set self.content = content
        Set self.likes = 0
        Set self.comments = []  // List of Comment objects

    Function like():
        Increment self.likes by 1

    Function comment(comment_text, user, timestamp):
        Create new_comment = new Comment(user, comment_text, timestamp)
        Append new_comment to self.comments

    Function get_post_details():
        Return { "content": self.content, "likes": self.likes, "comments": self.comments }

Class Comment:
    Function __init__(user, content, timestamp):
        Set self.user = user
        Set self.content = content
        Set self.timestamp = timestamp

'''

# Create a Class for a Simple Recipe Manager
'''
Core Components:
    - Recipe: Represents a recipe with a name, ingredients, and instructions.

    - RecipeManager: Manages a collection of Recipe objects.

Key Methods:
    - add_recipe(recipe): Add a new recipe.

    - remove_recipe(recipe_name): Remove a recipe by name.

    - search_recipe(recipe_name): Retrieve a recipe by name.

Scalability and Real-World Considerations:
    Data Storage: For a production system, recipes would be stored in a persistent database. For high availability, consider a NoSQL store if the dataset grows large.

    Search Efficiency: To support searching (by name or ingredient), indexing or a full-text search engine (like Elasticsearch) might be needed.

    Caching: Frequently accessed recipes can be cached in memory to improve read performance.

    Extensibility: The system could later support user ratings, comments, and categorization, which would affect data structure choices and require additional relationships.

Class Recipe:
    Function __init__(name, ingredients, instructions):
        Set self.name = name
        Set self.ingredients = ingredients  // List of ingredients
        Set self.instructions = instructions  // String or list of steps

Class RecipeManager:
    Function __init__():
        Set self.recipes = {}  // Map: recipe name -> Recipe

    Function add_recipe(recipe):
        Set self.recipes[recipe.name] = recipe

    Function remove_recipe(recipe_name):
        If recipe_name in self.recipes:
            Delete self.recipes[recipe_name]

    Function search_recipe(recipe_name):
        Return self.recipes.get(recipe_name, None)

'''

# Basic Inventory Management
'''
Core Components:

    Item: Represents a product with an ID, name, price, and stock quantity.

    Order: Represents an order for items (can include quantity, order date, etc.).

    Inventory: Manages a collection of Item objects and tracks stock levels.

    Order Processing: Handles purchase transactions and updates stock accordingly.

Key Methods:

    add_item(item): Add a new item to inventory.

    remove_item(item): Remove an item from inventory.

    update_stock(item, quantity): Increase or decrease stock.

    process_order(order): Deduct stock for each item in the order and record the order.

Scalability & Real-World Considerations:

    Concurrency: In high-volume inventory systems, concurrent orders may attempt to update stock. Using transactions or atomic counters in a database can prevent overselling.

    Database Sharding: For a large inventory, items can be partitioned by categories or by item ID range across multiple database nodes.

    Caching: Frequently accessed inventory data can be cached to reduce database load, especially for read-heavy operations like checking stock levels.

    Integration: Inventory systems often integrate with e-commerce frontends, payment gateways, and shipping services. This design can be extended by adding classes to handle these integrations.

    Event-Driven Updates: Orders may generate events (e.g., "stock low" notifications) that trigger automatic reordering. A message queue could help distribute these events.

Class Item:
    Function __init__(item_id, name, price, stock):
        Set self.item_id = item_id
        Set self.name = name
        Set self.price = price
        Set self.stock = stock

    Function update_stock(quantity):
        Set self.stock = self.stock + quantity  // quantity can be negative

Class Order:
    Function __init__(order_id, items):
        // items: Map of item_id -> quantity purchased
        Set self.order_id = order_id
        Set self.items = items
        Set self.timestamp = current_time

Class Inventory:
    Function __init__():
        Set self.items = {}  // Map: item_id -> Item

    Function add_item(item):
        Set self.items[item.item_id] = item

    Function remove_item(item_id):
        If item_id in self.items:
            Delete self.items[item_id]

    Function update_stock(item_id, quantity):
        If item_id in self.items:
            self.items[item_id].update_stock(quantity)

    Function process_order(order):
        For each (item_id, quantity) in order.items:
            If item_id in self.items and self.items[item_id].stock >= quantity:
                self.items[item_id].update_stock(-quantity)
            Else:
                Return "Insufficient stock for item: " + item_id
        // Record order in order history (could be a list or database)
        Append order to OrderHistory
        Return "Order processed successfully"


'''