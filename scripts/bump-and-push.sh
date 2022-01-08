# With a clean git stage, this script bumps up package version, tags it
# and pushes to PyPI, assuming PyPI API key is available in $HOME/.pypirc.
# It eventually opens the github release
# page where you need to create a new release used by pip
printf "Initiating Tag and Push ..."
printf "activate virtual env containing bump2version ..."
# bump version and tag
printf "bump the version ..."
bumpversion minor
# printf "push to github ..."
git push origin
# push tag
LAST_TAG=$(git describe --tags `git rev-list --tags --max-count=1`)
git push origin $LAST_TAG
# printf "push to PyPI ..."
python setup.py sdist
twine upload dist/*
printf "open github release page to create the latest release for pip use..."
open https://github.com/aljabadi/logster/releases/new
