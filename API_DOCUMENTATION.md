# API Documentation

**Author:** Avishek Devnath  
**Email:** avishekdevnath@gmail.com

# 🧪 Error Explainer API Documentation

## 📖 Overview

The Error Explainer API provides programmatic access to error explanation functionality, allowing you to integrate intelligent error analysis directly into your Python applications.

## 🚀 Quick Start

```python
import error_explainer

# Basic usage
result = error_explainer.explain_error("NameError: name 'x' is not defined")
print(result['explanation'])

# Quick explanation (rule-based only)
explanation = error_explainer.quick_explain("TypeError: can only concatenate str (not 'int') to str")
print(explanation)
```

## 📚 API Reference

### Core Functions

#### `explain_error(error_content, use_ai=True, api_key=None, model="gemini-1.5-flash", save_explanation=False)`

Explain an error programmatically.

**Parameters:**
- `error_content` (str): Error log content or traceback string
- `use_ai` (bool): Whether to use AI explanation (True) or rule-based (False)
- `api_key` (str, optional): Google Gemini API key
- `model` (str): AI model to use (only applies when use_ai=True)
- `save_explanation` (bool): Whether to save explanation to log directory

**Returns:**
- `dict`: Dictionary containing explanation and metadata

**Example:**
```python
import error_explainer

# Rule-based explanation (no API key needed)
result = error_explainer.explain_error(
    "NameError: name 'undefined_variable' is not defined",
    use_ai=False
)

print(f"Success: {result['success']}")
print(f"Method: {result['method']}")
print(f"Explanation: {result['explanation']}")
```

#### `explain_current_exception(use_ai=True, api_key=None, model="gemini-1.5-flash", save_explanation=False)`

Explain the currently active exception.

**Parameters:**
- `use_ai` (bool): Whether to use AI explanation (True) or rule-based (False)
- `api_key` (str, optional): Google Gemini API key
- `model` (str): AI model to use (only applies when use_ai=True)
- `save_explanation` (bool): Whether to save explanation to log directory

**Returns:**
- `dict`: Dictionary containing explanation and metadata

**Example:**
```python
import error_explainer

try:
    undefined_variable
except Exception:
    result = error_explainer.explain_current_exception(use_ai=False)
    print(f"Error: {result['error_summary']}")
    print(f"Explanation: {result['explanation']}")
```

### Context Managers

#### `auto_explain_exceptions(use_ai=True, api_key=None, model="gemini-1.5-flash", save_explanation=False, on_error=None, reraise=True)`

Context manager to automatically explain exceptions.

**Parameters:**
- `use_ai` (bool): Whether to use AI explanation (True) or rule-based (False)
- `api_key` (str, optional): Google Gemini API key
- `model` (str): AI model to use (only applies when use_ai=True)
- `save_explanation` (bool): Whether to save explanation to log directory
- `on_error` (callable, optional): Callback function called with explanation when exception occurs
- `reraise` (bool): Whether to reraise the exception after explaining it

**Example:**
```python
import error_explainer

def error_callback(result):
    print(f"🚨 Error occurred: {result['error_summary']}")
    print(f"Explanation: {result['explanation']}")

with error_explainer.auto_explain_exceptions(
    use_ai=False,
    on_error=error_callback,
    reraise=False
):
    # Your code here
    undefined_variable  # This will be automatically explained

print("Code continued after error!")
```

### Decorators

#### `explain_function_errors(use_ai=True, api_key=None, model="gemini-1.5-flash", save_explanation=False, on_error=None)`

Decorator to automatically explain errors in a function.

**Parameters:**
- `use_ai` (bool): Whether to use AI explanation (True) or rule-based (False)
- `api_key` (str, optional): Google Gemini API key
- `model` (str): AI model to use (only applies when use_ai=True)
- `save_explanation` (bool): Whether to save explanation to log directory
- `on_error` (callable, optional): Callback function called with explanation when exception occurs

**Example:**
```python
import error_explainer

@error_explainer.explain_function_errors(use_ai=False)
def problematic_function():
    return undefined_variable

try:
    problematic_function()
except Exception:
    print("Function error was automatically explained!")
```

### Integration Functions

#### `setup_logging_integration(use_ai=True, api_key=None, model="gemini-1.5-flash", save_explanation=False)`

Set up integration with Python's logging system to automatically explain errors.

**Parameters:**
- `use_ai` (bool): Whether to use AI explanation (True) or rule-based (False)
- `api_key` (str, optional): Google Gemini API key
- `model` (str): AI model to use (only applies when use_ai=True)
- `save_explanation` (bool): Whether to save explanation to log directory

**Example:**
```python
import error_explainer
import logging

# Set up logging integration
error_explainer.setup_logging_integration(use_ai=False)

# Configure logging
logging.basicConfig(level=logging.ERROR)

try:
    undefined_variable
except Exception:
    # This will automatically trigger error explanation
    logging.error("An error occurred", exc_info=True)
```

#### `explain_test_failures(use_ai=True, api_key=None, model="gemini-1.5-flash", save_explanation=False)`

Set up integration with pytest to automatically explain test failures.

**Parameters:**
- `use_ai` (bool): Whether to use AI explanation (True) or rule-based (False)
- `api_key` (str, optional): Google Gemini API key
- `model` (str): AI model to use (only applies when use_ai=True)
- `save_explanation` (bool): Whether to save explanation to log directory

