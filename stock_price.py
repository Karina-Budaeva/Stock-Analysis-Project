import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf


# Загружаем данные по акциям Apple, Nvidia, Tesla, Intel c Yahoo Finance
data = yf.download("NVDA TSLA INTC MSFT IBM", start="2024-01-29", end="2025-01-29", interval="1mo")

# 1. Создаем датафрейм с ценами на дату закрытия
data_close = data[['Close']].copy()
data_close.rename(columns = {'Close': 'Closing Price'}, inplace=True)
print(data)


# Построим график изменения цен с шагом 1 месяц
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize=(12, 8))
data_close.plot(ax=ax, lw=2)
ax.set_title('Closing Prices of NVDA, TSLA, INTC, MSFT and IBM (January 24 - January 25)')
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Closing Price', fontsize=12)
ax.legend(title="Companies", fontsize=10, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)
ax.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("closing_prices.png")
plt.show()


# 2. Рассчитываем месячные процентные изменения (returns)
data_returns = data['Close'].pct_change() * 100  # pct_change() возвращает изменения в процентах

# Построим график изменений цен
sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))

## Выбираем цвета
plt.plot(data_returns.index, data_returns['NVDA'], label='NVDA', color='tab:blue', lw=2)
plt.plot(data_returns.index, data_returns['TSLA'], label='TSLA', color='tab:orange', lw=2)
plt.plot(data_returns.index, data_returns['INTC'], label='INTC', color='tab:green', lw=2)
plt.plot(data_returns.index, data_returns['MSFT'], label='MSFT', color='tab:red', lw=2)
plt.plot(data_returns.index, data_returns['IBM'], label='IBM', color='tab:purple', lw=2)

plt.title('Monthly Returns of NVDA, TSLA, INTC, MSFT and IBM (January 24 - January 25 )', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Monthly Return (%)', fontsize=12)

# Добавляем аннотации (на самых больших изменениях)
for col in data_returns.columns:
    max_change = data_returns[col].max()
    max_date = data_returns[col].idxmax()
    plt.annotate(f'{max_change:.2f}%', xy=(max_date, max_change), xytext=(max_date, max_change + 3),
                 arrowprops=dict(arrowstyle="->", lw=1), fontsize=10)

plt.legend(title="Companies", fontsize=10, loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_returns.png")
plt.show()

# 3. Рассчитываем корреляцию между ценами закрытия акций
correlation = data_close.corr()
# Убираем "Closing Price"  и достаём тикеры акций
new_labels = [col[1] for col in correlation.columns]

# Построим тепловую карту корреляции
plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation,
    annot=True,
    cmap='Greens',
    fmt='.2f',
    annot_kws={"size": 10},
    xticklabels=new_labels,
    yticklabels=new_labels
)
plt.title('Корреляция цен закрытия (NVDA, TSLA, INTC, MSFT, IBM)', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.savefig("correlation_matrix.png")
plt.show()