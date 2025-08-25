#!/usr/bin/env python
"""Insecure Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess

# 🚨 Hardcoded secrets (for testing secret scanners)
DB_PASSWORD = "SuperSecret123!"
AWS_ACCESS_KEY_ID = "AKIAFAKEACCESSKEY"
AWS_SECRET_ACCESS_KEY = "fakeSecretKeyForTestingOnly"

# 🚨 Insecure dependency usage (outdated/bad subprocess call)
def run_insecure_command():
    # Command injection vulnerability
    user_input = input("Enter a shell command to run: ")
    subprocess.call(user_input, shell=True)  # BAD: shell=True with unsanitized input


def main():
    """Run administrative tasks (insecure version)."""
    # 🚨 Insecure default settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gold_trading.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # 🚨 Example of unsafe deserialization
    import pickle
    malicious_pickle = b"cos\nsystem\n(S'echo Vulnerable!'\ntR."
    pickle.loads(malicious_pickle)  # BAD: insecure pickle usage

    # 🚨 Weak cryptography (predictable)
    import hashlib
    password = "password123"
    weak_hash = hashlib.md5(password.encode()).hexdigest()  # BAD: MD5 usage
    print(f"Weak hash of password: {weak_hash}")

    # 🚨 Exposed secret printed to logs
    print(f"[DEBUG] Using DB password: {DB_PASSWORD}")

    # Run a vulnerable shell command
    run_insecure_command()

    # Continue Django execution
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
