# Importing libraries

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
import tkinter
import tkintermapview
import pygal
from datetime import datetime
from scipy import stats

a = []
b = []
dataset = pd.read_csv('../Data/juneroute.csv')
dataset.style.hide_index()
testMean = pd.DataFrame()
mapdatasetsudden = pd.DataFrame()
mapdatasetwhilein = pd.DataFrame()
mapdatawhileexit = pd.DataFrame()
mapdatainto = pd.DataFrame()
mapdataaccelinto = pd.DataFrame()

newData = pd.DataFrame()
newData.style.hide_index()
dataset.style.hide_index()
dataset.columns

meanSpeed_per_driver = dataset.groupby('Driver')['Speed'].mean()
barChart1 = pygal.Bar(height=400)
barChart1.title = "Average speed of individual driver"
[barChart1.add(x[0], x[1]) for x in meanSpeed_per_driver.items()]
# barChart1.render_to_file('../Charts/Average_Speed_Of_Driver.svg')

sudden_brake_event = dataset[dataset['Event'].str.contains("Sudden")]
braking_event = dataset[dataset['Event'].str.contains(r'(?:\s|^)Braking(?:,\s|$)')]
accel_event = dataset[dataset['Event'].str.contains(r'(?:\s|^)Acceleration(?:,\s|$)')]
accel_into_event = dataset[dataset['Event'].str.contains(r'(?:\s|^)Acceleration into turn(?:,\s|$)')]
braking_into_turn_event = dataset[dataset['Event'].str.contains("Braking into turn")]
braking_while_in_event = dataset[dataset['Event'].str.contains(r'(?:\s|^)Braking while in turn(?:,\s|$)')]
braking_while_exiting = dataset[dataset['Event'].str.contains("exiting")]
lane_change_event = dataset[dataset['Event'].str.contains("Lane Change")]
total_event = dataset['Event']

sudden_brake_event_count = len(sudden_brake_event)
braking_even_count = len(braking_event)
braking_into_turn_event_count = len(braking_into_turn_event)
braking_while_in_event_count = len(braking_while_in_event)
braking_while_exiting_count = len(braking_while_exiting)
accel_event_count = len(accel_event)
accel_into_event_count = len(accel_into_event)
total_event_count = len(total_event)
lane_change_event_count = len(lane_change_event)

total_unsafe_event = accel_into_event_count + braking_into_turn_event_count + braking_while_in_event_count + braking_while_exiting_count + sudden_brake_event_count

prob_of_sudden = sudden_brake_event_count / total_event_count
prob_of_braking_into = braking_into_turn_event_count / total_event_count
prob_of_while_in = braking_while_in_event_count / total_event_count
prob_while_exit = braking_while_exiting_count / total_event_count
prob_accel_into = accel_into_event_count / total_event_count

prob_event_of_sudden = sudden_brake_event_count / total_unsafe_event
prob_event_of_braking_into = braking_into_turn_event_count / total_unsafe_event
prob_event_of_while_in = braking_while_in_event_count / total_unsafe_event
prob_event_while_exit = braking_while_exiting_count / total_unsafe_event
prob_event_accel_into = accel_into_event_count / total_unsafe_event

bar_chart8 = pygal.StackedBar()
bar_chart8.title = "Probability of which unsafe event would happen"
bar_chart8.add('Sudden brake in turn ', prob_event_of_sudden)
bar_chart8.add('Braking into turn', prob_event_of_braking_into)
bar_chart8.add('Braking while in turn', prob_event_of_while_in)
bar_chart8.add('Braking while exiting', prob_event_while_exit)
bar_chart8.add('Accelerating into turn', prob_event_accel_into)
bar_chart8.render_to_file('../Charts/Prob_of_unsafe_event.svg')

bar_chart7 = pygal.HorizontalBar()
bar_chart7.title = 'Probability of Events'
bar_chart7.add('Sudden Brake in turn', prob_of_sudden)
bar_chart7.add('Braking while in turn', prob_of_while_in)
bar_chart7.add('Braking into turn ', prob_of_braking_into)
bar_chart7.add('Braking while exiting', prob_while_exit)
bar_chart7.add('Accelerating into turn', prob_accel_into)

