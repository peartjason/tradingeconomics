# TradingEconomics Dashboard 🌐📊

A simple Flask web app that displays economic indicators by country using the [TradingEconomics API](https://developer.tradingeconomics.com/).

## Features
- Search or select countries to view economic data
- Fetch real-time data using the TradingEconomics API
- Responsive UI using Tailwind CSS
- Deployable to Render in one click

## Setup

1. Clone this repo  
   git clone https://github.com/peartjason/tradingeconomics.git  
   cd tradingeconomics

2. Create virtual environment (Windows):  
   python -m venv venv  
   .\venv\Scripts\activate  

3. Install dependencies:  
   pip install -r requirements.txt  

4. Add your API key to .env  
   TRADINGECONOMICS_API_KEY=your_key_here  

5. Run the app:  
   flask run

## Deployment

Deploy on [Render](https://render.com/) or any Python-compatible host.

## License

MIT
