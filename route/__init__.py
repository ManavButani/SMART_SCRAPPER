from core.app import app
from . import auth
from . import user

# Include the authentication router with the prefix "/api/auth"
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

# Include the user management router with the prefix "/api"
app.include_router(user.router, prefix="/api", tags=["users"])
