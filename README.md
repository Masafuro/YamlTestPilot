# YamlTestPilot
YamlTestPilot - A YAML-driven testing tool that allows developers to configure, execute, and manage tests entirely via YAML files, automating the testing workflow.


YamlTestPilot is a YAML-based testing framework that simplifies the process of creating and managing test cases for Python functions. This framework is designed to eliminate the need for repetitive test scripts by allowing developers to define all necessary test information in a YAML file. Test execution, results tracking, and test history are all managed directly from this file, streamlining the testing workflow.

The template YAML file for YamlTestPilot is available [here](https://github.com/Masafuro/YamlTestPilot/blob/main/template.yaml).

## Features

- **Simple Test Case Management**: Define function test cases, expected outcomes, and exception handling all in a single YAML file.
- **Automatic Result Recording**: Test results, execution times, and function modifications are recorded directly in the YAML file during test execution.
- **Human-Readable Format**: Designed with readability in mind, making it easy to understand and update tests without modifying code.
- **Git-Friendly Version Tracking**: By managing test configurations in YAML, test history can be effectively tracked within Git, reducing the need for additional backups.

## YAML Structure

### Main Sections

The YAML file has three primary sections:

1. **Meta**: Contains metadata about the test suite, including name, description, and the last run timestamp.
2. **Settings**: Configuration information for the testing environment, such as the root path, module file, retry count, and timeout.
3. **Test Cases**: The core of the test suite, where each function’s test cases are defined.

### Test Cases Structure

Each function being tested is represented under `test_cases` with the following fields:

- **function_name**: The name of the function being tested.
- **function_description**: A brief description of the function’s purpose.
- **__function_hash__**: A hash value of the function code, which will be automatically updated during test execution to detect any changes.
- **summary**: Contains grouped test cases for the function, including the following:
  - **summary_name**: The name of the test group.
  - **description**: An explanation of the purpose of this test group.
  - **names**: A list of brief names describing each test case within the group.
  - **cases**: The details for each individual test case, including:
    - **name**: The name of the test case.
    - **arguments**: A list of arguments to pass to the function.
    - **expected_return**: The expected return value of the function.
    - **exception**: Any expected exception for this test case (if applicable).
    - **__result__**: Execution details (automatically filled during testing), including:
      - **status**: The test result status (pass/fail).
      - **actual_return**: The actual return value from the function.
      - **execution_time_ms**: Execution time in milliseconds.
