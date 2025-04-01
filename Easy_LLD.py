# source: https://www.finalroundai.com/blog/low-level-design-interview-questions
# https://www.geeksforgeeks.org/top-10-system-design-interview-questions-and-answers/
# https://github.com/ashishps1/awesome-low-level-design

# Encode and Decode TinyURL (MEDIUM)
# LLD Questions Easy
class Codec:
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

