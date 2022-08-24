# Requirements

  ```bash
  # Install wheel for modern installation
  python3 -m pip install wheel

  python3 -m pip install -r requirements-new.txt
  python3 -m pip install ./django-toolbelt-0.0.1.tar.gz

  # NOTE: update self.DIR_BASE in cloudynight/__init__.py first!
  python3 setup.py install
  ```

# PostgreSQL

Run the postgresql container with `docker-compose`:

  ```bash
  cd docker
  docker-compose up
  ```

# Personalize

Update the `media` variable in `settings.py`, as well as the

# Start the webapp

   ```bash
   cd ../cloudynightserver
   ./manage.py migrate
   ./manage.py createsuperuser
   ./manage.py runserver
   ```