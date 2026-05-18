# itp2-final


## Utilities Module (`utils/`)
This module contains core utility classes and functions shared across the application
1.Decorators (utils/decorators.py)
This module provides custom Python decorators to implement cross-cutting concerns like performance tracking without cluttering the business logic

#### Features:
The '@log_execution' decorator measures the exact time a function takes to execute and prints a benchmark log to the console. This is highly useful for verifying algorithmic efficiency during code defense

### Usage Example:
```python
from utils.decorators import log_execution

class AnalysisService:
    @log_execution
    def process_heavy_data(self):
        # The decorator will automatically log how long this method took to run
        pass
```