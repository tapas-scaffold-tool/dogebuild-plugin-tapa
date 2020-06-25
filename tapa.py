from tapas.tools import prompt_license, generate_license_file, prompt_str, prompt_enum, prompt_bool
from pathlib import Path
from shutil import rmtree


def ask():
    prompt_license()
    prompt_str("plugin_name", prompt_string="Plugin name: dogebuild_")
    test_tools = ["nox", "none"]
    prompt_enum("test_tool", values=test_tools, prompt_string=f"Use integration test tool ({', '.join(test_tools)})? ")
    prompt_bool("use_travis", prompt_string="Use travis? ")
    prompt_bool("use_docs", prompt_string="Create documentation? ")


def post_init(
    license: str,
    test_tool: str,
    use_travis: bool,
    use_docs: bool,
):
    generate_license_file(license)

    if test_tool != "nox":
        Path("noxfile.py").unlink()

    if not use_travis:
        Path(".travis.yml").unlink()

    if not use_docs:
        Path("mkdocs.yml").unlink()
        rmtree(Path("docs"))

