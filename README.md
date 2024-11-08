# YamlTestPilot
YamlTestPilot - A YAML-driven testing tool that allows developers to configure, execute, and manage tests entirely via YAML files, automating the testing workflow.


## Yaml Template

### meta field
```yaml
meta:
  name: "Add Function Test Suite"
  description: "Tests for add function handling various input cases"
  created_by: "Jane Doe"
  last_run: "2024-11-09 15:45:00"
```

### settings field
```yaml
settings:
  root_path: "./path/to/"
  module_file: "utils.py"
  retries: 2
  timeout: 5

```

### test_cases field
```yaml
test_cases:
  - function_name: "add"
    function_description: "Adds two numbers and returns the sum."
    function_hash: "a1b2c3d4e5f67890abcdef1234567890abcdef1234567890abcdef1234567890"
    
    summary:
      - summary_id: "summary1"
        description: "Basic addition tests with integers and floats."
        names:
          - "Addition with Positive Integers"
          - "Addition with Negative Integers"
          - "Addition with Mixed Sign Integers"
          - "Addition with Floats"
          - "Addition with Large Numbers"
        cases:
          - id: "TC001"
            name: "Addition with Positive Integers"
            arguments: [2, 3]
            expected_return: 5
            exception: None
            result:
              status: null
              actual_return: null
              execution_time_ms: null

          - id: "TC002"
            name: "Addition with Negative Integers"
            arguments: [-4, -6]
            expected_return: -10
            exception: None
            result:
              status: null
              actual_return: null
              execution_time_ms: null

      - summary_id: "summary2"
        description: "Edge cases for addition function."
        names:
          - "Addition with Zero"
          - "Addition with Non-numeric Types"
          - "Addition with None as Input"
          - "Addition with Missing Argument"
          - "Addition with Complex Numbers"
        cases:
          - id: "TC006"
            name: "Addition with Zero"
            arguments: [0, 10]
            expected_return: 10
            exception: None
            result:
              status: null
              actual_return: null
              execution_time_ms: null

          - id: "TC007"
            name: "Addition with Non-numeric Types"
            arguments: ["two", 3]
            expected_return: null
            exception: "TypeError"
            result:
              status: null
              actual_exception: null
              execution_time_ms: null

```
