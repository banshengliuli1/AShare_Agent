# agent_core.py
from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL_NAME

class AShareAgent:
    def __init__(self):
        self.client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    def _call_llm(self, prompt, system_prompt):
        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3 # 保持金融分析的严谨性
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"❌ LLM 调用失败: {e}"

    def step1_extract_info(self, announcement):
        """长链推理节点 1：信息结构化抽取"""
        system = "你是一个专业的金融数据分析师，请从公告中提取关键结构化信息。"
        prompt = f"""
        请分析以下A股公告，提取以下信息并以简洁的文本返回：
        1. 公告类型（如：减持、增发、业绩预告等）
        2. 核心事件要素（如减持比例、时间窗口、利润增长率等）
        3. 表面情绪倾向（利好/利空/中性）
        
        公告内容：{announcement['title']} - {announcement['content']}
        """
        return self._call_llm(prompt, system)

    def step2_strategy_reasoning(self, extracted_info, holding_info):
        """长链推理节点 2：结合持仓的量化逻辑推演"""
        system = "你是一个资深的A股操盘手与风控经理。"
        prompt = f"""
        基于以下公告提取信息和用户的当前持仓情况，进行深度逻辑推演，并给出行动建议。
        
        【公告提取信息】：
        {extracted_info}
        
        【用户当前持仓】：
        股票：{holding_info['name']}
        持仓成本价：{holding_info['cost_price']}
        持有数量：{holding_info['shares']}
        用户既定策略：{holding_info['strategy']}
        
        请进行以下推理并输出：
        1. 【影响推演】：该公告对短期股价和长期复利目标的具体影响逻辑。
        2. 【持仓博弈】：结合用户的成本价和既定策略，分析目前是应该抢跑、观望还是加仓。
        3. 【最终建议】：给出一个明确的行动指令（如：明早开盘清仓、继续持有、减半仓）。
        """
        return self._call_llm(prompt, system)

    def run_pipeline(self, stock_code, announcement, holding_info):
        """执行完整工作流"""
        print("\n" + "="*50)
        print(f"🤖 Agent 开始处理 [{holding_info['name']}] 的公告：{announcement['title']}")
        print("="*50)
        
        print("\n▶ 节点 1：正在执行结构化信息抽取...")
        extracted_info = self.step1_extract_info(announcement)
        print(extracted_info)
        
        print("\n▶ 节点 2：结合成本价进行长链策略推演...")
        strategy_result = self.step2_strategy_reasoning(extracted_info, holding_info)
        print(strategy_result)
        
        return strategy_result
