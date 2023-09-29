from datetime import datetime

import os
import requests
import shutil

extensions = []
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = "Alabaster"
copyright = f"{datetime.now().year} Jeff Forcier"

exclude_patterns = ["_build"]

html_theme = "alabaster"
html_static_path = ['_static']
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "donate.html",
    ]
}
html_theme_options = {
    "description": "A light, configurable Sphinx theme",
    "github_user": "sphinx-doc",
    "github_repo": "alabaster",
    "fixed_sidebar": True,
    "tidelift_url": "https://tidelift.com/subscription/pkg/pypi-alabaster?utm_source=pypi-alabaster&utm_medium=referral&utm_campaign=docs",  # noqa
}

extensions.append("releases")
releases_github_path = "sphinx-doc/alabaster"
# Our pre-0.x releases are unstable / mix bugs+features
releases_unstable_prehistory = True

# source, destination
video_files = [
    ("https://overtag.dk/files/enable-pull-request-builders.mp4", "enable-pull-request-builders.mp4")
]

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename

rootdir = os.path.dirname(os.path.realpath(__file__))
videodir = os.path.join(rootdir, "_static", "videos")

if not os.path.exists(videodir):
    os.makedirs(videodir)

for source, dest in video_files:
    dest_path = os.path.join(videodir, dest)
    download_file(source, dest_path)
