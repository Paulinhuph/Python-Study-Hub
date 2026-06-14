from pydantic import BaseModel, Field, EmailStr

class UserRegister(BaseModel):
    nome: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserUpdate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=50)
    email: EmailStr

class PasswordUpdate(BaseModel):
    senha_atual: str = Field(..., min_length=8)
    nova_senha: str = Field(..., min_length=8)

class AvatarUpdate(BaseModel):
    avatar_url: str