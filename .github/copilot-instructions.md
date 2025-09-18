# War Card Game Project

War is a simple card game project currently in initial development. This repository is minimal and contains only basic documentation at this time.

**Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Current Repository State

This repository is in its initial state with minimal content:
- Only contains a basic README.md file
- No build system, dependencies, or source code exists yet
- No CI/CD pipeline configured
- No specific programming language chosen yet

## Working Effectively

### Initial Project Setup
Since this is a minimal repository, you'll likely need to bootstrap a project. The environment supports multiple programming languages:

**Available Languages and Tools:**
- Python 3.12.3 - Available and working
- Node.js v20.19.5 with npm 10.8.2 - Available and working  
- Go 1.24.7 - Available and working
- GCC compiler - Available for C/C++ development
- Git, Make - Standard development tools available

**Timing Expectations:**
- Python execution: < 1 second
- Node.js/npm init: < 1 second
- Basic file operations: Instantaneous
- NEVER CANCEL: If choosing to add build systems later, allow 2+ minutes for initial setup

### For Node.js Development
If developing as a Node.js project:
```bash
# Initialize package.json (takes < 1 second)
npm init -y

# Install dependencies (timing varies by packages)
npm install

# Common commands would be:
npm test      # Run tests (none exist yet)
npm start     # Start application (none configured yet)
npm run build # Build project (none configured yet)
```

### For Python Development  
If developing as a Python project:
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies from requirements.txt (if it exists)
pip install -r requirements.txt

# Run the application
python3 main.py  # or whatever main file exists
```

### For Go Development
If developing as a Go project:
```bash
# Initialize Go module
go mod init github.com/rescuereli1/war

# Build the project
go build

# Run tests
go test ./...

# Run the application  
go run main.go  # or whatever main file exists
```

## Current Repository Structure

```
/home/runner/work/war/war/
├── .git/           # Git repository data
├── .github/        # GitHub configuration (created for these instructions)
│   └── copilot-instructions.md
└── README.md       # Basic project description
```

## Validation

Since this is a minimal repository:
- **No build validation needed yet** - No build system exists
- **No test validation needed yet** - No tests exist  
- **No linting needed yet** - No code exists to lint
- **No application testing possible** - No application exists yet

**When the project grows, always:**
- Validate any new code by running it
- Test new features manually to ensure they work
- Run any linting tools that get added to the project
- Ensure builds complete successfully before committing
- Test at least one complete user scenario after making changes

**For a Card Game "War" Project - Expected Manual Testing Scenarios:**
When the application is developed, test these scenarios:
- Create/shuffle a deck of cards
- Deal cards to two players  
- Play several rounds of the war card game
- Handle ties (war situations) correctly
- Display winner when game ends
- Restart/reset game functionality

## Navigation and Key Areas

Currently there are no key areas since this is a minimal repository. When the project develops:
- Look for main application entry points (main.py, index.js, main.go, etc.)
- Check for configuration files (package.json, requirements.txt, go.mod, etc.)
- Find test directories (test/, tests/, __tests__/, etc.)
- Look for build scripts (Makefile, build.sh, npm scripts)

## Development Workflow

1. **Choose a programming language** based on requirements
2. **Initialize the project** using language-specific tools
3. **Create basic project structure** (src/, test/, docs/, etc.)
4. **Add build and test automation**
5. **Set up CI/CD pipeline** in .github/workflows/
6. **Add linting and formatting tools**

## Common Commands That Work

These commands are validated to work in the current environment:

```bash
# Check available tools
python3 --version    # Python 3.12.3
node --version       # v20.19.5  
npm --version        # 10.8.2
go version          # go1.24.7 linux/amd64
git --version       # Available
which make gcc      # Available

# Basic operations
ls -la              # List files
git status          # Check repository status
git log --oneline   # View commit history

# File operations (all instantaneous)
cat README.md       # View readme content
mkdir dirname       # Create directories
touch filename      # Create files
```

## Future Development Notes

When adding features to this repository:
- **NEVER CANCEL builds or tests** - Allow adequate time for completion
- **Set timeouts of 60+ minutes** for any build processes you add
- **Always test manually** after making code changes
- **Document new commands** and their expected timing in these instructions
- **Update validation scenarios** when adding new functionality
- **Add specific build/test/run instructions** once you establish the project structure

## Troubleshooting

Current known issues:
- No known issues since no complex functionality exists yet
- All basic commands (git, python3, node, npm, go) work correctly  
- File operations are instantaneous as expected

When issues arise:
- Check these instructions first
- Verify the command worked in the current environment
- Document any new command timing or issues discovered
- Update these instructions if you find missing or incorrect information

**If you need to start development:**
1. Choose your preferred language (Python, Node.js, or Go recommended)
2. Follow the appropriate setup section above
3. Create a basic project structure
4. Add a simple "Hello World" or basic card game functionality  
5. Test it works before expanding features
6. Update these instructions with any new build/test/run commands

---
*These instructions were created for a minimal repository state. Update them as the project grows and develops new capabilities.*