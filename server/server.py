import os

from inventory import create_app


app = create_app(os.getenv("FLASK_ENV", "development"))

if __name__ == "__main__":
    app.run()
