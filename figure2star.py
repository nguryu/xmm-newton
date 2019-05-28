from numpy import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
import warnings
import time
start = time.time()
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=RuntimeWarning)

# Error bars
x = []
y = []
ye = []
y1 = []
y1e = []
# Lists for table data
src_id = []
type = []
u_type = []
var14 = []
f14 = []
det_no = []
hr1 = []
hr2 = []
hr3 = []
hr4 = []
e_hr1 = []
e_hr2 = []
e_hr3 = []
e_hr4 = []
star_src_id = []
star_hr1 = []
star_hr2 = []
star_hr3 = []
star_hr4 = []
e_star_hr1 = []
e_star_hr2 = []
e_star_hr3 = []
e_star_hr4 = []
hr1_1 = []
hr2_1 = []
hr3_1 = []
hr4_1 = []
e_hr1_1 = []
e_hr2_1 = []
e_hr3_1 = []
e_hr4_1 = []

with open('plotdata_star_a_hr', 'r') as data_file:
    for line in data_file:
        li = line.strip()
        if not li.startswith('#'):
            col = line.split(' ')
            src_id.append(col[0])
            type.append(col[1])
            u_type.append(col[2])
            var14.append(float(col[3]))
            f14.append(float(col[4]))
            det_no.append(int(col[6]))
            hr1.append(float(col[10]))
            e_hr1.append(float(col[11]))
            hr2.append(float(col[12]))
            e_hr2.append(float(col[13]))
            hr3.append(float(col[14]))
            e_hr3.append(float(col[15]))
            hr4.append(float(col[16]))
            e_hr4.append(float(col[17]))

# Check for number of detections.
for i in range(0, len(src_id)):
    if det_no[i] > 0:
        star_src_id.append(src_id[i])
        star_hr1.append(hr1[i])
        star_hr2.append(hr2[i])
        star_hr3.append(hr3[i])
        star_hr4.append(hr4[i])
        e_star_hr1.append(e_hr1[i])
        e_star_hr2.append(e_hr2[i])
        e_star_hr3.append(e_hr3[i])
        e_star_hr4.append(e_hr4[i])

# Convert from list to array
star_hr1 = array(star_hr1)
star_hr2 = array(star_hr2)
star_hr3 = array(star_hr3)
star_hr4 = array(star_hr4)
e_star_hr1 = array(e_star_hr1)
e_star_hr2 = array(e_star_hr2)
e_star_hr3 = array(e_star_hr3)
e_star_hr4 = array(e_star_hr4)

# ========== Connect Points by Descending HR3 ========== #
def hrLine(hr1, hr2, hr3, hr4, e_hr1, e_hr2, e_hr3, e_hr4):
    # Use pandas data frame to sort hardness ratios.
    data = {'hr1': hr1,
            'e_hr1': e_hr1,
            'hr2': hr2,
            'e_hr2': e_hr2,
            'hr3': hr3,
            'e_hr3': e_hr3,
            'hr4': hr4,
            'e_hr4': e_hr4}
    df = pd.DataFrame(data)
    # Sort by descending HR3.
    t0 = df.sort_values(by = 'hr3', ascending = 0)
    # print t0
    # Convert data frame columns to lists and then to arrays
    hr1_arr = array(t0['hr1'].tolist())
    hr2_arr = array(t0['hr2'].tolist())
    hr3_arr = array(t0['hr3'].tolist())
    hr4_arr = array(t0['hr4'].tolist())
    e_hr1_arr = array(t0['e_hr1'].tolist())
    e_hr2_arr = array(t0['e_hr2'].tolist())
    e_hr3_arr = array(t0['e_hr3'].tolist())
    e_hr4_arr = array(t0['e_hr4'].tolist())
    # Connect HR1 and HR2 points by descending HR3.
    t1 = where((e_hr1_arr <= 0.1) & (e_hr2_arr <= 0.1))[0]
    sub3.plot(hr1_arr[t1], hr2_arr[t1], color = '#777777', linewidth = 0.1, zorder = 0)
    # Connect HR2 and HR3 points by descending HR3.
    t2 = where((e_hr2_arr <= 0.1) & (e_hr3_arr <= 0.1))[0]
    sub2.plot(hr2_arr[t2], hr3_arr[t2], color = '#777777', linewidth = 0.1, zorder = 0)
    # Connect HR3 and HR4 points by descending HR3.
    t3 = where((e_hr3_arr <= 0.1) & (e_hr4_arr <= 0.1))[0]
    sub1.plot(hr3_arr[t3], hr4_arr[t3], color = '#777777', linewidth = 0.1, zorder = 0)

