```python
import sys
import platform

def check_platform_compatibility():
    """
    Check if the current platform and its version are compatible with Elysium OS.
    Returns a tuple (is_compatible, message) indicating compatibility and an informative message.
    """
    # Define the minimum required versions for different platforms
    required_versions = {
        'Windows': '10',
        'Darwin': '10.13',  # macOS High Sierra
        'Linux': None  # Assume all Linux versions are compatible
    }

    current_os = platform.system()
    current_version = platform.release()

    if current_os not in required_versions:
        return (False, f"Elysium OS is not supported on your operating system: {current_os}")

    # If the OS is Linux, it's assumed to be compatible
    if current_os == 'Linux' or (required_versions[current_os] and current_version >= required_versions[current_os]):
        return (True, f"Elysium OS is compatible with your platform: {current_os} {current_version}")
    else:
        return (False, f"Elysium OS requires at least {current_os} version {required_versions[current_os]}")

def main():
    """
    Main function to run the platform compatibility check.
    """
    is_compatible, message = check_platform_compatibility()
    if is_compatible:
        print("Compatibility check passed:", message)
    else:
        print("Compatibility check failed:", message)
        sys.exit(1)  # Exit with a non-zero status code to indicate an error

if __name__ == "__main__":
    main()
```