from pydantic_ai import Agent
from openai import AsyncOpenAI
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.mcp import MCPServerStdio
import os

from pydantic import BaseModel

class AgentOutput(BaseModel):
    output: str

system_prompt = """
You are an online music store agent tasked to retrieve a list of song tracks.
Only base your reply on the context provided.
"""

class QNAAgent:
    def __init__(self,nvidia_api_key,mcp_server_qna_path,inf_url):
        ## TODO
        ## define MCP server, model and agent
        self.mcp_server = MCPServerStdio(mcp_server_qna_path)
        self.model = OpenAIModel(
            model="nvidia/llama-3.3-nemotron-super-49b-v1",
            provider=OpenAIProvider(
                base_url=inf_url,
                api_key=nvidia_api_key
            )
        )
        self.agent = Agent(
            model=self.model,
            system_prompt=system_prompt,
            mcp_server=self.mcp_server,
            output_model=AgentOutput
        )
        pass

    async def run(self,query):
        ## TODO
        ## run agent with mcp servers and return output
        response = await self.agent.run(query)
        if response.output is None:
            raise ValueError("No output from agent")
        if not isinstance(response.output, str):
            raise ValueError("Output is not a string")
        if response.output.strip() == "":
            raise ValueError("Output is empty")
        if not response.output.endswith("."):
            response.output += "."
        if not response.output[0].isupper():
            response.output = response.output[0].upper() + response.output[1:]
        return response.output
        pass