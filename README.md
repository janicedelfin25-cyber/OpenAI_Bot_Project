# 🎯 Digital Marketing Consultancy Bot

An AI-powered digital marketing consultancy chatbot built with OpenAI's GPT-3.5-turbo model. This project includes two versions: a basic bot and an advanced bot with specialized marketing functions.

## Features

### Basic Bot (`marketing_bot.py`)
- Natural language conversation with a digital marketing expert
- Real-time consulting on marketing strategies
- Conversation history tracking
- Easy-to-use command interface

### Advanced Bot (`advanced_marketing_bot.py`)
- All basic features plus:
- **Strategy Analysis**: Analyze and improve marketing strategies
- **Social Media Planning**: Generate comprehensive social media plans
- **Conversion Funnel Optimization**: Optimize your sales funnel
- **SEO Audit**: Get detailed SEO recommendations
- **Budget Allocation**: Create intelligent marketing budget plans
- **Session Management**: Create and save consultation sessions
- **Session Export**: Save sessions to JSON for later review

## Installation

1. **Prerequisites**
   - Python 3.8 or higher
   - Virtual environment (already created)

2. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Setup API Key**
   - Your `.env` file is already configured with your OpenAI API key
   - The bot will automatically load it

## Usage

### Basic Bot
```powershell
python marketing_bot.py
```

**Commands:**
- `clear` - Clear conversation history
- `help` - Show help message
- `quit` - Exit the bot

**Example:**
```
You: What's the best way to increase my e-commerce conversion rate?

🤖 Consultant: Based on my experience, here are the top strategies...
```

### Advanced Bot
```powershell
python advanced_marketing_bot.py
```

**Commands:**
- `strategy` - Analyze a marketing strategy
- `social` - Generate a social media marketing plan
- `funnel` - Get conversion funnel optimization tips
- `seo` - Receive SEO audit recommendations
- `budget` - Create a budget allocation plan
- `session` - Create a new consultation session
- `list` - List all created sessions
- `save` - Save the current session
- `clear` - Clear conversation history
- `quit` - Exit the bot

**Example - Strategy Analysis:**
```
You: strategy
Describe your marketing strategy:
Currently we're doing organic social media with 2 posts per week, no PPC, and minimal content marketing.

🤖 Consultant: I see several opportunities here...
```

**Example - Budget Planning:**
```
You: budget
Total budget: $50000
Business goals: Increase sales by 50% in 6 months
Industry: E-commerce

🤖 Consultant: Based on your goals, here's the recommended allocation...
```

## Project Structure

```
New_AI_Folder/
├── marketing_bot.py              # Basic marketing consultancy bot
├── advanced_marketing_bot.py      # Advanced bot with specialized functions
├── .env                           # API configuration (contains your API key)
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## How It Works

1. **OpenAI Integration**: Uses GPT-3.5-turbo via OpenAI's API
2. **System Prompt**: The bot operates under a detailed system prompt that establishes it as a digital marketing expert
3. **Conversation History**: Maintains context throughout your consultation
4. **Session Management** (Advanced): Save consultations for future reference

## Example Use Cases

1. **Startup Marketing Plan**: Ask for help creating an initial marketing strategy
2. **Social Media Optimization**: Get recommendations for your social channels
3. **Budget Planning**: Allocate marketing budget effectively
4. **SEO Strategy**: Receive technical and content recommendations
5. **Funnel Analysis**: Identify and fix conversion bottlenecks
6. **Competitive Analysis**: Get insights on competitor strategies
7. **Campaign Planning**: Design specific marketing campaigns

## API Costs

- The OpenAI API charges based on token usage
- GPT-3.5-turbo is the most cost-effective option
- Average response: ~200-400 tokens
- Monitor your API usage in the OpenAI dashboard

## Tips for Better Consultation

1. **Be Specific**: Provide details about your business, industry, and goals
2. **Ask Follow-ups**: Ask clarifying questions to get personalized advice
3. **Save Sessions**: Use the advanced bot to save important consultations
4. **Iterate**: Come back with revised strategies for feedback
5. **Use Specialized Functions**: Leverage specific functions for detailed analysis

## Troubleshooting

**API Key Error:**
- Verify the API key in `.env` is correct
- Ensure your OpenAI account has active credits

**Connection Issues:**
- Check your internet connection
- Verify OpenAI services are online

**Rate Limiting:**
- Wait a few minutes before making new requests
- Consider spacing out requests if using the bot frequently

## Future Enhancements

- Web scraping for competitor analysis
- Data visualization for marketing metrics
- Integration with Google Analytics
- Multi-language support
- Voice input/output capabilities
- Marketing template library

## Support

For issues with the OpenAI API:
- Visit: https://platform.openai.com/help
- Check API documentation: https://platform.openai.com/docs

## License

This project is provided as-is for educational and business purposes.

---

**Happy consulting!** 🚀
