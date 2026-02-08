uv init --app uv-fast-api && uv-fast-api


uv add "fastapi[standard]"

### Direct script
uv run python main.py

### DEV
uv run fastapi dev

### PROD
uv run fastapi run