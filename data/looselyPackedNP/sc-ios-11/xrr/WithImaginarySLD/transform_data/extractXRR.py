import jcnsBrukerD8

app = jcnsBrukerD8.App()
app.qmin = 0.01
app.load_dat('../rawdata/ES-S14.txt', mode=0)
app.footprint_correct_and_rescale(17, 0.2)
# app.gaussian_footprint_correct_and_rescale(17, 0.2)
app.save('ES-S14.xye')