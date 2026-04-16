#!/usr/bin/env python3
"""
DSA 系统 - AI 模型配置检查工具

使用方法：
    python check_ai_config.py
    
功能：
    - 检查 .env 文件是否存在
    - 验证 Gemini API Key 配置
    - 验证 Qwen 模型配置
    - 测试模型连接（可选）
"""

import os
import sys
from pathlib import Path

# 颜色输出
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*60}{Colors.RESET}\n")

def print_success(text):
    print(f"{Colors.GREEN}✅ {text}{Colors.RESET}")

def print_error(text):
    print(f"{Colors.RED}❌ {text}{Colors.RESET}")

def print_warning(text):
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.RESET}")

def print_info(text):
    print(f"{Colors.BLUE}ℹ️  {text}{Colors.RESET}")

def check_env_file():
    """检查 .env 文件是否存在"""
    print_header("1️⃣ 检查 .env 文件")
    
    env_path = Path('.env')
    if not env_path.exists():
        print_error("未找到 .env 文件")
        print_info("请复制 .env.example 并配置：")
        print(f"  {Colors.BOLD}cp .env.example .env{Colors.RESET}")
        print_info("然后编辑 .env 文件填入 API Key\n")
        return False
    
    print_success("找到 .env 文件")
    return True

def check_gemini_config():
    """检查 Gemini 配置"""
    print_header("2️⃣ 检查 Gemini 配置")
    
    # 读取 .env 文件
    gemini_key = None
    gemini_keys = None
    
    with open('.env', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('GEMINI_API_KEY='):
                gemini_key = line.split('=', 1)[1].strip()
            elif line.startswith('GEMINI_API_KEYS='):
                gemini_keys = line.split('=', 1)[1].strip()
    
    if not gemini_key and not gemini_keys:
        print_error("未配置 Gemini API Key")
        print_info("请在 .env 文件中添加：")
        print(f"  {Colors.BOLD}GEMINI_API_KEY=your_gemini_api_key{Colors.RESET}")
        print_info("\n获取地址：https://aistudio.google.com\n")
        return False
    
    if gemini_keys:
        keys = [k.strip() for k in gemini_keys.split(',') if k.strip()]
        print_success(f"已配置 Gemini API Keys（{len(keys)} 个）")
        for i, key in enumerate(keys, 1):
            masked = key[:8] + '...' + key[-4:] if len(key) > 12 else '***'
            print_info(f"  Key{i}: {masked}")
    else:
        masked = gemini_key[:8] + '...' + gemini_key[-4:] if len(gemini_key) > 12 else '***'
        print_success(f"已配置 Gemini API Key: {masked}")
    
    # 检查 Key 格式
    if gemini_key and len(gemini_key) < 10:
        print_warning("API Key 长度过短，可能无效")
    
    print_info("\nGemini 支持模型：")
    print("  - gemini-2.5-flash (推荐)")
    print("  - gemini-2.0-flash")
    print("  - gemini-pro\n")
    
    return True

def check_qwen_config():
    """检查 Qwen 配置"""
    print_header("3️⃣ 检查 Qwen 配置")
    
    # 读取 .env 文件
    litellm_model = None
    openai_base = None
    openai_model = None
    openai_key = None
    qwen_channels = None
    
    with open('.env', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('LITELLM_MODEL='):
                litellm_model = line.split('=', 1)[1].strip()
            elif line.startswith('OPENAI_BASE_URL='):
                openai_base = line.split('=', 1)[1].strip()
            elif line.startswith('OPENAI_MODEL='):
                openai_model = line.split('=', 1)[1].strip()
            elif line.startswith('OPENAI_API_KEY='):
                openai_key = line.split('=', 1)[1].strip()
            elif line.startswith('LLM_CHANNELS='):
                qwen_channels = line.split('=', 1)[1].strip()
    
    # 检查配置方式
    config_found = False
    
    # 方式 1: LITELLM_MODEL 直接配置
    if litellm_model and 'qwen' in litellm_model.lower():
        print_success(f"已配置 LITELLM_MODEL: {litellm_model}")
        config_found = True
    
    # 方式 2: OpenAI 兼容配置
    if openai_base and 'qwen' in openai_base.lower():
        print_success(f"已配置 OpenAI 兼容接口：{openai_base}")
        if openai_model:
            print_info(f"  模型：{openai_model}")
        if openai_key:
            masked = openai_key[:8] + '...' + openai_key[-4:] if len(openai_key) > 12 else '***'
            print_info(f"  API Key: {masked}")
        config_found = True
    
    # 方式 3: 渠道模式配置
    if qwen_channels and 'qwen' in qwen_channels.lower():
        print_success(f"已配置多渠道模式：{qwen_channels}")
        config_found = True
    
    if not config_found:
        print_warning("未检测到 Qwen 相关配置")
        print_info("\nQwen 配置方式：")
        print(f"  {Colors.BOLD}方式 1 - 直接配置:{Colors.RESET}")
        print(f"    LITELLM_MODEL=ollama/qwen3:8b")
        print(f"    OLLAMA_API_BASE=http://localhost:11434")
        print(f"\n  {Colors.BOLD}方式 2 - OpenAI 兼容:{Colors.RESET}")
        print(f"    OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1")
        print(f"    OPENAI_API_KEY=sk-xxx")
        print(f"    OPENAI_MODEL=qwen-plus")
        print(f"\n  {Colors.BOLD}方式 3 - 渠道模式:{Colors.RESET}")
        print(f"    LLM_CHANNELS=qwen")
        print(f"    LLM_QWEN_BASE_URL=...")
        print(f"    LLM_QWEN_API_KEY=...")
        print(f"    LLM_QWEN_MODELS=qwen-plus\n")
        return False
    
    print_info("\nQwen 支持模型：")
    print("  - qwen-plus (推荐)")
    print("  - qwen-max")
    print("  - qwen-turbo")
    print("  - qwen3:8b (Ollama 本地)\n")
    
    return True

def check_other_models():
    """检查其他可能的模型配置"""
    print_header("4️⃣ 检查其他模型配置")
    
    models_found = []
    
    with open('.env', 'r', encoding='utf-8') as f:
        content = f.read()
        
        if 'DEEPSEEK_API_KEY' in content and 'DEEPSEEK_API_KEY=' in content:
            models_found.append("DeepSeek")
        
        if 'ANTHROPIC_API_KEY' in content and 'ANTHROPIC_API_KEY=' in content:
            models_found.append("Claude")
        
        if 'AIHUBMIX_KEY' in content and 'AIHUBMIX_KEY=' in content:
            models_found.append("AIHubmix")
        
        if 'OPENAI_API_KEY' in content and 'OPENAI_API_KEY=' in content:
            models_found.append("GPT")
    
    if models_found:
        print_info("还配置了以下模型：")
        for model in models_found:
            print(f"  - {model}")
    else:
        print_info("未配置其他模型")
    
    print()

def print_summary():
    """打印总结"""
    print_header("📊 配置总结")
    print("请根据上述检查结果：")
    print("  1. 确保 .env 文件存在")
    print("  2. 至少配置一个 AI 模型（Gemini 或 Qwen）")
    print("  3. API Key 格式正确且有效")
    print("  4. 运行测试脚本验证连接\n")
    print(f"{Colors.BOLD}下一步:{Colors.RESET}")
    print(f"  {Colors.GREEN}python test_env.py{Colors.RESET} - 测试环境配置")
    print(f"  {Colors.GREEN}python main.py{Colors.RESET} - 运行分析\n")

def main():
    """主函数"""
    print_header("🤖 DSA 系统 - AI 模型配置检查工具")
    
    # 检查 .env 文件
    if not check_env_file():
        return 1
    
    # 检查 Gemini
    check_gemini_config()
    
    # 检查 Qwen
    check_qwen_config()
    
    # 检查其他模型
    check_other_models()
    
    # 总结
    print_summary()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
