from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.contact import EmergencyContact
from routers.contact import router as contact_router
from models.emergency import Emergency
from routers.emergency import router as emergency_router
from models.tracking import Tracking
from routers.tracking import router as tracking_router
from models.complaint import Complaint
from routers.complaint import router as complaint_router
from models.volunteer import Volunteer
from routers.volunteer import router as volunteer_router

from database import engine, Base

# Import Models
from models.user import User

# Import Routers
from routers.auth import router as auth_router

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Create FastAPI App
app = FastAPI(
    title="GuardWell API",
    version="2.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(auth_router)
app.include_router(contact_router)
app.include_router(emergency_router)
app.include_router(tracking_router)
app.include_router(complaint_router)
app.include_router(volunteer_router)

# Root Endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to GuardWell API",
        "status": "Running"
    }