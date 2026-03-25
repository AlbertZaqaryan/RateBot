
# 🚀 RateBot — Telegram Currency Exchange Bot

**RateBot** is a simple and fast Telegram bot that provides real-time currency exchange rates (USD, EUR, etc.) converted to AMD (Armenian Dram).

It is built using Python and interacts with public exchange rate APIs to deliver актуальные курсы валют прямо в Telegram.

---

## ✨ Features

* 💱 Get real-time currency rates
* 🇦🇲 Convert USD / EUR → AMD
* ⚡ Fast response via Telegram Bot API
* 🔄 Uses external exchange rate API
* 🧩 Simple and extensible architecture

---

## 🛠 Tech Stack

* **Python 3**
* **pyTelegramBotAPI (TeleBot)**
* **Requests**
* **dotenv (.env config)**

---

## 📂 Project Structure

```
RateBot/
│
├── main.py           # Bot logic
├── .env              # Environment variables (TOKEN)
├── requirements.txt  # Dependencies
└── README.md
```

---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/AlbertZaqaryan/RateBot.git
cd RateBot
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create `.env` file:

```
TOKEN=your_telegram_bot_token
```

👉 You can get your token from **@BotFather**

---

## ▶️ Run the Bot

```bash
python main.py
```

---

## 💬 Usage

Start the bot in Telegram:

```
/start
```

Example output:

```
💵 USD → AMD: 387.25
💶 EUR → AMD: 420.10
```

---

## 🔗 API Used

* Exchange rates API (e.g. exchangerate-api.com)

---

## 🧠 How It Works

1. Bot receives command from user
2. Sends request to exchange rate API
3. Parses JSON response
4. Converts currency to AMD
5. Sends formatted message back to user

---

## 🚀 Future Improvements

* 📊 Add more currencies (RUB, GBP, etc.)
* 📈 Historical data charts
* 🔔 Daily rate notifications
* 🌍 Multi-language support (EN / RU / AM)
* 📱 Inline buttons UI

---

## 🤝 Contributing

Contributions are welcome!

```bash
fork → create branch → commit → push → pull request
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Albert Zaqaryan**

* GitHub: [https://github.com/AlbertZaqaryan](https://github.com/AlbertZaqaryan)

---

## ⭐ Support

If you like this project:

👉 Star the repository
👉 Share with friends
👉 Improve & contribute

