import ui

def wear_connect(sender):
	wear['connect_result'].text = 'done'
	
def belt_adjust(sender):
	if belt['slider1'].value < .25:
		belt['lbl1'].text = 'Gentle Setting'
	else:
		if belt['slider1'].value < .75:
			belt['lbl1'].text = 'Moderate Intensity'
		else:
			belt['lbl1'].text = 'This will hurt you more than it does me'

def clear_data(sender):
	environ['mag'].text = ''
	environ['geo'].text = ''
	environ['acc'].text = ''
	environ['att'].text = ''
	environ['grav'].text = ''
	
def environ_data(sender):
	import motion
	import location
	
	motion.start_updates()
	location.start_updates()
	
	x = motion.get_attitude()
	environ['att'].text = str(x) + '\n' + environ['att'].text
	x = motion.get_gravity()
	environ['grav'].text = str(x) + '\n' + environ['grav'].text
	x = motion.get_user_acceleration()
	environ['acc'].text = str(x) + '\n' + environ['acc'].text
	x = motion.get_magnetic_field()
	environ['mag'].text = str(x) + '\n' + environ['mag'].text
	
	x=location.get_location()
	coord = {'latitude': x['latitude'], 'longitude':x['longitude']}
	print(coord)
	y = location.reverse_geocode(coord)
	print(y)
	environ['geo'].text=str(x)
				
	motion.stop_updates()	
	location.stop_updates()

def increase_contrast():
	if (v.background_color == '#000000'):
		v.background_color = 'N/A'
	else:		
		v.background_color = '#000000'
	
def button_tapped(sender):
	if sender.title == 'Low Vision Settings':
		increase_contrast()
		
	if sender.title == 'Environmental Data':
		environ.present('sheet')
	
	if sender.title == 'Fall/Trip History':
		history.present('sheet')
		
	if sender.title == 'Safety Review':
		webview.present('sheet')
		webview['wb1'].load_url('http://www.cviga.org/sightseeing/safe_sight_tips_visually_impaired_trick_or_treater/')
		
	if sender.title == 'Wearable Connect':
		wear.present('sheet')
		
	if sender.title == 'Adjust Belt Output':
		belt.present('sheet')

belt = ui.load_view('belt')
wear = ui.load_view('wear')
history = ui.load_view('history')
environ = ui.load_view('environ')
webview = ui.load_view('web')

	
v = ui.load_view('Fall_detect')
v.name = 'Eye Robot'
v.present('sheet')
