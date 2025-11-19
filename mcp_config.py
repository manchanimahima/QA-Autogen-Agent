import os

from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench


class McpConfig:
    os.environ["JIRA_URL"] = "https://mmancha2510.atlassian.net"
    os.environ["JIRA_USERNAME"] = "mmancha2510@gmail.com"
    os.environ[
        "JIRA_API_TOKEN"] = "Enter JIRA API TOKEN"
    os.environ["JIRA_PROJECTS_FILTER"] = "CRED"

    @staticmethod
    def get_jira_workbench():
        jira_server_params = StdioServerParams(command="docker",
                                               args=[
                                                   "run", "-i", "--rm",
                                                   "--dns", "8.8.8.8", "--dns",
                                                   "1.1.1.1"  # for network connection issue
                                                   "-e", f"JIRA_URL={os.environ['JIRA_URL']}",
                                                   "-e", f"JIRA_USERNAME={os.environ['JIRA_USERNAME']}",
                                                   "-e", f"JIRA_API_TOKEN={os.environ['JIRA_API_TOKEN']}",
                                                   "-e", f"JIRA_PROJECTS_FILTER={os.environ['JIRA_PROJECTS_FILTER']}",
                                                   "ghcr.io/sooperset/mcp-atlassian:latest"
                                               ])

        return McpWorkbench(server_params=jira_server_params)

    def get_playwright_workbench(self):
        playwright_server_params = StdioServerParams(command="npx",
                                                     args=[
                                                         "@playwright/mcp@latest"
                                                     ])

        return McpWorkbench(server_params=playwright_server_params)

    def get_browser_workbench(self):
        browser_server_params = StdioServerParams(type="websocket",
                                                     url="ws://localhost:8000")

        return McpWorkbench(server_params=browser_server_params)

    def get_fileServer_workbench(self):
        fileSystem_server_params = StdioServerParams(command="npx",
                                                 args=[
                                                     "-y",
                                                     "@modelcontextprotocol/server-filesystem",
                                                     "C:/Users/spars/PycharmProjects/PythonProject/AutoGenAgenticAIProject",

                                                 ])

        return McpWorkbench(fileSystem_server_params)

