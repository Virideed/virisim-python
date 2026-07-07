# ViriSIM Python SDK

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)

Official Python SDK for integrating the ViriSIM AI Governance, Observability, Runtime Control, and Compliance API into Python applications and AI agents.

Audit AI inputs and outputs for PII, regulatory violations, bias, hallucinations, safety risks, and policy violations before they reach users.

---

## Features

- AI Compliance Auditing
- PII Detection
- Regulatory Compliance Checks
- Bias Detection
- Hallucination Detection
- Safety Risk Detection
- Policy Enforcement
- Real-Time Risk Scoring
- Compliance Logging
- Callback Support
- Cryptographic Audit Evidence (SHA-256, ECDSA, RFC 3161)
- Hash-Chained Session Integrity
- Pre-Generation Guardrails
- Safe Input/Output Redaction
- Fine-Tuning Data Generation
- DPO Documentation
- Coverage of 330+ Global Regulations, Standards & Frameworks
- Support for 83 Jurisdictions
- Compatible with LangChain, CrewAI, OpenAI Agents SDK, AutoGen, and custom Python applications

---

## Installation

```bash
pip install virisim
```

---

## Quick Start

The example below shows a typical integration. Optional fields such as your_company_signature and your_company_signing_key_id can be provided for advanced integrations.

```python
from virisim import VirisimClient

client = VirisimClient(api_key="sk-viri-YOUR-API-KEY")

result = client.audit(
    user_id="YOUR_USER_ID",
    company_name="RothsMind Corp",
    use_case="finance",
    your_company_user_id="user_123",
    your_company_user_session_id="session_456",
    model_version="gpt-5", 
    input={
        "value": "Summarize the attached financial report.",
        "format": "text",
        "country": "canada"
    },
    output={
        "value": "The report shows a 14% increase in revenue.",
        "format": "text",
        "country": "canada"
    }
)

print(result)
```

---

## Framework Integrations

### LangChain

```python
from virisim import VirisimClient
from langchain.tools import tool

client = VirisimClient(api_key="sk-viri-xxx")

@tool
def audit_ai_output(input_text: str, output_text: str, policy: str = None) -> dict:
    """Audit AI output for compliance before returning to user."""
    return client.audit(
        user_id="agent_001",
        company_name="Acme Inc.",
        use_case="general",
        your_company_user_id="agent_001",
        your_company_user_session_id="session_001",
        model_version="gpt-5",
        agent_tool="LangChain",
        callback_url="https://your-domain.com/webhook",
        policy=policy,
        input={"value": input_text, "format": "text", "country": "US"},
        output={"value": output_text, "format": "text", "country": "US"}
    )
    
``` 
### CrewAI

```python
from virisim import VirisimClient
from crewai.tools import tool

client = VirisimClient(api_key="sk-viri-xxx")

@tool
def audit_ai_output(input_text: str, output_text: str, policy: str = None) -> dict:
    """Audit AI output for compliance before returning to user."""
    return client.audit(
        user_id="agent_001",
        company_name="Acme Inc.",
        use_case="general",
        your_company_user_id="agent_001",
        your_company_user_session_id="session_001",
        model_version="gpt-5",
        agent_tool="CrewAI",
        callback_url="https://your-domain.com/webhook",
        policy=policy,
        input={"value": input_text, "format": "text", "country": "US"},
        output={"value": output_text, "format": "text", "country": "US"}
    )
    
``` 

### OpenAI Agents SDK

```python
from virisim import VirisimClient
from agents import function_tool

client = VirisimClient(api_key="sk-viri-xxx")

@function_tool
def audit_ai_output(input_text: str, output_text: str, policy: str = None) -> dict:
    """Audit AI output for compliance before returning to user."""
    return client.audit(
        user_id="agent_001",
        company_name="Acme Inc.",
        use_case="general",
        your_company_user_id="agent_001",
        your_company_user_session_id="session_001",
        model_version="gpt-5",
        agent_tool="OpenAI",
        callback_url="https://your-domain.com/webhook",
        policy=policy,
        input={"value": input_text, "format": "text", "country": "US"},
        output={"value": output_text, "format": "text", "country": "US"}
    )
    
```  

### Custom Python

```python
from virisim import VirisimClient

client = VirisimClient(api_key="sk-viri-xxx")

result = client.audit(
    user_id="agent_001",
    company_name="Acme Inc.",
    use_case="general",
    your_company_user_id="agent_001",
    your_company_user_session_id="session_001",
    model_version="gpt-5",
    agent_tool="python-sdk",
    callback_url="https://your-domain.com/webhook",
    input={"value": input_text, "format": "text", "country": "US"},
    output={"value": output_text, "format": "text", "country": "US"}
)

if result.get("verdict") == "Review needed":
    return "Response blocked for compliance review."
```  
  
 ---

## Requirements

- Python 3.9+

---

## API Payload


### Payload Fields

- `user_id`
- `company_name`
- `use_case`
- `api_key`
- `timestamp`
- `your_company_user_id`
- `your_company_user_session_id`
- `model_version`
- `your_company_signature` *(optional)*
- `your_company_signing_key_id` *(optional)*
- `agent_tool`
- `callback_url`
- `policy`

- `input`
  - `value`
  - `format`
  - `country`

- `output`
  - `value`
  - `format`
  - `country`
  
The SDK automatically constructs the payload, authenticates requests, and communicates securely with the ViriSIM Compliance API, allowing developers to focus on building AI applications rather than managing API requests.

---

## Documentation

[ViriSIM Documentation](https://www.virideed.com/virisim/documentation/?search=agent-tool)

---

## Support

[support@virideed.com](mailto:support@virideed.com)

---

## License

MIT License
