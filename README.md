# HUUB Challenge
This project is a Django  API with two GET endpoints:
    - `/api/orders` returns all orders, alongisde its deliveries from the system. Endpoint can also take query parameter brand to filter orders by brand name; `/api/orders?brand=`
    - `/api/deliveries` returns all shipped deliveries in the system. Can also be queried with either of two parameters, `id` or `reference` of an order. `/api/deliveries?order_id=` or `/api/deliveries?order_ref=`.

## Requirements
- Python 3.6 or later
- PostgreSQL

## Setup
- Create a virtual environment in the root of this folder with command `python3 -m venv venv`.
- Activate the environment `. venv/bin/activate`.
- Run `pip install -r requirements.txt` to install the dependencices in the environment.
- Create a PostgreSQL db and edit the .env values accordingly.
- Run `python manage.py migrate` to set up the new database.
- Populate the db with command `python manage.py loaddata data.json`.
- Run the python server `python manage.py runserver` and visit the endpoints.
- You can run tests with command `python manage.py test`.