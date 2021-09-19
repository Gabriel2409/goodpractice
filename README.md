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

# Creation of package (src folder)

# Basic api
