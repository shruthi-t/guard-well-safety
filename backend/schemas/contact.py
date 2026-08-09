from pydantic import BaseModel, ConfigDict


# Create Contact
class ContactCreate(BaseModel):
    user_id: int
    contact_name: str
    contact_mobile: str


# Response
class ContactResponse(BaseModel):
    id: int
    user_id: int
    contact_name: str
    contact_mobile: str

    model_config = ConfigDict(from_attributes=True)