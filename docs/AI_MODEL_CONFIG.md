# DSA 系统 - AI 模型配置详解

> 项目：daily_stock_analysis  
> 更新时间：2026-04-16  
> AI 框架：LiteLLM 统一调用

---

## 🤖 支持的 AI 模型

### 1. Gemini 系列（Google）⭐ 推荐

**配置方式**:
```bash
# 简单配置（单 Key）
GEMINI_API_KEY=your_gemini_key

# 多 Key 负载均衡
GEMINI_API_KEYS=key1,key2,key3
```

**支持模型**:
- `gemini-2.5-flash` - 主力模型，性价比高
- `gemini-2.0-flash` - 快速响应
- `gemini-pro` - 经典版本

**特点**:
- ✅ 免费额度充足
- ✅ 支持 Vision 图像识别
- ✅ 中文理解优秀
- ✅ 金融分析能力强

**获取地址**: https://aistudio.google.com

---

### 2. DeepSeek 系列（深度求索）⭐ 推荐

**配置方式**:
```bash
# 简单配置
DEEPSEEK_API_KEY=sk-deepseek-xxx

# 渠道模式
LLM_CHANNELS=deepseek
LLM_DEEPSEEK_API_KEY=sk-deepseek-xxx
LLM_DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
LLM_DEEPSEEK_MODELS=deepseek-chat,deepseek-reasoner
```

**支持模型**:
- `deepseek-chat` - 对话模型，支持思考模式
- `deepseek-reasoner` - 推理模型（自动思考）
- `deepseek-r1` - 最新推理模型
- `deepseek-coder` - 代码专用

**思考模式**:
```python
# 自动思考模型（无需配置）
deepseek-reasoner, deepseek-r1, qwq

# 需要启用思考模式
deepseek-chat → extra_body: {"thinking": {"type": "enabled"}}
```

**特点**:
- ✅ 性价比极高
- ✅ 推理能力强
- ✅ 支持中文思考链
- ✅ 金融逻辑清晰

**获取地址**: https://platform.deepseek.com

---

### 3. AIHubmix 聚合平台 ⭐ 推荐

**配置方式**:
```bash
# 一个 Key 使用所有模型
AIHUBMIX_KEY=your_aihubmix_key

# 无需配置 BASE_URL，系统自动适配
```

**支持模型**:
- GPT-4o / GPT-4o-mini
- Claude-3.5-Sonnet / Claude-3-Opus
- Gemini 全系列
- GLM-4 / GLM-3
- Qwen（通义千问）
- DeepSeek

**特点**:
- ✅ 一个 Key 通用所有模型
- ✅ 无需科学上网
- ✅ 高稳定性无限并发
- ✅ 含免费模型（glm-5, gpt-4o-free）
- ✅ 项目享 10% 充值优惠

**获取地址**: https://aihubmix.com/?aff=CfMq

---

### 4. Claude 系列（Anthropic）

**配置方式**:
```bash
# 简单配置
ANTHROPIC_API_KEY=sk-ant-xxx
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022

# 渠道模式
LLM_CHANNELS=anthropic
LLM_ANTHROPIC_API_KEY=sk-ant-xxx
LLM_ANTHROPIC_MODELS=claude-3-5-sonnet-20241022
```

**支持模型**:
- `claude-3-5-sonnet-20241022` - 主力模型
- `claude-3-opus-20240229` - 最强模型
- `claude-3-haiku-20240307` - 快速模型

**特点**:
- ✅ 逻辑推理最强
- ✅ 长文本理解优秀
- ✅ 代码能力强
- ❌ 需要科学上网

**获取地址**: https://console.anthropic.com

---

### 5. GPT 系列（OpenAI 兼容）

**配置方式**:
```bash
# OpenAI 官方
OPENAI_API_KEY=sk-xxx
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o-mini

# 第三方兼容（DeepSeek/通义千问等）
OPENAI_API_KEY=sk-xxx
OPENAI_BASE_URL=https://api.deepseek.com/v1
OPENAI_MODEL=deepseek-chat
```

