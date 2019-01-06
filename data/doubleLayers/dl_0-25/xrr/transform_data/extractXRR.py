import jcnsBrukerD8

app = jcnsBrukerD8.App()
app.load_dat('../txtfile/DD205_10.txt', 0)
app.footprint_correct_and_rescale(10, 0.2)
app.save('DD205_10.xye')