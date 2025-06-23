# ADK Multi-Agent 測試

測試 ADK Multi-Agent 

## 一、問題說明

當使用 `adk api_server ./agents` 啟動時，ADK 會把搜尋路徑定在 `./agents` 目錄下。此時若請求中包含 `appName: "agents"`，ADK 會嘗試在 `./agents/agents` 路徑下尋找套件而失敗。

**解決方案：** 從專案根目錄啟動，確保 Python path 包含正確的 agents 目錄，使 ADK Loader 能夠找到 root_agent。

## 二、前置準備

### 1. 工作目錄結構

```
your-project/
├── agents/
│   ├── __init__.py
│   └── agent.py      ← 內含 root_agent 定義
├── pyproject.toml
└── … 其他檔案 …
```

### 2. 環境準備

* 確保在專案根目錄下已建立並啟用 ADK 專用虛擬環境（應只顯示 (test-agents)，無 (base)）
* 確認 adk 指令可用
* 確認 root_agent 已在 agents/agent.py 中正確匯出

## 三、本地測試 (Local Testing)

### 1. 啟動 API Server

```bash
# 確認只剩 (test-agents) 提示符
conda deactivate   

# 啟動 API Server，綁定本機所有介面
adk api_server . --host 0.0.0.0 --port 8000
```

### 2. 建立 Session

```bash
curl -X POST http://127.0.0.1:8000/apps/agents/users/u_123/sessions/s_12 \
  -H "Content-Type: application/json" \
  -d '{"state": {"key1": "value1", "key2": 42}}'
```

### 3. 送出訊息

```bash
curl -X POST http://127.0.0.1:8000/run \
  -H "Content-Type: application/json" \
  -d '{
    "appName": "agents",
    "userId": "u_123",
    "sessionId": "s_12",
    "newMessage": {
      "role": "user",
      "parts": [{ "text": "給我 tesla 股價" }]
    }
  }'
```

## 四、遠端測試 (Remote Testing via ngrok)

### 4.1 設定 ngrok

```bash
# 登入並設定 authtoken
ngrok config add-authtoken <YOUR_AUTH_TOKEN>

# （可選）指定區域為亞太
# ngrok http --region ap 8000
ngrok http 8000
```

預設會產生類似：
```
Forwarding  https://a25b-123-51-152-88.ngrok-free.app -> http://localhost:8000
```

### 4.2 啟動 API Server

```bash
# 確保只剩 (test-agents)
conda deactivate

# 綁定所有介面
adk api_server . --host 0.0.0.0 --port 8000
```

### 4.3 從外部呼叫

#### 1. 建立 Session

```bash
curl -X POST https://a25b-123-51-152-88.ngrok-free.app/apps/agents/users/u_123/sessions/s_123 \
  -H "Content-Type: application/json" \
  -d '{"state": {"key1": "value1", "key2": 42}}'
```

#### 2. 送出訊息

```bash
curl -X POST https://a25b-123-51-152-88.ngrok-free.app/run \
  -H "Content-Type: application/json" \
  -d '{
    "appName": "agents",
    "userId": "u_123",
    "sessionId": "s_123",
    "newMessage": {
      "role": "user",
      "parts": [{ "text": "現在台北幾點" }]
    }
  }'
```
