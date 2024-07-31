import logging
from typing import Dict, Optional

from tavern._core.dict_util import check_expected_keys

logger = logging.getLogger(__name__)


class PluginTestSession:
    def __init__(self, **kwargs):
        expected_blocks = {
            # TODO
        }

        check_expected_keys(expected_blocks.keys(), kwargs)

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
        # TODO
        ...
