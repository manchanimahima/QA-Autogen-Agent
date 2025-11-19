# QA-Autogen-Agent

This framework contains 2 project related to day to day QA activities.

1. Automated Test Code Generator using AutoGen + MCP

This project is an AI-driven QA Automation Agent built using AutoGen, browser-mcp, and filesystem-mcp.
It automatically analyzes webpages, extracts DOM elements, and generates Java Selenium Test Automation code using POM + TestNG.

Perfect for:

Smart Test Case Generation
Auto-Selenium Locator Extraction
Automatic POM Class Creation
End-to-End Test Script Generation
Saving files directly using FileSystem MCP

| Component          | Technology                     |
| ------------------ | ------------------------------ |
| Agent Framework    | AutoGen                        |
| LLM                | gpt-4o-mini / gpt-3o  |
| Browser Automation | browser-mcp                    |
| File Management    | filesystem-mcp                 |
| Output Code        | Java + Selenium + TestNG + POM |
| Python Runtime     | Python 3.10+                   |


2. JiraDashboard

This is another project which takes the recent closed bugs from Jira Dashboard.
Creates the end to end smoke test cases.
Converts it into Playwright automation scripts.
Run the script.
If the case gets failed, reopen the defect in Jira dashboard.


