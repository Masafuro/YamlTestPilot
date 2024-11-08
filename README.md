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
    # ここに summary や cases が続く

```
