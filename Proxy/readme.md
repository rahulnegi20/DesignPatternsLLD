The Proxy Pattern is a structural design pattern that provides a placeholder or surrogate for another object to control access to it. The proxy object has the same interface as the original object, allowing it to act as an intermediary to add additional functionalities like access control, lazy initialization, logging, or caching without modifying the original class.
Real-Life Example: Network Request Caching

Consider an application that fetches data from an external API. If the data does not change frequently, we could introduce a proxy to cache the data instead of fetching it repeatedly. This proxy will make a network call only when the data isn’t available in the cache.
Implementation of the Proxy Pattern

In this example:

    We define an APIService interface with a fetch_data method.
    We implement a RealAPIService class that represents the actual API service.
    We create a CachedAPIProxy class that acts as a proxy to control access to RealAPIService and provides caching.


Explanation

    RealAPIService: This is the actual service that fetches data. It represents the real object which could be costly to create or call frequently.
    CachedAPIProxy: This is the proxy that controls access to the RealAPIService. It stores fetched data in _cache and returns cached data when available, reducing network calls.
    Client Code: The client code interacts with the APIService through CachedAPIProxy. It doesn’t need to know whether data is coming from the real service or the cache.

Real-World Use Cases for the Proxy Pattern

    Lazy Initialization: Creating objects only when they are needed. This is especially useful for resource-intensive objects.
    Access Control: Controlling access to sensitive resources by introducing an authorization check in the proxy.
    Remote Proxy: Representing an object in a different address space (e.g., handling communication between client and server).
    Virtual Proxy: Used in situations where creating an expensive object on the fly is avoided by using a lightweight proxy.
    Logging/Monitoring: The proxy can log requests or monitor usage statistics without changing the real object.

The Proxy Pattern is especially valuable when access to an object needs to be controlled, or when there’s a need for added functionality such as caching, access control, or logging without altering the original object.