# 🧪 Error Explainer

**Author:** Avishek Devnath  
**Email:** avishekdevnath@gmail.com

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/badge/PyPI-xerror-blue.svg)](https://pypi.org/project/xerror/)
[![Downloads](https://img.shields.io/pypi/dm/xerror)](https://pypi.org/project/xerror/)
[![Version](https://img.shields.io/pypi/v/xerror)](https://pypi.org/project/xerror/)
[![Status](https://img.shields.io/badge/status-active-success.svg)](https://github.com/xerror/xerror)
[![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/xerror/xerror/graphs/commit-activity)

**AI-powered error analysis and explanation tool for multiple programming languages.**

Explain error logs from Python, JavaScript, TypeScript, C++, and Java using Google's Gemini AI directly from your terminal. Get instant, intelligent explanations and fix suggestions for any programming error.

> **Built with ❤️ by [Avishek Devnath](mailto:avishekdevnath@gmail.com)**

## ✨ Features

- 🤖 **AI-Powered Explanations**: Uses Google Gemini 1.5 Flash for intelligent error analysis
- 🔍 **Offline Rule-Based Analysis**: Works without AI - instant explanations for common errors
- 🌐 **Multi-Language Support**: Python, JavaScript, TypeScript, C++, Java
- 📁 **Multiple Input Methods**: Read from files, stdin, or paste interactively
- 💾 **Save & Search**: Store explanations and search through your error history
- 🎨 **Rich Output**: Beautiful terminal formatting with progress indicators
- 🔍 **Smart Parsing**: Intelligent traceback and error detection across languages
- 📊 **Markdown Export**: Export explanations in markdown format
- ⚡ **Fast & Lightweight**: Quick analysis with minimal dependencies
- 🌐 **Works Offline**: No internet connection required for rule-based mode
- 🔄 **Real-time Monitoring**: Watch running processes for live error detection
- 🐍 **Python API**: Programmatic access for integration with your tools
- 🔧 **Multi-Model Support**: Switch between different AI providers
- 🎯 **Language Auto-Detection**: Automatically identifies programming language from error logs

## 🚀 Quick Start

### Installation

**For Users:**
```bash
pip install xerror
```

**For Developers:**
```bash
# Clone the repository
git clone https://github.com/xerror/xerror.git
cd xerror

# Install in development mode
pip install -e .
```

### Setup API Key

1. Get your Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Set the environment variable:

```bash
export GOOGLE_API_KEY=your-api-key-here
```

Or create a `.env` file in your project directory:

```env
GOOGLE_API_KEY=your-api-key-here
```

### Basic Usage

```bash
# Explain error from file (AI mode - requires API key)
xerror error.log

# Explain error offline (no API key required)
xerror error.log --offline

# Paste error interactively
xerror --paste

# Paste error offline
xerror --paste --offline

# Pipe error from stdin
xerror < error.log

# Save explanation to history
xerror error.log --save

# Output in markdown format
xerror error.log --markdown
```

## 🌐 Supported Languages

| Language | Error Detection | AI Explanation | Rule-Based | Examples | Status |
|----------|----------------|----------------|------------|----------|--------|
| Python | ✅ | ✅ | ✅ | NameError, TypeError, ImportError | 🟢 Production Ready |
| JavaScript | ✅ | ✅ | ✅ | TypeError, ReferenceError, SyntaxError | 🟢 Production Ready |
| TypeScript | ✅ | ✅ | ✅ | TS2322, TS2339, TS2307 | 🟢 Production Ready |
| C++ | ✅ | ✅ | ✅ | Compilation errors, runtime errors | 🟢 Production Ready |
| Java | ✅ | ✅ | ✅ | NullPointerException, ClassNotFoundException | 🟢 Production Ready |

## 📖 Usage Examples

### 1. Multi-Language Error Analysis

```bash
# Python error
xerror python_error.log

# JavaScript error
xerror javascript_error.log

# TypeScript error
xerror typescript_error.log

# C++ error
xerror cpp_error.log

# Java error
xerror java_error.log
```

### 2. Language Detection

```bash
# Auto-detect language from error
xerror detect "NameError: name 'x' is not defined"
xerror detect "TypeError: Cannot read property 'length' of undefined"
xerror detect "TS2322: Type 'string' is not assignable to type 'number'"
xerror detect "error: 'cout' was not declared in this scope"
xerror detect "Exception in thread \"main\" java.lang.NullPointerException"
```

### 3. Real-time Process Monitoring

```bash
# Watch a running process for errors
xerror watch "python my_script.py"

# Watch with custom command
xerror watch "npm start"

# Watch in background mode
xerror watch "python long_running_script.py" --background
```

### 4. Python API Examples

```python
import xerror

# Basic error explanation
result = xerror.explain_error("NameError: name 'x' is not defined")
print(result['explanation'])

# Language detection
language = xerror.detect_language("TypeError: Cannot read property 'length' of undefined")
print(f"Detected language: {language}")

# Parse error details
error_info = xerror.parse_error("TS2322: Type 'string' is not assignable to type 'number'")
print(f"Error type: {error_info.error_type}")
print(f"Language: {error_info.language}")

# Quick explanation (rule-based only)
explanation = xerror.quick_explain("TypeError: can only concatenate str (not 'int') to str")
print(explanation)

# Automatic error handling
with xerror.auto_explain_exceptions():
    undefined_variable  # This will be automatically explained

# Function decorator
@xerror.explain_function_errors()
def my_function():
    return undefined_variable
```

### 5. Error Examples by Language

#### Python Errors
```python
# NameError
NameError: name 'x' is not defined

# TypeError
TypeError: can only concatenate str (not 'int') to str

# ImportError
ImportError: No module named 'requests'

# IndentationError
IndentationError: expected an indented block

# AttributeError
AttributeError: 'list' object has no attribute 'append'

# ValueError
ValueError: invalid literal for int() with base 10: 'abc'
```

#### JavaScript Errors
```javascript
// TypeError
TypeError: Cannot read property 'length' of undefined

// ReferenceError
ReferenceError: x is not defined

// SyntaxError
SyntaxError: Unexpected token '{'

// RangeError
RangeError: Maximum call stack size exceeded

// URIError
URIError: URI malformed
```

#### TypeScript Errors
```typescript
// TS2322: Type assignment error
TS2322: Type 'string' is not assignable to type 'number'

// TS2339: Property does not exist
TS2339: Property 'length' does not exist on type 'number'

// TS2307: Module not found
TS2307: Cannot find module './Component'

// TS2345: Argument type mismatch
TS2345: Argument of type 'string' is not assignable to parameter of type 'number'

// TS2531: Object is possibly null
TS2531: Object is possibly 'null'
```

#### C++ Errors
```cpp
// Compilation error
error: 'cout' was not declared in this scope

// Syntax error
error: expected ';' before '}' token

// Missing include
error: 'vector' was not declared in this scope

// Linker error
undefined reference to 'main'

// Runtime error
Segmentation fault (core dumped)
```

#### Java Errors
```java
// NullPointerException
Exception in thread "main" java.lang.NullPointerException

// Compilation error
error: cannot find symbol: variable x

// Class not found
java.lang.ClassNotFoundException: com.example.MyClass

// ArrayIndexOutOfBoundsException
java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 3

// NumberFormatException
java.lang.NumberFormatException: For input string: "abc"
```

## 🐍 Python API Reference

### Core Functions

| Function | Description | Returns | Example |
|----------|-------------|---------|---------|
| `explain_error(error_text)` | Full AI-powered error explanation | Dict with explanation, confidence, method | `explain_error("NameError: name 'x' is not defined")` |
| `quick_explain(error_text)` | Fast rule-based explanation | String explanation | `quick_explain("TypeError: can only concatenate str (not 'int') to str")` |
| `detect_language(error_text)` | Detect programming language | Language enum | `detect_language("TypeError: Cannot read property 'length' of undefined")` |
| `parse_error(error_text)` | Parse error details | ErrorInfo object | `parse_error("TS2322: Type 'string' is not assignable to type 'number'")` |
| `get_supported_languages()` | Get list of supported languages | List of Language enums | `get_supported_languages()` |

### Context Managers

| Context Manager | Description | Example |
|----------------|-------------|---------|
| `auto_explain_exceptions()` | Automatically explain any exceptions | `with auto_explain_exceptions(): ...` |
| `watch_process(command)` | Monitor a running process for errors | `with watch_process("python script.py"): ...` |

### Decorators

| Decorator | Description | Example |
|-----------|-------------|---------|
| `explain_function_errors()` | Automatically explain errors in decorated function | `@explain_function_errors()` |

**See [API Documentation](API_DOCUMENTATION.md) for complete API reference.**

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest

# Run specific test categories
python -m pytest test_multi_language.py
python -m pytest test_api_proper.py
python -m pytest test_watcher.py
python -m pytest test_multi_model.py

# Run with coverage
python -m pytest --cov=xerror

# Run with verbose output
python -m pytest -v

# Run tests in parallel
python -m pytest -n auto
```

### Test Coverage

| Component | Test Files | Coverage | Status |
|-----------|------------|----------|--------|
| Core Language Detection | `test_multi_language.py` | ✅ 100% | 🟢 Complete |
| Python API | `test_api_proper.py` | ✅ 100% | 🟢 Complete |
| Real-time Monitoring | `test_watcher.py` | ✅ 100% | 🟢 Complete |
| Multi-Model Support | `test_multi_model.py` | ✅ 100% | 🟢 Complete |
| Error Parsing | `test_parser.py` | ✅ 100% | 🟢 Complete |
| Rule-Based Explainer | `test_rule_based.py` | ✅ 100% | 🟢 Complete |

### Test Examples

```bash
# Test language detection
python test_multi_language.py

# Test API functionality
python test_api_proper.py

# Test watcher functionality
python test_watcher.py

# Test multi-model support
python test_multi_model.py
```

## 🔧 Advanced Usage

### AI Mode vs Offline Mode

| Feature | AI Mode | Offline Mode |
|---------|---------|--------------|
| API Key Required | ✅ Yes | ❌ No |
| Internet Connection | ✅ Yes | ❌ No |
| Response Time | 2-5 seconds | Instant |
| Explanation Quality | High (contextual) | Good (rule-based) |
| Coverage | All errors | Common errors |
| Cost | API usage | Free |
| Best For | Complex/unique errors | Common errors, offline use |

```bash
# AI mode (requires API key)
xerror error.log

# Offline mode (no API key needed)
xerror error.log --offline
```

### Multi-Model Support

| Model | Provider | Status | Features | Cost |
|-------|----------|--------|----------|------|
| Gemini 1.5 Flash | Google | ✅ Active | Fast, cost-effective | Low |
| Gemini 1.5 Pro | Google | ⚠️ Limited | Higher quality, slower | Medium |
| OpenAI GPT-4 | OpenAI | 🔧 Optional | High quality, paid | High |
| Ollama Local | Local | 🔧 Optional | Offline, customizable | Free |

### Custom Configuration

```bash
# Use custom API key for this session
xerror error.log --api-key your-custom-key

# Use different AI model
xerror error.log --model gemini-1.5-pro

# Set custom log directory
export ERROR_EXPLAINER_LOG_DIR=/custom/path
xerror error.log --save

# Set default model
export DEFAULT_MODEL=gemini-1.5-flash
```

### Search with Filters

```bash
# Search by error type
xerror search "NameError"

# Search by language
xerror search "python"

# Search by keyword
xerror search "undefined"

# Search by filename
xerror search "views.py"

# Limit search results
xerror search "error" --limit 5

# Search with date range
xerror search "error" --since "2024-01-01" --until "2024-12-31"
```

## 🚨 Troubleshooting

### Common Issues

| Issue | Solution | Status |
|-------|----------|--------|
| **API Key Error** | Set `GOOGLE_API_KEY` environment variable | ✅ Fixed |
| **Language Not Detected** | Use `--offline` mode or check error format | ✅ Fixed |
| **Slow Response** | Use offline mode or check internet connection | ✅ Fixed |
| **Import Error** | Install with `pip install xerror` | ✅ Fixed |
| **Permission Denied** | Check file permissions or use `--offline` | ✅ Fixed |

### Error Messages

```bash
# If you see: "No API key found"
export GOOGLE_API_KEY=your-api-key-here

# If you see: "Language not detected"
xerror error.log --offline

# If you see: "Import error"
pip install --upgrade xerror

# If you see: "Permission denied"
chmod +r error.log
```

### Performance Tips

- Use `--offline` mode for faster responses
- Save explanations with `--save` to avoid re-analyzing
- Use specific error messages rather than full logs
- Set up your API key in `.env` file for convenience

## 📁 Supported File Formats

| Format | Extension | Description | Example |
|--------|-----------|-------------|---------|
| Log files | `.log` | Standard log files | `error.log` |
| Text files | `.txt` | Plain text files | `error.txt` |
| Python files | `.py` | Python source files | `script.py` |
| Error files | `.error` | Dedicated error files | `error.error` |
| Any text | `*` | Any text-based file | `output` |

## 🏗️ Project Structure

```
xerror/
├── xerror/
│   ├── __init__.py              # Package initialization
│   ├── cli.py                   # Command line interface
│   ├── config.py                # Configuration management
│   ├── explainer.py             # AI explanation engine
│   ├── parser.py                # Error parsing logic
│   ├── rule_based_explainer.py  # Offline rule-based analysis
│   ├── api.py                   # Python API functions
│   ├── watcher.py               # Real-time process monitoring
│   ├── models.py                # Multi-model support
│   ├── language_parsers.py      # Multi-language parsing
│   └── utils.py                 # Utility functions
├── examples/
│   ├── error_sample.log         # Python error example
│   ├── javascript_error.log     # JavaScript error example
│   ├── typescript_error.log     # TypeScript error example
│   ├── cpp_error.log            # C++ error example
│   ├── java_error.log           # Java error example
│   └── api_usage_examples.py    # API usage examples
├── setup.py                     # Package setup
├── requirements.txt             # Dependencies
├── env.example                  # Environment template
├── README.md                    # This file
└── API_DOCUMENTATION.md         # API documentation
```

## 🔮 Roadmap

| Feature | Status | Priority | ETA | Description |
|---------|--------|----------|-----|-------------|
| VSCode Extension | 🔧 In Progress | High | Q4 2024 | IDE integration with real-time error detection |
| GitHub Actions CI | 🔧 In Progress | Medium | Q4 2024 | Automated testing and deployment |
| Desktop Notifications | 📋 Planned | Medium | Q1 2025 | Get notified of critical errors |
| More Languages (Go, Rust) | 📋 Planned | Low | Q2 2025 | Extended language support |
| Web Interface | 📋 Planned | Low | Q3 2025 | Browser-based error analysis |
| Mobile App | 📋 Planned | Low | Q4 2025 | iOS/Android error analysis |

## 🛠️ Development

### Local Development Setup

```bash
# Clone the repository
git clone https://github.com/xerror/xerror.git
cd xerror

# Install in development mode
pip install -e .

# Install development dependencies
pip install -r requirements.txt

# Set up environment
cp env.example .env
# Edit .env with your API keys
```

### Development Commands

```bash
# Run tests
python -m pytest

# Run linting
flake8 xerror/

# Format code
black xerror/

# Type checking
mypy xerror/

# Build package
python setup.py sdist bdist_wheel

# Install from local build
pip install dist/xerror-0.1.0.tar.gz

# Run security checks
bandit -r xerror/
```

### Contributing Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run tests: `python -m pytest`
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📋 Requirements

| Component | Version | Required | Notes |
|-----------|---------|----------|-------|
| Python | 3.10+ | ✅ Yes | Core requirement |
| Google Gemini API | Latest | ⚠️ For AI mode | Free tier available |
| Internet Connection | - | ⚠️ For AI mode | Not needed for offline mode |
| Click | 8.1.0+ | ✅ Yes | CLI framework |
| Rich | 13.0.0+ | ✅ Yes | Terminal formatting |

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Areas

| Area | Description | Priority | Status |
|------|-------------|----------|--------|
| Language Support | Add new programming languages | High | 🔧 In Progress |
| Error Patterns | Improve error detection patterns | High | 🔧 In Progress |
| AI Models | Add support for new AI providers | Medium | 📋 Planned |
| Performance | Optimize parsing and analysis speed | Medium | 📋 Planned |
| Documentation | Improve docs and examples | Low | ✅ Complete |

### How to Contribute

1. **Report Bugs**: Use [GitHub Issues](https://github.com/xerror/xerror/issues)
2. **Request Features**: Use [GitHub Discussions](https://github.com/xerror/xerror/discussions)
3. **Submit Code**: Follow the contributing guidelines above
4. **Improve Docs**: Submit PRs for documentation improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Gemini](https://ai.google.dev/) for providing the AI capabilities
- [Click](https://click.palletsprojects.com/) for the CLI framework
- [Rich](https://rich.readthedocs.io/) for beautiful terminal output
- [Python Community](https://www.python.org/community/) for inspiration
- All contributors and users who provided feedback

## 👨‍💻 Author

**Avishek Devnath**
- 📧 Email: [avishekdevnath@gmail.com](mailto:avishekdevnath@gmail.com)
- 🌐 GitHub: [@avishekdevnath](https://github.com/avishekdevnath)
- 💼 LinkedIn: [Avishek Devnath](https://linkedin.com/in/avishekdevnath)

## 📞 Support

| Channel | Link | Response Time | Best For |
|---------|------|---------------|----------|
| 📧 Email | [avishekdevnath@gmail.com](mailto:avishekdevnath@gmail.com) | 24-48 hours | Personal support, feature requests |
| 🐛 Issues | [GitHub Issues](https://github.com/xerror/xerror/issues) | 1-3 days | Bug reports, technical issues |
| 📖 Documentation | [GitHub Wiki](https://github.com/xerror/xerror/wiki) | Instant | How-to guides, tutorials |
| 💬 Discussions | [GitHub Discussions](https://github.com/xerror/xerror/discussions) | 1-2 days | General questions, community help |

---

**Made with ❤️ by [Avishek Devnath](mailto:avishekdevnath@gmail.com) for developers everywhere** 