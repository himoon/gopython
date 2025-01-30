import matplotlib.pyplot as plt

fig, axes = plt.subplots(figsize=(9, 3), dpi=100, nrows=1, ncols=3)

names = ["apple", "orange", "lemon"]
values = [3, 2, 5]
axes[0].bar(names, values)  # 바 그래프
axes[1].scatter(names, values)  # 산점도 그래프
axes[2].plot(names, values)  # 선 그래프
plt.show()  # 그래프 출력
