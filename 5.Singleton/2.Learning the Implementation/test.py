class Singleton:
    _instance = None  # Static variable to hold the one and only instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Create and store the instance if it doesn't exist
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        print("Initializing Singleton")

# Test
a = Singleton()
b = Singleton()