pie_chart = pygal.Pie(inner_radius=.4, height=400)
pie_chart.title = 'Events compared'
pie_chart.add('Sudden Brakes', sudden_brake_event_count)
pie_chart.add('Braking', braking_even_count)
pie_chart.add('Braking into turn ', braking_into_turn_event_count)
pie_chart.add('Braking while in turn', braking_while_in_event_count)
pie_chart.add('Braking while exiting turn', braking_while_exiting_count)
pie_chart.add('Acceleration', accel_event_count)
pie_chart.add('Acceleration into turn', accel_into_event_count)
pie_chart.add('Lane Change', lane_change_event_count)
# pie_chart.render_to_file('../Charts/Events_Compared.svg')


bar_chart = pygal.HorizontalBar(height=400)
bar_chart.title = 'Unsafe events compared'
bar_chart.add('Sudden Brakes', sudden_brake_event_count)
bar_chart.add('Braking into turn ', braking_into_turn_event_count)
bar_chart.add('Braking while in turn', braking_while_in_event_count)
bar_chart.add('Braking while exiting turn', braking_while_exiting_count)
bar_chart.add('Acceleration into turn', accel_into_event_count)

dataset['Time'] = pd.to_datetime(dataset['Time'])
dataset['Date'] = dataset['Time'].dt.date
dataset['Hour'] = dataset['Time'].dt.hour
dataset['Minute'] = dataset['Time'].dt.minute

dataset['Time'] = [datetime.time(d) for d in dataset['Time']]

time_while_brake = dataset[dataset['Event'].str.contains("while in")]
time_of = time_while_brake['Hour'].astype(str)
hour_count = time_of.value_counts()
sorted_hour = time_of.sort_values()
# sorted_hour.drop_duplicates(['Hour'], keep=False)
hour_counts = hour_count.sum()

# print(hour_count)


# barChart2 = pygal.Bar(height=400)
# barChart2.title = "Frequency of event Braking while in turn by hour"
# barChart2.x_labels = (x[0] for x in hour_count.items())
# barChart2.add("Count", hour_count.values)
# [barChart2.add(x[0], x[1]) for x in hour_count.items()]
# barChart2.render_to_file('/Users/mihonakagawa/Downloads/Frequency_suddenBrakeInTurn_Hour.svg')

pie_chart4 = pygal.Pie(inner_radius=.75)
pie_chart4.title = "Frequency of event Braking while in turn by hour"
[pie_chart4.add(x[0], x[1]) for x in hour_count.items()]
pie_chart4.render_in_browser()

time_sudden_brake = dataset[dataset['Event'].str.contains("Sudden")]
time_of_sudden = time_sudden_brake['Hour'].astype(str)
hour_count_sudden = time_of_sudden.value_counts()
# sorted_hour.drop_duplicates(['Hour'], keep=False)
hour_counts_sudden = hour_count_sudden.sum()
# print(hour_count_sudden)


# barChart3 = pygal.Bar(height=400)
# barChart3.title = "Frequency of event Braking while in turn by hour"
# [barChart3.add(x[0], x[1]) for x in hour_count_sudden.items()]
# barChart3.render_to_file('/Users/mihonakagawa/Downloads/Frequency_BrakingWhileInTurn_Hour.svg')

pie_chart3 = pygal.Pie(inner_radius=.75)
pie_chart3.title = "Frequency of event Sudden brake in turn by hour"
[pie_chart3.add(x[0], x[1]) for x in hour_count_sudden.items()]
pie_chart3.render_in_browser()

time_exiting_brake = dataset[dataset['Event'].str.contains("exiting")]
time_of_exiting = time_exiting_brake['Hour'].astype(str)
hour_count_exiting = time_of_exiting.value_counts()
hour_counts_exiting = hour_count_exiting.sum()

# print(hour_count_exiting)
# barChart4 = pygal.Bar(height=400)
# barChart4.title = "Frequency of event Braking while exiting turn by hour"
# [barChart4.add(x[0], x[1]) for x in hour_count_exiting.items()]
# barChart4.render_to_file('/Users/mihonakagawa/Downloads/Frequency_BrakingWhileExit_Hour.svg')

pie_chart5 = pygal.Pie(inner_radius=.75)
pie_chart5.title = "Frequency of event Braking while exiting turn by hour"
[pie_chart5.add(x[0], x[1]) for x in hour_count_exiting.items()]
pie_chart5.render_in_browser()

time_intoTurn_brake = dataset[dataset['Event'].str.contains("Braking into turn")]
time_of_intoTurn = time_intoTurn_brake['Hour'].astype(str)
hour_count_intoTurn = time_of_intoTurn.value_counts()
hour_counts_intoTurn = hour_count_intoTurn.sum()
# print(hour_count_intoTurn)
# barChart5 = pygal.Bar(height=400)
# barChart5.title = "Frequency of event Braking into turn by hour"
# [barChart5.add(x[0], x[1]) for x in hour_count_intoTurn.items()]
# barChart5.render_in_browser()
# barChart5.render_to_file('/Users/mihonakagawa/Downloads/Frequency_BrakingIntoTurn_Hour.svg')