# =========== Graph Set-up ========== #
# Figure size
xr = 4.
yr = 8.
fig = plt.figure(figsize = (xr, yr)) # (width, height)
# Font size
SMALL_SIZE = 8
MEDIUM_SIZE = 12
LARGE_SIZE = 16
plt.rc('font', size = SMALL_SIZE)          # Controls default text sizes
plt.rc('axes', titlesize = LARGE_SIZE)     # Font size of the axes title
plt.rc('axes', labelsize = SMALL_SIZE)     # Font size of the x and y labels
plt.rc('xtick', labelsize = SMALL_SIZE)    # Font size of the tick labels
plt.rc('ytick', labelsize = SMALL_SIZE)    # Font size of the tick labels
plt.rc('legend', fontsize = SMALL_SIZE)    # Legend font size
# Axes ticks
majorFormatter = FormatStrFormatter('%1.1f')
majorLocator = MultipleLocator(0.5)  # Major tick intervals
minorLocator = MultipleLocator(0.1)  # Minor tick intervals

# ========== Subplot 1 ========== #
sub1 = plt.subplot(311)
sub1.set_position([0.25, 0.15+2/yr+2/yr, 2/xr, 2/yr])  # (left, bottom, width, height)
# Axes parameters
sub1.set_xlim([-1.1, 1.1])
sub1.set_ylim([-1.1, 1.1])
plt.setp(sub1.get_xticklabels(), visible = False)
plt.setp(sub1.get_yticklabels(), visible = False)
sub1.text(-1.45, 0, 'HR4', rotation = 90)
sub1.text(0.6, -1.0, 'HR3')
sub1.text(-1.275, -1.05, '-1', rotation = 90)
sub1.text(-1.275, -0.46, '-0.5', rotation = 90)
sub1.text(-1.275, -0.06,  '0', rotation = 90)
sub1.text(-1.275, 0.5,  '0.5', rotation = 90)
sub1.text(-1.275, 0.95, '1', rotation = 90)
# Set tick marks
sub1.yaxis.set_major_formatter(majorFormatter)
sub1.yaxis.set_major_locator(majorLocator)
sub1.yaxis.set_minor_locator(minorLocator)
# Graph parameters
t = where((e_star_hr3 <= 0.1) & (e_star_hr4 <= 0.1))[0]
sub1.scatter(star_hr3[t], star_hr4[t], color = '#FF0000', marker = '.', s = 1, label = 'Star', zorder = 1)

# ========== Subplot 2 ========== #
sub2 = plt.subplot(312, sharex = sub1)
sub2.set_position([0.25, 0.15+2/yr, 2/xr, 2/yr])
# Axes parameters
sub2.set_xlim([-1.1, 1.1])
sub2.set_ylim([-1.1, 1.1])
plt.setp(sub2.get_xticklabels(), visible = False)
plt.setp(sub2.get_yticklabels(), visible = False)
sub2.text(-1.45, 0, 'HR3', rotation = 90)
sub2.text(0.6, -1.0, 'HR2')
sub2.text(-1.275, -1.05, '-1', rotation = 90)
sub2.text(-1.275, -0.46, '-0.5', rotation = 90)
sub2.text(-1.275, -0.06,  '0', rotation = 90)
sub2.text(-1.275, 0.5,  '0.5', rotation = 90)
sub2.text(-1.275, 0.95, '1', rotation = 90)
# Set tick marks
sub2.yaxis.set_major_formatter(majorFormatter)
sub2.yaxis.set_major_locator(majorLocator)
sub2.yaxis.set_minor_locator(minorLocator)
# Graph parameters
t = where((e_star_hr2 <= 0.1) & (e_star_hr3 <= 0.1))[0]
sub2.scatter(star_hr2[t], star_hr3[t], color = '#FF0000', marker = '.', s = 1, label = 'Star', zorder = 1)

