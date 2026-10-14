import matplotlib.pyplot as plt
from matplotlib.widgets import Button

data = [38, 27, 43, 3, 9, 82, 10]

# Record every step as (array snapshot, highlighted range, message)
steps = []
def merge_sort(a, lo, hi):
    if hi - lo < 1:
        return
    mid = (lo + hi) // 2
    steps.append((a[:], (lo, hi), f"Split [{lo}..{hi}] at {mid}"))
    merge_sort(a, lo, mid)
    merge_sort(a, mid + 1, hi)
    L, R = a[lo:mid + 1], a[mid + 1:hi + 1]
    i = j = 0
    k = lo
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            a[k] = L[i]; i += 1
        else:
            a[k] = R[j]; j += 1
        k += 1
    while i < len(L):
        a[k] = L[i]; i += 1; k += 1
    while j < len(R):
        a[k] = R[j]; j += 1; k += 1
    steps.append((a[:], (lo, hi), f"Merged [{lo}..{hi}]"))

work = data[:]
steps.append((work[:], None, "Start"))
merge_sort(work, 0, len(work) - 1)
steps.append((work[:], None, "Sorted!"))

fig, ax = plt.subplots(figsize=(8, 4))
plt.subplots_adjust(bottom=0.2)
idx = [0]

def draw():
    arr, rng, msg = steps[idx[0]]
    ax.clear()
    colors = ["tab:orange" if rng and rng[0] <= i <= rng[1] else "tab:blue"
              for i in range(len(arr))]
    ax.bar(range(len(arr)), arr, color=colors)
    for i, v in enumerate(arr):
        ax.text(i, v + 1, str(v), ha="center")
    ax.set_title(f"Step {idx[0]+1}/{len(steps)}: {msg}")
    fig.canvas.draw_idle()

def nxt(_):
    if idx[0] < len(steps) - 1:
        idx[0] += 1; draw()

def prev(_):
    if idx[0] > 0:
        idx[0] -= 1; draw()

b1 = Button(plt.axes([0.3, 0.05, 0.15, 0.08]), "Back");  b1.on_clicked(prev)
b2 = Button(plt.axes([0.55, 0.05, 0.15, 0.08]), "Next"); b2.on_clicked(nxt)
draw()
plt.show()
