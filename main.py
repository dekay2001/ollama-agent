import asyncio

from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider
from ddgs import DDGS

provider = OllamaProvider(base_url="http://localhost:11434/v1")
model = OllamaModel(model_name="llama3.1:latest", provider=provider)
agent = Agent(
    model,
    system_prompt="You are a helpful research assistant with web search access.",
    retries=2,
)


@agent.tool
async def search_web(ctx, query: str) -> str:
    """Search the web using DuckDuckGo."""
    print(f"  [Searching: {query}]")
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=5))
    print(f"  [Found {len(results)} results]")
    return "\n".join(f"- {r['title']}: {r['body']}" for r in results)


async def main():
    print("Ollama Agent with Web Search (type 'quit' to exit)")
    print("-" * 50)
    while True:
        query = input("\nYou: ").strip()
        if not query or query.lower() in ("quit", "exit", "q"):
            break
        print("  [Thinking...]")
        result = await agent.run(query)
        print(f"\nAgent: {result.output}")


if __name__ == "__main__":
    asyncio.run(main())
