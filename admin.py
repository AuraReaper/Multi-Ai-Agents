from openagi.llms.gemini import GeminiModel
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
os.environ['Gemini_MODEL'] = 'gemini-1.5-flash-002'
os.environ['Gemini_TEMP'] = '0.5'

config = GeminiModel.load_from_env_config()
llm_g = GeminiModel(config=config)


from openagi.actions.tools.ddg_search import DuckDuckGoSearch
from openagi.memory import Memory
from openagi.planner.task_decomposer import TaskPlanner
from openagi.actions.tools.tavilyqasearch import TavilyWebSearchQA
from openagi.actions.tools.serper_search import SerperSearch
from openagi.actions.tools.exasearch import ExaSearch
from openagi.agent import Admin
from openagi.worker import Worker
from openagi.actions.files import WriteFileAction , ReadFileAction , CreateFileAction
from openagi.actions.tools.webloader import WebBaseContextTool


os.environ['TAVILY_API_KEY'] = os.getenv('TAVILY_API_KEY')
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
os.environ['EXA_API_KEY'] = os.getenv('EXA_API_KEY')

admin = Admin(
    llm=llm_g,
    planner=TaskPlanner(human_intervene=True),
    memory=Memory(
        long_term=True,
        ltm_threshold=0.8,
        long_term_dir="memory"
    ),
    actions=[CreateFileAction , WriteFileAction] ,
    max_iterations=2
)




industry_insight_specialist = Worker(
        role="Senior Industry Analyst",
        instructions=""" As an Industry Research Analyst, you will perform an in-depth analysis of the target company or industry to identify strategic opportunities for AI and Generative AI applications.
                Follow these steps :
                1. Segment the Industry: Use a tools to research the target industry (e.g., Automotive, Retail, Healthcare) and identify primary market segments.
                2. Analyze Offerings: Identify key products, services, and strategic areas (e.g., operations, supply chain) that define the company’s positioning.
                3. Competitive Landscape: Find competitors and assess their AI/ML adoption by using industry reports, annual reports, and press releases.
                4. Highlight AI Readiness: Identify gaps in AI adoption within the industry and the specific company.
                5. Summarize Findings: Compile findings in a report with an overview of industry opportunities and competitor insights, prioritizing relevance to the company's goals.

                Output: A structured summary that details the industry landscape, primary competitors, and key areas where AI/ML could be impactful for the target company.
        """,
        actions=[
                DuckDuckGoSearch,
                SerperSearch,
                WriteFileAction,
                ReadFileAction,
                WebBaseContextTool,
                CreateFileAction,
        ],
        llm=llm_g,
)

technology_strategist = Worker(
        role="AI & Innovation Strategist",
        instructions=""" As a Use Case Innovator, your task is to propose AI and GenAI use cases that align with industry standards and market trends. Follow these steps:

                1. Trend Analysis: Leverage tools such as ExaSearch or SerperSearch for industry trend analysis, focusing on how AI, ML, and GenAI are being used in similar industries.
                2. Use Case Ideation: Based on the industry research, brainstorm and draft relevant AI/ML use cases for the target company that could enhance operations, customer service, or product quality.
                3. Benchmarking: Compare the proposed use cases to industry standards, ensuring they align with successful applications of AI in the sector.
                4. Prioritize Use Cases: Rank use cases by feasibility, impact, and alignment with company objectives.
                5. Summarize in a Proposal: Draft a concise report on the top 3-5 use cases, including potential benefits, challenges, and resource requirements.
                6. You can refer to reports and insights on AI and digital transformation from industry-specific sources such as McKinsey, Deloitte, or Nexocode.
                7. Search for industry-specific use cases (e.g., “how is the retail industry leveraging AI and ML” or “AI applications in automotive manufacturing”).

                Output: A detailed proposal highlighting feasible and impactful AI/ML applications, prioritized by strategic fit and potential impact
        """,
        actions=[
                DuckDuckGoSearch,
                ExaSearch ,
                SerperSearch,
                WriteFileAction,
                ReadFileAction,
                WebBaseContextTool,
                CreateFileAction
        ] ,
        llm=llm_g,
)

resource_curator = Worker(
        role="Data Asset Manager",
        instructions=""" As a Data Resource Curator, your role is to gather essential datasets and assets to support the identified AI/ML use cases.Follow these steps:
                        1. Dataset Discovery: Search platforms like Kaggle, Hugging Face, and GitHub for datasets aligned with each proposed use case.
                        2. Data Quality Assessment: Evaluate datasets based on relevance, volume, and quality, ensuring they align with company needs and model requirements.
                        3. Link Resources: Save resource links and categorize them by use case.
                        4. GenAI Solution Recommendation (Optional): Suggest additional generative AI solutions like automated reporting or AI-driven document searches that complement the collected resources.
                        5. Compile Resource Summary: Create a list of resources, including links and a brief description of each dataset's purpose, in a text or markdown file.

                        Output: A structured list of resource assets, including datasets, tools, and potential GenAI solutions, organized by use case applicability.
        """,
        actions=[
                WriteFileAction,
                ReadFileAction,
                WebBaseContextTool,
                DuckDuckGoSearch,
                CreateFileAction
        ],
        llm=llm_g,
)


final_proposal = Worker(
    role="Proposes the final output",
    instructions= """
                List down the top use cases that can be delivered to the customer, ensuring they are relevant to the company’s goals and operational needs.
                1. Ensure to add references through which certain use cases were suggested
                2. Resource Asset links should be clickable.
        """ ,
    actions=[
                WriteFileAction,
                ReadFileAction,
                WebBaseContextTool,
                CreateFileAction
        ],
    llm=llm_g,
)

admin.assign_workers([industry_insight_specialist , technology_strategist , resource_curator , final_proposal ])

output_filename = "jindal_steel_ai_proposal.md"

res = admin.run(
    query=""" 
        How can Jindal Steel and Power Limited  use AI/ML to enhance operational efficiency, improve product quality, and expand service offerings in India. 
    """,
    description="""
        - Identify the company’s key offerings and strategic focus areas (e.g., operations,supply chain, customer experience, etc.).
        - Based on the industry conducted, analyze industry trends and standards within the company’s sector related to automation.
        - Save the resource links fetched in a text or markdown file.
    """,
)

print(res)



