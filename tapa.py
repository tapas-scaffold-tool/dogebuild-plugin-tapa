from pathlib import Path
from shutil import rmtree
import os

from tapas.tools import prompt_bool, prompt_enum, init_git_repo, prompt_str, prompt_license, generate_license_file


def ask():
    prompt_str("plugin_name", prompt_string="Plugin name: dogebuild_")
    test_tools = ["nox", "none"]
    prompt_enum("test_tool", values=test_tools, prompt_string=f"Use integration test tool ({', '.join(test_tools)})? ")
    prompt_bool("use_travis", prompt_string="Use travis? ")
    prompt_bool("use_docs", prompt_string="Create documentation? ")

    prompt_bool('readme', default_value="y", prompt_string="Create README.md file? [Y/n]: ")
    prompt_license()
    prompt_bool('git', default_value="y", prompt_string="Init git repository? [Y/n]: ")


def post_init(
    license: str,
    test_tool: str,
    use_travis: bool,
    use_docs: bool,
    readme: bool,
    git: bool
):
    if not readme:
        os.remove('README.md')

    generate_license_file(license)

    if test_tool != "nox":
        Path("noxfile.py").unlink()

    if not use_travis:
        Path(".travis.yml").unlink()

    if not use_docs:
        Path("mkdocs.yml").unlink()
        rmtree(Path("docs"))

    if git:
        init_git_repo(dot_files=[
            ".gitignore",
            ".travis.yml",
        ])

