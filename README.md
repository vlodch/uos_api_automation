# UosClient Testing Framework

This project is designed to provide a robust testing framework featuring an API client, comprehensive test suites, 
fixtures for reusable test data, detailed logging, and a mock server to simulate API responses.

## Table of Contents

- [Installation](#installation)
- [Running the Mock Server](#running-the-mock-server)
- [Running Tests](#running-tests)
- [Generating and Viewing Allure Reports](#generating-and-viewing-allure-reports)
- [Framework Structure](#framework-structure)

## Installation

Before running the tests, Python 3.7 or higher installed.

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. It is recommended to create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This will install all necessary packages including `pytest`, `allure-pytest`, and any other dependencies.

## Running the Mock Server

The mock server simulates the API endpoints used in testing, allowing for consistent and isolated test runs.

To start the mock server:

```bash
python mock_server.py
```

By default, the server listens on `http://localhost:5000`. 
Ensure this server is running before executing tests that depend on it.

## Running Tests

Tests are written using `pytest`. To run all tests, execute:

```bash
pytest
```

You can run specific tests or test files by specifying their path:

```bash
pytest tests/test_integration_workflow.py
```

For more verbose output, use:

```bash
pytest -v
```

## Generating and Viewing Allure Reports

Allure is used to generate detailed and visually appealing test reports.

1. Run tests with Allure reporting enabled:

   ```bash
   pytest --alluredir=allure-results
   ```

   This command will execute the tests and store results in the `allure-results` directory.

2. Generate and serve the Allure report locally:

   ```bash
   allure serve allure-results
   ```

   This will open a web browser displaying the test report. If you don't have Allure installed, follow the official installation guide at [Allure Framework](https://docs.qameta.io/allure/).

## Framework Structure

The project is organized to promote maintainability, clarity, and ease of use:

- **API Client (`api/uos_client.py`)**: Contains the `UOSClient` class responsible for interacting with the API endpoints. It abstracts HTTP requests and provides methods for various API operations.

- **Tests (`tests/`)**: Directory containing all test cases written using `pytest`. Tests are organized logically and use fixtures for setup and teardown.

- **Fixtures (`conftest.py`)**: Defines reusable test fixtures such as the API client instance and sample test data. Fixtures help in reducing redundancy and managing test dependencies.

- **Logging**: The framework includes logging mechanisms to capture detailed information during test execution. Logs assist in debugging and provide insights into test behavior.

- **Mock Server (`mock_server.py`)**: A lightweight server that mimics the real API's behavior. It is used during testing to provide predictable responses, enabling reliable and isolated tests without depending on external systems.

---