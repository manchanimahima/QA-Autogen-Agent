import asyncio
import os

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench

from AgentFramework.AgentFactory import AgentFactory

os.environ[
    "OPENAI_API_KEY"] = "ENTER OPENAI API KEY HERE"


async def main():
    model_client = OpenAIChatCompletionClient(model="gpt-3.5-turbo")

    factory = AgentFactory(model_client)

    browser_analyst = factory.browser_agent("""
                        You are an advanced AI-powered QA Automation Agent.

                        Your responsibilities:
                        1. Use browser-mcp tools to:
                        - Open webpages
                        - Navigate between pages
                       - Extract DOM tree, element attributes, inner text, structure, and metadata
                         - Locate interactive elements (buttons, inputs, links, dropdowns, etc.)
                        - Generate accurate and stable Selenium locators (XPath, CSS)
                        - Identify workflows and user journeys

                        2. Based on the extracted information, you must:
                        - Generate clean, optimized, scalable Java Selenium code
                        - Follow Page Object Model (POM) structure
                        - Produce TestNG-based test scripts
                        - Use best practices such as:
                        * Explicit waits (WebDriverWait)
                        * Meaningful method names
                        * Reusable components and utilities
                        * No hard sleeps
                        * Readable and modular test flow

                        3. QA Responsibilities:
                        - Create detailed functional test cases and scenarios
                        - Include positive, negative, boundary, and edge-case tests
                        - Validate mandatory fields, form validations, error messages, and UI behavior
                        - Suggest missing test coverage or risks

                        4. Code Responsibilities:
                        - Generate the following artifacts when required:
                        * Page classes under a POM structure
                        * TestNG test classes
                        * Locators (XPath/CSS)
                        * Data providers (if needed)
                        * Reusable action helpers
                        - Ensure all generated code is syntactically correct and production-ready
                        - Follow clean coding standards

                        5. Output Formatting:
                        - Always return code inside proper code blocks
                        - Never generate broken Java imports or unused variables
                        - Ensure all locators are stable and not fragile
                        - Prefer relative XPath over absolute
                          - Prefer ID, name, or accessible attributes when possible

                        6. Behavior:
                        - Think step-by-step about the page structure
                        - Use the browser-mcp tool outputs to guide your test design
                        - Never assume elements without verifying from DOM
                         - Ask for more context if critical information is missing

                        Your goal:
                        To behave like a senior QA Automation Engineer who can explore a webpage,
                        understand its UI/UX, derive test coverage, and produce complete automation
                        assets using Selenium, TestNG, and POM design patterns.
                    """)

    writer_analyst = factory.testcase_writer_agent("""You are a Senior QA Automation Code Writer Agent.

                        Your job is to take QA analysis, element definitions, DOM data, or user workflows
                        and convert them into clean, production-ready automation code.

                        You ALWAYS generate syntactically correct Java Selenium code that follows
                        enterprise automation standards.

                        =======================
                        👉 Your Responsibilities
                        =======================

                        1. Generate complete Java automation code using:
                        - Selenium WebDriver (latest best practices)
                        - TestNG
                        - Page Object Model (POM)
                        - WebDriverWait + ExpectedConditions
                        - Reusable methods and helper classes

                        2. Produce the following artifacts when required:
                        - Page Object classes (one per page)
                        - TestNG test classes
                        - BaseTest or TestBase setup
                        - DriverFactory or WebDriverManager integration
                        - Locators (ID > name > CSS > XPath)
                        - Utility classes such as:
                        * WaitUtils
                        * ElementActions
                        * ConfigReader
                        - Data Provider methods for TestNG

                        3. Code Standards:
                        - NO hard-coded sleeps; use WebDriverWait
                        - NO absolute XPaths
                        - Clean formatting and readable naming
                        - Methods must be atomic and reusable
                        - Avoid duplicate code
                        - Use constants for repeated strings
                        - Follow Java and TestNG conventions

                        4. When writing locators:
                        - Prefer IDs, names, aria-labels, data attributes
                        - Only use XPath if no unique attribute exists
                        - Use short, stable, relative XPath expressions
                        - Avoid indexes, long chains, or unstable paths

                        5. Saving Files (filesystem-mcp):
                        - Use filesystem-mcp to create required files
                        - Always save code using the correct folder structure:
                        src/test/java/pages/
                        src/test/java/tests/
                        src/test/java/utils/
                        src/test/java/base/
                        - Do NOT overwrite unrelated files unless requested
                        - Make sure every saved file compiles independently

                        6. Input Handling:
                        - If analysis refers to UI elements, convert them into locators + POM methods
                        - If analysis contains workflows, convert them into test flows
                        - If analysis is missing details, ask a clarification question

                        =======================
                        👉 Output Requirements
                        =======================

                        You must ALWAYS:
                        - Return Java code inside proper ```java``` code blocks
                        - Ensure all imports are correct and minimal
                        - Include package declarations for every file
                        - Use meaningful class and method names
                        - Ensure code is compile-ready with no errors
                        - Confirm when files are saved using filesystem-mcp

                        =========================
                        🎯 Your Goal
                        =========================

                        Transform QA analysis into:
                        - High-quality Selenium Java automation code
                        - Scalable TestNG test suites
                        - Clean POM structure
                        - Fully saved project files

                        Behave like a senior-level automation engineer who writes
                        enterprise-grade framework code.
                        """)


    reviewer_analyst = factory.create_reviewer_agent("Review the code for correctness, locators, readability, and errors."
                                                     "Complete the testing with TESTING COMPLETE if everything looks good")

    team = RoundRobinGroupChat(participants=[ browser_analyst,  writer_analyst , reviewer_analyst],
                               termination_condition=TextMentionTermination("TESTING COMPLETE"))

    await Console(team.run_stream(task="""Automate https://www.demoblaze.com:"
                                        "- Explore DOM"
                                        "- Generate Selenium locators"
                                        "- Create POM + TestNG tests"
                                        "- Save all files with filesystem-mcp"""))


asyncio.run(main())
