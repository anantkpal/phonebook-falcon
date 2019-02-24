import os

env = os.environ.get("ENV", "DEV")

_settings = {
    'DEV': {
        'DB_URL': 'postgresql://usr:pass@localhost:5432/contacts'
    },
    'PROD': {
        'DB_URL': 'postgresql://usr:pass@localhost:5432/contacts'
    },
    'TEST': {
        'DB_URL': 'sqlite:///.pytest_cache/contacts.db'
    },
}

SETTINGS = _settings[env]
