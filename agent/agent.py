from .prompts import DEAL_ANALYSIS_PROMPT


class DealIntelligenceAgent:

    def __init__(self):
        self.system_prompt = DEAL_ANALYSIS_PROMPT

    def analyze_deal(self, deal_text):
        if not deal_text:
            return {
                "error": "Deal information is required"
            }

        return {
            "deal_text": deal_text,
            "analysis": {
                "summary": "Deal received for analysis.",
                "requirements": [],
                "risks": [],
                "opportunities": [],
                "deadlines": [],
                "next_actions": []
            }
        }


if __name__ == "__main__":
    agent = DealIntelligenceAgent()

    result = agent.analyze_deal(
        "Example deal: Customer wants an enterprise software contract."
    )

    print(result)