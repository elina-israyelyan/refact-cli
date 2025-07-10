# Refact CLI

A command-line interface for interacting with the Refact AI platform, providing three distinct modes: Refact, Reason, and Act.

## Overview

This CLI communicates with the Refact API server available at: https://github.com/elina-israyelyan/refact

The Refact platform provides AI-powered reasoning, action execution, and conversational capabilities through a REST API and with utilizing  [`ReAct: Synergizing Reasoning and Acting in Language Models`]( https://arxiv.org/abs/2210.03629)


## Installation

### Prerequisites
- Python 3.10 or higher

### Install from source
```bash
git clone <repository-url>
cd refact-cli
pip install .
```

## Usage

Run the CLI with:
```bash
refact
```

This will present you with a menu to choose between three modes:

### 1. Refact Mode
Interactive chat mode that provides a conversational interface with the Refact agent.

**Features:**
- Real-time streaming responses with color-coded output
- Thought process visualization


**Usage:**
```bash
refact> What is the capital of France?
```

**Output Format:**
- **Thought**: Agent's reasoning process
- **Observation**: Agent's observations
- **Final answer**: Direct response

### 2. Reason Mode
Simple question-answer mode for getting reasoning responses.

**Features:**
- Direct text responses
- Clean, simple interface

**Usage:**
```bash
reason> Explain quantum computing in simple terms
```

### 3. Act Mode
Action-oriented mode for performing specific operations.

**Available Actions:**

#### Mathematical Operations
- **multiply**: Multiply two numbers (a × b)
- **power**: Raise a number to a power (a^b)
- **divide**: Divide two numbers (a ÷ b)
- **subtract**: Subtract two numbers (a - b)
- **sum**: Add two numbers (a + b)

#### Search Operations
- **lookup**: Search for specific information with entity and string parameters
- **search**: Search for information about a specific entity

**Usage Examples:**
```bash
# Mathematical operations
Choose an action: multiply
Enter value for a: 5
Enter value for b: 3
Result: 15

# Search operations
Choose an action: lookup
Enter entity: weather
Enter string: New York
```

## General Commands

| Command | Description |
|---------|-------------|
| `exit` or `quit` | Exit the current mode and return to main menu |

## Configuration

The CLI connects to the Refact API server. Make sure you have proper API URL by exporting environmental variable `REFACT_API_URL` and the Refact server is running.

### API Server
This CLI communicates with the Refact API server available at: https://github.com/elina-israyelyan/refact

The server provides the following endpoints:
- `/refact` - Streaming conversational responses
- `/reason` - Reasoning responses
- `/act` - Action execution (mathematical operations, search, etc.)

## Dependencies

- `aiohttp==3.12.13` - Async HTTP client
- `pydantic==2.11.7` - Data validation
- `pydantic_core==2.33.2` - Pydantic core functionality
- `questionary==2.0.1` - Interactive command line prompts


