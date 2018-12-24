import jcnsBrukerD8

sample_name = 'DD213_7'
app = jcnsBrukerD8.App()
app.load_dat('./'+sample_name+'.txt', 0)
app.footprint_correct_and_rescale(10, 0.2)
app.save('../'+sample_name+'.xye')
