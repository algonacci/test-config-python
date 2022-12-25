from dotenv import dotenv_values

environment = 'production'


def get_config():
    if environment == 'development':
        config = dotenv_values(".development.env")
        return config
    elif environment == 'staging':
        config = dotenv_values(".staging.env")
        return config
    elif environment == 'production':
        config = dotenv_values(".production.env")
        return config
    else:
        raise ValueError('Invalid environment')