**Example (in conftest.py):**
```python
import error_explainer

def pytest_runtest_logreport(report):
    if report.failed and report.longrepr:
        result = error_explainer.explain_error(
            str(report.longrepr), 
            use_ai=False
        )
        if result.get('success', False):
            print(f"🧐 Test Failure Explanation:\n{result['explanation']}")
```

### Convenience Functions

#### `quick_explain(error_content)`

Quick explanation using rule-based system (no AI required).

**Parameters:**
- `error_content` (str): Error log content

**Returns:**
- `str`: Simple explanation string

**Example:**
```python
import error_explainer

explanation = error_explainer.quick_explain("NameError: name 'x' is not defined")
print(explanation)
```

#### `ai_explain(error_content, api_key=None)`

AI-powered explanation (requires API key).

**Parameters:**
- `error_content` (str): Error log content
- `api_key` (str, optional): Google Gemini API key

**Returns:**
- `str`: AI-generated explanation string

**Example:**
```python
import error_explainer

explanation = error_explainer.ai_explain("NameError: name 'x' is not defined")
print(explanation)
```

## 🔧 Advanced Usage Examples

### Automated Error Handling in Applications

```python
import error_explainer

class DataProcessor:
    def __init__(self):
        # Set up automatic error explanation for this class
        self.explainer = error_explainer.auto_explain_exceptions(
            use_ai=False,
            save_explanation=True,
            on_error=self._log_error
        )
    
    def _log_error(self, result):
        print(f"🔍 Error in DataProcessor: {result['error_summary']}")
        print(f"📝 Full explanation saved to: {result.get('log_file', 'N/A')}")
    
    def process_data(self, data):
        with self.explainer:
            # Simulate some data processing that might fail
            if not data:
                raise ValueError("Data cannot be empty")
            
            result = data / 0  # This will cause a ZeroDivisionError
            return result

# Usage
processor = DataProcessor()
try:
    processor.process_data([])  # This will trigger ValueError
except Exception:
    print("Error was automatically explained and logged!")
```

### Batch Error Processing

```python
import error_explainer

error_logs = [
    "NameError: name 'x' is not defined",
    "TypeError: can only concatenate str (not 'int') to str",
    "IndexError: list index out of range",
    "KeyError: 'missing_key'",
    "ZeroDivisionError: division by zero"
]

print("Processing batch of errors...")

for i, error_log in enumerate(error_logs, 1):
    result = error_explainer.explain_error(error_log, use_ai=False)
    print(f"{i}. {result['error_summary']}")
    print(f"   Explanation: {result['explanation'][:80]}...")
    print()
```

### Testing Framework Integration

```python
# conftest.py
import error_explainer

def pytest_runtest_logreport(report):
    if report.failed and report.longrepr:
        result = error_explainer.explain_error(
            str(report.longrepr), 
            use_ai=False
        )
        if result.get('success', False):
            print(f"\n🧐 Test Failure Explanation:")
            print(f"Error: {result['error_summary']}")
            print(f"Explanation: {result['explanation']}")
```

## 📊 Response Format

All API functions return a dictionary with the following structure:

```python
{
    'success': bool,                    # Whether the explanation was successful
    'method': str,                      # 'rule-based' or 'ai'
    'error_summary': str,               # Brief error summary
    'error_type': str,                  # Type of error (e.g., 'NameError')
    'error_message': str,               # Error message
    'explanation': str,                 # Full explanation
    'suggested_fixes': list,            # List of suggested fixes
    'prevention_tips': list,            # List of prevention tips
    'confidence': str,                  # Confidence level ('low', 'medium', 'high')
    'timestamp': str,                   # Timestamp of explanation
    'log_file': str,                    # Path to saved log file (if saved)
    'ai_fallback': bool,                # Whether AI failed and fell back to rule-based
    'ai_error': str                     # AI error message (if applicable)
}
```

## 🔑 API Key Setup

For AI-powered explanations, you need a Google Gemini API key:

```bash
# Set environment variable
export GOOGLE_API_KEY=your-api-key-here

# Or use in code
result = error_explainer.explain_error(
    "NameError: name 'x' is not defined",
    use_ai=True,
    api_key="your-api-key-here"
)
```

## 🎯 Best Practices

1. **Use Rule-Based for Simple Errors**: For common errors, use `use_ai=False` for faster responses
2. **Use AI for Complex Errors**: For unique or complex errors, use `use_ai=True` for detailed analysis
3. **Handle API Failures**: Always handle cases where AI might fail and fall back to rule-based
4. **Save Important Explanations**: Use `save_explanation=True` for critical errors you want to review later
5. **Use Callbacks**: Implement error callbacks for automated logging and monitoring

## 🚀 Performance Tips

- **Rule-based explanations** are instant and work offline
- **AI explanations** take 1-3 seconds and require internet connection
- **Batch processing** is efficient for multiple errors
- **Context managers** have minimal overhead
- **Decorators** add negligible performance impact

## 🔧 Error Handling

The API gracefully handles various error scenarios:

- **Invalid error content**: Returns failure with error message
- **AI API failures**: Automatically falls back to rule-based
- **Missing API key**: Uses rule-based mode
- **Network issues**: Falls back to offline mode
- **Invalid parameters**: Returns descriptive error messages

## 📝 Examples Directory

See `examples/api_usage_examples.py` for comprehensive usage examples covering all API features. 