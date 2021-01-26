from flask import Flask  # Import the Flask class
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.ext.flask.flask_middleware import FlaskMiddleware
from opencensus.trace.samplers import ProbabilitySampler
app = Flask(__name__)    # Create an instance of the class for our use

middleware = FlaskMiddleware(
    app,
    exporter=AzureExporter(connection_string="InstrumentationKey=[your key goes here]"),
    sampler=ProbabilitySampler(rate=1.0),
)
