import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize the OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please set it in your .env file or system environment.")

client = OpenAI(api_key=api_key)

class DigitalMarketingConsultant:
    """A digital marketing consultancy bot powered by OpenAI."""
    
    def __init__(self):
        self.conversation_history = []
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

When responding to clients:
1. Provide specific, actionable recommendations
2. Consider their budget, industry, and target audience
3. Suggest data-driven metrics to track success
4. Offer both short-term quick wins and long-term strategies
5. Be practical and realistic about timelines and ROI
6. Ask clarifying questions when needed to provide better advice

Always maintain a professional, consultative tone while being approachable and encouraging."""
    
    def chat(self, user_message: str) -> str:
        """Send a message to the bot and get a response."""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
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
            max_tokens=1000
        )
        
        # Extract assistant response
        assistant_message = response.choices[0].message.content
        
        # Add assistant response to history
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message
    
    def reset_conversation(self):
        """Reset conversation history."""
        self.conversation_history = []
        print("\n✓ Conversation history cleared.\n")
    
    def get_conversation_history(self) -> list:
        """Get the current conversation history."""
        return self.conversation_history


def main():
    """Main function to run the digital marketing consultancy bot."""
    print("=" * 70)
    print("🎯 DIGITAL MARKETING CONSULTANCY BOT")
    print("=" * 70)
    print("\nWelcome! I'm your AI-powered digital marketing consultant.")
    print("Ask me anything about digital marketing strategy, tactics, and optimization.")
    print("\nCommands:")
    print("  'clear'  - Clear conversation history")
    print("  'quit'   - Exit the bot")
    print("  'help'   - Show this help message")
    print("\n" + "=" * 70 + "\n")
    
    consultant = DigitalMarketingConsultant()
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Handle commands
            if not user_input:
                continue
            elif user_input.lower() == 'quit':
                print("\nThank you for using the Digital Marketing Consultancy Bot!")
                print("Goodbye! 👋\n")
                break
            elif user_input.lower() == 'clear':
                consultant.reset_conversation()
                continue
            elif user_input.lower() == 'help':
                print("\n" + "=" * 70)
                print("Commands:")
                print("  'clear'  - Clear conversation history")
                print("  'quit'   - Exit the bot")
                print("  'help'   - Show this help message")
                print("=" * 70 + "\n")
                continue
            
            # Get response from consultant
            print("\n🤖 Consultant: ", end="")
            response = consultant.chat(user_input)
            print(response)
            print()
            
        except KeyboardInterrupt:
            print("\n\nBot interrupted. Exiting...\n")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")


if __name__ == "__main__":
    main()
