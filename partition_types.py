from enum import Enum

import uuid

class PartitionTypes(Enum):
    Unused = uuid.UUID('00000000-0000-0000-0000-000000000000')

    MicrosoftBasicData = uuid.UUID('a2a0d0eb-e5b9-3344-87c0-68b6b72699c7')
    LinuxFilesystem = uuid.UUID('af3dc60f-8384-7247-8e79-3d69d8477de4')
