import jcnsBrukerD8

app = jcnsBrukerD8.App()
app.qmin = 0.02
app.load_dat('../rawdata/ES-S15.txt', mode=0)
app.footprint_correct_and_rescale(27, 0.2, 0.02, 0.025)
# app.gaussian_footprint_correct_and_rescale(17, 0.2)
app.save('ES-S15.xye')