from fastapi import FastAPI, status, Depends, HTTPException
from typing import Annotated



#from app.routes import hello
app = FastAPI()
from app.routes.auth_routes import auth_router
from app.routes.user_routes import user_router 

print("app :", app)
print("auth_router:", auth_router)
print("type:", type(auth_router))
print("has attribute 'routes'?", hasattr(auth_router, "routes"))


#hello()
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])
for route in app.routes:
    print(route.path, route.methods)

@app.get("/")
def read_root():
    return {"message": "FastAPI authentication and authorization example"}