"""
Implementation of the Proxy Pattern

In this example:

    We define an APIService interface with a fetch_data method.
    We implement a RealAPIService class that represents the actual API service.
    We create a CachedAPIProxy class that acts as a proxy to control access to RealAPIService and provides caching. 
"""


# Step 1: Define the API Service Interface

from abc import ABC, abstractmethod

class APIService(ABC):
    @abstractmethod
    def fetch_data(self, url: str) -> str:
        pass

# Step 2: Implement the Real API Service

class RealAPIService(APIService):
    def fetch_data(self, url: str) -> str:
        print(f"Fetching data from {url}")
        # Simulate network delay
        return f"Data from {url}"

"""
Step 3: Create the Cached Proxy

The CachedAPIProxy class acts as a proxy to RealAPIService and caches data to avoid repeated network calls for the same URL.
"""


class CachedAPIProxy(APIService):
    def __init__(self):
        self._real_service = RealAPIService()
        self._cache = {}

    def fetch_data(self, url: str) -> str:
        # Check if data is in the cache
        if url in self._cache:
            print(f"Retrieving cached data for {url}")
            return self._cache[url]

        # If not in cache, fetch from the real API service and store it in the cache
        data = self._real_service.fetch_data(url)
        self._cache[url] = data
        return data


# Usage

# Create the proxy instance
proxy_service = CachedAPIProxy()

# Fetch data using the proxy
print(proxy_service.fetch_data("https://api.example.com/data1"))
print(proxy_service.fetch_data("https://api.example.com/data1"))  # This should retrieve cached data
print(proxy_service.fetch_data("https://api.example.com/data2"))  # New URL, so fetch from real service
print(proxy_service.fetch_data("https://api.example.com/data2"))  # Cached data for this URL
