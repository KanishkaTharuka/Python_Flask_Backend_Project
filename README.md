# Python_Flask_Backend_Project



# Clone the Project
git clone https://github.com/KanishkaTharuka/Python_Flask_Backend_Project.git
cd your-repo-name

# Create Virtual Environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux / Mac)
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Run the Project
python run.py

# API Endpoints (Examples)
# Register
POST /api/user/register

# Login
POST /api/user/login

# Get All Users (Protected)
GET /api/user/
Authorization: Bearer <TOKEN>

# Run Tests
pytest
