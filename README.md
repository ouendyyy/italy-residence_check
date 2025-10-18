# Italy Residence Permit Checker / 意大利居留许可查询工具

自动查询意大利居留软件 - Automatic Italy residence permit status checker

## 简介 / Introduction

这是一个用于查询意大利居留许可状态的自动化工具。
This is an automated tool for checking the status of Italian residence permits.

## 功能特性 / Features

- ✅ 自动查询居留许可状态 / Automatic residence permit status checking
- ✅ 支持单次查询和持续监控 / Support for single check and continuous monitoring
- ✅ 详细的日志记录 / Detailed logging
- ✅ 可配置的查询间隔 / Configurable check intervals
- ✅ 简单的配置文件 / Simple configuration file

## 安装 / Installation

### 前提条件 / Prerequisites

- Python 3.7 或更高版本 / Python 3.7 or higher
- pip (Python 包管理器) / pip (Python package manager)

### 安装步骤 / Installation Steps

1. 克隆仓库 / Clone the repository:
```bash
git clone https://github.com/ouendyyy/italy-residence_check.git
cd italy-residence_check
```

2. 安装依赖 / Install dependencies:
```bash
pip install -r requirements.txt
```

3. 配置文件 / Configuration:
```bash
cp config.example.json config.json
```

编辑 `config.json` 填入您的信息：
Edit `config.json` with your information:
```json
{
  "username": "your_receipt_number",
  "password": "your_tracking_code",
  "check_interval": 300,
  "notification": {
    "enabled": false,
    "email": "your_email@example.com"
  }
}
```

## 使用方法 / Usage

### 单次查询 / Single Check

运行单次状态查询：
Run a single status check:
```bash
python residence_checker.py
```

### 持续监控 / Continuous Monitoring

启动持续监控模式（按配置的间隔自动查询）：
Start continuous monitoring mode (automatic checks at configured interval):
```bash
python residence_checker.py --continuous
```

按 `Ctrl+C` 停止监控。
Press `Ctrl+C` to stop monitoring.

### 查看帮助 / Help

```bash
python residence_checker.py --help
```

## 配置说明 / Configuration

| 参数 / Parameter | 说明 / Description |
|-----------------|-------------------|
| `username` | 用户名或回执编号 / Username or receipt number |
| `password` | 密码或追踪代码 / Password or tracking code |
| `check_interval` | 查询间隔（秒）/ Check interval in seconds |
| `notification.enabled` | 是否启用通知 / Enable notifications |
| `notification.email` | 通知邮箱 / Notification email |

## 日志 / Logs

程序运行时会生成日志文件 `residence_check.log`，记录所有操作和状态变化。
The program generates a log file `residence_check.log` that records all operations and status changes.

## 注意事项 / Notes

⚠️ **重要提示 / Important Notes:**

1. 请勿频繁查询，建议间隔至少 5 分钟（300 秒）
   Do not query too frequently, recommend at least 5 minutes (300 seconds) interval

2. 妥善保管您的配置文件，不要将其上传到公开仓库
   Keep your configuration file secure, do not upload it to public repositories

3. 本工具仅用于个人查询，请遵守相关网站的使用条款
   This tool is for personal use only, please comply with the website's terms of service

## 故障排除 / Troubleshooting

### 配置文件未找到 / Configuration file not found
确保已从 `config.example.json` 复制并创建了 `config.json` 文件。
Make sure you have copied `config.example.json` and created `config.json`.

### 依赖安装失败 / Dependency installation failed
尝试升级 pip 后重新安装：
Try upgrading pip and reinstalling:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 许可证 / License

Apache License 2.0 - 详见 [LICENSE](LICENSE) 文件。
Apache License 2.0 - See [LICENSE](LICENSE) file for details.

## 免责声明 / Disclaimer

本工具仅供学习和个人使用。使用本工具产生的任何后果由使用者自行承担。
This tool is for educational and personal use only. Users are responsible for any consequences of using this tool.

## 贡献 / Contributing

欢迎提交问题和拉取请求！
Issues and pull requests are welcome!
