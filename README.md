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

### settings filed
```yaml
settings:
  root_path: "./path/to/"
  module_file: "utils.py"
  retries: 2
  timeout: 5

```
