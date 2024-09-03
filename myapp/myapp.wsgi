#import sys
#import os

# Add the project directory to the sys.path
#sys.path.insert(0, '/var/www/html/litonline/myapp')

# Set the environment variable to point to your Flask app's entry point
#os.environ['FLASK_APP'] = 'app.py'

# Import the Flask app (assuming your Flask app is named `app` in app.py)
#from app import app as application


import sys
import os

# Add the project directory to the sys.path
sys.path.insert(0, '/var/www/html/litonline/myapp')

# Import the Flask app (assuming your Flask app is named `app` in app.py)
from app import app as application

# Optionally set the Flask environment to production
os.environ['FLASK_ENV'] = 'app.py'
