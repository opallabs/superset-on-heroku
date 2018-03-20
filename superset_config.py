import os
#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
# ROW_LIMIT = 5000
SUPERSET_WORKERS = 16 # for it to work in heroku basic/hobby dynos increase as you like
SUPERSET_WEBSERVER_PORT = os.environ['PORT']
#---------------------------------------------------------
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY')

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = os.environ['SECRET_KEY']

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# Superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


CACHE_CONFIG = {
'CACHE_TYPE': 'redis',
'CACHE_KEY_PREFIX': 'superset_cache',
'CACHE_REDIS_HOST': 'ec2-54-174-198-121.compute-1.amazonaws.com',
'CACHE_REDIS_PORT': 7819,
'CACHE_REDIS_DB': 0,
'CACHE_REDIS_URL': 'redis://h:pd9fe08e309449296cda1d76d4bc6d6e0ae24165adf28914141375c49016d2a23@ec2-54-174-198-121.compute-1.amazonaws.com:7819'
}

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = CSRF_ENABLED = True

# use inserted X-Forwarded-For/X-Forwarded-Proto headers
ENABLE_PROXY_FIX = True
SQLLAB_ASYNC_TIME_LIMIT_SEC = 1000
SQLLAB_TIMEOUT = 1000
SUPERSET_WEBSERVER_TIMEOUT = 1000

