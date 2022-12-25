from config import get_config

config = get_config()

# Use config variables
print(config["DATABASE_CONNECTION_STRING"])
