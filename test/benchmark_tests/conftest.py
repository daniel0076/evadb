# coding=utf-8
# Copyright 2018-2022 EVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from test.util import copy_sample_videos_to_upload_dir, file_remove, load_inbuilt_udfs

import pytest

from eva.catalog.catalog_manager import CatalogManager
from eva.server.command_handler import execute_query_fetch_all


@pytest.fixture(autouse=False)
def setup_pytorch_tests():
    file_remove("ua_detrac.mp4")
    CatalogManager().reset()
    copy_sample_videos_to_upload_dir()
    query = """LOAD VIDEO 'ua_detrac.mp4'
                INTO MyVideo;"""
    execute_query_fetch_all(query)
    query = """LOAD VIDEO 'mnist.mp4'
                INTO MNIST;"""
    execute_query_fetch_all(query)
    load_inbuilt_udfs()
    yield None
    file_remove("ua_detrac.mp4")