import os
import litellm
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key or groq_api_key == "gsk_PASTE_YOUR_NEW_KEY_HERE":
    raise RuntimeError("Set a valid GROQ_API_KEY in .env before starting the app.")

# Drop unsupported cache parameters.
litellm.drop_params = True

class GroqLLM(LLM):
    def _format_messages_for_provider(self, messages):
        formatted_messages = super()._format_messages_for_provider(messages)
        return [
            {key: value for key, value in message.items() if key != "cache_breakpoint"}
            for message in formatted_messages
        ]


groq_llm = GroqLLM(
    model="groq/openai/gpt-oss-120b",
    api_key=groq_api_key
)

# 5. Define Agents
data_analyst = Agent(
    role="Senior Business Data Analyst",
    goal="Analyze raw business context and identify key trends, risks, and performance metrics.",
    backstory="You are an expert data strategist who excels at uncovering core business operational insights.",
    verbose=True,
    llm=groq_llm
)

strategy_advisor = Agent(
    role="Chief Business Strategist",
    goal="Transform analytical insights into clear, actionable executive decisions.",
    backstory="You are an experienced business consultant skilled at turning data findings into practical growth strategies.",
    verbose=True,
    llm=groq_llm
)

# 6. Define Tasks
analysis_task = Task(
    description="Analyze the following query: '{query}'. Provide key analytical insights.",
    expected_output="A structured bullet-point breakdown of primary insights and potential risks.",
    agent=data_analyst
)

strategy_task = Task(
    description="Based on the findings, outline 3 high-impact strategic actions for executive leadership.",
    expected_output="A structured markdown table containing columns for Action, Core Elements (what will be done), Owner(s), Timeline (Key Milestones), and Expected Impact (Why it matters).",
    agent=strategy_advisor
)
# 7. Form Crew
bi_crew = Crew(
    agents=[data_analyst, strategy_advisor],
    tasks=[analysis_task, strategy_task],
    process=Process.sequential
)

# 8. Execute Crew Workflow
if __name__ == "__main__":
    prompt = "Our SaaS company saw a 15% increase in churn rate among small business customers last quarter."
    print("\n--- Running BI Copilot Analysis ---\n")
    result = bi_crew.kickoff(inputs={"query": prompt})
    print("\n================ FINAL REPORT ================\n")
    print(result)
