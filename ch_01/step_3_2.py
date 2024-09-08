from pathlib import Path

import matplotlib.pyplot as plt

import step_1  # 이전에 작성한 모듈을 불러옵니다.
import step_3_1

plot_data = step_3_1.load_plot_data()

fig, ax = plt.subplots()
ax.barh(plot_data["stem"], plot_data["size"])

fig.savefig(step_1.OUT_DIR / f"{Path(__file__).stem}.png")
