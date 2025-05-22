#API/Service Object Modeling.
'''
Design an online order service with a RESTful API. We have Order, Item, and a User. Show the Python classes and how you’d handle basic endpoints."
Domain Classes: User (represents cusomter or usr), Item, and Order. 
	-these are like real world entitties modeled in code
Service Layer: Order Service. Manages all in order in-memory dictionaries (self.orders) and has the methods to create new orders, add items and retrieve orders
	-This is the like the backend structural that organizeds data and business logic


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Item:
    def __init__(self, item_id, item_name, price):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price

class Order:
    def __init__(self, order_id, user: User):
        self.order_id = order_id
        self.user = user
        self.items = []
        self.total_price = 0

    def add_item(self, item: Item):
        self.items.append(item)
        self.total_price += item.price

# Example of an in-memory service
class OrderService:
    def __init__(self):
        self.orders = {}
        self.next_order_id = 1

    def create_order(self, user: User):
        order = Order(self.next_order_id, user)
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        return order.order_id

    def add_item_to_order(self, order_id, item: Item):
        if order_id not in self.orders:
            return None
        order = self.orders[order_id]
        order.add_item(item)
        return order

    def get_order(self, order_id):
        return self.orders.get(order_id, None)

    def list_orders(self):
        return list(self.orders.values())
'''

