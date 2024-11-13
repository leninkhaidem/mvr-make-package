import pathlib

from cookiecutter.main import cookiecutter
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from . import __version__

template = pathlib.Path(pathlib.Path(__file__).parent,
                        "mvr-template").absolute().as_posix()


def banner():
    tool_name = "mvr-make-package"

    description = ("This tool generates a folder structure with boilerplate files based on user input. "
                   "This will be used by the MVR framework")

    banner_text = Text(f"{tool_name} - {__version__}\n",
                       justify="center", style="bold bright_white")
    banner_text.append(f"\n{description}", style="bold white")

    banner = Panel(banner_text, expand=False, border_style="green",
                   title="Welcome", subtitle="Generating packages...")

    # Display the banner
    console = Console()
    console.print("\n")
    console.print(banner)
    console.print("\n")


def success():
    # Console instance
    console = Console()
    # Example completion message
    success_message = Text(
        "🎉 Package generated successfully! 🎉", justify="center", style="bold green")
    # Display the success message
    console.print(success_message)


def error(message: str):
    console = Console()
    error_text = Text(f"❌ {message}",
                      justify="center", style="bold red")
    error_panel = Panel(error_text, expand=False,
                        border_style="red", title="Error")
    console.print(error_panel)


def main():
    banner()
    try:
        cookiecutter(template)
        success()
    except Exception as e:
        error(str(e))
