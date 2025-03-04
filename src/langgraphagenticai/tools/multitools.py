from src.langgraphagenticai.tools.wikitools import WikipediaQueryRun
from src.langgraphagenticai.tools.wikitools import ArxivQueryRun

combinedtools ={
    "wiki":WikipediaQueryRun, 
    "arxiv":ArxivQueryRun
}
#    return [WikipediaQueryRun, ArxivQueryRun]
