# Back-End Developer Capstone

**Coursera | Meta**

Final project to obtain the Meta Back-End Developer professional certificate.

## Run Locally

Clone the project

```bash
  git clone https://github.com/EduardoKstillo/Capstone-Project-by-Meta.git
```

Go to the project directory

```bash
  cd Capstone-Project-by-Meta/littlelemon
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Change these settings according to your local configuration in settings.py

```jsx
DATABASES = {
  default: {
    ENGINE: "django.db.backends.mysql",
    NAME: "LittleLemon",
    USER: "root",
    PASSWORD: "password",
    HOST: "127.0.0.1",
    PORT: "3306",
    OPTIONS: {
      init_command: "SET sql_mode='STRICT_TRANS_TABLES'",
    },
  },
};
```

Start the server

```bash
  python manage.py runserver
```

## API Reference

#### Auth

| Method    | Path                 | Action                                                                                                   |
| :-------- | :------------------- | :------------------------------------------------------------------------------------------------------- |
| `POST`    | /auth/users/      	 | Get all users                                                                                            |
| `GET`     | /api-token-auth/     | Login and get token with authtoken from rest_framework. <br> Send a json with the username and password. |
| `POST`    | /auth/token/login/	 | Login and get token with djoser. <br> Send a json with the username and password                         |
| `POST`    | /auth/token/logout/	 | Sign out with djoser                                                                                     |

#### Menu

```http
  /restaurant/menu/
```

| Method    | Action                               | TOKEN AUTH |
| :-------- | :----------------------------------- | :--------- |
| `GET`     | Retrieves all menu items	           |     Yes    |
| `POST`    | Creates a menu item		               |     Yes    |

```http
  /restaurant/menu/{id}
```

| Method    | Action                               | TOKEN AUTH |
| :-------- | :----------------------------------- | :--------- |
| `GET`     | Retrieves a menu item   	           |     Yes    |
| `PUT`     | Update this item     	               |     Yes    |
| `DELETE`  | Delete this item    	               |     Yes    |

#### Booking

```http
  /restaurant/booking/tables/
```

| Method    | Action                               | TOKEN AUTH |
| :-------- | :----------------------------------- | :--------- |
| `GET`     | Retrieves all bookings		           |     Yes    |
| `POST`    | Creates a booking		                 |     Yes    |

```http
  /restaurant/booking/tables/{id}
```

| Method    | Action                               | TOKEN AUTH |
| :-------- | :----------------------------------- | :--------- |
| `GET`     | Retrieves a booking     	           |     Yes    |
| `PUT`     | Update the booking	     	           |     Yes    |
| `DELETE`  | Delete the booking	                 |     Yes    |

## Running Tests

To run tests, run the following command

```bash
  python manage.py test
```

## 🛠 Skills
Python, Django, MySQL

