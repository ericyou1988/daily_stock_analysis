# 🔍 Gemini + Qwen3.5-plus 配置验证指南

> 创建时间：2026-04-16  
> 状态：⚠️ 待配置

---

## 📊 当前配置状态

### ❌ 未找到 .env 配置文件

**检查结果**:
- ❌ `.env` 文件不存在
- ❌ Gemini API Key 未配置
- ❌ Qwen 模型未配置

---

## 🚀 快速配置指南

### 步骤 1: 创建 .env 文件

```bash
cd /home/admin/daily_stock_analysis
cp .env.template .env
```

或直接复制模板：
```bash
cp .env.example .env
```

---

### 步骤 2: 配置 Gemini API Key

**获取 Key**:
1. 访问：https://aistudio.google.com
2. 登录 Google 账号
3. 创建 API Key
4. 复制 Key

**配置**:
```bash
# 编辑 .env 文件
nano .env

# 添加或修改
GEMINI_API_KEY=你的_GEMINI_API_KEY
```

---

### 步骤 3: 配置 Qwen3.5-plus

**获取 Key**:
1. 访问：https://dashscope.aliyuncs.com
2. 登录阿里云账号
3. 开通 DashScope 服务
4. 创建 API Key

**配置（3 种方式任选其一）**:

#### 方式 1: OpenAI 兼容接口（推荐）
```bash
OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
OPENAI_API_KEY=你的_阿里云_API_KEY
OPENAI_MODEL=qwen-plus
```

#### 方式 2: 直接指定模型
```bash
LITELLM_MODEL=openai/qwen-plus
```

#### 方式 3: 渠道模式
```bash
LLM_CHANNELS=qwen
LLM_QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_QWEN_API_KEY=你的_阿里云_API_KEY
LLM_QWEN_MODELS=qwen-plus,qwen-max
```

---

## ✅ 验证配置是否生效

### 方法 1: 运行测试脚本

```bash
python3 test_env.py
```

**预期输出**:
```
✅ 环境配置检查通过
✅ Gemini API Key 已配置
✅ Qwen 模型已配置
✅ 所有依赖已安装
```

---

### 方法 2: 运行主程序

```bash
python3 main.py
```

**观察日志**:

#### Gemini 生效标志 ✅
```
[INFO] 使用 AI 模型：gemini/gemini-2.5-flash
[INFO] Gemini API 调用成功
[INFO] 开始分析 600519...
```

#### Qwen 生效标志 ✅
```
[INFO] 使用 AI 模型：openai/qwen-plus
[INFO] Qwen API 调用成功
[INFO] 生成分析报告...
```

#### 配置失败标志 ❌
```
[ERROR] 未找到 API Key
[ERROR] Invalid API Key
[ERROR] Connection timeout
```

---

### 方法 3: 查看实际使用的模型

**运行后查看日志**:
```bash
# 查看最近的日志
tail -f logs/daily_analysis.log

# 或查看输出
python3 main.py 2>&1 | grep -i "使用模型\|AI 模型"
```

**预期看到**:
- `gemini/gemini-2.5-flash` - Gemini 生效
- `openai/qwen-plus` - Qwen 生效
- `ollama/qwen3:8b` - Ollama 本地 Qwen 生效

---

## 🔧 常见问题排查

### 问题 1: "未找到 API Key"

**原因**: .env 文件不存在或未配置

**解决**:
```bash
# 创建 .env 文件
cp .env.example .env

# 编辑填入 Key
nano .env
```

---

### 问题 2: "Invalid API Key"

**原因**: Key 无效或过期

**解决**:
1. 检查 Key 是否正确复制（无空格/换行）
2. 确认 Key 未过期
3. 检查配额是否用完
4. 重新获取 Key

---

### 问题 3: 模型优先级冲突

**说明**: 系统默认优先级：
```
Gemini > Anthropic > OpenAI (含 Qwen) > Ollama
```

**解决**: 明确指定主模型
```bash
LITELLM_MODEL=gemini/gemini-2.5-flash
# 或
LITELLM_MODEL=openai/qwen-plus
```

---

### 问题 4: Qwen 连接超时

**原因**: BASE_URL 错误或网络问题

**解决**:
1. 检查 BASE_URL 是否正确
2. 测试网络连接：
   ```bash
   curl -I https://dashscope.aliyuncs.com
   ```
3. 如使用代理，配置：
   ```bash
   HTTP_PROXY=http://proxy:port
   HTTPS_PROXY=http://proxy:port
   ```

---

## 📝 推荐配置方案

### 方案 1: Gemini 主力 + Qwen 备用

```bash
# 主力模型
GEMINI_API_KEY=xxx
LITELLM_MODEL=gemini/gemini-2.5-flash

# 备用模型
OPENAI_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
OPENAI_API_KEY=xxx
OPENAI_MODEL=qwen-plus
```

**优点**:
- ✅ Gemini 免费额度充足
- ✅ Qwen 作为备用，提高稳定性
- ✅ 自动故障转移

---

### 方案 2: 双模型负载均衡

```bash
LLM_CHANNELS=gemini,qwen

# Gemini
LLM_GEMINI_API_KEY=xxx
LLM_GEMINI_MODELS=gemini-2.5-flash

# Qwen
LLM_QWEN_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_QWEN_API_KEY=xxx
LLM_QWEN_MODELS=qwen-plus
```

**优点**:
- ✅ 多模型轮询
- ✅ 降低单点故障风险
- ✅ 提高并发能力

---

## 🎯 确认生效检查清单

### Gemini 检查清单
- [ ] `.env` 文件中配置了 `GEMINI_API_KEY`
- [ ] Key 格式正确（长度>20）
- [ ] 运行日志显示 `gemini/` 前缀
- [ ] 分析结果包含详细技术指标
- [ ] 无 API Key 错误

### Qwen 检查清单
- [ ] 配置了 `OPENAI_BASE_URL` 或 `LITELLM_MODEL`
- [ ] 配置了 `OPENAI_API_KEY`
- [ ] BASE_URL 正确（阿里云地址）
- [ ] 运行日志显示 `qwen` 字样
- [ ] 分析结果逻辑清晰

---

## 📁 相关文件

| 文件 | 用途 |
|------|------|
| `.env.template` | 配置模板（已创建） |
| `.env.example` | 官方配置示例 |
| `check_ai_config.py` | 配置检查脚本 |
| `docs/AI_MODEL_CONFIG.md` | 详细配置文档 |
| `CHECK_AI_CONFIG_GUIDE.md` | 检查指南 |

---

## 🔗 获取 API Key

### Gemini
- **地址**: https://aistudio.google.com
- **要求**: Google 账号
- **配额**: 免费额度充足

### Qwen（阿里云）
- **地址**: https://dashscope.aliyuncs.com
- **要求**: 阿里云账号
- **配额**: 新用户赠送额度

---

## ✅ 下一步

1. **创建 .env 文件**
   ```bash
   cp .env.template .env
   ```

2. **填入 API Key**
   ```bash
   nano .env
   ```

3. **运行测试**
   ```bash
   python3 test_env.py
   ```

4. **验证生效**
   ```bash
   python3 main.py
   ```

---

*创建时间：2026-04-16*  
*状态：待配置*  
*下一步：创建 .env 并填入 API Key*
