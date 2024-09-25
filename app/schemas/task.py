from pydantic import BaseModel



class TaskBase(BaseModel):

    title: str
    description: str | None = None



class TaskCreate(TaskBase):

    pass



class TaskOut(TaskBase):

    id: int
    completed: bool
    owner_id: int

    class Config:
        
        orm_mode = True


