from flask import Flask
from flask_cors import CORS

from services.terraform_service import (
    terraform_init,
    terraform_apply,
    terraform_destroy,
    terraform_output
)

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return {
        "project": "CloudForge",
        "status": "Backend Running",
        "version": "1.0"
    }


@app.route("/create-lab")
def create_lab():

    # Initialize Terraform
    terraform_init()

    # Apply Terraform
    result = terraform_apply()

    if result.returncode != 0:
        return {
            "status": "error",
            "message": result.stderr
        }, 500

    outputs = terraform_output()

    return {
        "status": "success",
        "outputs": outputs
    }


@app.route("/destroy-lab")
def destroy_lab():

    result = terraform_destroy()

    if result.returncode != 0:
        return {
            "status": "error",
            "message": result.stderr
        }, 500

    return {
        "status": "success",
        "message": "Lab destroyed successfully."
    }


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)