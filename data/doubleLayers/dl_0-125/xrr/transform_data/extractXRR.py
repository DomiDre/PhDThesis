import jcnsBrukerD8

app = jcnsBrukerD8.App()
app.load_dat('../txtfile/DD213_7.txt', 0)
app.footprint_correct_and_rescale(10, 0.2)
app.save('DD213_7.xye')