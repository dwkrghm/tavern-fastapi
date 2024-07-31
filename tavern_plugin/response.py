import logging

import flask
from tavern._plugins.rest.response import RestResponse

logger = logging.getLogger(__name__)


class PluginResponse(RestResponse):
    """Response verifier"""

    def verify(self, response: flask.Response):
        ...
        # TODO