# Bewerbung API

This repository contains the implementation of an API as part of the application assignment. The API is publicly accessible and provides three endpoints: `/temp`, `/prime`, and `/number`.

## Endpoints

### /temp

Converts temperatures between Celsius and Kelvin. The temperature in Celsius is provided as a GET parameter and the response is returned in JSON format.

#### Request
```bash
curl https://ace-bewerbung-fef0559fb5f3.herokuapp.com/api/temp?celsius=25
```

#### Response
```json
{
  "kelvin": 298.15,
  "celsius": 25
}
```

### /prime

Returns all prime numbers up to a specified limit. The limit is provided as a GET parameter and the primes are returned as an array in JSON format.

#### Request
```bash
curl https://ace-bewerbung-fef0559fb5f3.herokuapp.com/api/prime?limit=10
```

#### Response
```json
{
  "primes": [2, 3, 5, 7]
}
```

### /number (Bonus Task)

Returns a specific number for each integer `n` between 0 and 50. The response is returned in JSON format. 

#### Request
```bash
curl https://ace-bewerbung-fef0559fb5f3.herokuapp.com/api/number?n=45
```

#### Response
```json
{
  "number": 1134903170
}
```

## Deployment

The API is deployed on Heroku and can be accessed using the following link:

[https://ace-bewerbung.herokuapp.com](https://ace-bewerbung.herokuapp.com)

### Deployment Instructions

To deploy this API yourself, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/anjalybenny/ACE-Bewerbung.git
    cd <repository-directory>
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application locally:**
    ```bash
    python main.py
    ```

5. **Deploy to Heroku:**
    - Ensure you have the Heroku CLI installed and you are logged in.
    - Create a new Heroku application:
      ```bash
      heroku create <your-app-name>
      ```
    - Push the code to Heroku:
      ```bash
      git push heroku main
      ```

6. **Open the deployed application:**
    ```bash
    heroku open
    ```


## License

This project is licensed under the MIT License - see the LICENSE file for details.