pie_chart2 = pygal.Pie(inner_radius=.75)
pie_chart2.title = "Frequency of event Braking into turn by hour"
[pie_chart2.add(x[0], x[1]) for x in hour_count_intoTurn.items()]
pie_chart2.render_in_browser()
pie_chart2.render_to_file('C:/Users/2102667/Downloads/Freq_brakeIntoTurn.svg')

time_intoTurn_accel = dataset[dataset['Event'].str.contains(r'(?:\s|^)Acceleration into turn(?:,\s|$)')]
time_of_intoTurn_accel = time_intoTurn_accel['Hour'].astype(str)
hour_count_intoTurn_accel = time_of_intoTurn_accel.value_counts()
hour_counts_intoTurn_accel = hour_count_intoTurn_accel.sum()
# print(hour_count_intoTurn_accel)
# barChart6 = pygal.Bar(height=400)
# barChart6.title = "Frequency of event Acceleration into turn by hour"
# [barChart6.add(x[0], x[1]) for x in hour_count_intoTurn_accel.items()]
# barChart6.render_to_file('/Users/mihonakagawa/Downloads/Frequency_BrakingIntoTurn_Hour.svg')

pie_chart6 = pygal.Pie(inner_radius=.75)
pie_chart6.title = "Frequency of event Acceleration into turn by hour"
[pie_chart6.add(x[0], x[1]) for x in hour_count_intoTurn_accel.items()]
pie_chart6.render_in_browser()

speed = dataset['Speed']
time_of_hour = dataset['Hour']
time_of_min = dataset['Minute']
final_time = []
b = 0
for thousands in time_of_hour:
    Hour = thousands * 100
    final_time.append(Hour)
for mins in time_of_min:
    final_time[b] = final_time[b] + mins
    b = b + 1
result = stats.linregress(x=final_time, y=speed)
# print(f"R-squared: {result.rvalue**2:.6f}")

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Scatter Plot of Speed vs Time'
xy_chart.add('A', [(final_time[x], speed[x]) for x in range(len(time_of_hour))])
xy_chart.add('best fit', [(0, result.intercept), (2359, 2359 * result.slope + result.intercept)], stroke=True)
xy_chart.render_to_file('C:/Users/2102667/Downloads/ScatterPlotSpeedVsTime.svg')
# print(result.intercept)
# print(result.slope)
xychart = pygal.XY(range=(0, 50))
xychart.title = 'Best Fit line for Speed vs Time'
xychart.add('best fit', [(0, result.intercept), (2359, 2359 * result.slope + result.intercept)])
xychart.render_to_file('C:/Users/2102667/Downloads/BestFitLineSpeedVsTime.svg')
newData['Driver'] = dataset.query('Event != "Braking" != "Acceleration" != "Lane Change"')['Driver']
newData['Event'] = dataset.query('Event != "Braking" != "Acceleration" != "Lane Change"')['Event']
newData['Latitude'] = dataset.query('Event != "Braking" != "Acceleration" != "Lane Change"')['Latitude']
newData['Longitude'] = dataset.query('Event != "Braking" != "Acceleration" != "Lane Change"')['Longitude']
newData['Date'] = dataset.query('Event != "Braking" != "Acceleration" != "Lane Change"')['Date']
newData['Vehicle'] = dataset.query('Event != "Braking" != "Acceleration" != "Lane Change"')['Vehicle']
newData['DriverSafe'] = dataset.query('Event == "Braking" == "Acceleration" == "Lane Change"')['Driver']

unsafeEventDriver_Ali = newData.query('Driver == "Ali"')['Driver']
unsafeEventDriverCount_Ali = len(unsafeEventDriver_Ali)
unsafeEventDriver_Chong = newData.query('Driver == "Chong"')['Driver']
unsafeEventDriverCount_Chong = len(unsafeEventDriver_Chong)
unsafeEventDriver_George = newData.query('Driver == "George"')['Driver']
unsafeEventDriverCount_George = len(unsafeEventDriver_George)
unsafeEventDriver_Gerald = newData.query('Driver == "Gerald"')['Driver']
unsafeEventDriverCount_Gerald = len(unsafeEventDriver_Gerald)
unsafeEventDriver_Keith = newData.query('Driver == "Keith"')['Driver']
unsafeEventDriverCount_Keith = len(unsafeEventDriver_Keith)
unsafeEventDriver_Lim = newData.query('Driver == "Lim"')['Driver']
unsafeEventDriverCount_Lim = len(unsafeEventDriver_Lim)
unsafeEventDriver_Ridwan = newData.query('Driver == "Ridwan"')['Driver']
unsafeEventDriverCount_Ridwan = len(unsafeEventDriver_Ridwan)
unsafeEventDriver_Siva = newData.query('Driver == "Siva"')['Driver']
unsafeEventDriverCount_Siva = len(unsafeEventDriver_Siva)
unsafeEventDriver_Yeo = newData.query('Driver == "Yeo"')['Driver']
unsafeEventDriverCount_Yeo = len(unsafeEventDriver_Yeo)

