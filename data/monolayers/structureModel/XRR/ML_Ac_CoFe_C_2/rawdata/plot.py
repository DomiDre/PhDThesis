import jcnsBrukerD8
import matplotlib.pyplot as plt
app = jcnsBrukerD8.App()
app.load_dat('../rawdata/DD175_28.txt', 0)
app.footprint_correct_and_rescale(10, 0.2)
fig, ax = plt.subplots()
ax.errorbar(app.q, app.I, app.sI)
ax.set_yscale('log')
plt.show()