**支持模型**:
- `gpt-4o` - 最强 GPT
- `gpt-4o-mini` - 性价比
- `gpt-4-turbo` - 快速版本
- `gpt-3.5-turbo` - 经济版本

**特点**:
- ✅ 生态完善
- ✅ 工具调用成熟
- ✅ 多语言支持
- ❌ 需要科学上网（官方）

---

### 6. Ollama 本地模型

**配置方式**:
```bash
# 简单配置
OLLAMA_API_BASE=http://localhost:11434
LITELLM_MODEL=ollama/qwen3:8b

# 渠道模式
LLM_CHANNELS=ollama
LLM_OLLAMA_BASE_URL=http://localhost:11434
LLM_OLLAMA_MODELS=qwen3:8b,llama3.2,mistral:7b
```

**支持模型**:
- `qwen3:8b` - 通义千问
- `llama3.2` - Meta Llama
- `mistral:7b` - Mistral AI
- `codellama` - 代码专用
- 任何 Ollama 支持的模型

**特点**:
- ✅ 完全免费
- ✅ 本地部署，隐私安全
- ✅ 无需 API Key
- ❌ 需要本地 GPU 资源

**获取地址**: https://ollama.ai

---

## 🔧 配置模式

### 模式 1: 简单配置（推荐新手）

```bash
# .env 文件
# 只需填一个 Key，系统自动识别

GEMINI_API_KEY=xxx          # 使用 Gemini
# 或
DEEPSEEK_API_KEY=xxx        # 使用 DeepSeek
# 或
AIHUBMIX_KEY=xxx            # 使用 AIHubmix 聚合平台
```

**优先级**: Gemini > Anthropic > OpenAI > Ollama

---

### 模式 2: 多渠道配置（进阶）

```bash
# .env 文件
# 配置多个渠道，自动 fallback

LLM_CHANNELS=deepseek,gemini,ollama

# DeepSeek 渠道
LLM_DEEPSEEK_API_KEY=sk-deepseek-xxx
LLM_DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
LLM_DEEPSEEK_MODELS=deepseek-chat,deepseek-reasoner

# Gemini 渠道
LLM_GEMINI_API_KEYS=key1,key2,key3
LLM_GEMINI_MODELS=gemini-2.5-flash

# Ollama 渠道
LLM_OLLAMA_BASE_URL=http://localhost:11434
LLM_OLLAMA_MODELS=qwen3:8b
```

---

### 模式 3: YAML 配置（专业）

```bash
# .env 文件
LITELLM_CONFIG=./litellm_config.yaml
```

```yaml
# litellm_config.yaml
model_list:
  # Siliconflow（OpenAI 兼容）
  - model_name: openai/Qwen/Qwen3.5-397B-A17B
    litellm_params:
      model: openai/Qwen/Qwen3.5-397B-A17B
      api_key: "os.environ/LITELLM_API_KEY"
      api_base: https://api.siliconflow.cn/v1
      extra_body:
        chat_template_kwargs:
          enable_thinking: true

  # AIHubmix
  - model_name: openai/gpt-4o-mini
    litellm_params:
      model: openai/gpt-4o-mini
      api_key: "os.environ/AIHUBMIX_KEY"
      api_base: https://aihubmix.com/v1

  # DeepSeek
  - model_name: deepseek/deepseek-chat
    litellm_params:
      model: deepseek/deepseek-chat
      api_key: "os.environ/DEEPSEEK_API_KEY"

  # Gemini（多 Key 负载均衡）
  - model_name: gemini/gemini-2.5-flash
    litellm_params:
      model: gemini/gemini-2.5-flash
      api_key: "os.environ/GEMINI_API_KEY_1"

  - model_name: gemini/gemini-2.5-flash
    litellm_params:
      model: gemini/gemini-2.5-flash
      api_key: "os.environ/GEMINI_API_KEY_2"

router_settings:
  routing_strategy: simple-shuffle  # simple-shuffle / least-busy / latency-based
  num_retries: 2                    # 失败重试次数
  timeout: 30                       # 超时（秒）
```

