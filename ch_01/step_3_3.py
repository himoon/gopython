from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from step_2_1 import OUT_DIR  # 이전에 작성한 모듈을 불러옵니다.
from step_3_1 import load_plot_data

plot_data = load_plot_data()
log_size = np.log(plot_data["size"])

fig, ax = plt.subplots(figsize=(16, 9), dpi=100)
ax.barh(plot_data["stem"], log_size)
ax.grid(True, axis="x")  # 축 그리드
ax.tick_params(labelbottom=False, length=0, labelsize=30)  # 축 눈금

fig.set_layout_engine("tight")  # 차트 여백
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png")
