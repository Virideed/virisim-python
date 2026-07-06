import requests
from datetime import datetime, timezone
from typing import TypedDict

class Message(TypedDict):
    value: str
    format: str
    country: str

class VirisimClient:
    """Official Python SDK for the ViriSIM Compliance API."""

    def __init__(
        self,
        api_key: str,
        endpoint: str = "https://analyzecompliance-vrbinbrbkq-uc.a.run.app",
        timeout: int = 30,
    ):
        self.api_key = api_key
        self.endpoint = endpoint
        self.timeout = timeout

    def audit(
        self,
        *,
        user_id: str,
        company_name: str,
        use_case: str,
        your_company_user_id: str,
        your_company_user_session_id: str,
        model_version: str,
        input: Message,
        output: Message,
        your_company_signature: str | None = None,
        your_company_signing_key_id: str | None = None,
        agent_tool: str = "python-sdk",
        callback_url: str | None = None,
        policy: str | None = None,
    ) -> dict:
        """
        Audit AI prompts and responses for compliance, safety,
        hallucinations, bias, privacy and regulatory violations.

        Returns:
            JSON response from the ViriSIM Compliance API.
        """

        payload = {
            "user_id": user_id,
            "company_name": company_name,
            "use_case": use_case,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "your_company_user_id": your_company_user_id,
            "your_company_user_session_id": your_company_user_session_id,
            "model_version": model_version,
            "agent_tool": agent_tool,
            "callback_url": callback_url,
            "policy": policy,
            "input": input,
            "output": output,
        }

        if your_company_signature is not None:
            payload["your_company_signature"] = your_company_signature

        if your_company_signing_key_id is not None:
            payload["your_company_signing_key_id"] = your_company_signing_key_id

        response = requests.post(
            self.endpoint,
            json=payload,
            headers={
                "X-API-Key": self.api_key,
                "Content-Type": "application/json",
            },
            timeout=self.timeout,
        )

        response.raise_for_status()

        return response.json()
