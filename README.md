# Good practices for a new repo

## Virtual environment

- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install --upgrade pip`

## Requirements

- Create a requirements.txt file and add the necessary packages in it
- To install requirements : `pip install -r requirements.txt`

## Requirements dev

### black : code formatter

- command line : `black <filename>`
- in vscode, when trying to format for the first time, choose black to format
  code
- Bonus : format on save

in your settings.json

```json
"python.formatting.provider": "black",
"editor.formatOnSave": true
```

### isort : sort import

- command line : `isort <filename>`
- Bonus : vscode :

```json
"editor.codeActionsOnSave": {
	"source.organizeImports": true
}
```

### flake8 : python linting and problems

Configuration : create a .flake8 file :

```
[flake8]
max-line-length = 88
extend-ignore = E203, E265
exclude = .git,__pycache__,old,build,dist,venv
```

Notes

- max-line-length 88 and E203 (whitespace before ':') to avoid conflicts with black
- E265 block comment should start with '# ' confilcts with vscode interactive windows where some lines are just #%%

Usage

- command line : `flake8 <filename>`

-vscode :

```json
"python.linting.flake8Enabled": true
```

### interrogate : check docstrings

Configuration : in the pytproject.toml file:

```
[tool.interrogate]
ignore-init-method = true
ignore-init-module = true
ignore-magic = false
ignore-semiprivate = false
ignore-private = false
ignore-property-decorators = false
ignore-module = true
ignore-nested-functions = false
ignore-nested-classes = true
ignore-setters = false
fail-under = 80
exclude = ["setup.py", "docs", "build", "venv"]
ignore-regex = ["^get$", "^mock_.*", ".*BaseClass.*"]
# possible values: 0 (minimal output), 1 (-v), 2 (-vv)
verbose = 2
quiet = false
whitelist-regex = []
color = true
omit-covered-files = false
```

Usage

- command line : `interrogate <filename> -vv`

-vscode : no settings.json but good extension : Python Docstring Generator

# Creation of package (src folder)

# Basic api
