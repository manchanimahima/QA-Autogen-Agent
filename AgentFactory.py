from autogen_agentchat.agents import AssistantAgent

from AgentFramework.mcp_config import McpConfig


# A factory which can create all agents

class AgentFactory :

    def __init__(self, model_client):
        self.model_client=model_client

        self.mcp_config = McpConfig()

    def create_jira_agent(self, system_message):
        bug_analyst = AssistantAgent(name="BugAnalyst", model_client=self.model_client, workbench=self.mcp_config.get_jira_workbench(),
                                 system_message=system_message)

        return bug_analyst

    def create_automation_agent(self, system_message):
        automation_analyst = AssistantAgent(name="AutomationAgent", model_client=self.model_client, workbench=self.mcp_config.get_playwright_workbench(),
                                        system_message=system_message)

        return automation_analyst

    def browser_agent(self, system_message):
        automation_analyst = AssistantAgent(name="BrowserAgent", model_client=self.model_client, workbench=self.mcp_config.get_browser_workbench(),
                                        system_message=system_message)

        return automation_analyst

    def testcase_writer_agent(self, system_message):
        testcase_writer_analyst = AssistantAgent(name="TestCaseWriterAgent", model_client=self.model_client, workbench=self.mcp_config.get_fileServer_workbench(),
                                        system_message=system_message)

        return testcase_writer_analyst

    def create_reviewer_agent(self,system_message):
        testcase_reviewer_agent = AssistantAgent(name="reviewer",model_client=self.model_client, system_message=system_message)

        return testcase_reviewer_agent