---

## 🎯 Agent 策略对话配置

### 启用 Agent 模式

```bash
# .env 文件
AGENT_MODE=true
AGENT_LITELLM_MODEL=deepseek-chat
AGENT_MAX_STEPS=10
AGENT_SKILLS=all
```

### 内置策略技能

| 技能 ID | 说明 |
|--------|------|
| `bull_trend` | 多头趋势（MA5>MA10>MA20 + 低乖离） |
| `ma_golden_cross` | 均线金叉（MA5 上穿 MA10/MA20） |
| `volume_breakout` | 放量突破（价格突破 + 成交量放大） |
| `shrink_pullback` | 缩量回踩（回踩均线 + 量能萎缩） |
| `bottom_volume` | 底部放量（地量见地价） |
| `dragon_head` | 龙头策略（强势龙头） |
| `one_yang_three_yin` | 一阳夹三阴（洗盘反包） |
| `box_oscillation` | 箱体震荡（高抛低吸） |
| `chan_theory` | 缠论（笔/线段/中枢） |
| `wave_theory` | 波浪理论（艾略特波浪） |

---

## 📊 模型对比

| 模型 | 优点 | 缺点 | 推荐场景 |
|------|------|------|----------|
| **Gemini** | 免费额度多，Vision 强 | 需要科学上网 | 日常分析，图像识别 |
| **DeepSeek** | 性价比高，推理强 | 品牌知名度低 | 金融分析，逻辑推理 |
| **AIHubmix** | 一个 Key 通用，稳定 | 需要充值 | 多模型切换，生产环境 |
| **Claude** | 逻辑最强，长文本 | 贵，需科学上网 | 复杂分析，报告生成 |
| **GPT** | 生态好，工具强 | 贵，需科学上网 | 工具调用，多语言 |
| **Ollama** | 免费，隐私 | 需要 GPU | 本地部署，测试 |

---

## 🔑 密钥管理

### 环境变量引用

```yaml
# YAML 配置中
api_key: "os.environ/GEMINI_API_KEY"  # 从环境变量读取
api_key: "sk-xxxxxxxx"                # 直接写入（不推荐）
```

### 多 Key 负载均衡

```bash
# 方式 1: 逗号分隔
GEMINI_API_KEYS=key1,key2,key3

# 方式 2: 多个变量
GEMINI_API_KEY_1=key1
GEMINI_API_KEY_2=key2
GEMINI_API_KEY_3=key3
```

---

## 🚀 快速开始

### 5 分钟配置指南

#### 步骤 1: 选择模型
- 新手：Gemini（免费）
- 性价比：DeepSeek
- 多模型：AIHubmix

#### 步骤 2: 获取 API Key
访问对应平台注册获取

#### 步骤 3: 配置 .env
```bash
cp .env.example .env
# 编辑 .env 填入 API Key
```

#### 步骤 4: 测试运行
```bash
python test_env.py
python main.py
```

#### 步骤 5: 设置定时任务
GitHub Actions 自动运行

---

## 📝 配置检查清单

- [ ] 至少配置一个 AI 模型
- [ ] API Key 格式正确
- [ ] BASE_URL 正确（如使用第三方）
- [ ] 模型名称拼写正确
- [ ] 多 Key 用逗号分隔
- [ ] 运行 `test_env.py` 测试
- [ ] 检查日志无报错

---

## 🔗 相关资源

- **完整指南**: docs/LLM_CONFIG_GUIDE.md
- **LiteLLM 文档**: https://docs.litellm.ai
- **配置示例**: .env.example
- **YAML 模板**: litellm_config.example.yaml
- **测试脚本**: test_env.py

---

*更新时间：2026-04-16*  
*项目版本：v2.0.0*  
*AI 框架：LiteLLM*
