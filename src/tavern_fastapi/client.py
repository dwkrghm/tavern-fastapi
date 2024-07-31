import json as jsonlib
import logging
from typing import Dict, Optional
from urllib.parse import urlencode, urlparse

from fastapi.testclient import TestClient
from tavern._core import exceptions
from tavern._core.dict_util import check_expected_keys
from tavern._core.extfunctions import import_ext_function

logger = logging.getLogger(__name__)


class FastAPITestSession:
    def __init__(self, **kwargs):
        expected_blocks = {
            "app": {
                "location",
            },
        }

        check_expected_keys(expected_blocks.keys(), kwargs)

        try:
            self._app_args = kwargs.pop("app", {})
            app_location = self._app_args["location"]
        except KeyError as e:
            msg = "Need to specify app location (in the form my.module:application)"
            logger.error(msg)
            raise exceptions.MissingKeysError(msg) from e

        self._fastapi_app = import_ext_function(app_location)
        # self._test_client = TestClient(app=self._fastapi_app)

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def make_request(
        self,
        *,
        url: str,
        method: str,
        verify: bool = True,
        headers: Optional[Dict] = None,
        params: Optional[Dict] = None,
        json: Optional[Dict] = None,
        data=None,
    ):
        # This isn't used - won't be using SSL
        if not verify:
            logger.warning("'verify' has no use when using fastapi test client")

        # TODO
        # set host header with url?
        parsed = urlparse(url)
        route = parsed.path

        args = {}

        if headers:
            args["headers"] = headers

        if params:
            args["params"] = params

        if data:
            args["body"] = urlencode(data)

        if json:
            args["json"] = json

        with TestClient(app=self._fastapi_app) as _test_client:
            return _test_client.request(method=method, url=route, **args)
