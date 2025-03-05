import matplotlib.pyplot as plt

def load_data():
	fh = open("finaldata.csv", "r")
	lines = fh.readlines()
	fh.close()
	digits = set(list("1234567890"))
	t, r = [], []
	for line in lines:
		if line[0] not in digits or "overload" in line: # Skip lines which are invalid data
			continue
		vals = line.split(",") # CSV so separate on comma
		assert len(vals) == 2
		t_val, r_val = vals
		t_val, r_val = float(t_val), float(r_val)
		t.append(t_val)
		r.append(r_val)

	return t, r


def r():
	t, r = load_data()
	# Create the plot
	plt.plot(t, r, marker='o', linestyle='-', color='b')

	# Add labels and title
	plt.xlabel('Aika t (s)')
	plt.ylabel('Resistanssi r (ohmia)')
	plt.title('Vastus ajan funktiona')

	# Display the plot
	plt.savefig("resistance_plot.eps", format="eps", dpi=1000)
	plt.show()
	return

if __name__=="__main__":
	r()
	exit()
