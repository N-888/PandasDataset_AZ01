import pandas as pd

# Загрузка данных
df = pd.read_csv('dz AZ01.csv')

# Заполнение пропусков в зарплате нулями
df['Salary'] = df['Salary'].fillna(0)

# Фильтруем только Москву и вычисляем среднюю зарплату
moscow_salary = df[df['City'] == 'Москва']['Salary'].mean()

# Создаем DataFrame с результатом
result_df = pd.DataFrame({
    'City': ['Москва'],
    'Average_Salary': [moscow_salary]
})

# Сохраняем результат в файл
result_df.to_csv('moscow_average_salary.csv', index=False)

# Выводим результаты в консоли
print(f"Средняя зарплата в Москве: {moscow_salary:.2f} руб.")
print("Результат сохранен в файл 'moscow_average_salary.csv'")
