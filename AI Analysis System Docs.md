# AI Analysis System Documentation

## Table of Contents
1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Components](#components)
4. [Configuration](#configuration)
5. [Workers](#workers)
6. [Usage](#usage)
7. [Dependencies](#dependencies)

## Overview

This system implements an AI-powered business analysis framework that leverages Google's Gemini LLM to perform comprehensive industry analysis and AI use case identification. The system employs a multi-worker architecture to break down complex business analysis tasks into specialized components.

## System Architecture

The system follows a hierarchical structure with an `Admin` class orchestrating multiple specialized `Worker` instances. Each worker is designed to handle specific aspects of the analysis process, from industry research to resource curation.

### Core Components Flow
```
Admin
  ├─ Industry Insight Specialist
  ├─ Technology Strategist
  ├─ Resource Curator
  └─ Final Proposal Generator
```

## Components

### Core Classes

#### 1. GeminiModel
- Handles interactions with Google's Gemini LLM
- Configurable through environment variables
- Supports model version selection and temperature settings

#### 2. Admin
```python
admin = Admin(
    llm=llm_g,
    planner=TaskPlanner(human_intervene=True),
    memory=Memory(
        long_term=True,
        ltm_threshold=0.8,
        long_term_dir="memory"
    ),
    actions=[CreateFileAction, WriteFileAction],
    max_iterations=2
)
```

Key Features:
- Task planning with human intervention capability
- Long-term memory management
- File operation handling
- Limited iteration control

## Configuration

### Environment Variables
Required environment variables:
- `GOOGLE_API_KEY`: Authentication for Gemini API
- `TAVILY_API_KEY`: For web search functionality
- `SERPER_API_KEY`: For search operations
- `EXA_API_KEY`: For specialized search functions

Model Configuration:
- `Gemini_MODEL`: Set to 'gemini-1.5-flash-002'
- `Gemini_TEMP`: Temperature setting (default: 0.5)

## Workers

### 1. Industry Insight Specialist
**Role**: Senior Industry Analyst

Capabilities:
- Industry segmentation analysis
- Competitive landscape assessment
- AI readiness evaluation
- Market positioning analysis

Actions:
- DuckDuckGoSearch
- SerperSearch
- File operations (Read/Write/Create)
- Web context analysis

### 2. Technology Strategist
**Role**: AI & Innovation Strategist

Capabilities:
- Trend analysis
- Use case ideation
- Industry benchmarking
- Solution prioritization

Actions:
- Multiple search capabilities (DuckDuckGo, Exa, Serper)
- Document management
- Web context analysis

### 3. Resource Curator
**Role**: Data Asset Manager

Capabilities:
- Dataset discovery
- Quality assessment
- Resource categorization
- GenAI solution recommendations

Actions:
- File operations
- Web context analysis
- DuckDuckGo search

### 4. Final Proposal Generator
**Role**: Proposal Synthesizer

Capabilities:
- Use case prioritization
- Reference management
- Resource linking
- Final document compilation

## Usage

### Basic Implementation
```python
# Initialize the system
admin.assign_workers([
    industry_insight_specialist,
    technology_strategist,
    resource_curator,
    final_proposal
])

# Run analysis
result = admin.run(
    query="How can [Company] use AI/ML to enhance operations?",
    description="Analysis parameters and requirements"
)
```

### Output Format
- Results are saved in Markdown format
- Default output file: `jindal_steel_ai_proposal.md`
- Includes clickable resource links
- Structured analysis with references

## Dependencies

Required Python packages:
- openagi.llms.gemini
- python-dotenv
- Various search tool implementations (DuckDuckGo, Serper, Exa)
- File operation handlers

## Best Practices

1. **Environment Setup**
   - Secure API key management
   - Proper environment variable configuration
   - Memory directory setup

2. **Worker Configuration**
   - Clear role definition
   - Appropriate action assignment
   - Specific instruction sets

3. **Output Management**
   - Consistent file naming
   - Proper markdown formatting
   - Resource link validation

## Error Handling

The system implements:
- API key validation
- Memory threshold management
- Iteration limits
- Human intervention points

## Notes

- The system is designed for business analysis and AI use case identification
- Supports human intervention in the analysis process
- Maintains long-term memory for context preservation
- Generates structured, referenceable output
