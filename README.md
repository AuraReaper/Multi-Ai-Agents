# Market Research & Use Case Generation Agent

## Overview
This project implements a Multi-Agent architecture system designed to generate relevant AI and Generative AI (GenAI) use cases for companies and industries. The system conducts market research, analyzes industries, and provides resource assets for AI/ML solutions, with a focus on enhancing operations and customer experiences.

## Features
- Industry and company research automation
- Market standards analysis
- Use case generation for AI/ML implementation
- Resource asset collection and curation
- Automated proposal generation

## System Requirements
- Python 3.8+
- Google API Key (for Gemini)
- Tavily API Key
- Serper API Key
- Exa API Key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with the following:
```
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
SERPER_API_KEY=your_serper_api_key
EXA_API_KEY=your_exa_api_key
```

## Project Structure
```
├── main.py
├── requirements.txt
├── .env
├── memory/
│   └── long_term_memory/
└── output/
    └── proposals/
```

## Usage

1. Configure the environment variables in `.env`
2. Run the main script:
```python
python main.py
```

The system will:
1. Analyze the specified company/industry
2. Generate AI/ML use cases
3. Collect relevant resources
4. Create a comprehensive proposal

## Components

### 1. Industry Insight Specialist
- Conducts market research
- Analyzes industry segments
- Evaluates competitive landscape

### 2. Technology Strategist
- Identifies AI/ML opportunities
- Generates use cases
- Assesses technical feasibility

### 3. Resource Curator
- Collects relevant datasets
- Evaluates resource quality
- Organizes implementation assets

### 4. Final Proposal Generator
- Synthesizes findings
- Creates structured recommendations
- Generates detailed documentation

## Output
The system generates a markdown file containing:
- Industry analysis
- Proposed AI/ML use cases
- Resource links
- Implementation recommendations

## Contributing
1. Fork the repository
2. Create a feature branch
3. Submit a pull request