safeEventDriver_Ali = newData.query('Driver == "Ali"')['DriverSafe']
safeEventDriverCount_Ali = len(safeEventDriver_Ali)
safeEventDriver_Chong = newData.query('Driver == "Chong"')['DriverSafe']
safeEventDriverCount_Chong = len(safeEventDriver_Chong)
safeEventDriver_George = newData.query('Driver == "George"')['DriverSafe']
safeEventDriverCount_George = len(safeEventDriver_George)
safeEventDriver_Gerald = newData.query('Driver == "Gerald"')['DriverSafe']
safeEventDriverCount_Gerald = len(safeEventDriver_Gerald)
safeEventDriver_Keith = newData.query('Driver == "Keith"')['DriverSafe']
safeEventDriverCount_Keith = len(safeEventDriver_Keith)
safeEventDriver_Lim = newData.query('Driver == "Lim"')['DriverSafe']
safeEventDriverCount_Lim = len(safeEventDriver_Lim)
safeEventDriver_Ridwan = newData.query('Driver == "Ridwan"')['DriverSafe']
safeEventDriverCount_Ridwan = len(safeEventDriver_Ridwan)
safeEventDriver_Siva = newData.query('Driver == "Siva"')['DriverSafe']
safeEventDriverCount_Siva = len(safeEventDriver_Siva)
safeEventDriver_Yeo = newData.query('Driver == "Yeo"')['DriverSafe']
safeEventDriverCount_Yeo = len(safeEventDriver_Yeo)

prob_of_unsafe_Ali = unsafeEventDriverCount_Ali / len(dataset.query('Driver == "Ali"')['Event'])
prob_of_unsafe_Chong = unsafeEventDriverCount_Chong / len(dataset.query('Driver == "Chong"')['Event'])
prob_of_unsafe_George = unsafeEventDriverCount_George / len(dataset.query('Driver == "George"')['Event'])
prob_of_unsafe_Gerald = unsafeEventDriverCount_Gerald / len(dataset.query('Driver == "Gerald"')['Event'])
prob_of_unsafe_Keith = unsafeEventDriverCount_Keith/ len(dataset.query('Driver == "Keith"')['Event'])
prob_of_unsafe_Lim = unsafeEventDriverCount_Lim/ len(dataset.query('Driver == "Lim"')['Event'])
prob_of_unsafe_Ridwan = unsafeEventDriverCount_Ridwan/ len(dataset.query('Driver == "Ridwan"')['Event'])
prob_of_unsafe_Siva = unsafeEventDriverCount_Siva/ len(dataset.query('Driver == "Siva"')['Event'])
prob_of_unsafe_Yeo = unsafeEventDriverCount_Yeo/ len(dataset.query('Driver == "Yeo"')['Event'])

bar_chart8 = pygal.HorizontalBar()
bar_chart8.title = 'Probability of Driver being in a unsafe event'
bar_chart8.add('Ali', prob_of_unsafe_Ali)
bar_chart8.add('Chong', prob_of_unsafe_Chong)
bar_chart8.add('George', prob_of_unsafe_George)
bar_chart8.add('Gerald', prob_of_unsafe_Gerald)
bar_chart8.add('Keith', prob_of_unsafe_Keith)
bar_chart8.add('Lim', prob_of_unsafe_Lim)
bar_chart8.add('Ridwan', prob_of_unsafe_Ridwan)
bar_chart8.add('Siva', prob_of_unsafe_Siva)
bar_chart8.add('Yeo', prob_of_unsafe_Yeo)
bar_chart8.render_in_browser()

