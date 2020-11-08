from tempfile import TemporaryDirectory
from json import dumps

import nox


@nox.session()
@nox.parametrize("tapas_version", [
    "0.1.10",
    # Add another supported tapas version
    "latest",  # Keep it if you want to always test latest version
])
def tests(session, tapas_version):
    if tapas_version == "latest":
        session.install(f"tapas")
    else:
        session.install(f"tapas=={tapas_version}")
    with TemporaryDirectory() as tmp:
        params = {
            "plugin_name": "test-name",
            "license": "mit",
            "test_tool": "nox",
            "use_travis": "y",
            "use_docs": "y",
            "readme": "y",
            "git": "y",
        }
        session.run("tapas", "dir:.", tmp, "-p", dumps(params))
