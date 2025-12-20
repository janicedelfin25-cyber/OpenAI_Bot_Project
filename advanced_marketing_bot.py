import os
import json
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class AdvancedMarketingConsultant:
    """An advanced digital marketing consultancy bot with specialized functions."""
    
    def __init__(self):
        self.conversation_history = []
        self.sessions = {}
        self.current_session = None
        self.system_prompt = """You are an expert digital marketing consultant with 15+ years of experience.
        
Your expertise includes:
- Strategic digital marketing planning
- SEO and SEM optimization
- Social media marketing and management
- Content marketing and strategy
- Email marketing campaigns
- PPC advertising (Google Ads, Facebook Ads)
- Marketing analytics and data interpretation
- Brand development and positioning
- Customer acquisition and retention strategies
- Marketing automation
- Conversion rate optimization
- Market research and competitor analysis
- Growth hacking techniques
- Influencer marketing
- Video marketing strategy

When responding:
1. Provide specific, actionable recommendations
2. Consider budget, industry, and target audience
3. Suggest data-driven metrics to track success
4. Offer both quick wins and long-term strategies
5. Be practical about timelines and ROI expectations
6. Ask clarifying questions when needed
7. Provide examples and case studies when relevant

Maintain a professional, consultative tone while being approachable."""
    
    def create_session(self, session_name: str) -> str:
        """Create a new consultation session."""
        session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.sessions[session_id] = {
            "name": session_name,
            "created": datetime.now().isoformat(),
            "history": []
        }
        self.current_session = session_id
        return session_id
    
    def analyze_marketing_strategy(self, strategy_description: str) -> str:
        """Analyze a marketing strategy and provide recommendations."""
        prompt = f"""Please analyze the following marketing strategy and provide:
1. Strengths
2. Weaknesses
3. Opportunities for improvement
4. Potential risks
5. ROI estimation
6. 90-day action plan

Strategy Description:
{strategy_description}"""
        
        return self.chat(prompt)
    
    def generate_social_media_plan(self, industry: str, audience: str, budget: str) -> str:
        """Generate a social media marketing plan."""
        prompt = f"""Create a comprehensive social media marketing plan with:
1. Platform selection and justification
2. Content calendar overview (30 days)
3. Posting frequency and best times
4. Content types and themes
5. Engagement strategies
6. Analytics metrics to track
7. Budget allocation per platform

Industry: {industry}
Target Audience: {audience}
Monthly Budget: {budget}"""
        
        return self.chat(prompt)
    
    def optimize_conversion_funnel(self, funnel_description: str) -> str:
        """Provide recommendations to optimize a conversion funnel."""
        prompt = f"""Analyze this conversion funnel and provide optimization recommendations:

Current Funnel:
{funnel_description}

Please provide:
1. Identified bottlenecks
2. Conversion rate improvement strategies
3. A/B testing recommendations
4. Landing page optimization tips
5. Call-to-action improvements
6. Implementation priority and timeline"""
        
        return self.chat(prompt)
    
    def seo_audit_recommendations(self, website_info: str) -> str:
        """Provide SEO audit recommendations."""
        prompt = f"""Based on this website information, provide comprehensive SEO recommendations:

Website Info:
{website_info}

Include:
1. On-page SEO improvements
2. Technical SEO fixes
3. Backlink strategy
4. Keyword research focus areas
5. Content optimization priorities
6. Local SEO recommendations (if applicable)
7. Competitive analysis insights
8. Implementation roadmap with timeline and priority"""
        
        return self.chat(prompt)
    
    def budget_allocation_plan(self, total_budget: str, goals: str, industry: str) -> str:
        """Create a budget allocation plan across marketing channels."""
        prompt = f"""Create a detailed budget allocation plan with:

Total Budget: {total_budget}
Business Goals: {goals}
Industry: {industry}

Provide:
1. Recommended channel allocation (percentages and amounts)
2. Justification for each allocation
3. Expected ROI by channel
4. Month-by-month breakdown for first 90 days
5. Quick wins vs. long-term investments
6. Contingency recommendations
7. Key metrics to monitor per channel"""
        
        return self.chat(prompt)
    
    def chat(self, user_message: str) -> str:
        """Send a message to the bot and get a response."""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Store in session if exists
        if self.current_session and self.current_session in self.sessions:
            self.sessions[self.current_session]["history"].append({
                "role": "user",
                "content": user_message,
                "timestamp": datetime.now().isoformat()
            })
        
        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                }
            ] + self.conversation_history,
            temperature=0.7,
            max_tokens=1500
        )
        
        # Extract assistant response
        assistant_message = response.choices[0].message.content
        
        # Add assistant response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        # Store in session if exists
        if self.current_session and self.current_session in self.sessions:
            self.sessions[self.current_session]["history"].append({
                "role": "assistant",
                "content": assistant_message,
                "timestamp": datetime.now().isoformat()
            })
        
        return assistant_message
    
    def save_session(self, filename: str = None) -> str:
        """Save current session to a JSON file."""
        if not self.current_session or self.current_session not in self.sessions:
            return "No active session to save."
        
        session = self.sessions[self.current_session]
        if filename is None:
            filename = f"session_{self.current_session}.json"
        
        with open(filename, 'w') as f:
            json.dump(session, f, indent=2)
        
        return f"Session saved to {filename}"
    
    def reset_conversation(self):
        """Reset conversation history."""
        self.conversation_history = []
    
    def list_sessions(self) -> str:
        """List all sessions."""
        if not self.sessions:
            return "No sessions created yet."
        
        result = "Sessions:\n"
        for session_id, session_data in self.sessions.items():
            result += f"  - {session_data['name']} ({session_id})\n"
        return result