bus1_unsafeEvent = newData.query('Vehicle == "SBS6289D"')['Vehicle']
bus1_unsafeEvent_count = len(bus1_unsafeEvent)
bus2_unsafeEvent = newData.query('Vehicle == "SBS6431D"')['Vehicle']
bus2_unsafeEvent_count = len(bus2_unsafeEvent)
bus3_unsafeEvent = newData.query('Vehicle == "SG8625P"')['Vehicle']
bus3_unsafeEvent_count = len(bus3_unsafeEvent)
bus4_unsafeEvent = newData.query('Vehicle == "SBS8657E"')['Vehicle']
bus4_unsafeEvent_count = len(bus4_unsafeEvent)
bus5_unsafeEvent = newData.query('Vehicle == "SBS2235P"')['Vehicle']
bus5_unsafeEvent_count = len(bus5_unsafeEvent)
bus6_unsafeEvent = newData.query('Vehicle == "SG8189H"')['Vehicle']
bus6_unsafeEvent_count = len(bus6_unsafeEvent)
bus7_unsafeEvent = newData.query('Vehicle == "SG1369L"')['Vehicle']
bus7_unsafeEvent_count = len(bus7_unsafeEvent)
bus8_unsafeEvent = newData.query('Vehicle == "SBS1915P"')['Vehicle']
bus8_unsafeEvent_count = len(bus8_unsafeEvent)
bus9_unsafeEvent = newData.query('Vehicle == "SBS1895G"')['Vehicle']
bus9_unsafeEvent_count = len(bus9_unsafeEvent)
bus10_unsafeEvent = newData.query('Vehicle == "SBS7539M"')['Vehicle']
bus10_unsafeEvent_count = len(bus10_unsafeEvent)
bus11_unsafeEvent = newData.query('Vehicle == "SBS6583R"')['Vehicle']
bus11_unsafeEvent_count = len(bus11_unsafeEvent)

gauge_chart2 = pygal.Gauge(human_readable=True, height=410)
gauge_chart2.title = 'Number of unsafe events per vehicle'
gauge_chart2.range = [0, 35]
gauge_chart2.add('SBS6289D', bus1_unsafeEvent_count)
gauge_chart2.add('SBS6431D', bus2_unsafeEvent_count)
gauge_chart2.add('SG8625P', bus3_unsafeEvent_count)
gauge_chart2.add('SBS8657E', bus4_unsafeEvent_count)
gauge_chart2.add('SBS2235P', bus5_unsafeEvent_count)
gauge_chart2.add('SG8189H', bus6_unsafeEvent_count)
gauge_chart2.add('SG1369L', bus7_unsafeEvent_count)
gauge_chart2.add('SBS1915P', bus8_unsafeEvent_count)
gauge_chart2.add('SBS1895G', bus9_unsafeEvent_count)
gauge_chart2.add('SBS7539M', bus10_unsafeEvent_count)
gauge_chart2.add('SBS6583R', bus11_unsafeEvent_count)

# gauge_chart2.render_to_file('C:/Users/2102667/Downloads/UnsafeEventPerVehicle.svg')


gauge_chart = pygal.Gauge(human_readable=True, height=410)
gauge_chart.title = 'Number of unsafe events per driver'
gauge_chart.range = [0, 50]
gauge_chart.add('Ali', unsafeEventDriverCount_Ali)
gauge_chart.add('Chong', unsafeEventDriverCount_Chong)
gauge_chart.add('George', unsafeEventDriverCount_George)
gauge_chart.add('Gerald', unsafeEventDriverCount_Gerald)
gauge_chart.add('Keith', unsafeEventDriverCount_Keith)
gauge_chart.add('Lim', unsafeEventDriverCount_Lim)
gauge_chart.add('Ridwan', unsafeEventDriverCount_Ridwan)
gauge_chart.add('Siva', unsafeEventDriverCount_Siva)
gauge_chart.add('Yeo', unsafeEventDriverCount_Yeo)
# gauge_chart.render_to_file('C:/Users/2102667/Downloads/UnsafeEventPerDriver.svg')


newDataArrayDriver = newData['Driver'].to_numpy()
newDataArrayEvent = newData['Event'].to_numpy()
newDataArrayLat = newData['Latitude'].to_numpy()
newDataArrayLong = newData['Longitude'].to_numpy()
# newDataArrayDate = newData['Date'].to_numpy()

newData['Date1'] = newData['Date'].astype(str)
# newData['Date2'] = newData['Date1'].reset_index().values
newDateArray = newData['Date1'].to_numpy()
# print(newDateArray)


# for index, row in dataset.iterrows():
# print (index,row["Event"], row["Address"])
# dataset['Sudden'] = dataset['Event'].str.contains("Sudden")

