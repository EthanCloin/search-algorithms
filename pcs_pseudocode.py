""" Psuedocode for Potential Cost Search """

# Intialize START and GOAL

	# Initialize OPEN as a heap of nodes
	# Initialize CLOSED as a list of nodes
	# Add obstacle nodes and border to CLOSED

	# Heappop will return highest U_SCORE
	# Calculate scores and push START to heap

	# Loop until OPEN is empty
		# Pop node from OPEN and append to CLOSED
		# Get neighbors by step method

			# Skip neighbor if in CLOSED(obstacle/bounds)
			# Skip neighbor if in OPEN with neighbor.GSCORE > stored.GSCORE
			# Skip neighbor if (GSCORE + HSCORE) >= CONSTRAINT
			
			# If neighbor == GOAL, return path by backtracking

			# If neighbor already in OPEN
				# stored.GSCORE = neighbor.GSCORE

			# Else
				# calculate USCORE
				# push neighbor onto OPEN