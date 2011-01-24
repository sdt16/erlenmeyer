from flask import Flask
import settings

app = Flask('erlenmeyer')
app.config.from_object('erlenmeyer.settings')

import views