dataset['Sudden'] = dataset.query('Event == "Sudden brake in turn"')['Event']
dataset['AccelInto'] = dataset.query('Event == "Acceleration into turn"')['Event']
dataset['BrakingInto'] = dataset.query('Event == "Braking into turn"')['Event']
dataset['BrakingWhile'] = dataset.query('Event == "Braking while in turn"')['Event']
dataset['BrakingWhileExit'] = dataset.query('Event == "Braking while exiting turn"')['Event']

dataset['SuddenLat'] = dataset.query('Event == "Sudden brake in turn"')['Latitude']
dataset['SuddenLong'] = dataset.query('Event == "Sudden brake in turn"')['Longitude']

mapdatasetsudden['Driver'] = dataset.query('Event == "Sudden brake in turn"')['Driver']
mapdatasetsudden['Event'] = dataset.query('Event == "Sudden brake in turn"')['Event']
mapdatasetsudden['Latitude'] = dataset.query('Event == "Sudden brake in turn"')['Latitude']
mapdatasetsudden['Longitude'] = dataset.query('Event == "Sudden brake in turn"')['Longitude']
mapdatasetsudden['Date'] = dataset.query('Event == "Sudden brake in turn"')['Date']

suddenArrayname = mapdatasetsudden['Driver'].to_numpy()
suddenArraydate = mapdatasetsudden['Date'].to_numpy()

mapdatasetwhilein['Driver'] = dataset.query('Event == "Braking while in turn"')['Driver']
mapdatasetwhilein['Event'] = dataset.query('Event == "Braking while in turn"')['Event']
mapdatasetwhilein['Latitude'] = dataset.query('Event == "Braking while in turn"')['Latitude']
mapdatasetwhilein['Longitude'] = dataset.query('Event == "Braking while in turn"')['Longitude']
mapdatasetwhilein['Date'] = dataset.query('Event == "Braking while in turn"')['Date']

mapdatawhileexit['Driver'] = dataset.query('Event == "Braking while exiting turn"')['Driver']
mapdatawhileexit['Event'] = dataset.query('Event == "Braking while exiting turn"')['Event']
mapdatawhileexit['Latitude'] = dataset.query('Event == "Braking while exiting turn"')['Latitude']
mapdatawhileexit['Longitude'] = dataset.query('Event == "Braking while exiting turn"')['Longitude']
mapdatawhileexit['Date'] = dataset.query('Event == "Braking while exiting turn"')['Date']

mapdatainto['Driver'] = dataset.query('Event == "Braking into turn"')['Driver']
mapdatainto['Event'] = dataset.query('Event == "Braking into turn"')['Event']
mapdatainto['Latitude'] = dataset.query('Event == "Braking into turn"')['Latitude']
mapdatainto['Longitude'] = dataset.query('Event == "Braking into turn"')['Longitude']
mapdatainto['Date'] = dataset.query('Event == "Braking into turn"')['Date']

mapdataaccelinto['Driver'] = dataset.query('Event == "Acceleration into turn"')['Driver']
mapdataaccelinto['Event'] = dataset.query('Event == "Acceleration into turn"')['Event']
mapdataaccelinto['Latitude'] = dataset.query('Event == "Acceleration into turn"')['Latitude']
mapdataaccelinto['Longitude'] = dataset.query('Event == "Acceleration into turn"')['Longitude']
mapdataaccelinto['Date'] = dataset.query('Event == "Acceleration into turn"')['Date']

testing_help = dataset.groupby(['Event', 'Longitude', 'Latitude'], axis=0, as_index=False).sum()
testing_help1 = (dataset[dataset.duplicated()])
latlongsudden = dataset.groupby(['Latitude', 'Longitude'])['Sudden'].value_counts().to_frame('count')
# latlongsudden = dataset.groupby(['Latitude', 'Longitude'])['Sudden'].
latlongaccel = dataset.groupby(['Latitude', 'Longitude'])['AccelInto'].value_counts().to_frame('count')
latlongbrakinginto = dataset.groupby(['Latitude', 'Longitude'])['BrakingInto'].value_counts().to_frame('count')
latlongbrakingwhile = dataset.groupby(['Latitude', 'Longitude'])['BrakingWhile'].value_counts().to_frame('count')
latlongbrakingwhileexit = dataset.groupby(['Latitude', 'Longitude'])['BrakingWhileExit'].value_counts().to_frame(
    'count')
testing_help3 = dataset.groupby(['Address'])['Event'].value_counts().to_frame('count')
testing_help4 = dataset.groupby(['Address'])['Event'].value_counts().to_frame('count')


