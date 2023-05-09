#  Copyright 2021-present, the Recognai S.L. team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

if sys.version_info > (3, 7):
    from typing import Literal
else:
    from typing_extensions import Literal

from argilla.server.models import FieldType


class TextFieldSettings(BaseModel):
    type: Literal[FieldType.text]


class Field(BaseModel):
    id: UUID
    name: str
    title: str
    required: bool
    settings: TextFieldSettings
    dataset_id: UUID
    inserted_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
