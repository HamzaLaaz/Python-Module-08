import sys
import importlib


def check_dependency(package_name: str) -> tuple:
    """
    Check if a package is installed and return its version.
    Args:
        package_name: The pip package name (e.g. 'pandas')
    Returns:
        Tuple of (is_available: bool, version: str)
    """
    try:
        module = importlib.import_module(package_name)
        version = module.__version__
        return True, version
    except ImportError:
        return False, 'not installed'


def check_all_dependencies() -> bool:
    """
    Check all required dependencies and print their status.
    Returns:
        True if all dependencies are available, False otherwise.
    """
    print("Checking dependencies:")
    required = [
        ('pandas', 'Data manipulation ready'),
        ('requests', 'Network access ready'),
        ('matplotlib', 'Visualization ready'),
    ]
    all_ok = True
    for package, description in required:
        available, version = check_dependency(package)
        if available:
            print(f"  [OK] {package} ({version}) - {description}")
        else:
            print(f"  [MISSING] {package} - {version}")
            all_ok = False
    return all_ok


def show_install_instructions() -> None:
    """Display installation instructions for missing dependencies."""
    print()
    print("Some dependencies are missing. To install them:")
    print()
    print("  Using pip:")
    print("    pip install -r requirements.txt")
    print()
    print("  Using Poetry:")
    print("    poetry install")
    print("    poetry run python loading.py")


def generate_visualization() -> None:
    """
    Generate simulated Matrix data and save a line plot
    of the first 50 signal values.
    """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    np.random.seed(42)
    numbers = np.random.randint(1, 101, size=1000)
    df = pd.DataFrame({"value": numbers})
    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")
    x = np.arange(1, 51)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(
        x,
        df['value'].values[:50],
        color='steelblue',
        marker='o',
        linewidth=2,
        markersize=6,
        label='Matrix Signal'
    )
    ax.set_title('Matrix Data Analysis')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.grid(True)
    ax.legend()
    output_file = 'matrix_analysis.png'
    plt.savefig(output_file)
    plt.close()
    print(f"\nAnalysis complete!\nResults saved to: {output_file}")


def main() -> None:
    """Main entry point for the loading program."""
    print("\nLOADING STATUS: Loading programs...\n")
    # Check all dependencies first
    all_available = check_all_dependencies()
    if not all_available:
        show_install_instructions()
        sys.exit(1)
    # Generate and save the visualization
    generate_visualization()


if __name__ == '__main__':
    main()