testMean['Hour'] = dataset['Hour']
testMean['Speed']= dataset['Speed']
testMean['Speed0'] = testMean.query('Hour == 0')['Speed']
testMean['Speed1'] = testMean.query('Hour == 1')['Speed']
testMean['Speed2'] = testMean.query('Hour == 2')['Speed']
testMean['Speed3'] = testMean.query('Hour == 3')['Speed']
testMean['Speed4'] = testMean.query('Hour == 4')['Speed']
testMean['Speed5'] = testMean.query('Hour == 5')['Speed']
testMean['Speed6'] = testMean.query('Hour == 6')['Speed']
testMean['Speed7'] = testMean.query('Hour == 7')['Speed']
testMean['Speed8'] = testMean.query('Hour == 8')['Speed']
testMean['Speed9'] = testMean.query('Hour == 9')['Speed']
testMean['Speed10'] = testMean.query('Hour == 10')['Speed']
testMean['Speed11'] = testMean.query('Hour == 11')['Speed']
testMean['Speed12'] = testMean.query('Hour == 12')['Speed']
testMean['Speed13'] = testMean.query('Hour == 13')['Speed']
testMean['Speed14'] = testMean.query('Hour == 14')['Speed']
testMean['Speed15'] = testMean.query('Hour == 15')['Speed']
testMean['Speed16'] = testMean.query('Hour == 16')['Speed']
testMean['Speed17'] = testMean.query('Hour == 17')['Speed']
testMean['Speed18'] = testMean.query('Hour == 18')['Speed']
testMean['Speed19'] = testMean.query('Hour == 19')['Speed']
testMean['Speed20'] = testMean.query('Hour == 20')['Speed']
testMean['Speed21'] = testMean.query('Hour == 21')['Speed']
testMean['Speed22'] = testMean.query('Hour == 22')['Speed']
testMean['Speed23'] = testMean.query('Hour == 23')['Speed']

