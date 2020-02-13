import sys
import flask

from pathlib import Path

folder = str(Path(__file__).parent.absolute().parent)
sys.path.insert(0, folder)

# from pypi_org.infrastructure.view_modifiers import response
# import pypi_org.services.package_service as package_service

app = flask.Flask(__name__)


def main():
    register_blueprints()
    app.run(debug=True)


def register_blueprints():
    from pypi_org.views import home_views
    from pypi_org.views import package_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)


# @app.route("/")
# @response(template_file="home/index.html")
# def index():
#     test_packages = package_service.get_latest_packages()
#     return {"packages": test_packages}
#     # return flask.render_template("home/index.html", packages=test_packages)
#
#
# @app.route("/about")
# @response(template_file="home/about.html")
# def about():
#     return {}


if __name__ == "__main__":
    main()
