 WorkInside Employee Experience Reviews for Hospitality

A Django powered platform where hotel employees can anonymously review their workplace, rate departments, and share real experiences.
Designed to help hospitality professionals make better career decisions.

    Features
- Anonymous employee reviews
- Google Places autocomplete (hotel name, address, country, geo)
- Department-based ratings (Front Office, Housekeeping, F&B, Engineering, etc.)
- Smart content moderation
- Banned words detection
- Sensitive content detection
- Contact info blocking (emails, phones, URLs)
- Email verification for trusted reviews
- Top hotels ranking (verified only reviews)
- AJAX search
- Loadmore reviews (infinite scrolling)
- Hotel detail page with rating statistics
- Responsive UI (custom CSS)

    Tech Stack

Backend: Django 5.2, SQLite (dev), Django ORM
Frontend: HTML, CSS, JavaScript
APIs: Google Places Autocomplete
Email: Django Email Backend (SMTP)
Deployment: (Coming soon: Render / DigitalOcean)



    Project Structure
workinside hospitality reviews/
│
├── backend/              # Django project root
├── reviews/              # Main review app
├── static/               # CSS / JS / Icons
├── templates/            # HTML templates
├── db.sqlite3            # Database (development only)
└── manage.py

    How to Run Locally
1) Clone the repository
git clone https://github.com/NtinosTr/workinsidehospitalityreviews.git
cd workinside hospitality reviews

2) Create a virtual environment
python -m venv venv
source venv/bin/activate     # Mac / Linux
venv\Scripts\activate        # Windows

3) Install dependencies
pip install -r requirements.txt

4) Run server
python manage.py runserver


Project runs at: http://127.0.0.1:8000/

- Environment Variables (Google Places + Email)
- GOOGLE_MAPS_API_KEY=your_key_here
- EMAIL_HOST=your_email_host
- EMAIL_PORT=587
- EMAIL_HOST_USER=your_email
- EMAIL_HOST_PASSWORD=your_password
- EMAIL_USE_TLS=True

Contact

Created by NtinosTr
For ideas / feedback: workinside.contact@gmail.com

    Status
- MVP Completed Deployment in progress
More features coming soon!
