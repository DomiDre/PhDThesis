import jcnsBrukerD8

app = jcnsBrukerD8.App()
app.load_dat('../rawdata/SiScan.txt', 1)
app.footprint_correct_and_rescale(10, 0.2)
app.save('SiWafer.xye')