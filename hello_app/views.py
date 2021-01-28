import logging
from datetime import datetime
from flask import Flask, render_template
from . import app
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=' + app.config['APPINSIGHTS_INSTRUMENTATIONKEY'])
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/api/exception")
def badder_stuff():
    # Use properties in exception logs
    programming_languages = ["Java", "Python", "C++"]
    language = programming_languages[100]
    return "uho"

@app.errorhandler(500)
def handle_internal_server_error(e):
    original = getattr(e, "original_exception", None)
    print(original)
    logger.exception('Captured an exception.', exc_info=original)
    return render_template('500.html'), 500