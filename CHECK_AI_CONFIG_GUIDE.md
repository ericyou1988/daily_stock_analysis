# 🔍 DSA 系统 - AI 模型配置检查指南

> 检查 Gemini 和 Qwen3.5-plus 是否生效

---

## ✅ 检查步骤

### 步骤 1: 检查 .env 文件是否存在

```bash
cd /home/admin/daily_stock_analysis
ls -la .env*
```

**预期结果**:
- ✅ `.env` 文件存在
- ❌ 只有 `.env.example`（需要创建）

**如果没有 .env 文件**:
```bash
cp .env.example .env
```

---

### 步骤 2: 检查 Gemini 配置

```bash
grep "GEMINI_API_KEY" .env
```

**预期结果**:
```bash
GEMINI_API_KEY=AIzaSy...  # 实际的 Key
```

**配置位置**:
- 单 Key: `GEMINI_API_KEY=xxx`
- 多 Key: `GEMINI_API_KEYS=key1,key2,key3`

**获取 Key**: https://aistudio.google.com

---

### 步骤 3: 检查 Qwen 配置

Qwen 有 3 种配置方式，检查你的配置属于哪种：

#### 方式 1: Ollama 本地模型
```bash
grep -E "LITELLM_MODEL|OLLAMA" .env
```

**预期配置**:
```bash
LITELLM_MODEL=ollama/qwen3:8b
OLLAMA_API_BASE=http://localhost:11434
```

#### 方式 2: OpenAI 兼容接口（阿里云）
```bash
grep -E "OPENAI_BASE_URL|OPENAI_MODEL|OPENAI_API_KEY" .env
```

**预期配置**:
```bash
OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
OPENAI_API_KEY=sk-xxx
OPENAI_MODEL=qwen-plus
```

#### 方式 3: 渠道模式
```bash
grep "LLM_CHANNELS" .env
```

**预期配置**:
```bash
LLM_CHANNELS=qwen
LLM_QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_QWEN_API_KEY=sk-xxx
LLM_QWEN_MODELS=qwen-plus
```

---

### 步骤 4: 运行测试脚本

```bash
# 测试环境配置
python3 test_env.py

# 或运行主程序测试
python3 main.py
```

**观察日志**:
- ✅ 看到 "AI 模型初始化成功"
- ✅ 看到使用的模型名称
- ❌ 看到 API Key 错误
- ❌ 看到连接超时

---

## 🎯 验证是否生效

### Gemini 验证

**查看日志中的模型标识**:
```
使用模型：gemini/gemini-2.5-flash
✅ Gemini API 调用成功
```

**成功标志**:
- 日志中出现 `gemini/` 前缀
- 无 API Key 错误
- 返回正常的分析结果

### Qwen 验证

**查看日志中的模型标识**:
```
使用模型：openai/qwen-plus
或
使用模型：ollama/qwen3:8b
✅ Qwen API 调用成功
```

**成功标志**:
- 日志中出现 `qwen` 字样
- 无连接错误
- 返回中文分析结果

---

## 🔧 常见问题排查

### 问题 1: 未配置 .env 文件

**症状**: 程序报错 "未找到 API Key"

**解决**:
```bash
cp .env.example .env
# 编辑 .env 填入 API Key
```

---

### 问题 2: Gemini Key 无效

**症状**: "Invalid API Key" 或 "403 Forbidden"

**解决**:
1. 检查 Key 是否正确复制（无空格）
2. 确认 Key 未过期
3. 检查配额是否用完
4. 重新获取 Key: https://aistudio.google.com

---

### 问题 3: Qwen 连接失败

**症状**: "Connection timeout" 或 "404 Not Found"

**解决**:
1. 检查 BASE_URL 是否正确
2. 确认 API Key 有效
3. 检查网络连接
4. 如使用 Ollama，确认服务已启动：
   ```bash
   ollama list
   ollama run qwen3:8b
   ```

---

### 问题 4: 模型优先级冲突

**症状**: 使用了意外的模型

**说明**: 系统默认优先级：
```
Gemini > Anthropic > OpenAI > Ollama
```

**解决**: 在 .env 中明确指定：
```bash
LITELLM_MODEL=openai/qwen-plus
```

---

## 📝 推荐配置示例

### 配置 1: Gemini 主力 + Qwen 备用

```bash
# Gemini（主力）
GEMINI_API_KEY=AIzaSy...

# Qwen（备用，通过 OpenAI 兼容）
OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
OPENAI_API_KEY=sk-xxx
OPENAI_MODEL=qwen-plus

# 明确指定主模型
LITELLM_MODEL=gemini/gemini-2.5-flash
```

---

### 配置 2: 多渠道负载均衡

```bash
# 多渠道配置
LLM_CHANNELS=gemini,qwen

# Gemini 渠道
LLM_GEMINI_API_KEYS=key1,key2
LLM_GEMINI_MODELS=gemini-2.5-flash

# Qwen 渠道
LLM_QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_QWEN_API_KEY=sk-xxx
LLM_QWEN_MODELS=qwen-plus,qwen-max
```

---

## ✅ 确认生效的标志

### Gemini 生效标志
- ✅ 日志显示 `gemini/gemini-2.5-flash`
- ✅ 分析结果包含详细的技术指标
- ✅ 支持图像识别（如配置 Vision）
- ✅ 中文理解准确

### Qwen 生效标志
- ✅ 日志显示 `openai/qwen-plus` 或 `ollama/qwen3:8b`
- ✅ 分析结果逻辑清晰
- ✅ 中文表达自然
- ✅ 响应速度快

---

## 🔗 相关资源

- **检查脚本**: `check_ai_config.py`
- **配置示例**: `.env.example`
- **详细文档**: `docs/AI_MODEL_CONFIG.md`
- **Gemini 官网**: https://aistudio.google.com
- **Qwen 官网**: https://dashscope.aliyuncs.com

---

*更新时间：2026-04-16*
