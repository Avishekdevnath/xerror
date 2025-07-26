#!/usr/bin/env python3
"""
Examples of using the Error Explainer API for automated error handling.
"""

import error_explainer
import logging


def example_1_basic_usage():
    """Basic usage - explain an error string."""
    print("=== Example 1: Basic Usage ===")
    
    error_msg = "NameError: name 'undefined_variable' is not defined"
    
    # Rule-based explanation (no API key needed)
    result = error_explainer.explain_error(error_msg, use_ai=False)
    print(f"Rule-based explanation: {result['explanation'][:100]}...")
    
    # AI explanation (requires API key)
    # result = error_explainer.explain_error(error_msg, use_ai=True)
    # print(f"AI explanation: {result['explanation'][:100]}...")


def example_2_current_exception():
    """Explain the currently active exception."""
    print("\n=== Example 2: Current Exception ===")
    
    try:
        # This will cause an error
        undefined_variable
    except Exception:
        # Explain the current exception
        result = error_explainer.explain_current_exception(use_ai=False)
        print(f"Current exception explanation: {result['explanation'][:100]}...")


def example_3_context_manager():
    """Use context manager for automatic error explanation."""
    print("\n=== Example 3: Context Manager ===")
    
    def on_error_callback(result):
        print(f"🚨 Error occurred! Explanation: {result['explanation'][:100]}...")
    
    with error_explainer.auto_explain_exceptions(
        use_ai=False,
        on_error=on_error_callback,
        reraise=False  # Don't reraise the exception
    ):
        # This error will be automatically explained
        undefined_variable
    
    print("Code continued after error!")


def example_4_function_decorator():
    """Use decorator to automatically explain function errors."""
    print("\n=== Example 4: Function Decorator ===")
    
    @error_explainer.explain_function_errors(use_ai=False)
    def problematic_function():
        return undefined_variable
    
    try:
        problematic_function()
    except Exception:
        print("Function error was automatically explained!")


def example_5_logging_integration():
    """Integrate with Python's logging system."""
    print("\n=== Example 5: Logging Integration ===")
    
    # Set up logging integration
    error_explainer.setup_logging_integration(use_ai=False)
    
    # Configure logging
    logging.basicConfig(level=logging.ERROR)
    
    try:
        undefined_variable
    except Exception:
        # This will automatically trigger error explanation
        logging.error("An error occurred", exc_info=True)


def example_6_quick_explanations():
    """Use quick explanation functions."""
    print("\n=== Example 6: Quick Explanations ===")
    
    error_msg = "TypeError: can only concatenate str (not 'int') to str"
    
    # Quick rule-based explanation
    explanation = error_explainer.quick_explain(error_msg)
    print(f"Quick explanation: {explanation[:100]}...")
    
    # AI explanation (if API key is available)
    # ai_explanation = error_explainer.ai_explain(error_msg)
    # print(f"AI explanation: {ai_explanation[:100]}...")


def example_7_test_integration():
    """Example of test integration (would be used in conftest.py)."""
    print("\n=== Example 7: Test Integration ===")
    
    # This would typically be in conftest.py
    def pytest_runtest_logreport(report):
        if report.failed and report.longrepr:
            result = error_explainer.explain_error(
                str(report.longrepr), 
                use_ai=False
            )
            if result.get('success', False):
                print(f"🧐 Test Failure Explanation:\n{result['explanation']}")
    
    print("Test integration function created!")


def example_8_automated_error_handling():
    """Complete example of automated error handling in a real application."""
    print("\n=== Example 8: Automated Error Handling ===")
    
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
    
    # Test the automated error handling
    processor = DataProcessor()
    
    try:
        processor.process_data([])  # This will trigger ValueError
    except Exception:
        print("Error was automatically explained and logged!")
    
    try:
        processor.process_data(10)  # This will trigger ZeroDivisionError
    except Exception:
        print("Another error was automatically explained and logged!")


def example_9_batch_error_processing():
    """Process multiple errors in batch."""
    print("\n=== Example 9: Batch Error Processing ===")
    
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


if __name__ == "__main__":
    print("🧪 Error Explainer API Examples")
    print("=" * 50)
    
    # Run all examples
    example_1_basic_usage()
    example_2_current_exception()
    example_3_context_manager()
    example_4_function_decorator()
    example_5_logging_integration()
    example_6_quick_explanations()
    example_7_test_integration()
    example_8_automated_error_handling()
    example_9_batch_error_processing()
    
    print("\n✅ All examples completed!")
    print("\n💡 To use AI explanations, set your GOOGLE_API_KEY environment variable")
    print("   and change use_ai=False to use_ai=True in the examples above.") 