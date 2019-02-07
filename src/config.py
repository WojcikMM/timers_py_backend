jwt_settings: {} = {
    'issuer': 'timers.com',
    'secret': 'my_secret_change_this!',
    'expiration_time_seconds': 600,
    'algorithm': 'HS256'
}

database_settings: {} = {
    'connection_string': 'mongodb://localhost:27017/',
    'database_name': 'timers'
}