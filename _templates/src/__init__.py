import datetime


name = "<<name>>"
package_name = "<<package-name>>"
author = "<<author>>"
author_email = "<<email>>"
description = "<<description>>"
url = "<<url>>"
project_urls = {
    <<requires::docs "Documentation": "https://automl.github.io/<<package-name>>/main" endrequires::docs>>,
    "Source Code": "https://github.com/automl/<<package-name>>",
}
copyright = f"Copyright {datetime.date.today().strftime('%Y')}, AutoML.org Freiburg-Hannover"
version = "0.0.1"