def main():
    """Main function to run the advanced marketing consultancy bot."""
    print("=" * 70)
    print("🎯 ADVANCED DIGITAL MARKETING CONSULTANCY BOT")
    print("=" * 70)
    print("\nWelcome! I'm your AI-powered advanced digital marketing consultant.")
    print("I can help with comprehensive marketing strategies and analysis.")
    print("\nCommands:")
    print("  'strategy'  - Analyze a marketing strategy")
    print("  'social'    - Generate social media plan")
    print("  'funnel'    - Optimize conversion funnel")
    print("  'seo'       - SEO audit recommendations")
    print("  'budget'    - Create budget allocation plan")
    print("  'session'   - Create new consultation session")
    print("  'list'      - List all sessions")
    print("  'save'      - Save current session")
    print("  'clear'     - Clear conversation history")
    print("  'quit'      - Exit the bot")
    print("\n" + "=" * 70 + "\n")
    
    consultant = AdvancedMarketingConsultant()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            elif user_input.lower() == 'quit':
                print("\nThank you for using the Advanced Marketing Consultancy Bot!")
                print("Goodbye! 👋\n")
                break
            
            elif user_input.lower() == 'session':
                session_name = input("Enter session name: ").strip()
                session_id = consultant.create_session(session_name)
                print(f"✓ Session '{session_name}' created: {session_id}\n")
            
            elif user_input.lower() == 'list':
                print(consultant.list_sessions() + "\n")
            
            elif user_input.lower() == 'save':
                result = consultant.save_session()
                print(f"✓ {result}\n")
            
            elif user_input.lower() == 'clear':
                consultant.reset_conversation()
                print("✓ Conversation history cleared.\n")
            
            elif user_input.lower() == 'strategy':
                print("\nDescribe your marketing strategy:")
                strategy = input().strip()
                print("\n🤖 Consultant: ", end="")
                response = consultant.analyze_marketing_strategy(strategy)
                print(response + "\n")
            
            elif user_input.lower() == 'social':
                industry = input("Industry: ").strip()
                audience = input("Target audience: ").strip()
                budget = input("Monthly budget: ").strip()
                print("\n🤖 Consultant: ", end="")
                response = consultant.generate_social_media_plan(industry, audience, budget)
                print(response + "\n")
            
            elif user_input.lower() == 'funnel':
                print("Describe your conversion funnel:")
                funnel = input().strip()
                print("\n🤖 Consultant: ", end="")
                response = consultant.optimize_conversion_funnel(funnel)
                print(response + "\n")
            
            elif user_input.lower() == 'seo':
                print("Describe your website:")
                website = input().strip()
                print("\n🤖 Consultant: ", end="")
                response = consultant.seo_audit_recommendations(website)
                print(response + "\n")
            
            elif user_input.lower() == 'budget':
                budget = input("Total budget: ").strip()
                goals = input("Business goals: ").strip()
                industry = input("Industry: ").strip()
                print("\n🤖 Consultant: ", end="")
                response = consultant.budget_allocation_plan(budget, goals, industry)
                print(response + "\n")
            
            else:
                print("\n🤖 Consultant: ", end="")
                response = consultant.chat(user_input)
                print(response + "\n")
        
        except KeyboardInterrupt:
            print("\n\nBot interrupted. Exiting...\n")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")


if __name__ == "__main__":
    main()
