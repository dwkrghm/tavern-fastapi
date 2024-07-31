import functools
import logging
import typing
from typing import Dict

import requests
from box import Box
from tavern._core import exceptions
from tavern._core.dict_util import check_expected_keys
from tavern.request import BaseRequest

from tavern_plugin.client import PluginTestSession

if typing.TYPE_CHECKING:
    from tavern._core.pytest.config import TestConfig
from tavern._plugins.rest.request import get_request_args

logger = logging.getLogger(__name__)


class PluginRequest(BaseRequest):
    def __init__(self, session: PluginTestSession, rspec: Dict, test_block_config: "TestConfig"):
        """Prepare request

        Args:
            rspec: test spec
            test_block_config: Any configuration for this the block of
                tests

        Raises:
            UnexpectedKeysError: If some unexpected keys were used in the test
                spec. Only valid keyword args to requests can be passed
        """

        expected = {
            "method",
            "url",
            "headers",
            "data",
            "params",
            "auth",
            "json",
            "verify",
            # "files",
            # "cookies",
            # "hooks",
        }

        check_expected_keys(expected, rspec)

        request_args = get_request_args(rspec, test_block_config)

        logger.debug("Request args: %s", request_args)

        self._request_args = request_args

        self._prepared = functools.partial(session.make_request, **request_args)

    def run(self):
        """Runs the prepared request and times it

        Todo:
            time it

        Returns:
            requests.Response: response object
        """

        return self._prepared()

    @property
    def request_vars(self):
        return Box(self._request_args)
