## README

# Number Classification API

Number Classification API is a Flask-based web application that provides various mathematical properties of a number, including whether it's prime, perfect, Armstrong, or odd/even. It also fetches a fun fact about the number using an external API.

---

## Features

- **Prime Check**:
  Identifies whether a number is prime.
  
- **Perfect Number Check**:
  Determines if a number is a perfect number.

- **Armstrong Number Check**:
  Checks if the number is an Armstrong number.

- **Digit Sum Calculation**:
  Computes the sum of the digits of a number.

- **Odd/Even Classification**:
  Classifies whether the number is odd or even.

- **Fun Fact**:
  Fetches a fun fact about the number from [Numbers API](http://numbersapi.com).

---

## Technologies

- **Python**: The backend is built using Python’s Flask framework.
- **Flask-CORS**: To handle Cross-Origin Resource Sharing (CORS).
- **Requests**: To fetch data from external APIs.

---

## Installation

### Prerequisites
- Python 3.x installed on your system.
- `pip` (Python package manager).

### Steps
1. Clone or download the repository to your local system.
2. Open a terminal and navigate to the project directory.
3. Install the required dependencies by running:
   ```bash
   pip install flask flask-cors requests
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. The service will be available at `http://127.0.0.1:5000/`.

---

## API Usage

### Endpoint
`GET /api/classify-number`

### Query Parameters
| Parameter | Type   | Description                       |
|-----------|--------|-----------------------------------|
| `number`  | Integer| The number to classify. (Required)|

### Response
- **Success Response (Status Code: 200)**:
  ```json
  {
      "number": 28,
      "is_prime": false,
      "is_perfect": true,
      "properties": ["even"],
      "digit_sum": 10,
      "fun_fact": "28 is a perfect number."
  }
  ```
- **Error Response (Status Code: 400)**:
  ```json
  {
      "number": null,
      "error": true
  }
  ```

### Example Usage
To classify the number **28**:
```bash
curl http://127.0.0.1:5000/api/classify-number?number=28
```

---

## How It Works

1. **Input Validation**: The API checks if the input parameter is a valid integer.
2. **Classification**:
   - It checks if the number is prime, perfect, and Armstrong.
   - It calculates the sum of digits and determines if the number is odd or even.
3. **Fun Fact**: Using the Numbers API, the server fetches and returns a fun fact about the number.
4. **Response**: Returns the number’s properties in JSON format.

---

## Example Outputs

### Input: 28
```json
{
    "number": 28,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["even"],
    "digit_sum": 10,
    "fun_fact": "28 is a perfect number."
}
```

### Input: 153
```json
{
    "number": 153,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 9,
    "fun_fact": "153 is an Armstrong number (1^3 + 5^3 + 3^3 = 153)."
}
```

### Invalid Input (e.g., "abc")
```json
{
    "number": null,
    "error": true
}
```

---

## Development and Contribution

### Directory Structure
Since this version consolidates all the functionality into a single `app.py`, there is no directory tree. The entire app operates from this file.

### Modifications
If you wish to extend or modify the application:
1. Add/modify helper functions inside `app.py`.
2. Update the `/api/classify-number` route to include the extended features.

---

## Potential Improvements
- Add more mathematical classifications (e.g., Fibonacci, Palindrome).
- Wrap statistical analysis or visualization for input numbers.
- Migrate to a microservices architecture for better scalability.

---

## License

This project is open-source and available under the MIT License.

---

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web development framework.
- [Numbers API](http://numbersapi.com) - For providing fun facts about numbers.
- Inspiration from everyday mathematical surprises!