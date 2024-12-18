### DEPLOYMENT INSTRUCTIONS ###

## FOR DEPLOTMENT ##

1. set DEBUG = False
2. run - pip freeze > requirements.txt - locally
3. set up env variables



create super user?
set ALLOWED_HOSTS

Alter the database used


## FOR DEV ##

1. set





for deployment check out to another branch


Create a Procfile for Heroku
Ensure Superuser Creation (script)
AWS Database Link (Heroku Postgres) - adding secrets and keys
Update settings.py
Heroku Setup Commands








Pre-Deployment Checklist for Django + React Project
1. Review Changes for Deployment
 Ensure all code changes have been committed and pushed to the correct branch (e.g., production or main).
 Run tests (if any) to ensure that everything is working locally.
 Check for uncommitted changes (e.g., run git status to confirm).
2. Environment Variables
 Set and verify all environment variables for production, such as:
DEBUG=False
SECRET_KEY=<your_production_secret_key>
Database URL (e.g., DATABASE_URL for Heroku PostgreSQL)
Any third-party API keys (e.g., Stripe, AWS, etc.)
 Ensure that .env files or environment settings are not being pushed to the repo (they should be added to .gitignore).
3. Django Settings Adjustments
 Debugging: Set DEBUG=False in settings.py for production.
 Allowed Hosts: Update ALLOWED_HOSTS to include your Heroku domain or IPs.
 Static and Media Files:
Ensure django.contrib.staticfiles is configured correctly.
Run python manage.py collectstatic to collect static files into the correct folder (/static), which Heroku can serve or use an external service like AWS S3.
 CORS (Cross-Origin Resource Sharing): If your React frontend is separate, make sure to update CORS_ALLOWED_ORIGINS in settings.py.
 Database Config: Ensure that DATABASE_URL is set correctly for the production database (for Heroku, it’s often automatically managed, but check that it's configured).
 Logging: Enable appropriate logging configurations for errors and requests.
4. React Frontend
 Production Build: Ensure that the React frontend is built for production:
bash
Copy code
npm run build
 Environment Variables for React: Update .env for production-specific settings, like API URLs, keys, etc.
 Ensure that React's production build (build/ folder) is being served correctly by Django or through a static server.
5. Database Migrations
 Run Django migrations to ensure the database schema is up to date:
bash
Copy code
python manage.py migrate
6. Heroku Specific
 Heroku Config Vars: Ensure that Heroku’s environment variables (config vars) are set correctly:
DEBUG=False
DATABASE_URL (automatically managed by Heroku)
Other environment variables (e.g., AWS keys, Stripe keys, etc.)
 Heroku Logs: Check the logs from previous deployments for any errors or warnings:
bash
Copy code
heroku logs --tail
7. Procfile and Deployment Scripts
 Ensure that your Procfile is correct for Heroku to start the Django server and React production build. Example:
c
Copy code
web: gunicorn your_project_name.wsgi --log-file -
 Check that any other deployment-related scripts (like the ones for creating the superuser) are included if necessary.
8. Superuser Creation (Optional)
 If you're creating a superuser automatically, ensure the createsuperuser command is either invoked through a script or manually during deployment.
9. Testing Before Deployment
 Test your changes in a local production-like environment (e.g., use Docker or run python manage.py runserver with DEBUG=False).
 Test React frontend by running the production build locally (serve -s build).
 Run end-to-end tests if possible (e.g., post-deployment smoke tests, if available).
10. Backup
 Backup your database before deploying (especially if you’re making any changes to the schema or data).
 Make sure that your production database is connected and not in any locked state.
Deployment Steps
1. Push Code to GitHub (or Git Remote)
 Ensure all changes have been committed and pushed to GitHub (or whichever Git service you're using).
 Push to the appropriate branch (e.g., production).
bash
Copy code
git push origin production
2. Deploy to Heroku
 Push to Heroku for deployment:
bash
Copy code
git push heroku production:master
 If needed, restart the Heroku app after deployment:
bash
Copy code
heroku restart
3. Create Superuser (if necessary)
 If you haven’t already created a superuser, run:
bash
Copy code
heroku run python manage.py createsuperuser
4. Check Deployment
 Check Heroku logs for any issues:
bash
Copy code
heroku logs --tail
 Visit the Heroku app URL to ensure everything is working (both frontend and backend).
5. Post-Deployment
 Test the app to make sure all features are functioning as expected.
 Verify that the frontend is correctly integrated with the backend, and API calls are functioning.
 If any issues are found, fix them and redeploy.
Ongoing Maintenance
 Regularly monitor the app for errors using logs or services like Sentry.
 Update dependencies in requirements.txt or package.json as necessary.
 Regularly test the app on staging or production to ensure stability.
By following this checklist, you ensure that your production environment remains consistent, and you reduce the chances of introducing bugs or issues during deployme





















# All Backend APi calls
    User Resftul
    path('register', RegisterView.as_view()),
    payload -- name email password

    path('login', LoginView.as_view()),
    paylaod -- email password

    path('user', UserView.as_view()),
    payload -- none

    path('logout', LogoutView.as_view()),
    payload -- none

    path('admin', PermissionView.as_view()),
    payload -- none

    Anime restful
    path('create', CreateAnimeView.as_view()),
    payload -- list of anime data

    path('index', IndexAnimeView.as_view()),
    paylaod -- none

    path('<int:id>', FindAnimeView.as_view()),
    payload -- none

    path('<int:id>/delete', DeleteAnimeView.as_view()),
    payload -- none

    path('<int:id>/update', UpdateAnimeView.as_view()),
    payload -- list of anime data

    Rating based views
    path('<int:userId>/rate/<int:animeId>', UserAnimeRatingView.as_view()),
    payload -- score: 1-10

# still need to add a call to retrieve user rating
# reviews for each anime seperate model?




# unfinished
    path('link/<int:arr>/<str:id>', AnimeListLinkView.as_view())
# navigate to run:
python manage.py runserver
npm run start
.\djangoenv\Scripts\activate
djangoenv\Scripts\deactivate.bat
8000 for production build and api
5173 for react development




# User Model {plans}

img?
user
email
password
background color
favorites
/media link rating from user
/friends link


##### WORK ON MEDIA MDOEL FIRST #########
# Anime Model {plans}

img?
Type:{tv, movie, etc}
studio
premire season
air date to end date
demographic
rating
title
(
    Japaense(kanji)
    japanese(roamanized)
    english
)
genre
global rating?
rating user?
episode length
episode number
description
reviews user?
adaptaion
sequel / prequel?
status user?


Score: 8.921 (scored by 200,890 users) Ranked: #1822 based on the top anime page. Please note that 'Not yet aired' and 'R18+' titles are excluded.
Popularity: #569
Members: 404,709
Favorites: 15,094


episode and episode name?
recommended algo?

# Manga Model {plans}

img?

# Global stats api



notifications for air dates and end dates?
link format
[test](https://test.com)