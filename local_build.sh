#!/bin/bash
set -e

# Install dependencies if needed
if ! uv run python -c "import hardboiled" 2>/dev/null; then
    uv sync
fi
if [ ! -d "node_modules" ]; then
    npm install
fi

# Build HTML FIRST (creates directory structure)
echo "Building HTML..."
uv run python main.py

# Build CSS SECOND (after directories exist)
echo "Building CSS..."
npm run build:css

echo "Build complete! Starting Netlify dev server..."
netlify dev --no-open
