import subprocess
import json
from pathlib import Path

# Path to the Terraform folder
TERRAFORM_DIR = Path(__file__).resolve().parents[2] / "terraform"


def terraform_init():
    """Initialize Terraform."""
    result = subprocess.run(
        ["terraform", "init"],
        cwd=TERRAFORM_DIR,
        capture_output=True,
        text=True
    )
    return result


def terraform_apply():
    """Create infrastructure."""
    result = subprocess.run(
        ["terraform", "apply", "-auto-approve"],
        cwd=TERRAFORM_DIR,
        capture_output=True,
        text=True
    )
    return result


def terraform_destroy():
    """Destroy infrastructure."""
    result = subprocess.run(
        ["terraform", "destroy", "-auto-approve"],
        cwd=TERRAFORM_DIR,
        capture_output=True,
        text=True
    )
    return result


def terraform_output():
    """Read Terraform outputs."""

    result = subprocess.run(
        ["terraform", "output", "-json"],
        cwd=TERRAFORM_DIR,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return None

    raw_outputs = json.loads(result.stdout)

    outputs = {}

    for key, value in raw_outputs.items():
        outputs[key] = value["value"]

    return outputs