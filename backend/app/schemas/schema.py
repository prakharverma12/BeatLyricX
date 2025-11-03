from pydantic import BaseModel, Field, ConfigDict, BeforeValidator
from bson import ObjectId
from typing import Optional, Annotated

# -------------------------------------------------------------------
# 1. Pydantic V2 Way to Handle ObjectId
#
# We use 'Annotated' to add a 'BeforeValidator'.
# This validator will run *before* Pydantic checks the type.
# It checks if the input is a valid ObjectId and converts it.
# -------------------------------------------------------------------

def validate_object_id(v: any) -> ObjectId:
    """Validates that a value is a valid ObjectId."""
    if isinstance(v, ObjectId):
        return v
    if ObjectId.is_valid(v):
        return ObjectId(v)
    raise ValueError("Invalid ObjectId")

def convert_object_id_to_str(v: any) -> str:
    """Converts a valid ObjectId to a string."""
    if isinstance(v, ObjectId):
        return str(v)
    if ObjectId.is_valid(v):
        return str(v)
    raise ValueError("Invalid ObjectId for string conversion")

# This annotated type will be used for 'UserInDB'
# It ensures the data *is* an ObjectId
PyObjectId = Annotated[ObjectId, BeforeValidator(validate_object_id)]

# This annotated type will be used for 'UserResponse'
# It takes an ObjectId and validates it as a string
StrFromObjectId = Annotated[str, BeforeValidator(convert_object_id_to_str)]


# -------------------------------------------------------------------
# 2. Your Schemas (Updated for Pydantic V2)
# -------------------------------------------------------------------

class UserBase(BaseModel):
    username: str
    is_active: bool = True

class UserCreate(UserBase):
    password: str

# -------------------------------------------------------------------
# 3. Model for data *in the database*
# -------------------------------------------------------------------
class UserInDB(UserBase):
    # 'id' is aliased to '_id' and uses our V2 validator
    id: PyObjectId = Field(alias="_id")
    hashed_password: str

    # V2 Config: 'class Config' is replaced by 'model_config'
    model_config = ConfigDict(
        populate_by_name=True,       # Replaces 'allow_population_by_field_name'
        from_attributes=True,        # Replaces 'orm_mode'
        arbitrary_types_allowed=True,# This is still needed
        json_encoders={ObjectId: str} # This still works for *serialization*
    )

# -------------------------------------------------------------------
# 4. Model for data *sent to the client*
# -------------------------------------------------------------------
class UserResponse(UserBase):
    # 'id' is aliased to '_id' and uses our V2 string converter
    id: StrFromObjectId = Field(alias="_id")

    # V2 Config
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )