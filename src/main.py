import click
import os
import json

__version__ = "1.2.1"
__author__ = "Anderson Braz de Sousa"
__credits__ = "Open Community"


@click.command()
@click.option(
    "--project",
    prompt="Nome do Projeto",
    default="python-project",
    help="Project Name Python.",
)
def main(project):
    if os.path.isdir(project):
        click.echo(f"Projeto [{project}] já existe.")
    else:
        create_folder(project)
        create_vscode(project)
        click.echo(f"Criando projeto... [{project}]")
        start_project(project)


def create_vscode(source):
    path = source + "/" + ".vscode/"
    create_folder(path)
    configure_vscode(path)
    pass


def configure_vscode(path):
    set_settings(path)
    set_extensions(path)
    pass


def set_settings(path):
    content = fetch_settings()
    parsed = json.loads(content)
    file_settings = path + "settings.json"
    settings = open(file_settings, "w")
    settings.write(json.dumps(parsed, indent=4, sort_keys=True))
    settings.close()
    pass


def set_extensions(path):
    content = fetch_extensions()
    parsed = json.loads(content)
    file_extensions = path + "extensions.json"
    extensions = open(file_extensions, "w")
    extensions.write(json.dumps(parsed, indent=4, sort_keys=True))
    extensions.close()
    pass


def create_folder(folder):
    access_rights = 0o755
    os.mkdir(folder, access_rights)
    pass


def fetch_settings():
    settings = '{"python.pythonPath":".venv/bin/python","code-runner.executorMap":{"python":".venv/bin/python"},"code-runner.ignoreSelection":true,"code-runner.runInTerminal":true,"python.linting.enabled":true,"python.linting.mypyEnabled":false,"python.linting.flake8Enabled":true,"[python]":{"editor.formatOnSave":true,"editor.codeActionsOnSave":{"python.sortImports":true}},"python.testing.unittestEnabled":false,"python.testing.pytestEnabled":true,"python.testing.pytestPath":".venv/bin/pytest","python.formatting.provider":"black"}'
    return settings


def fetch_extensions():
    extensions = '{"recommendations":["formulahendry.code-runner","dracula-theme.theme-dracula","eamodio.gitlens","vscode-icons-team.vscode-icons","ms-python.python","ms-vscode.notepadplusplus-keybindings"]}'
    return extensions


def start_project(path):
    os.chdir(path)
    os.system("python3 -m venv .venv")
    # os.system("python -m pip install --upgrade pip")
    click.echo(f"Projeto: [{path}] - Criado com sucesso...")


if __name__ == "__main__":
    main()