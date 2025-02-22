# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ToolType(str, enum.Enum):
    """
    An enumeration.
    """

    BROWSER = "BROWSER"
    BING_SEARCH = "BING_SEARCH"
    REPLICATE = "REPLICATE"
    WOLFRAM_ALPHA = "WOLFRAM_ALPHA"
    ZAPIER_NLA = "ZAPIER_NLA"
    AGENT = "AGENT"
    OPENAPI = "OPENAPI"
    CHATGPT_PLUGIN = "CHATGPT_PLUGIN"
    METAPHOR = "METAPHOR"
    PUBMED = "PUBMED"
    CODE_EXECUTOR = "CODE_EXECUTOR"

    def visit(
        self,
        browser: typing.Callable[[], T_Result],
        bing_search: typing.Callable[[], T_Result],
        replicate: typing.Callable[[], T_Result],
        wolfram_alpha: typing.Callable[[], T_Result],
        zapier_nla: typing.Callable[[], T_Result],
        agent: typing.Callable[[], T_Result],
        openapi: typing.Callable[[], T_Result],
        chatgpt_plugin: typing.Callable[[], T_Result],
        metaphor: typing.Callable[[], T_Result],
        pubmed: typing.Callable[[], T_Result],
        code_executor: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToolType.BROWSER:
            return browser()
        if self is ToolType.BING_SEARCH:
            return bing_search()
        if self is ToolType.REPLICATE:
            return replicate()
        if self is ToolType.WOLFRAM_ALPHA:
            return wolfram_alpha()
        if self is ToolType.ZAPIER_NLA:
            return zapier_nla()
        if self is ToolType.AGENT:
            return agent()
        if self is ToolType.OPENAPI:
            return openapi()
        if self is ToolType.CHATGPT_PLUGIN:
            return chatgpt_plugin()
        if self is ToolType.METAPHOR:
            return metaphor()
        if self is ToolType.PUBMED:
            return pubmed()
        if self is ToolType.CODE_EXECUTOR:
            return code_executor()
