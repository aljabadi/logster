#------------ bump package version and push
# With a clean git stage, this script bumps up package version, tags it, pushes to github
# and pushes to PyPI, assuming PyPI API key is available in $HOME/.pypirc.
# It eventually opens the github release
# page where you need to create a new release used by pip
#------------
# it requires the following packages:
# pip install bump2version twine
#------------
printf "initiating Tag and Push ..."
# bump version and tag
printf "bump the version, tag, commit and push ..."
bumpversion minor
# printf "push to github ..."
git push origin
printf "push the tag ..."
LAST_TAG=$(git describe --tags `git rev-list --tags --max-count=1`)
git push origin $LAST_TAG
printf "push to PyPI ..."
python setup.py sdist
twine upload dist/*
printf "open github release page to create the latest release for pip use..."
open https://github.com/aljabadi/logster/releases/new
