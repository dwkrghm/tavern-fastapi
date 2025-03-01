import logging
import typing
from os.path import abspath, dirname, join
from typing import Dict

import yaml
from tavern._core.dict_util import format_keys

from .client import FastAPITestSession
from .request import FastAPIRequest
from .response import FastAPIResponse

if typing.TYPE_CHECKING:
    from tavern._core.pytest.config import TestConfig

logger = logging.getLogger(__name__)

session_type = FastAPITestSession

request_type = FastAPIRequest
request_block_name = "request"


def get_expected_from_request(
    response_block: Dict, test_block_config: "TestConfig", session
):
    f_expected = format_keys(response_block, test_block_config.variables)
    return f_expected


verifier_type = FastAPIResponse
response_block_name = "response"

schema_path = join(abspath(dirname(__file__)), "schema.yaml")
with open(schema_path, "r") as schema_file:
    schema = yaml.load(schema_file, Loader=yaml.SafeLoader)
