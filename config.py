# config.py

# 你的初始持仓与成本价配置，Agent 将基于此进行逻辑推演
PORTFOLIO = {
    "300964": {"name": "本川智能", "cost_price": 45.50, "shares": 2000, "strategy": "逢高减持"},
    "600299": {"name": "安迪苏", "cost_price": 10.20, "shares": 5000, "strategy": "长期持有"}
}

# 大模型 API 配置 (建议使用支持 OpenAI 接口格式的国产大模型，如 DeepSeek, Kimi, 或 Qwen)
# 填入你申请到的 API_KEY 和对应的 BASE_URL
API_KEY = "sk-your-api-key-here" 
BASE_URL = "https://api.your-llm-provider.com/v1"
MODEL_NAME = "your-model-name" # 例如 "deepseek-chat"