# ========== Subplot 3 ========== #
sub3 = plt.subplot(313, sharex = sub1)
sub3.set_position([0.25, 0.15, 2/xr, 2/yr])
# Axes parameters
sub3.set_xlim([-1.1, 1.1])
sub3.set_ylim([-1.1, 1.1])
plt.setp(sub3.get_xticklabels(), visible = False)
plt.setp(sub3.get_yticklabels(), visible = False)
sub3.text(-1.45, 0, 'HR2', rotation = 90)
sub3.text(0.6, -1.0, 'HR1')
sub3.text(-1.05, -1.275, '-1')
sub3.text(-0.65, -1.275, '-0.5')
sub3.text(-0.02, -1.275, '0')
sub3.text(0.42, -1.275, '0.5')
sub3.text(1.0, -1.275, '1')
sub3.text(-1.275, -1.05, '-1', rotation = 90)
sub3.text(-1.275, -0.46, '-0.5', rotation = 90)
sub3.text(-1.275, -0.06,  '0', rotation = 90)
sub3.text(-1.275, 0.5,  '0.5', rotation = 90)
sub3.text(-1.275, 0.95, '1', rotation = 90)
# Set tick marks
sub3.xaxis.set_major_formatter(majorFormatter)
sub3.yaxis.set_major_formatter(majorFormatter)
sub3.xaxis.set_major_locator(majorLocator)
sub3.xaxis.set_minor_locator(minorLocator)
sub3.yaxis.set_major_locator(majorLocator)
sub3.yaxis.set_minor_locator(minorLocator)
# Graph parameters
t = where((e_star_hr1 <= 0.1) & (e_star_hr2 <= 0.1))[0]
sub3.scatter(star_hr1[t], star_hr2[t], color = '#FF0000', marker = '.', s = 1, label = 'Star', zorder = 1)
lgnd1 = plt.legend(loc = 'upper left', scatterpoints = 1, fontsize = 6)
lgnd1.get_frame().set_linewidth(0.0)

# Sort sources by matching source IDs.
i = 0
while(i < len(star_src_id)):
    # Count how many sources there are with matching IDs.
    n = src_id.count(star_src_id[i])
    # Put hardness ratio properties of source(s) into lists.
    for j in range(i, i+n):
        hr1_1.append(star_hr1[j])
        hr2_1.append(star_hr2[j])
        hr3_1.append(star_hr3[j])
        hr4_1.append(star_hr4[j])
        e_hr1_1.append(e_star_hr1[j])
        e_hr2_1.append(e_star_hr2[j])
        e_hr3_1.append(e_star_hr3[j])
        e_hr4_1.append(e_star_hr4[j])
    # Pass into function to connect sources with same IDs.
    if(n >= 2):
        hrLine(hr1_1, hr2_1, hr3_1, hr4_1, e_hr1_1, e_hr2_1, e_hr3_1, e_hr4_1)
    # Reset lists after each iteration.
    del hr1_1[:], hr2_1[:], hr3_1[:], hr4_1[:], e_hr1_1[:], e_hr2_1[:], e_hr3_1[:], e_hr4_1[:]
    # Continue to next different source ID by incrementing by the number of matches.
    i += n

# ========== Output ========== #
fig.savefig('fig2star.eps',format = 'eps', bbox_inches = 'tight', pad_inches = 0.02, dpi = 1000)

end = time.time()
print "\nRuntime:", end - start, "s"