lengthOf0 = len(testMean[testMean['Speed0'].notna()])
speedValuesof0 = testMean['Speed0'].sum()
lengthOf1 = len(testMean[testMean['Speed1'].notna()])
speedValuesof1 = testMean['Speed1'].sum()
lengthOf2 = len(testMean[testMean['Speed2'].notna()])
speedValuesof2 = testMean['Speed2'].sum()
lengthOf3 = len(testMean[testMean['Speed3'].notna()])
speedValuesof3 = testMean['Speed3'].sum()
lengthOf4 = len(testMean[testMean['Speed4'].notna()])
speedValuesof4 = testMean['Speed4'].sum()
lengthOf5 = len(testMean[testMean['Speed5'].notna()])
speedValuesof5 = testMean['Speed5'].sum()
lengthOf6 = len(testMean[testMean['Speed6'].notna()])
speedValuesof6 = testMean['Speed6'].sum()
lengthOf7 = len(testMean[testMean['Speed7'].notna()])
speedValuesof7 = testMean['Speed7'].sum()
lengthOf8 = len(testMean[testMean['Speed8'].notna()])
speedValuesof8 = testMean['Speed8'].sum()
lengthOf9 = len(testMean[testMean['Speed9'].notna()])
speedValuesof9 = testMean['Speed9'].sum()
lengthOf10 = len(testMean[testMean['Speed10'].notna()])
speedValuesof10 = testMean['Speed10'].sum()
lengthOf11 = len(testMean[testMean['Speed11'].notna()])
speedValuesof11 = testMean['Speed11'].sum()
lengthOf12 = len(testMean[testMean['Speed12'].notna()])
speedValuesof12 = testMean['Speed12'].sum()
lengthOf13 = len(testMean[testMean['Speed13'].notna()])
speedValuesof13 = testMean['Speed13'].sum()
lengthOf14 = len(testMean[testMean['Speed14'].notna()])
speedValuesof14 = testMean['Speed14'].sum()
lengthOf15 = len(testMean[testMean['Speed15'].notna()])
speedValuesof15 = testMean['Speed15'].sum()
lengthOf16 = len(testMean[testMean['Speed16'].notna()])
speedValuesof16 = testMean['Speed16'].sum()
lengthOf17 = len(testMean[testMean['Speed17'].notna()])
speedValuesof17 = testMean['Speed17'].sum()
lengthOf18 = len(testMean[testMean['Speed18'].notna()])
speedValuesof18 = testMean['Speed18'].sum()
lengthOf19 = len(testMean[testMean['Speed19'].notna()])
speedValuesof19 = testMean['Speed19'].sum()
lengthOf20 = len(testMean[testMean['Speed20'].notna()])
speedValuesof20 = testMean['Speed20'].sum()
lengthOf21 = len(testMean[testMean['Speed21'].notna()])
speedValuesof21 = testMean['Speed21'].sum()
lengthOf22 = len(testMean[testMean['Speed22'].notna()])
speedValuesof22 = testMean['Speed22'].sum()
lengthOf23 = len(testMean[testMean['Speed23'].notna()])
speedValuesof23 = testMean['Speed23'].sum()
mean0 = speedValuesof0/lengthOf0
mean1 = speedValuesof1/lengthOf1
mean2 = speedValuesof2/lengthOf2
mean3 = speedValuesof3/lengthOf3
mean4 = speedValuesof4/lengthOf4
mean5 = speedValuesof5/lengthOf5
mean6 = speedValuesof6/lengthOf6
mean7 = speedValuesof7/lengthOf7
mean8 = speedValuesof8/lengthOf8
mean9 = speedValuesof9/lengthOf9
mean10 = speedValuesof10/lengthOf10
mean11 = speedValuesof11/lengthOf11
mean12 = speedValuesof12/lengthOf12
mean13 = speedValuesof13/lengthOf13
mean14 = speedValuesof14/lengthOf14
mean15 = speedValuesof15/lengthOf15
mean16 = speedValuesof16/lengthOf16
mean17 = speedValuesof17/lengthOf17
mean18 = speedValuesof18/lengthOf18
mean19 = speedValuesof19/lengthOf19
mean20 = speedValuesof20/lengthOf20
mean21 = speedValuesof21/lengthOf21
mean22 = speedValuesof22/lengthOf22
mean23 = speedValuesof23/lengthOf23
mean_array = [mean0, mean1, mean4, mean5, mean6, mean7, mean8, mean9, mean10, mean11, mean12, mean13, mean14, mean15, mean16, mean17, mean18, mean19, mean20, mean21, mean22, mean23]
number_of_hour = [0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
result = stats.linregress(x = number_of_hour, y= mean_array)

#print(mean_array)
xy2_chart = pygal.XY(stroke=False)
xy2_chart.title = 'Mean of speed vs time'
xy2_chart.add('A', [(number_of_hour[x], mean_array[x]) for x in range(22)])
xy2_chart.add('best fit',[(0,result.intercept),(23, 23*result.slope+result.intercept)], stroke = True)
xy2_chart.render_in_browser()
xy2_chart.render_to_file('C:/Users/2102667/Downloads/Mean.svg')
date1 = []
date5 = []
name = []
lat1 = []
long1 = []
name1 = []
address = []
events = []
dataset.info()

date = dataset['Time']
lat = dataset['Latitude']
long = dataset['Longitude']
naming = dataset['Driver']
address1 = dataset['Address']
event1 = dataset['Event']
address_checker = []
for i in lat:
    a = round(i, 5)
    lat1.append(a)
for i in long:
    a = round(i, 5)
    long1.append(a)
for i in date:
    date1.append(i)
for i in naming:
    name1.append(i)
for i in address1:
    address.append(i)
for i in event1:
    events.append(i)
for i in range(1453):
    name.append("marker" + str(i))
# print(date1[0])
y = 0
# print(name)
# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("map_view_example.py")


def show_name():
    date3 = date2.get()
    date4 = str(date3)
    name3 = name2.get()
    name3 = str(name3)

    for i in range(len(newDataArrayDriver)):
        if name3 == newDataArrayDriver[i] and date3 == newDateArray[i]:
            eventText = newDataArrayEvent[i]

            name[i] = map_widget.set_marker(newDataArrayLat[i], newDataArrayLong[i], eventText)
    map_widget.set_position(1.39643, 103.90348)  # Singapore
    map_widget.set_zoom(15)


# create map widget

map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
date2 = tkinter.Entry()
#date2.place(x=500, y=500, sticky="NSEW", padx=2, pady=2)
date2.insert(0, "Input Date")
date2.pack(side=tkinter.BOTTOM)
name2 = tkinter.Entry()
name2.insert(0,"Input Name of Driver" )
name2.pack(side=tkinter.BOTTOM)
#name2.grid(x=600, y=600, sticky="NSEW", padx=2, pady=2)

button = tkinter.Button(root_tk, text="Search", command=show_name)
button.pack(side=tkinter.BOTTOM)
#button.grid(row=0, column=1, sticky="NSEW", padx=2, pady=2)

root_tk.mainloop()
