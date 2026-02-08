# Will's Homelab
#### Documenting my various homelab projects

[wmboeckman.github.io/homelab](https://wmboeckman.github.io/homelab/)

## Running a local build

Ensure you have python 3 installed, then run the following to build and activate the virtual environment:

#### Windows (CMD or PowerShell)

```python.exe .\build-env.py && .\.venv\Scripts\activate```

#### Linux

```python build-env.py && source .venv/bin/activate```

From here, you can start a live server via MkDoc:

```mkdocs serve --livereload```