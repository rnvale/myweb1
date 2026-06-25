import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))
print("Path:", sys.path[0])

from app import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
