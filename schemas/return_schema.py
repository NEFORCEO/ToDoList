from pydantic import BaseModel

class StaticResponse(BaseModel):
    id: int
    title: str  
    task_name: str 
    
    model_config = {"from_attributes": True}
    
class ResponseSchema(BaseModel):
    status: int 
    result: list[StaticResponse] 
