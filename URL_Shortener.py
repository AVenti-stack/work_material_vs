'''
source: https://educative.pxf.io/tinyURL

THINGS TO DISCUSS AND ANALYZE
1. Given a long URL, the service should generate a shorter and unique alias for it
2. When tahe user hits a short link, the service should redirect to the original link
3. Consider scalability if 1000's URL shortening requests come every second
4. Service handle redirects
5. Track click stats 
6. Delete exprired URLS
7. The system should be highly available

THINGS TO CONSIDER WHEN DESIGNING THE SERVICE 
1. API(REST) - Discuss how the client will follow an approach to communucate with the service along with teh load
balance which is the front end of the service 
2. APPLICATION LAYER - Discuss how the worker thread or hosts that will take the long URL, generate the 
tiny URL and how it will store both of the URLs in the database
3. PERSISTANCE LAYER - Database

'''