# System Design Interview Summary with Scalability Considerations
# URL Shortening Service (TinyURL)
'''-------------------------------------------------
Core Components:
    - API (REST): Receives long URLs and returns short URLs.
    - Application Layer: Generates a unique short code (e.g., using an auto-increment counter + Base62 encoding).
    - Persistence Layer: Stores mappings (short_code -> long_url) in a database or key-value store.
Key Methods/Functionalities:
    - shortenUrl(longUrl): Generates a short alias.
    - redirect(shortUrl): Retrieves and redirects to the original URL.
Additional Features:
    - Support custom short URLs, track click stats, delete expired URLs.
Scalability Considerations:
    - Use hash tables or in-memory stores (like Redis) for O(1) lookups.
    - Scale API servers horizontally behind a load balancer.
    - Partition the data for high QPS.
    - Use CDN caching for high-frequency redirects.
'''
#Video Streaming Service (YouTube/Netflix)
'''-------------------------------------------------
Core Components:
    - Upload & Transcoding Service: Converts videos to multiple formats.
    - Content Storage: Distributed object storage for video files.
    - CDN: Caches and serves video segments.
    - Metadata Database: Stores video details (title, views, etc.).
    - Search/Recommendation Engine: Supports video discovery.
Key Methods/Functionalities:
    - Upload video, generate manifest files for streaming (HLS/DASH).
    - Record view counts, handle real-time comments.
Scalability Considerations:
    - Distributed storage and transcoding pipelines.
    - CDN usage for global low-latency streaming.
    - Partition metadata (by video ID or region) and use caching.
'''    
# Global Chat Service (Facebook Messenger/WhatsApp)
'''-------------------------------------------------
Core Components:
    - User: Represents a chat user with connection info.
    - Message: Represents an individual message.
    - ChatRoom/Conversation: One-on-one or group chat.
    - Real-Time Communication Service: Handles persistent connections (WebSockets).
Key Methods/Functionalities:
    - send_message(sender, recipient, content)
    - receive_message() and storing chat history.
Scalability Considerations:
    - Use WebSockets or similar protocols for real-time communication.
    - Scale chat servers horizontally; load balancers with user-to-server mapping.
    - Implement fan-out for group chats via a pub/sub system.
    - Use a distributed database for message storage.
    - Handle offline users with push notifications.
    - Implement end-to-end encryption on the client.
'''    
# 4. Social Network / Message Board (Quora/Reddit/HackerNews)
''' -------------------------------------------------
Core Components:
    - Post/Question: User-generated content.
    - Comment: Replies to posts.
    - User: Manages profiles and follow relationships.
    - Feed Service: Generates a timeline based on follows and trending content.
Key Methods/Functionalities:
    - Post content, comment, vote (up/down).
    - Generate personalized news feed.
Scalability Considerations:
    - Choose push (fan-out on write) or pull (fan-out on read) for feeds.
    - Use caching and denormalization for popular posts.
    - Partition data (by topic or user ID) for massive scale.
    - Use search indexing (e.g., Elasticsearch) for fast full-text search.
'''    
# Search Typeahead (Autocomplete)
'''-------------------------------------------------
Core Components:
    - Data Store for Queries: Dictionary, sorted list, or Trie for search queries.
    - Search Service: API endpoint that returns suggestions.
    - Ranking/Scoring: Uses frequency counts for popularity.
Key Methods/Functionalities:
    - autocomplete(prefix): Returns suggestions matching the prefix.
    - Update query frequencies for freshness.
Scalability Considerations:
    - Keep data in memory for low latency (Trie or sorted array).
    - Partition data if large (by locale or first letter).
    - Use efficient algorithms (binary search or O(m) lookup in Trie).
    - Replicate the service across servers behind a load balancer.
'''  
#6. Global File Storage & Sharing Service (Dropbox/Google Drive/Google Photos)
'''-------------------------------------------------
Core Components:
    - Client Applications: Sync files across devices.
    - Upload/Download Service: Handles file transfers (often chunked).
    - Metadata Service: Manages directories, file versions, and permissions.
    - File Storage: Distributed, scalable file storage (cloud object store).
    - Sync Service: Synchronizes files across devices.
Key Methods/Functionalities:
    - Upload, download, search, share, and delete files.
    - Automatic synchronization and version control.
Scalability Considerations:
    - Use chunking and resumable uploads for large files.
    - Partition metadata by user; use distributed storage.
    - Implement caching for frequently accessed files/directories.
    - Ensure ACID transactions for metadata operations.
'''
# 7. Web Crawler
''' -------------------------------------------------
Core Components:
    - URL Frontier: Queue for URLs to be crawled.
    - Crawler Workers: Fetch pages concurrently.
    - HTML Parser: Extract links from pages.
    - Deduplication Store: Avoid revisiting the same URL (e.g., Bloom filter).
    - Robots.txt Manager: Respects crawling rules.
Key Methods/Functionalities:
    - enqueue_url(url), fetch_page(url), parse_page(content)
    - Schedule recrawls for dynamic pages.
Scalability Considerations:
    - Distribute crawling tasks across machines.
    - Partition the URL frontier (by domain or hash).
    - Use asynchronous I/O to handle many simultaneous network requests.
    - Ensure fault tolerance with persistent crawl state.
'''
# 8. Social Media Service (Facebook/Twitter/Instagram)
''' -------------------------------------------------
Core Components:
    - User: Stores profiles and follow relationships.
    - Post/Tweet: User content (text, images, videos).
    - News Feed Service: Aggregates and ranks posts.
    - Interaction Services: Manage likes, comments, direct messages.
    - Search & Trending: Supports discovery of content.
Key Methods/Functionalities:
    - Post content, reply, vote, and generate a personalized feed.
Scalability Considerations:
    - Decide between push (fan-out on write) and pull (fan-out on read) for feeds.
    - Use caching and denormalization to support high read traffic.
    - Partition data by user or region; implement a scalable social graph.
'''   
# Ride-Sharing Service (Uber/Lyft)
''' -------------------------------------------------
Core Components:
    - Mobile Apps (Driver & Rider): Interfaces for ride requests and location updates.
    - Backend API/Gateway: Processes ride requests and tracks trips.
    - Dispatch Service: Matches riders with nearby drivers using geospatial queries.
    - Real-Time Location Service: Maintains drivers’ positions.
    - Trip Manager: Tracks ride states and manages transitions.
    - Mapping & Routing Service: Calculates routes and ETAs.
    - Payment Service: Processes fare calculations and payments.
Key Methods/Functionalities:
    - request_ride(), update_location(), assign_driver(), complete_trip()
Scalability Considerations:
    - Use geospatial indexing (e.g., Redis GEO) for fast driver queries.
    - Partition dispatch services by geographic region.
    - Use asynchronous messaging for ride assignment and notifications.
    - Ensure high availability and low latency with redundant services.
'''
# API Rate Limiter (GitHub API Example)
''' -------------------------------------------------
Core Components:
    - Client Identifier: API key, user ID, or IP address.
    - Rate Limiting Rules: Define limits and time windows.
    - Counter Store: In-memory store (e.g., Redis) to track requests.
    - Middleware: Checks counts and enforces limits.
Key Methods/Functionalities:
    - is_allowed(client_id): Increments the counter and returns allowance status.
    - reset_counters(): Automatically resets counts after time windows.
Scalability Considerations:
    - Use a centralized store (Redis) with atomic increments and key expiration.
    - For distributed systems, ensure all API servers share rate limit data.
    - Consider token bucket or sliding window algorithms for smoother throttling.
'''
# Notification System (Push Notifications)
'''-------------------------------------------------
Core Components:
    - Notification: Represents a message (content, type, timestamp).
    - User: Stores user info and preferences (delivery channels).
    - DeliveryMethod: Abstracts channels like email, SMS, or push.
    - Notification Service: Manages creation, management, and dispatch.
Key Methods/Functionalities:
    - create_notification(user, message, type)
    - send_notification(user, notification)
    - manage_notifications(user): Viewing, marking as read, or deleting.
Scalability Considerations:
    - Use an event-driven architecture with message queues (Kafka) to decouple creation from delivery.
    - Scale delivery services horizontally by channel.
    - Cache user preferences and implement throttling/batching for high volumes.
    - Ensure high availability with redundant servers and secure token management.
'''
# Conclusion
''' Mastering system design involves not only defining core components and functionalities, but also addressing real-world scalability, fault tolerance, and performance. Be prepared to discuss:
    - How your components interact.
    - Trade-offs between simplicity and efficiency.
    - Techniques like caching, data partitioning, load balancing, and asynchronous processing.
    
These are common discussion points in interviews for backend and system architecture roles. Use this summary to guide your conversation and to demonstrate both your technical depth and your practical approach to scalable system design.'''
