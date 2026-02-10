# Singleton pattern in Python

#from cx_Oracle import SessionPool, InterfaceError
#from sqlite3 import InterfaceError

##################################
# Oracle Session Pool Singleton. #
##################################

class OracleSessionPoolSingleton:
    '''
    Singleton class to provide a pool of DB connections via SessionPooling
    '''
    _instance = None
    _counter = 0 

    class Singleton:
        def __call__(self, *args, **kwargs):
            if OracleSessionPoolSingleton._instance is None:
                OracleSessionPoolSingleton._counter += 1
                OracleSessionPoolSingleton._instance = OracleSessionPoolSingleton(*args, **kwargs)
            return OracleSessionPoolSingleton._instance
        
    get_instance = Singleton()

    def __init__(self, dsn, user, password, min_sesssions=1, max_sessions=4, increment=1):
        ''' 
        # init dunder method
        Initialize the singleton instance with DB connection parameters.
        '''
        if OracleSessionPoolSingleton._instance is not None:
            #raise InterfaceError('DBIHelper: only one instance of OracleSessionPoolSingleton class allowed!')
            raise Exception("This class is a singleton!")

        self.dsn = dsn
        self.user = user
        self.password = password
        self.min_sesssions = min_sesssions
        self.max_sessions = max_sessions
        self.increment = increment  

        # pool variable which is initiated as Non
        self.pool = None

        OracleSessionPoolSingleton._instance = self

    def get_pool(self):
        '''
        Method to get the session pool instance.
        If the pool is not created, it creates a new session pool.
        '''
        if self.pool is None:
            #self.pool = SessionPool(user=self.user,
            #                        password=self.password,
            #                        dsn=self.dsn,
            #                        min=self.min_sesssions,
            #                        max=self.max_sessions,
            #                        increment=self.increment,
            #                        threaded=True)
            self.pool = "Simulated Session Pool"  # Placeholder for actual SessionPool
        return self.pool
    

# Example usage
if __name__ == "__main__":
    # Create singleton instance
    db_pool_singleton = OracleSessionPoolSingleton.get_instance(
        dsn="mydsn",   
        user="myuser", 
        password="mypassword"
    )

    # Get the session pool
    pool = db_pool_singleton.get_pool()
    print(f"Session Pool: {pool}")

    # Verify singleton behavior
    another_instance = OracleSessionPoolSingleton.get_instance(
        dsn="anotherdsn",   
        user="anotheruser",
        password="anotherpassword"
    )   
    print(f"Are both instances the same? {db_pool_singleton is another_instance}")
   