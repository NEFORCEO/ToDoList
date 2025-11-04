from pydantic import BaseModel

class StaticResponse(BaseModel):
    id: int
    title: str  
    task_name: str 
    
    model_config = {"from_attributes": True}
    
class ResponseGetSchema(BaseModel):
    status: int 
    result: list[StaticResponse] 
    
class ResponseGETINTSchema(BaseModel):
    status: int
    result: StaticResponse
    
    
class ResponsePOSTSchema(BaseModel):
    status: int
    id: int
    title: str 
    task_name: str
    
class ResponsePATCHSchema(BaseModel):
    status: int 
    title: str
    
class ResponseDELETESchema(BaseModel):
    status: int 
    result: str 