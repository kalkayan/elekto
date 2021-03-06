# Copyright 2020 Manish Sahani
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
#
# Author(s):         Manish Sahani <rec.manish.sahani@gmail.com>

import os
from dotenv import load_dotenv

# Load the custom environment file into the program
targetenv = '.env.testing' if os.getenv('TESTING') else '.env'
load_dotenv(os.path.join(os.path.dirname(__file__), targetenv))


def env(key, default=None):
    v = os.getenv(key)
    return default if v is None or v == '' else v
