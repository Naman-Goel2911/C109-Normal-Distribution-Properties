import statistics as stats
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv('StudentsPerformance.csv')
mathsPerformance = df['math score'].tolist()
readingPerformance = df['reading score'].tolist()
writingPerformance = df['writing score'].tolist()
df.pop('0')

sumOfMaths = sum(mathsPerformance)
sumOfReading = sum(readingPerformance)
sumOfWriting = sum(writingPerformance)

sum = sum(sumOfMaths, sumOfReading)
totalPerformance = sum(sum, sumOfWriting)

mean = stats.mean(totalPerformance)
std_dev = stats.stdev(totalPerformance)
median = stats.median(totalPerformance)
mode = stats.mode(totalPerformance)

first_std_start, first_std_end = mean-std_dev, mean+std_dev
sec_std_start, sec_std_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_start, third_std_end = mean-(3*std_dev), mean+(3*std_dev)
list_of_data_within_1_std_dev = [result for result in totalPerformance if result > first_std_start and result < first_std_end]
list_of_data_within_2_std_dev = [result for result in totalPerformance if result > sec_std_start and result < sec_std_end]
list_of_data_within_3_std_dev = [result for result in totalPerformance if result > third_std_start and result < third_std_end]

print('{}% of data lies withing first standard deviation.'. format(len(list_of_data_within_1_std_dev)*100/len(totalPerformance)))
print('{}% of data lies withing second standard deviation.'. format(len(list_of_data_within_2_std_dev)*100/len(totalPerformance)))
print('{}% of data lies withing third standard deviation.'. format(len(list_of_data_within_3_std_dev)*100/len(totalPerformance)))

print('Mean of height is ', mean)
print('Median of height is ', median)
print('Mode of height is ', mode)
print('Standard Deviation of height is ', std_dev)

fig = ff.create_distplot([totalPerformance], ['Total Performance'], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.23], mode='lines', name='Mean'))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.23], mode='lines', name='Standard Deviation 1 Start'))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.23], mode='lines', name='Standard Deviation 1 End'))
fig.add_trace(go.Scatter(x=[sec_std_start, sec_std_start], y=[0, 0.23], mode='lines', name='Standard Deviation 2 Start'))
fig.add_trace(go.Scatter(x=[sec_std_end, sec_std_end], y=[0, 0.23], mode='lines', name='Standard Deviation 2 End'))
fig.add_trace(go.Scatter(x=[third_std_start, third_std_start], y=[0, 0.23], mode='lines', name='Standard Deviation 3 Start'))
fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[0, 0.23], mode='lines', name='Standard Deviation 3 End'))
fig.show()
