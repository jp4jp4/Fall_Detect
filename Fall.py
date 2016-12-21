import ui

def read_data(sender):
	import motion, location
	import time, datetime
	import io
	import numpy as np
	import matplotlib.pyplot as plt
	
	val = view['switch1'].value
	if val==True:
		motion.start_updates()
			
		y=0
		nx = np.empty(1)
		ny = np.empty(1)
		nz = np.empty(1)
		view['mag'].text = ''
		view['accel'].text = ''
		view['gyro'].text = ''
		view['gravity'].text = ''
		
		while (y<=100):
			time.sleep(.05)
			x = motion.get_attitude()
			view['gyro'].text = str(x) + '\n' + view['gyro'].text
			x = motion.get_gravity()
			view['gravity'].text = str(x) + '\n' + view['gravity'].text
			x = motion.get_user_acceleration()
			nx = np.append(nx,x[0])
			ny = np.append(ny,x[1])
			nz = np.append(nz,x[2])
			view['accel'].text = str(x) + '\n' + view['accel'].text
			x = motion.get_magnetic_field()
			view['mag'].text = str(x) + '\n' + view['mag'].text
			y +=1
			view['y'].text = str(y) + 'measurements'
				
		motion.stop_updates()	
		plt.plot(nx)
		plt.show()
		plt.savefig('x.tif')
		plt.close()
		plt.plot(ny)
		plt.show()
		plt.savefig('y.tif')
		plt.close()
		plt.plot(nz)
		plt.show()
		plt.savefig('z.tif')
		plt.close()
		medianx = np.median(nz)
		stdx = np.std(nz)
		apex = np.amax(np.absolute(nz))
		print (apex)
		print (stdx)
		if apex >= stdx*2:
			if apex > stdx*5:
				view['fell'].text = 'Fall'
			else:
				view['fell'].text = 'Trip'
					
		fname = 'motion' + str(datetime.datetime.now()).split('.')[1] + '.txt'
		with open(fname, 'w') as fo:
			fo.write('gyro\n')
			fo.write(view['gyro'].text)
			fo.write('gravity\n')
			fo.write(view['gravity'].text)
			fo.write('accel\n')
			fo.write(view['accel'].text)
			fo.write('mag\n')
			fo.write(view['mag'].text)
	else:
		view['mag'].text = ''
		view['accel'].text = ''
		view['gyro'].text = ''
		view['gravity'].text = ''
		view['y'].text = str(0)

view = ui.load_view('Fall')

view.name = "fall"
view.present('sheet')

