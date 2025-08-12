#!/bin/bash

echo "🚀 Setting up Carlos Arroyo Portfolio..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first:"
    echo "   Visit: https://nodejs.org/"
    echo "   Or use Homebrew: brew install node"
    exit 1
fi

# Check Node.js version
NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "❌ Node.js version 18 or higher is required. Current version: $(node -v)"
    echo "   Please update Node.js: https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js version: $(node -v)"

# Check for package managers
if command -v pnpm &> /dev/null; then
    echo "📦 Using pnpm..."
    pnpm install
elif command -v yarn &> /dev/null; then
    echo "📦 Using yarn..."
    yarn install
elif command -v npm &> /dev/null; then
    echo "📦 Using npm..."
    npm install
else
    echo "❌ No package manager found. Please install npm, yarn, or pnpm."
    exit 1
fi

echo "✅ Dependencies installed successfully!"
echo ""
echo "🎉 Setup complete! To start the development server:"
echo "   npm run dev"
echo "   or"
echo "   pnpm dev"
echo "   or"
echo "   yarn dev"
echo ""
echo "🌐 Then open http://localhost:4321 in your browser"
