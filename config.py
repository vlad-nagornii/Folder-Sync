import json

config_file = 'config.json'

# Initial configuration
initial_config = {
    "sync_interval": 60,
    "source_path": "",
    "replica_path": "",
    "log_path": ""
}

# Create and write the initial configuration to config.json
def create_initial_config():
    with open(config_file, 'w') as file:
        json.dump(initial_config, file, indent=4)

# Function to load configuration
def load_config():
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

# Function to save configuration
def save_config(config):
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)

# Function to get a configuration value
def get_config_value(key):
    config = load_config()
    return config.get(key)

# Function to set a configuration value
def set_config_value(key, value):
    config = load_config()
    config[key] = value
    save_config(config)
