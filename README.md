# google_adk_mastery
A collection of hands-on projects built with Google's Agent Development Kit (ADK), demonstrating how to create, manage, and orchestrate sophisticated AI agents. The repository showcases practical applications of single agents, multi-agent collaboration, and advanced workflows (sequential, parallel, and looping) to automate complex tasks.
<img width="1808" height="820" alt="image" src="https://github.com/user-attachments/assets/0190ccb6-f446-4c56-867c-a766db69aae6" />
<img width="1823" height="808" alt="image" src="https://github.com/user-attachments/assets/d4c0c63d-1e40-4fc0-872f-c6a52b55d248" />
<img width="1871" height="613" alt="image" src="https://github.com/user-attachments/assets/37926727-0e65-4473-94bb-d846fe66784a" />
<img width="1887" height="390" alt="image" src="https://github.com/user-attachments/assets/5ef2ba8a-869a-40d7-940b-f417e760b7be" />


Agent Development Kit (ADK) – Hands-On Projects
A curated collection of practical, end-to-end projects built with Google's Agent Development Kit (ADK).
This repository demonstrates how to create, manage, and orchestrate sophisticated AI agents — from simple, single-agent setups to multi-agent collaboration and advanced workflows (sequential, parallel, looping) for automating complex tasks.

About the Agent Development Kit (ADK)
Google’s ADK is a full-stack, modular toolkit for developers and data scientists to build, manage, and scale real-world AI agent systems.
It moves beyond simple, single-prompt interactions to enable multi-step, intelligent workflows that can:

Chain together tools, memory, and runners

Break down complex business problems into logical micro-actions

Automate decision-making processes with persistent state and orchestration

💡 Core Strength: Turning high-level problems into a structured, automated series of steps — a critical skill in modern AI development.

Repository Structure
Each folder is a standalone project, designed to teach a specific ADK concept. Together, they form a progressive learning path from basics to advanced orchestration.

Project 1 – The Basic Agent
A foundation for understanding ADK agent structure:

Setting up folder hierarchy

Writing an agent’s instructions & description

Installing dependencies and running a minimal agent

Project 2 – Agents with Tools
Enhancing basic agents with real-world interactivity:

Creating custom Python functions

Integrating built-in tools (e.g., Google Search)

Allowing agents to fetch and process dynamic data

Project 3 – Multi-Agent Systems
Building specialized agent teams for complex problems:

Primary agent delegates tasks to sub-agents

Example roles: research_agent, writing_agent

Collaboration & information passing between agents

Project 4 – Workflow Orchestration
Harnessing ADK’s workflow engine with three key patterns:

Sequential – Ordered step-by-step execution

Parallel – Multiple agents working simultaneously, consolidated by a consolidation_agent

Looping – Continuous iteration until a condition is met (e.g., refinement loops)

Key Features Demonstrated
Multi-Model Support – Integrating Google Gemini, OpenAI, Anthropic, and more

Structured Outputs – Enforcing JSON schema for API/system integration

Session & State Management – Maintaining context across runs, persistent DB storage

Callbacks – Fine-grained control for logging, monitoring, and lifecycle customization

Getting Started
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git


2️⃣ Set up a virtual environment

python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows


3️⃣ Install dependencies
pip install google-adk

4️⃣ Configure API Keys
Create a .env file in the repo root:

GOOGLE_API_KEY=your_google_key_here
OPENAI_API_KEY=your_openai_key_here


5️⃣ Run a project
cd Project-Name
python agent.py
Then open the ADK Web UI to interact with your agent.

Sources & References
Google AI Studio – API keys & model docs

ADK Official Documentation

OpenAI API – Model integration guide
