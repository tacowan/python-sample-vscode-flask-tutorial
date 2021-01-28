import os
from flask import Flask  # Import the Flask class
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
app = Flask(__name__)    # Create an instance of the class for our use
app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = os.getenv('APPINSIGHTS_INSTRUMENTATIONKEY')

middleware = FlaskMiddleware(
    app,
    exporter=AzureExporter(connection_string="InstrumentationKey=" + app.config['APPINSIGHTS_INSTRUMENTATIONKEY']),
    sampler=ProbabilitySampler(rate=1.0),
)