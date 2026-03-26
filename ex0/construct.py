import sys
import os
import site


def is_virtual_env() -> bool:
    """Detect whether we are running inside a virtual environment."""
    # Method 1: Check VIRTUAL_ENV environment variable
    virtual_env = os.environ.get('VIRTUAL_ENV')
    # Method 2: Compare sys.prefix with sys.base_prefix
    # If different, we're in a venv
    in_venv = sys.prefix != sys.base_prefix
    return bool(virtual_env) or in_venv


def get_env_info() -> dict:
    """Collect information about the current Python environment."""
    virtual_env_path = os.environ.get('VIRTUAL_ENV', '')
    env_name = (os.path.basename(virtual_env_path)
                if virtual_env_path else 'None detected')
    return {
        'python_path': sys.executable,
        'virtual_env_name': env_name,
        'virtual_env_path': virtual_env_path,
        'is_venv': is_virtual_env(),
        'site_packages': site.getsitepackages() if is_virtual_env() else [],
    }


def show_outside_matrix(info: dict) -> None:
    """Display output when running in the global environment."""
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {info['python_path']}")
    print(f"Virtual Environment: {info['virtual_env_name']}")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\nScripts\nactivate   # On Windows")
    print("\nThen run this program again.")


def show_inside_matrix(info: dict) -> None:
    """Display output when running inside a virtual environment."""
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {info['python_path']}")
    print(f"Virtual Environment: {info['virtual_env_name']}")
    print(f"Environment Path: {info['virtual_env_path']}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("\nPackage installation path:")
    packages = site.getsitepackages()[0]
    print(f"{packages}")


def main() -> None:
    """Main entry point — detect environment and display info."""
    info = get_env_info()
    if info['is_venv']:
        show_inside_matrix(info)
    else:
        show_outside_matrix(info)


if __name__ == '__main__':
    main()
