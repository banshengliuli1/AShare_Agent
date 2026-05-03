# main.py
from config import PORTFOLIO
from crawler import fetch_latest_announcements
from agent_core import AShareAgent

def main():
    print("🚀 A股公告监控与资产策略 Agent 启动...")
    agent = AShareAgent()

    # 遍历用户的股票池
    for code, holding_info in PORTFOLIO.items():
        # 1. 触发抓取
        announcements = fetch_latest_announcements(code)
        
        if not announcements:
            print(f"[{holding_info['name']}] 今日无重大公告。")
            continue
            
        # 2. 遍历公告，送入 Agent 长链推理管道
        for ann in announcements:
            agent.run_pipeline(code, ann, holding_info)

if __name__ == "__main__":
    main()
