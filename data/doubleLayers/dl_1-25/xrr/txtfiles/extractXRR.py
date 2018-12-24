import jcnsBrukerD8

app = jcnsBrukerD8.App()
app.load_dat('./DD205_3.txt', 0)
app.footprint_correct_and_rescale(10, 0.2)
app.save('../DD205_3.xye')


app = jcnsBrukerD8.App()
app.load_dat('./DD205_3_halfPieceAfterPNR.txt', 0)
app.footprint_correct_and_rescale(10, 0.2)
app.save('../DD205_3_halfPieceAfterPNR.xye')