# yogipatel.dev

This portfolio website was built using the Django framework and refined with Bootstrap to deliver an elegant user interface. It's hosted on Heroku, ensuring continuous integration and delivery (CI/CD), and seamlessly connected to a custom domain for a polished online presence.

You can explore the website at [www.yogipatel.dev](https://www.yogipatel.dev).

## Milestone Commits
1. **Commit e9ec3a0:**  
   At this commit, the project can be run locally, but deployment on Heroku is not yet possible.   
   To prepare the code for deployment, please follow the instructions outlined in [Deploying to Heroku](#deploying-to-heroku).

2. **Commit aa094bd:**  
   With this commit, the project is fully deployable on Heroku.  
   This commit not only updates `settings.py` to enable project deployment but also includes improvements to the project's visual aspects (template files) and enhances overall responsiveness.  
   Be sure to update the `ALLOWED_HOSTS` in `settings.py` and configure the Config Vars in your Heroku Dyno if you haven't done so already.

## [Deploying to Heroku](#deploying-to-heroku)
**NOTE:** The following steps are required to deploy Commit **e9ec3a0** on Heroku. Assume that you are currently at Commit **e9ec3a0** and wish to deploy the project.

1. **Create a Heroku Dyno:**  
   Start by creating a Heroku Dyno and installing Heroku Postgres and Cloudinary.  
   In the Buildpacks section of your Dyno's settings tab, **add a buildpack** for *python*.  

   As of September 2023, Heroku Postgres costs approximately $0.007/hour, and Cloudinary is free (hopefully). A Heroku Basic Dyno costs around $0.010/hour. A Basic Dyno is necessary if you want to add a custom domain because it provides a SSL certificate for you via ACM. 
    
   **NOTE:** Make sure that the `DATABASE_URL` has automatically been added to the config vars in your Dyno. If not, then click on the Heroku Postgres and get the Database URI from the Database Credentials section from the Settings tab. Add this as `Database_URL` to your Dyno Config Vars.  

2. **Connect Dyno to GitHub:**  
   In your Dyno settings, navigate to Deploy > Deployment Method, and connect it to your GitHub repository.

3. **Change Local Database Connection to Heroku Postgres:**  
   Initially, install `dj-database-url` by running (in cmd):  
   ```
   pip install dj-database-url
   ```  
   Then, in your `settings.py`, Replace the following:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```
    with:

    ```python
    DATABASES = {
        'default': {}
    }
    
    db_from_env = dj_database_url.config(conn_max_age=600)
    DATABASES['default'].update(db_from_env)
    ```

    Don't forget to add `import dj_database_url` at the top of your `settings.py`.  

4. **Add Support for Static files:**  
   Out of the box, Heroku will not be able to serve the staticfiles.  
   We will use a library called ***whitenoise*** to help.  
   Install whitenoise by running  
   
   ```
   pip install whitenoise
   ```

   Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware apart from Django’s SecurityMiddleware:  
   
   ```python
   MIDDLEWARE = [
    # ...
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ...
    ]
   ```   
   
   Then, Replace (still in `settings.py`)

   ```python
    STATIC_URL = '/static/'
    ```
    with:

    ```python
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'website', 'static'),
    )
    ```

5. **Add Support for Media/Uploaded Files:**  
   > The Heroku filesystem is ephemeral - that means that any changes to the filesystem whilst the dyno is running only last until that dyno is shut down or restarted. Each dyno boots with a clean copy of the filesystem from the most recent deploy. This is similar to how many container based systems, such as Docker, operate.
   > 
   > In addition, under normal operations dynos will restart every day in a process known as "Cycling".
   >
   > These two facts mean that the filesystem on Heroku is not suitable for persistent storage of data. In cases where you need to store data we recommend using a database addon such as Postgres (for data) or a dedicated file storage service such as AWS S3 (for static files).

   To support Media files (Instead of storing images in the database, django stores the images in the file system and stores the reference in the database) in django, we use Cloudinary.  

   Install `cloudinary` and `django-cloudinary-storage` by running  

   ```
   pip install cloudinary django-cloudinary-storage
   ``` 

   Now, Go to the Cloudinary dashboard by clicking on the Cloudinary add-on in the Overview tab of your Heroku Dyno. Copy the `CLOUD_NAME`, `API_KEY` AND `API_SECRET` from Cloudinary and save them as `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY` AND `CLOUDINARY_API_SECRET` respectively in your Heroku Dyno's Config Vars. 


   In `settings.py`,  
   update `INSTALLED_APPS` by adding:  
   
   ```python
   INSTALLED_APPS = [
    ....
    'cloudinary_storage',
    'django.contrib.staticfiles', # This is added by default
    ....
    'cloudinary',
    ]
   ```  

   At the end of `settings.py` add,  
   
   ```python
   CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
    }
   DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
   ```



6. **Save all sensitive information in Config Vars:**  
   The following are the variables that should be in the Config Vars and should not be present in your source code:
   - `CLOUDINARY_API_KEY` = API key that is used to connect to Cloudinary. Can get it from the Cloudinary dashboard.
   - `CLOUDINARY_API_SECRET` = API Secret that is used to connect to Cloudinary. Can get it from the Cloudinary dashboard.
   - `CLOUDINARY_CLOUD_NAME` = Cloud Name that is used to connect to Cloudinary. Can get it from the Cloudinary dashboard.
   - `CLOUDINARY_URL` = The URL that is  derived from the CLOUDINARY_API_KEY, `CLOUDINARY_API_SECRET` and `CLOUDINARY_CLOUD_NAME`. This is not used in the code. Can be found in the Cloudinary dashboard.
   - `DATABASE_URL` = This is the URL for Heroku Postgres. The django project connects to the database with the help of this. Heroku automatically adds this but it can be found in the Heroku Postgres dashboard (In the settings tab).
   - `EMAIL_HOST_PASSWORD` = The generated password for the google account. Can be generated at Manage Google account > Security > 2FA > App passwords (at the bottom).
   - `EMAIL_HOST_USER` =  The gmail account you will be used to send an email notification when a contact form is submitted.
   - `SERCET_KEY` = This is the secret key generated by django and stored in settings.py when project is created. 


7. **Change the values of DEBUG and ALLOWED_HOSTS:**  
   Change the values of `DEBUG` from  `True` to `False` and  
   Add the following to `ALLOWED_HOSTS`:
   - `'<heroku_app_name>-random_identifier.herokuapp.com'`:  
     At the top of your Heroku Dyno, click the **Open App** button. Copy the URL and add only the above part.
   - `'127.0.0.1'`: This is to allow running on the localhost while developing.
   - `'www.<your_custom_domain>.com'`, `'<your_custom_domain>.com'`, `'.<your_custom_domain>.com'`: Your custom domain name in different permutations.  

   Now your ALLOWED_HOSTS should look like:  
   
   ```python
   ALLOWED_HOSTS = ['<heroku_app_name>-random_identifier.herokuapp.com', '127.0.0.1', 'www.<your_custom_domain>.com'`, `'<your_custom_domain>.com'`, `'.<your_custom_domain>.com']
   ```

8. **Add requirements.txt, runtime.txt, procfile:**  
   Get a requirement.txt by running:  
   
   ```
   pip freeze > requirements.txt
   ```
   **Note:** Run the above command everytime you add/install a new library. This is what Heroku will use to create an environment. Hopefully, you were using a virtual environment.

   Create a .txt file called **runtime.txt** and add `python-<version>`. For me, it was `python-3.11.5`.  

   Create a procfile by running:
   
   ```
   echo web: gunicorn config.wsgi --log-file -  > Procfile
   ``` 

    **Note:** The three files must be in your Django project folder that you will push to GitHub. 

9. **Deploy**:  
    Commit and Push the changes to GitHub. In the Manual Deploy section of your Heroku Dyno's Deply tab, add the branch you want to deploy and click on **Deploy Branch**.


## Connect a custom google domain to the Heroku deployment
After the Heroku app is successfully built, follow the following steps to connect a custom google domain to the app:  
1. In your Heroku App, Settings > Add your domain:
   - Add `www.[your_custom_domain.com]` (`www` is **important**) 
   - Copy the **DNS_TARGET**
2. In your Heroku App, Settings > SSL Certificates:  
    Click on **Configure SSL** and select **ACM**
3. In Google Domains, DNS > Resource Records > Custom Records > Manage Custom Records:
   - **Host:** www,  
     **Type:** CNAME,  
     **Data:** The **DNS_TARGET**   
     Save.
4. In Google Domains, Website > Add a forwarding Address:
    - **From:** [your_custom_domain.com],  
     **To Field:** https://www.[your_custom_domain.com],  
     Select **Permanent Redirect (301)**,  
     Select **Forward Path** and,  
     Select **SSL Enabled**.

### Model Migration
If you want to make changes to the models, make the changes and then run:  
```python
    python manage.py makemigrations
```

then, commit and push the changes.
After the Heroku build is successful, run the following: 
``` 
    heroku run --app=<app_name> python manage.py makemigrations
    heroku run --app=<app_name> run python manage.py migrate
```



## Resources

1. [How to deploy to Heroku](https://youtu.be/kBwhtEIXGII)
2. [Setup Postgres on Heroku](https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1)  
3. [Django connection to Heroku Postgres](https://www.youtube.com/watch?v=TFFtDLZnbSs&t=187s) 
4. [How to add environment variables to Heroku](https://dev.to/vulcanwm/environment-variables-in-heroku-python-385o)
5. [How to add Cloudinary to support Media Files](https://www.dothedev.com/blog/heroku-django-store-your-uploaded-media-files-for-free/)
6. [How to connect a custom domain with ssl certificate to Heroku](https://nikodunk.com/heroku-ssl-google-domains-2019)
   

