# AgriConnect

AgriConnect is a hyper-local, decentralized marketplace connecting farmers directly to consumers.

## Project Structure

This monorepo contains the following components:

- **mobile/**: React Native (Expo) app for Farmers and Consumers.
- **backend/**: Python (FastAPI) backend API.
- **admin/**: React.js (Vite) Admin Portal.

## Getting Started

### Backend

1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### Mobile App (Expo)

1. Navigate to the `mobile` directory:
   ```bash
   cd mobile
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the project:
   ```bash
   npx expo start
   ```

### Admin Portal

1. Navigate to the `admin` directory:
   ```bash
   cd admin
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the dev server:
   ```bash
   npm run dev
   ```

## Tech Stack

- **Frontend:** React Native (Expo)
- **Backend:** FastAPI (Python)
- **Database:** MongoDB
- **Admin:** React.js
