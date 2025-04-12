########### This is the complete general LLM code from Metaculus tools ###################

import inspect
import logging
import os
from typing import Any
from groq import Groq
from perplexity import Perplexity

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
perplexity_client = Perplexity(api_key=os.getenv("PERPLEXITY_API_KEY"))


def groq_request(query, mode, system):
    try:
        if mode == "reasoning":
            reasoning_model="llama3-8b-8192"
            logging.info(f"Groq reasoning tasked with :{reasoning_model}")
            response = groq_client.chat.completions.create(
                model=reasoning_model,
                messages=[{"role": "user", "content": query}],
            )
            response = response.choices[0].message.content
            tokens = response.usage.total_tokens
            return response, tokens
        elif mode == "summary":
            summary_model="llama3-8b-8192"
            logging.info(f"Groq summary tasked with :{summary_model}")
            response = groq_client.chat.completions.create(
                model=summary_model,
                messages=[{"role": "user", "content": query}],
            )
            response = response.choices[0].message.content
            tokens = response.usage.total_tokens
            return response, tokens
        elif mode == "chat":
            chat_model="llama3-8b-8192"
            logging.info(f"Groq chat tasked with :{chat_model}")
            response = groq_client.chat.completions.create(
                model=chat_model,
                messages=[{"role": "user", "content": query}],
            )
            response = response.choices[0].message.content
            tokens = response.usage.total_tokens
            return response, tokens
    except Exception as e:
        fall_back(query, mode, system)
        return f"Exception raised: {e}"
    
def perplexity_request(query, mode, system):
    try:
        if mode == "short_answer":
            short_research_model="llama3-8b-8192"
            logging.info(f"Perplexity short research tasked with :{short_research_model}")
            response = perplexity_client.chat.completions.create(
                model=short_research_model,
                messages=[{"role": "user", "content": query}],
            )
            response = response.choices[0].message.content
            tokens = response.usage.total_tokens
            return response, tokens
        elif mode == "deep_research":
            deep_research_model="llama3-8b-8192"
            logging.info(f"Perplexity deep research tasked with :{deep_research_model}")
            response = perplexity_client.chat.completions.create(
                model=deep_research_model,
                messages=[{"role": "user", "content": query}],
            )
            response = response.choices[0].message.content
            tokens = response.usage.total_tokens
            return response, tokens
    except Exception as e:
        fall_back(query, mode, system)
        return f"Exception raised: {e}"

def fall_back(query, mode, system):
    pass
    # back up LLMs will be added here


