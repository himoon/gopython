import matplotlib.pyplot as plt

x_value = ["apple", "orange", "lemon"]  # 가로축 데이터
y_value = [3, 2, 5]  # 세로축 데이터
y_max = max(y_value)  # 5
y_min = min(y_value)  # 2

fig, axes = plt.subplots(figsize=(9, 3), dpi=100, ncols=2)  # 두 개의 Axes 객체 생성
axes[0].plot(x_value, y_value)  # 선 그래프
axes[0].fill_between(x_value, y_max, y_value, alpha=0.2)  # 위로 채우기
axes[1].plot(x_value, y_value)  # 선 그래프
axes[1].fill_between(x_value, y_value, y_min, alpha=0.2)  # 아래로 채우기
plt.show()  # 이미지 출력
