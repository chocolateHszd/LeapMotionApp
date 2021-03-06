import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class LeapMotionListener(Leap.Listener):
	finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
	bone_names = ['Metacarpal', 'Proximal','Intermediate','Distal']
	state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

	def on_init(self, controller):
		print "Initialized"

	def on_connect(self,controller):
		print "Motion Sensor Connected"

		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

	def on_disconnect(self,controller):
		print "Motion Sensor disconnected"

	def on_exit(self,controller):
		print "Exited"

	def on_frame(self, controller):
		frame = controller.frame()

		
		print "Frame ID: " + str(frame.id) \
		+ " timeStamp: " + str(frame.timestamp) \
		+ " #of Hands: " + str(len(frame.hands)) \
		+ " #of fingers: " + str(len(frame.fingers)) \
		+ " #of tools: " + str(len(frame.tools)) \
		+ " #of gesters: "+ str(len(frame.gestures()))

		for hand in frame.hands:
			
			handType = "Left Hand" if hand.is_left else "Right Hand"

			print handType + " Hand ID: "+str(frame.id) +" Palm Position: "+str(hand.palm_position)

			normal= hand.palm_normal
			direction = hand.direction

			print " Pitch: "+ str(direction.pitch * Leap.RAD_TO_DEG) + \
			      " Roll: " + str(normal.roll * Leap.RAD_TO_DEG) +\
			      " Yaw: " + str(direction.yaw * Leap.RAD_TO_DEG)

			print "----------"
			arm = hand.arm
			print "Arm Direction: "+ str(arm.direction) +" Wrist Position: "+ str(arm.wrist_position)+ " Elbow Position: "+ str(arm.elbow_position)
			
			
			for finger in hand.fingers:
				print " Finger Type: " + self.finger_names[finger.type()] + \
					  " ID: "+ str(finger.id) +\
					  " Length: "+ str(finger.length) + \
					  " Width: "+ str(finger.width)

				for b in range(0,4):
					bone = finger.bone(b)
					print "Bone: "+ self.bone_names[bone.type]+ \
						  " Start: "+ str(bone.prev_joint)+ \
						  " End: " + str(bone.next_joint) + \
						  " Direction: "+ str(bone.direction)

			for tool in frame.tools:
				print "ID: "+ str(tool.id) + \
					  " Tip Position: "+ str(tool.tip_position) + \
					  " Direction: "+ str(tool.direction)


def main():
	listener = LeapMotionListener()
	controller = Leap.Controller()

	controller.add_listener(listener)
	print "Press Enter to Quit ..."

	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass 
	finally:
		controller.remove_listener(listener)

if __name__ == "__main__":
	main()
